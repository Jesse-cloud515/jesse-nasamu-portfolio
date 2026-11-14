# Jesse Nasamu — portfolio

A static portfolio site: plain HTML, CSS and JavaScript with no framework and no runtime dependencies. Pages are generated from one content file by a small Python script, so the header, footer and project pages stay consistent.

## What's here

```
index.html                     Home: hero, work, about, skills, experience, services, testimonials, contact
work/<project>/index.html      One page per project, including the Cybersecurity Threat Intelligence Dashboard case study
404.html, sitemap.xml, robots.txt
assets/css/style.css           All styles
assets/js/main.js              Menu, work-list preview, gallery lightbox, contact form
assets/fonts/                  Schibsted Grotesk (self-hosted, SIL Open Font License)
assets/img/                    Optimised WebP images (800px and 1600px), favicons, Open Graph image
assets/files/jesse-nasamu-cv.pdf
_src/content.py                ALL text and project data. Edit this.
_src/build.py                  Generates the HTML pages from content.py
_src/images.py                 Converts original images into the optimised WebP sizes
```

## Editing content

1. Open `_src/content.py` and change the text, add a project or fill in an empty field.
2. From the project folder run: `python3 _src/build.py`
3. Commit and push the regenerated `.html` files.

Story fields left empty (`""` or `[]`) are not shown on the page, so there are never empty headings.

### Where the project content came from

- **Cybersecurity Threat Intelligence Dashboard:** `Cybersecurity Attacks Analysis – Final Report.pdf`, the project README and its images (Documents\Data Analysis\Project\Cyber Security Attacks). The report PDF is also offered as a download on the case study.
- **Bike sales, retail/regional sales, customer segmentation, global layoffs, fraud detection:** the write-ups (.docx/.pdf) and dashboard images in the same Project folder, plus the CV.
- Portrait: `profile-imga.jpg` from your old GitHub portfolio folder.

Adding a new image for any project: put the original in a folder and add it to the `MAP` in `_src/images.py`, then run `python3 _src/images.py <original-img-folder> .` (needs `pip install pillow`).

## Contact form

The form posts to [FormSubmit](https://formsubmit.co), which works on static hosting such as GitHub Pages with no server code.

1. Deploy the site, then send yourself one test message through the form.
2. FormSubmit emails **nasamujesse@gmail.com** an activation link. Click it. Messages are delivered from then on.
3. Optional: FormSubmit then gives you a random alias. Replace the email in `form_endpoint` in `content.py` with that alias so your address isn't in the page source, and rebuild.

If a send fails, visitors see an error message with your email address as a fallback. The page never reports success unless FormSubmit confirms it.

To use Formspree instead, create a form there, set `form_endpoint` to `https://formspree.io/f/<your-id>` and change the success check in `assets/js/main.js` from `String(body.success) === "true"` to `res.ok`.

## Previewing locally

Open `index.html` directly, or for exact behaviour run a local server:

```
python3 -m http.server 8000
```

and visit http://localhost:8000. (The 404 page uses absolute `/portfolio/` paths for GitHub Pages, so it only looks right once deployed.)

## Deploying to GitHub Pages

The site is set up for `https://jesse-cloud515.github.io/portfolio/`.

1. In your `portfolio` repository, replace the old files with the contents of this folder (keep a copy of the old site, e.g. in a branch named `old-site`).
2. Commit and push to the default branch.
3. In the repository go to **Settings → Pages**, set **Source** to "Deploy from a branch", choose the default branch and `/ (root)`, and save.
4. Wait a minute, then open the site and send a test message to activate the form.

Hosting somewhere else (Netlify, Vercel, cPanel)? Change `base_url` in `content.py`, rebuild, and upload everything except `_src/`. Folders starting with `_` are ignored by GitHub Pages automatically.

## What changed from the old site

- Replaced the BootstrapMade "FolioOne" template and ten vendor libraries with about 35 KB of hand-written CSS and JS.
- Removed leftover template content: lorem ipsum, the placeholder "Apple Inc." job, the sample service-details page, fake stats and stock testimonial photos.
- Removed skill percentages, which had no evidence behind them.
- Images reduced from ~41 MB to ~3 MB.
- Added the Cybersecurity Threat Intelligence Dashboard case study (real findings, response chart, findings table, recommendations, lessons) and individual pages for each project, with findings from your project reports.
- Updated experience and credentials from the latest CV (Zap24, Galaxy Backbone end date, certificates).
- Added page titles, meta descriptions, Open Graph tags, structured data, a sitemap and robots.txt.
