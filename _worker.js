const RESEND_ENDPOINT = "https://api.resend.com/emails";
const DEFAULT_TO_EMAIL = "info@aethermed.health";
const DEFAULT_FROM_EMAIL = "AetherMed Website <no-reply@aethermed.health>";

function escapeHtml(value) {
  return String(value || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function textValue(formData, key) {
  const value = formData.get(key);
  return typeof value === "string" ? value.trim() : "";
}

function jsonResponse(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      "Content-Type": "application/json; charset=utf-8"
    }
  });
}

function renderEmailHtml(fields, files) {
  const rows = [
    ["Name", `${fields.firstName} ${fields.lastName}`.trim()],
    ["Email", fields.email],
    ["WhatsApp", fields.whatsapp],
    ["Country", fields.country],
    ["Specialty", fields.specialty],
    ["Privacy consent", fields.privacyConsent ? "Yes" : "No"],
    ["Submitted at", new Date().toISOString()]
  ];

  const fileList = files.length
    ? `<ul>${files.map((file) => `<li>${escapeHtml(file.name)} (${escapeHtml(file.size)} bytes)</li>`).join("")}</ul>`
    : "<p>No files were attached to the form submission.</p>";

  return `
    <div style="font-family:Arial,sans-serif;color:#102335;line-height:1.6">
      <h1 style="font-size:22px;margin:0 0 16px">New AetherMed Website Inquiry</h1>
      <table style="border-collapse:collapse;width:100%;max-width:720px">
        ${rows
          .map(
            ([label, value]) => `
              <tr>
                <th style="border:1px solid #d9e5eb;background:#f5fafb;text-align:left;padding:8px 10px;width:170px">${escapeHtml(label)}</th>
                <td style="border:1px solid #d9e5eb;padding:8px 10px">${escapeHtml(value)}</td>
              </tr>
            `
          )
          .join("")}
      </table>
      <h2 style="font-size:18px;margin:22px 0 8px">Condition Summary</h2>
      <p style="white-space:pre-wrap;border:1px solid #d9e5eb;background:#f8fbfc;padding:12px">${escapeHtml(fields.message)}</p>
      <h2 style="font-size:18px;margin:22px 0 8px">Uploaded File Names</h2>
      ${fileList}
      <p style="color:#617282;font-size:13px;margin-top:24px">
        This email was generated from the AetherMed website contact form. Medical file attachments are not forwarded by email; follow up with the patient using a secure channel if documents are needed.
      </p>
    </div>
  `;
}

async function handleContactPost(request, env) {
  if (!env.RESEND_API_KEY) {
    return jsonResponse({ error: "Email service is not configured." }, 500);
  }

  const formData = await request.formData();
  const fields = {
    firstName: textValue(formData, "first_name"),
    lastName: textValue(formData, "last_name"),
    email: textValue(formData, "email"),
    whatsapp: textValue(formData, "whatsapp"),
    country: textValue(formData, "country"),
    specialty: textValue(formData, "specialty"),
    message: textValue(formData, "message"),
    privacyConsent: formData.get("privacy_consent") === "on"
  };

  if (!fields.firstName || !fields.lastName || !fields.email || !fields.whatsapp || !fields.country || !fields.specialty || !fields.message || !fields.privacyConsent) {
    return jsonResponse({ error: "Missing required form fields." }, 400);
  }

  const files = formData
    .getAll("documents")
    .filter((file) => typeof file === "object" && file && "name" in file && file.name)
    .map((file) => ({ name: file.name, size: file.size || 0 }));

  const fromEmail = env.CONTACT_FROM_EMAIL || DEFAULT_FROM_EMAIL;
  const subject = `New AetherMed inquiry: ${fields.firstName} ${fields.lastName} - ${fields.country}`;

  const payload = {
    from: fromEmail,
    to: [DEFAULT_TO_EMAIL],
    subject,
    html: renderEmailHtml(fields, files),
    reply_to: fields.email
  };

  const response = await fetch(RESEND_ENDPOINT, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${env.RESEND_API_KEY}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  });

  if (!response.ok) {
    const detail = await response.text();
    return jsonResponse({ error: "Email delivery failed.", detail }, 502);
  }

  return jsonResponse({ ok: true });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.pathname === "/api/contact") {
      if (request.method === "GET") {
        return jsonResponse({ ok: true, endpoint: "AetherMed contact form" });
      }

      if (request.method === "POST") {
        return handleContactPost(request, env);
      }

      return jsonResponse({ error: "Method not allowed." }, 405);
    }

    return env.ASSETS.fetch(request);
  }
};
