console.log("JS loaded")

/*
  Mobile nav
*/
const mobileMenuButton = document.querySelector("#mobile-menu-button")
const mobileMenu = document.querySelector("#mobile-menu")
const closeMobileMenu = document.querySelector("#close-mobile-menu")
const openMobileMenu = document.querySelector("#open-mobile-menu")

if (mobileMenuButton) {
  mobileMenuButton.addEventListener("click", () => {
    mobileMenu.classList.toggle("hidden")
    closeMobileMenu.classList.toggle("hidden")
    openMobileMenu.classList.toggle("block")
    openMobileMenu.classList.toggle("hidden")
  })
}