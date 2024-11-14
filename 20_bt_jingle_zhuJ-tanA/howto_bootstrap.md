# how-to :: BOOTSTRAP
---
## Overview
Bootstrap is a very useful CSS styling tool with prebuilt display functions (components, utilities, layout, etc.) that save developers the time to write intensive CSS codes. This guide will demonstrate some core features of Bootstrap, including 

### Estimated Time Cost: 1 hr

### Prerequisites:

- Create a html file with a header and body
- Install Bootstrap via package manager or include via CDN (Content Delivery Network) inside html file

### Procedure:
1. You can install via package manager:

    `$ npm install bootstrap@5.3.3`

    `$ gem install bootstrap -v 5.3.3`

   OR
   
    Include via CDN (Place the `<link>` tag in the `<head>`):
    ```
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Bootstrap demo</title>
      </head>
      <body>
        <h1>Hello, world!</h1>
      </body>
    </html>
    ```
1. If you plan to use dropdowns, popovers, or tooltips, place the `<script>` tag for JavaScript bundle before `</body>`:
    ```
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
    ```

### Creating a Navbar
1. Open and close nav tags: `<nav class="navbar"></nav>`
2. Vertically align (or stack) the navbar by adding `navbar-expand{-sm|-md|-lg|-xl}` as a class
    - Adding a size after "expand" will specify smaller than which sizes the navbar will collapse
    - Excluding a size will always collapse the navbar
3. Open and close div tags in the nav tags to contain links : `<div class=collapse navbar-collapse"></div>`
    - Assigning the collapse class will specify what collapses
4. Open an ordered list with ul tags indide the div tags: `<ul class="navbar-nav"></ul>`
    - Adding a `me-auto` class will auto-adjust margins
5. Create list objects for the nav bar with li and hyperlink tags inside the ul tags: `<li class="nav-item"><a class="nav-link"></a></li>`
     - Add the active class to the page currently open
     - Adding the "dropdown" class to an "li" tag will enable dropdown options:
         ```
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
         ```
6. Create a Search bar and Search button:
    ```
    <form class="d-flex">
      <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success" type="submit">Search</button>
    </form>
    ```
    
### Creating a grid
- Add `<div class="row"></div>` for all content that will be horizontally aligned together
- Add `<div class="col"></div>` for all content that will be vertically aligned
- Rows and columns can be put inside each other and vice versa
    - The broader class will take precedence
- Sizes can be added to rows and columns with `-{numeric size}`

### Resources
* [Bootstrap](https://getbootstrap.com)
 
---

Accurate as of (last update): 2024-11-14

#### Contributors:  
Amanda Tan, pd4  
Michelle Zhu, pd4

