// select all show info tabs for all plant card
const Dropdown_PlantInfo = document.querySelectorAll(
  ".plant-card > article > footer"
);
const PlantInfo = document.querySelectorAll(".plant-card > article > article");
console.log(PlantInfo);
// set the height of the components
PlantInfo.forEach((article) => {
  article.style.height = `${window
    .getComputedStyle(article)
    .getPropertyValue("height")}`;
});

Dropdown_PlantInfo.forEach((footer) => {
  // add event listener to each footer to toggle visibility
  footer.addEventListener("click", () => {
    const Parent_Article = footer.closest("article");
    const Siblings = Parent_Article.querySelectorAll("article");

    // for each sibling set its height
    Siblings.forEach((article) => {
      // Note the border-wisth prop acts as a placeholder for the components true height
      if (article.style.getPropertyValue("height") == "0rem") {
        // show the plant info tab
        article.style.setProperty(
          "height",
          `${article.style.getPropertyValue("border-width")}`
        );
        article.style.setProperty("margin-top", "1rem");
        article.style.removeProperty("border-width");
      }
      // hide the plant info
      else {
        article.style.setProperty(
          "border-width",
          `${window.getComputedStyle(article).getPropertyValue("height")}`
        );
        article.style.setProperty("height", "0rem");
        article.style.setProperty("margin-top", "0.1rem");
      }
    });
  });
});
