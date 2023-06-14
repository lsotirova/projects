For the purpose of showcasing my project, VeggieVisionary, I have used images and recipes from https://veganuary.com/. These resources from Veganuary have been utilized to provide visual representations of vegan dishes and inspire users to explore plant-based culinary options.

## Distinctiveness and Complexity:

### Distinctiveness:

- VeggieVisionary sets itself apart from other projects in this course by its specific focus on promoting veganism. While other projects may revolve around social networks or e-commerce, VeggieVisionary stands unique in its mission to inspire and support individuals in embracing a plant-based lifestyle. By emphasizing the ethical, environmental, and health benefits of veganism, the project offers a fresh perspective and an engaging platform for users to explore the world of vegan culinary possibilities.

### Complexity:

- VeggieVisionary goes beyond the basic requirements of previous projects, demonstrating a higher level of complexity through its use of various technologies. The web application utilizes HTML5, CSS3, JavaScript, Bootstrap, and Django—a powerful Python-based web framework. This blend of technologies enables VeggieVisionary to deliver an exceptional user experience with advanced functionalities.

- The complexity of VeggieVisionary is evident in its implementation of Django models. The project features intricate models such as User, Ingredient, Category, Recipe, MyRecipes, and MyPlan, establishing relationships and enabling advanced functionalities. These models handle essential aspects like user authentication, ingredient associations, recipe categorization, saved recipes, and meal planning. By leveraging Django models, VeggieVisionary ensures robust data management and efficient server-side operations.

- JavaScript is also employed to enhance interactivity and add complexity to the project. The JavaScript code utilized in VeggieVisionary introduces features like scrolling effects, dynamic category selection, and toggling recipe likes. These interactive elements not only elevate the user experience but also showcase the project's technical complexity and attention to detail.

- Moreover, VeggieVisionary incorporates a range of functionalities that contribute to its overall complexity. The responsive navigation bar allows seamless exploration of different sections, enabling users to effortlessly access various parts of the website. The Recipes section provides extensive filtering options, empowering users to refine their search based on categories. For logged-in users, the My Recipe Vault feature allows for personalized recipe management and easy access to saved recipes. Additionally, the exclusive "My Plan" section enables logged-in users to create and manage their daily healthy meals plan, enhancing the project's functionality and complexity.

- To ensure optimal user experience across different devices, VeggieVisionary incorporates responsive design techniques and external libraries such as Bootstrap. The web application adapts gracefully to various screen sizes, guaranteeing a visually appealing and user-friendly interface regardless of the device used.

In conclusion, VeggieVisionary exemplifies distinctiveness and complexity through its unique focus on promoting veganism and its utilization of diverse technologies. The integration of Django models, the inclusion of advanced functionalities like recipe filtering and saved recipe management, the implementation of the "My Plan" feature, and the mobile-responsive design collectively contribute to the project's distinctive nature and technical complexity. VeggieVisionary stands as a remarkable web application that inspires users to embrace a plant-based lifestyle while delivering a rich and engaging user experience.

### Files and directories

- webapp - main application directory.
  - static/webapp - contains all static content.
    - styles.css - compiled CSS file.
    - webapp.js - JavaScript file used in the project.
  - templates/webapp - contains all application templates.
    - layout.html - base template. All other templates extend it.
    - index.html - main template that shows the homepage.
    - all-recipes.html - template for displaying all recipes.
    - category.html - template for displaying recipes by category.
    - login.html - template for user login.
    - my-account.html - template for user account details.
    - my-plan-form.html - template for creating a meal plan.
    - my-planner.html - template for managing the meal plan.
    - recipe-detail.html - template for displaying a single recipe.
    - register.html - template for user registration.
    - search-results.html - template for displaying search results.
  - urls.py - file containing all application URLs.
  - admin.py - added some all the models to it
  - models.py - added some models such as User, Ingredient, Category, Recipe, MyRecipes and MyPlan
  - views.py - contains all the application's views.

### Video Demo:

https://youtu.be/D3uA105opoU
