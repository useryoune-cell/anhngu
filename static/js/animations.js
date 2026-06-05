const motionQuery = window.matchMedia("(prefers-reduced-motion: reduce)");

if (!motionQuery.matches) {
  document.documentElement.classList.add("motion-ready");

  const revealTargets = document.querySelectorAll(
    [
      ".idea-bunny",
      ".idea-copy",
      ".sun",
      ".map-icon",
      ".roadmap h2",
      ".timeline-area",
      ".road-list article",
      ".study-bunny",
      ".books-icon",
      ".method h2",
      ".method-grid article",
      ".reader-bunny",
      ".brain-icon",
      ".learning-map h2",
      ".cycle .node",
      ".tech .star-bunny",
      ".tech-title",
      ".pill",
      ".section-heading",
      ".testimonial-card",
      ".faq-list details",
      ".footer-brand",
      ".footer-links > div"
    ].join(",")
  );

  revealTargets.forEach((target, index) => {
    target.classList.add("reveal");
    target.style.setProperty("--reveal-delay", `${Math.min(index % 6, 5) * 80}ms`);
  });

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    {
      rootMargin: "0px 0px -12% 0px",
      threshold: 0.18
    }
  );

  revealTargets.forEach((target) => observer.observe(target));
}
