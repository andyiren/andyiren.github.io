(function(){
  // Highlight current language in switcher + remember selection
  const htmlLang = document.documentElement.lang || "en";
  document.querySelectorAll("[data-lang-link]").forEach(a=>{
    const l = a.getAttribute("data-lang-link");
    if(l === htmlLang){ a.setAttribute("aria-current","page"); }
    a.addEventListener("click", ()=> { try { localStorage.setItem("lang", l); } catch (_) {} });
  });

  // Discourage casual copying; publicly rendered content is still retrievable.
  function editable(target) {
    return target instanceof Element && !!target.closest('input, textarea, [contenteditable="true"]');
  }
  document.addEventListener('contextmenu', event => {
    if (!editable(event.target)) event.preventDefault();
  });
  document.addEventListener('copy', event => {
    if (!editable(event.target)) event.preventDefault();
  });
  document.addEventListener('dragstart', event => {
    if (event.target instanceof HTMLImageElement) event.preventDefault();
  });
  document.querySelectorAll('img').forEach(image => image.setAttribute('draggable', 'false'));
})();
