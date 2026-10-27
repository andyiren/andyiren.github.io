(function(){
  const supported = ["en","zh","ja","de"];
  function pickLang(){
    let saved; try { saved = localStorage.getItem("lang"); } catch (_) {}
    if(saved && supported.includes(saved)) return saved;
    const n = (navigator.language || "en").toLowerCase();
    if(n.startsWith("zh")) return "zh";
    if(n.startsWith("ja")) return "ja";
    if(n.startsWith("de")) return "de";
    return "en";
  }
  window.__pickLang = pickLang;
})();
