
(function () {
  const articles = window.AETHERMED_INSIGHTS || [];
  const normalize = (value) => String(value || "").toLowerCase();
  const matches = (article, query) => {
    const haystack = normalize([article.title, article.summary, ...(article.categories || []), ...(article.tags || [])].join(" "));
    return !query || haystack.includes(normalize(query));
  };
  const cardHtml = (article) => `
    <article class="insight-card">
      ${article.image ? `<a class="insight-card-image" href="${article.url}"><img src="../../assets/${article.image}" alt="${article.alt || ""}" loading="lazy" decoding="async" /></a>` : ""}
      <div class="insight-card-body">
        <div class="insight-card-categories">${(article.categories || []).map((name) => `<span class="insight-category-link">${name}</span>`).join("")}</div>
        <h2><a href="${article.url}">${article.title}</a></h2>
        <div class="insight-card-tags">${(article.tags || []).slice(0, 2).map((tag) => `<span class="insight-chip">${tag}</span>`).join("")}</div>
        <p>${article.summary}</p>
        ${article.updated ? `<time datetime="${article.updated}">Updated ${article.updated}</time>` : ""}
      </div>
    </article>`;

  document.querySelectorAll("[data-insights-search]").forEach((form) => {
    const input = form.querySelector("input[type='search']");
    const status = document.querySelector("[data-search-status]");
    const cards = Array.from(document.querySelectorAll("[data-search-results] .insight-card"));
    const clear = document.querySelector("[data-clear-search]");
    const apply = () => {
      const query = normalize(input.value.trim());
      let count = 0;
      cards.forEach((card) => {
        const haystack = normalize([card.dataset.title, card.dataset.summary, card.dataset.categories, card.dataset.tags].join(" "));
        const show = !query || haystack.includes(query);
        card.hidden = !show;
        if (show) count += 1;
      });
      if (status) status.textContent = query ? `${count} matching article${count === 1 ? "" : "s"}.` : "";
    };
    form.addEventListener("submit", (event) => { event.preventDefault(); apply(); });
    input.addEventListener("input", apply);
    if (clear) clear.addEventListener("click", () => { input.value = ""; apply(); input.focus(); });
  });

  document.querySelectorAll("[data-insights-search-page]").forEach((form) => {
    const params = new URLSearchParams(window.location.search);
    const input = form.querySelector("input[type='search']");
    const results = document.querySelector("[data-search-results]");
    const empty = document.querySelector("[data-empty-search]");
    const status = document.querySelector("[data-search-status]");
    const render = () => {
      const query = input.value.trim();
      const list = articles.filter((article) => matches(article, query));
      results.innerHTML = list.map(cardHtml).join("");
      if (empty) empty.hidden = list.length !== 0;
      if (status) status.textContent = query ? `${list.length} result${list.length === 1 ? "" : "s"} for "${query}".` : "Showing all Insights.";
    };
    input.value = params.get("q") || "";
    form.addEventListener("submit", () => {});
    render();
  });
})();
