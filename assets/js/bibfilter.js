document.addEventListener("DOMContentLoaded", function () {
  const filterButtons = document.querySelectorAll(".bib-filter");
  const bibliographyItems = document.querySelectorAll(".bibliography > li");

  const clearBibSearch = () => {
    const searchInput = document.getElementById("bibsearch");

    if (searchInput) {
      searchInput.value = "";
    }

    if (CSS.highlights) {
      CSS.highlights.clear();
    }

    if (window.location.hash) {
      history.replaceState(
        null,
        "",
        `${window.location.pathname}${window.location.search}`
      );
    }

    document
      .querySelectorAll(".bibliography, .unloaded")
      .forEach((element) => element.classList.remove("unloaded"));
  };

  const updateBibliographyGroups = () => {
    document.querySelectorAll("h2.bibliography").forEach((heading) => {
      let iterator = heading.nextElementSibling;
      let hasVisiblePublications = false;

      while (iterator && iterator.tagName !== "H2") {
        if (iterator.tagName === "OL") {
          const list = iterator;
          const items = list.querySelectorAll(":scope > li");
          const hiddenItems = list.querySelectorAll(":scope > li.unloaded");
          const groupingElement = list.previousElementSibling;

          const allItemsHidden =
            items.length === 0 || hiddenItems.length === items.length;

          list.classList.toggle("unloaded", allItemsHidden);

          if (groupingElement) {
            groupingElement.classList.toggle("unloaded", allItemsHidden);
          }

          if (!allItemsHidden) {
            hasVisiblePublications = true;
          }
        }

        iterator = iterator.nextElementSibling;
      }

      heading.classList.toggle("unloaded", !hasVisiblePublications);
    });
  };

  const filterItems = (selectedTag) => {
    bibliographyItems.forEach((item) => {
      const publication = item.querySelector(".row[data-tag]");

      const itemTags = (
        publication && publication.dataset
          ? publication.dataset.tag || ""
          : ""
      )
        .toLowerCase()
        .split(/[\s,;]+/)
        .map((tag) => tag.trim())
        .filter(Boolean);
        
      const matches =
        selectedTag === "all" ||
        selectedTag === "" ||
        itemTags.includes(selectedTag);

      item.classList.toggle("unloaded", !matches);
    });

    updateBibliographyGroups();
  };

  const setActiveButton = (selectedTag) => {
    filterButtons.forEach((button) => {
      const buttonTag = (button.dataset.filter || "").toLowerCase();
      const isActive = buttonTag === selectedTag;

      button.classList.toggle("active", isActive);
      button.setAttribute("aria-pressed", isActive ? "true" : "false");
    });
  };

  filterButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const selectedTag = (this.dataset.filter || "all").toLowerCase();

      clearBibSearch();
      setActiveButton(selectedTag);
      filterItems(selectedTag);
    });
  });

  setActiveButton("all");
  filterItems("all");
});