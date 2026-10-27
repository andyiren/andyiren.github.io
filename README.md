# Yi-dong portfolio

Static HTML/CSS/JavaScript for GitHub Pages. Production domain: `yi-dong.net`.

## Release

Development branch: `restore-cargo-frame`. Review the HTML/CSS and local assets before merging into `main`. Preserve the root `CNAME` file. No Node build or paid service is required; Pages can publish the repository root.

This release restores nine Design covers and two complete project sources, adds a short four-language Information biography, and provides responsive navigation and larger type. Photography awaits the owner's selected images. Other Design covers have no detail links until the original content is supplied. Project body text uses the original English in all languages.

## Preview

Run `python -m http.server 8766 --bind 127.0.0.1` from this folder, then open `http://127.0.0.1:8766/en/`. Local preview is available on the computer running the server; production uses the same responsive pages on every device.

## Content tools

The site itself has no runtime dependencies. Optional maintenance scripts require `beautifulsoup4`: `python -m pip install beautifulsoup4`.

- `python check_design.py` verifies Design links, language routes and image counts.
- `python update_information.py` generates the four Information pages from its shared biography copy.
- `python restore_design.py` reimports the original Cargo exports from the parent folder. It replaces Design content, so use it only when deliberately reimporting those sources.

No CV PDF or personal contact/reference details are included in the published files.
