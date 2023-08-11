const Menu_Hamburger = document.getElementById("Hamburger");

Menu_Hamburger.addEventListener("click", () => {
  const one = Menu_Hamburger.querySelector("#one");
  const two = Menu_Hamburger.querySelector("#two");
  const three = Menu_Hamburger.querySelector("#three");
  const Menu = document.getElementById("menu");

  if (Menu_Hamburger.classList.contains("ham")) {
    Menu_Hamburger.classList.remove("ham");
    one.classList.add("ham-one");
    two.classList.add("ham-two");
    three.classList.add("ham-three");
    Menu.classList.remove("hide-menu");
  } else if (!Menu_Hamburger.classList.contains("ham")) {
    Menu_Hamburger.classList.add("ham");
    one.classList.remove("ham-one");
    two.classList.remove("ham-two");
    three.classList.remove("ham-three");
    Menu.classList.add("hide-menu");
  }
});
