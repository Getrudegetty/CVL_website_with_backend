const menu = document.querySelector("#menu-btn");
      const nav = document.querySelector(".nav-links");

      menu.onclick = function () {
        menu.classList.toggle("fa-times");
        nav.classList.toggle("active");
      };
    // stick background
      window.onscroll = function () {
        menu.classList.remove("fa-times");
        nav.classList.remove("active");
      };
      window.addEventListener("scroll", function () {
        const header = document.querySelector("header");
        header.classList.toggle("sticky", window.scrollY > 0);
      });