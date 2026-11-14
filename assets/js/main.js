/* Jesse Nasamu portfolio — progressive enhancement only. The site works without JavaScript. */
(() => {
  "use strict";
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* Header: solid background once the page scrolls */
  const header = $("[data-header]");
  if (header) {
    const onScroll = () => header.classList.toggle("is-solid", window.scrollY > 24);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* Mobile menu */
  const menuBtn = $("[data-menu]");
  const nav = $("#nav");
  if (menuBtn && nav) {
    const setOpen = (open) => {
      menuBtn.setAttribute("aria-expanded", String(open));
      nav.classList.toggle("is-open", open);
    };
    menuBtn.addEventListener("click", () => setOpen(menuBtn.getAttribute("aria-expanded") !== "true"));
    nav.addEventListener("click", (e) => { if (e.target.closest("a")) setOpen(false); });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && nav.classList.contains("is-open")) { setOpen(false); menuBtn.focus(); }
    });
  }

  /* Highlight the nav link (or case-study contents link) for the section in view */
  const spy = (links) => {
    const map = new Map();
    links.forEach((a) => {
      const id = a.getAttribute("href").split("#")[1];
      const el = id && document.getElementById(id);
      if (el) map.set(el, a);
    });
    if (!map.size || !("IntersectionObserver" in window)) return;
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) {
          links.forEach((l) => l.removeAttribute("aria-current"));
          map.get(en.target).setAttribute("aria-current", "true");
        }
      });
    }, { rootMargin: "-40% 0px -55% 0px" });
    map.forEach((_, el) => io.observe(el));
  };
  if (document.body.classList.contains("home")) spy($$(".nav ul a"));
  spy($$(".cs-toc a"));

  /* Work list: image preview follows the pointer on desktop */
  const preview = $("[data-cursor-preview]");
  const list = $("[data-worklist]");
  if (preview && list && window.matchMedia("(pointer: fine)").matches && !reduceMotion) {
    let x = 0, y = 0, cx = 0, cy = 0, raf = 0;
    const tick = () => {
      cx += (x - cx) * 0.18; cy += (y - cy) * 0.18;
      preview.style.left = cx + 24 + 176 + "px";
      preview.style.top = cy + "px";
      raf = Math.abs(x - cx) + Math.abs(y - cy) > 0.5 ? requestAnimationFrame(tick) : 0;
    };
    list.addEventListener("pointermove", (e) => {
      x = e.clientX; y = e.clientY;
      if (!raf) raf = requestAnimationFrame(tick);
    });
    $$(".work-row", list).forEach((row) => {
      const src = row.dataset.preview;
      row.addEventListener("pointerenter", (e) => {
        if (!src) { preview.classList.remove("is-on"); return; }
        if (!preview.classList.contains("is-on")) { cx = x = e.clientX; cy = y = e.clientY; tick(); }
        preview.src = src;
        preview.classList.add("is-on");
      });
    });
    list.addEventListener("pointerleave", () => preview.classList.remove("is-on"));
  }

  /* Work filters */
  const filters = $("[data-filters]");
  if (filters && list) {
    filters.hidden = false;
    const items = $$("li", list);
    filters.addEventListener("click", (e) => {
      const b = e.target.closest("[data-filter]");
      if (!b) return;
      $$("[data-filter]", filters).forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
      const f = b.dataset.filter;
      items.forEach((li) => { li.hidden = f !== "all" && !(li.dataset.tags || "").split(" ").includes(f); });
    });
  }

  /* Case study: response bars grow once when they come into view */
  const bars = $("[data-bars]");
  if (bars) {
    if (reduceMotion || !("IntersectionObserver" in window)) bars.classList.add("is-in");
    else {
      const io = new IntersectionObserver((en) => {
        if (en.some((x) => x.isIntersecting)) { bars.classList.add("is-in"); io.disconnect(); }
      }, { threshold: 0.4 });
      io.observe(bars);
    }
  }

  /* Lightbox for the graphic design gallery */
  const lb = $("[data-lb]");
  if (lb) {
    const img = $("[data-lb-img]", lb);
    const cap = $("[data-lb-cap]", lb);
    const closeBtn = $(".lb-close", lb);
    let opener = null;
    const close = () => {
      lb.hidden = true;
      document.body.style.overflow = "";
      img.removeAttribute("src");
      if (opener) opener.focus();
    };
    $$("[data-lightbox]").forEach((btn) => btn.addEventListener("click", () => {
      opener = btn;
      img.src = btn.dataset.lightbox;
      img.alt = btn.querySelector("img")?.alt || "";
      cap.textContent = btn.dataset.caption || "";
      const link = $("[data-lb-link]", lb);
      link.hidden = !btn.dataset.link;
      if (btn.dataset.link) link.href = btn.dataset.link;
      lb.hidden = false;
      document.body.style.overflow = "hidden";
      closeBtn.focus();
    }));
    closeBtn.addEventListener("click", close);
    lb.addEventListener("click", (e) => { if (e.target === lb) close(); });
    document.addEventListener("keydown", (e) => {
      if (lb.hidden) return;
      if (e.key === "Escape") close();
      if (e.key === "Tab") { e.preventDefault(); closeBtn.focus(); }
    });
  }

  /* Contact form: validates, then sends to the form endpoint and reports the real result */
  const form = $("[data-form]");
  if (form) {
    const status = $("[data-status]", form);
    const submit = $("[data-submit]", form);
    const email = form.dataset.fallbackEmail || "nasamujesse@gmail.com";
    const messages = {
      name: "Enter your name.",
      email: "Enter an email address like name@example.com so I can reply.",
      message: "Write a short message so I know how I can help.",
    };
    const setError = (field, msg) => {
      const id = field.id + "-err";
      let el = document.getElementById(id);
      if (msg) {
        if (!el) {
          el = document.createElement("p");
          el.id = id; el.className = "field-error";
          field.insertAdjacentElement("afterend", el);
        }
        el.textContent = msg;
        field.setAttribute("aria-invalid", "true");
        field.setAttribute("aria-describedby", id);
      } else if (el) {
        el.remove();
        field.removeAttribute("aria-invalid");
        field.removeAttribute("aria-describedby");
      }
    };
    const validate = () => {
      let first = null;
      ["name", "email", "message"].forEach((n) => {
        const f = form.elements[n];
        const v = f.value.trim();
        const bad = !v || (n === "email" && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v));
        setError(f, bad ? messages[n] : "");
        if (bad && !first) first = f;
      });
      return first;
    };
    $$("input, textarea", form).forEach((f) => f.addEventListener("input", () => {
      if (f.getAttribute("aria-invalid")) validate();
    }));

    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      status.className = "form-status";
      status.textContent = "";
      const bad = validate();
      if (bad) { bad.focus(); return; }
      if (form.elements._honey.value) return; // bot

      const data = {
        name: form.elements.name.value.trim(),
        email: form.elements.email.value.trim(),
        topic: form.elements.topic.value,
        message: form.elements.message.value.trim(),
        _subject: `Portfolio enquiry: ${form.elements.topic.value} from ${form.elements.name.value.trim()}`,
        _replyto: form.elements.email.value.trim(),
        _template: "table",
      };
      submit.disabled = true;
      const label = submit.textContent;
      submit.textContent = "Sending…";
      try {
        const ctrl = new AbortController();
        const timer = setTimeout(() => ctrl.abort(), 15000);
        const res = await fetch(form.action, {
          method: "POST",
          headers: { "Content-Type": "application/json", Accept: "application/json" },
          body: JSON.stringify(data),
          signal: ctrl.signal,
        });
        clearTimeout(timer);
        const body = await res.json().catch(() => ({}));
        const ok = res.ok && String(body.success) === "true";
        if (!ok) throw new Error(body.message || `Request failed with status ${res.status}`);
        status.classList.add("is-ok");
        status.textContent = `Message sent. I'll reply to ${data.email}.`;
        form.reset();
      } catch (err) {
        status.classList.add("is-err");
        status.innerHTML = "";
        status.append(
          "Your message didn't send. Check your connection and try again, or email me directly at ",
          Object.assign(document.createElement("a"), { href: `mailto:${email}`, textContent: email }),
          "."
        );
        console.warn("Contact form:", err.message);
      } finally {
        submit.disabled = false;
        submit.textContent = label;
      }
    });
  }
})();
