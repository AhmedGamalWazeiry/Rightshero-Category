// Fetches top-level categories and appends them to the DOM on page load
document.addEventListener("DOMContentLoaded", async function () {
  await fetch("/api/categories/")
    .then((response) => response.json())
    .then((data) => {
      data.forEach((category) => {
        let parentID = "categories";
        appendCategory(category, parentID, false);
      });
    })
    .catch((error) => console.error("Error:", error));
});

// Fetches or appends children categories for a given parent category ID
async function getOrCreateChildren(id, parentID) {
  await fetch(`/api/categories/${id}/`)
    .then((response) => response.json())
    .then((data) => {
      data = data.data;
      data.forEach((category) => {
        appendCategory(category, parentID, true);
      });
    })
    .catch((error) => console.error("Error:", error));
}

// Fetches all children categories for a given category ID
async function getAllChildrenByID(id) {
  const children = await fetch(`/api/categories/${id}/all/`)
    .then((response) => response.json())
    .then((data) => {
      return data.data;
    })
    .catch((error) => console.error("Error:", error));
  return children;
}

// Removes a category element by its ID
function removeCategory(categoryID) {
  const category = document.getElementById(categoryID + "parent");
  const categoryListener = document.getElementById(categoryID);
  if (category != null) {
    categoryListener.removeEventListener("change", () => {});
    category.remove();
  }
}

// Appends a category element to the DOM, with checkbox and label
function appendCategory(category, parentID, isChild) {
  const container = document.createElement("div");
  container.id = category.id + "parent";
  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.id = category.id;
  checkbox.name = category.name;

  checkbox.addEventListener("change", async function () {
    // Check if the checkbox is checked
    if (checkbox.checked) {
      await getOrCreateChildren(category.id, container.id);
    } else {
      const children = await getAllChildrenByID(category.id);

      children.forEach((child) => {
        removeCategory(child);
      });
    }
  });

  const label = document.createElement("label");
  label.htmlFor = category.id;
  label.textContent = category.name;

  container.appendChild(checkbox);
  container.appendChild(label);

  if (isChild) {
    const parent = document.getElementById(parentID);
    parent.parentNode.insertBefore(container, parent.nextSibling);
  } else {
    document.getElementById(parentID).appendChild(container);
  }
}
