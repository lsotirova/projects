window.addEventListener("scroll", function () {
  var navbar = document.querySelector(".navbar");

  if (window.scrollY > 0) {
    navbar.classList.add("navbar-scroll");
  } else {
    navbar.classList.remove("navbar-scroll");
  }
});

document.addEventListener("DOMContentLoaded", function () {
  var ingredientTags = document.querySelectorAll(".form-check-label");

  ingredientTags.forEach(function (tag) {
    tag.addEventListener("click", function () {
      console.log("clicked");
      this.classList.toggle("ingredient-tag-clicked");
    });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  var selectElement = document.getElementById("category");
  var selectedOption = selectElement.options[selectElement.selectedIndex];
  var selectedCategoryName = selectedOption.text;

  // Check if there is a previously selected category in localStorage
  var storedCategory = localStorage.getItem("selectedCategory");
  if (storedCategory) {
    // Set the selected category from localStorage
    selectElement.value = storedCategory;
    selectedCategoryName =
      selectElement.options[selectElement.selectedIndex].text;
  }

  selectElement.addEventListener("change", function () {
    selectedOption = selectElement.options[selectElement.selectedIndex];
    selectedCategoryName = selectedOption.text;

    // Store the selected category in localStorage
    localStorage.setItem("selectedCategory", selectElement.value);

    this.form.submit();
  });

  // Clear the selected category from localStorage when the form is submitted
  var form = selectElement.form;
  form.addEventListener("submit", function () {
    localStorage.removeItem("selectedCategory");
  });
});

function recipeFunction(id, recipe_liked_ids) {
  const btnRecipe = document.getElementById(`${id}`);
  console.log("recipe_liked_ids:", recipe_liked_ids); // Check the value of recipe_liked_ids variable
  console.log("recipe_id:", id);
  let liked = recipe_liked_ids.includes(id);

  fetch(`/toggle_my_recipes/${id}`)
    .then((response) => response.json())
    .then((result) => {
      console.log("result:", result); // Check the value of the result from the server
      recipe_liked_ids = result.recipe_liked_ids;
      console.log("updated recipe_liked_ids:", recipe_liked_ids); // Check the updated value of recipe_liked_ids
      liked = recipe_liked_ids.includes(id);

      if (liked) {
        btnRecipe.innerText = "Remove from My Recipes";
        btnRecipe.classList.remove("btn-success");
        btnRecipe.classList.add("btn-warning");
      } else {
        btnRecipe.innerText = "Add to My Recipes";
        btnRecipe.classList.add("btn-success");
        btnRecipe.classList.remove("btn-warning");
      }
    });
}
// JavaScript/jQuery code to handle the category button click event
$(document).ready(function () {
  $(".category-button").on("click", function () {
    var categoryId = $(this).attr("id").split("Button")[0];
    fetchRecipes(categoryId);
    console.log("hello");
  });
});

// my_plan.js
