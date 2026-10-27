(function(){
  // Highlight current language in switcher + remember selection
  const htmlLang = document.documentElement.lang || "en";
  document.querySelectorAll("[data-lang-link]").forEach(a=>{
    const l = a.getAttribute("data-lang-link");
    if(l === htmlLang){ a.setAttribute("aria-current","page"); }
    a.addEventListener("click", ()=> { try { localStorage.setItem("lang", l); } catch (_) {} });
  });
})();
