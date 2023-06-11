let nav_btn = document.getElementById("nav-display");
let navbar = document.getElementById("navbar");

nav_btn.addEventListener("click", showNav);

function showNav()
{
    navbar.classList.toggle("show");
}