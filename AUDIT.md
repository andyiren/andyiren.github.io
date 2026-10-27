# Yi-dong repository audit — 2026-10-27

## Verified repository and deployment
- Public repository: https://github.com/andyiren/andyiren.github.io
- Default branch: main. GitHub API reports has_pages=true.
- Cloned production reference: 6efd20e (logo navigation). The code contains the v4 three-column header and its CSS overrides; no ZIP checksum exists to prove exact v4 identity.
- Local development branch: restore-cargo-frame. No push or production changes performed.
- Root CNAME: yi-dong.net. Root index redirects using browser language after saved preference; noscript already redirects to English.
- DNS A: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153. www CNAME: andyiren.github.io.
- HTTPS root request returned 200 with normal certificate validation.
- Pages source branch/folder, deployed commit, www HTTPS redirect, AAAA and mail records remain unverified. Do not alter DNS based on this report.

## Structure
21 HTML documents: root redirect plus five pages per language (index, information, photography, two projects). Shared css/style.css, js/lang.js, js/main.js and CNAME. No build system or workflow in the checkout. The original workspace is a set of three Cargo browser exports, not a Git repository. The actual repository is cloned into live-site/.

## Content and links
- Four homepages have five entries each; every thumbnail anchor is empty, so no portfolio cover image displays.
- Missing pages: skywalk-landscape.html, library.html and projects/photography.html in each language: 12 unique missing targets, 24 references. Full details: audit-broken-links.json.
- Photography and Information have placeholder content; non-English project introductions remain placeholders.
- Original homepage contains nine design projects. Only Sequence House and Day-care have local detail exports. Seven other project detail pages, Photography and Information need source content.
- Earlier extraction counted seven URLs per project, but two are the shared Logo and random-navigation arrow. Actual project galleries contain five unique work images each. Original HTML also includes layout, captions and interspersed prose that the flat migrated galleries do not preserve.
- English introductions are abbreviated; preserve and reparse original project DOM before completing content migration.
- No duplicate site header found by source inspection; a separate project introduction header is valid. A full HTML validator has not been run.

## External dependencies and original design
- Original exports reference freight.cargo.site for media originals, type.cargo.site for Plex Mono, Plex Sans and Tratex, and static.cargo.site for Icons and Cargo runtime/modules.
- Production code relies on freight.cargo.site for Logo, favicon and all project images. It has no local media directory before this branch.
- Original frame: left Logo (~94px in saved desktop snapshot), centered Design/Photography, right Information. Original header is pinned; migration header is in normal flow.
- Original CSS includes Plex Mono body text and Tratex headings. Migration uses system monospace. Accurate font acquisition/licensing and visual comparison remain pending.
- Black background is confirmed. Preserve requested #be002f for now; exported header selectors include black link colors, so red must not be described as independently verified from original CSS.
- Migration introduced bordered rounded cards, rounded gallery images, fixed 4:3 empty thumbnail areas and stacked mobile navigation. Original images use mixed proportions and individual grid placement.
- No desktop/mobile browser visual QA completed in this pass. Changes below are first-pass source fixes, not a completed visual match.

## Changes on development branch
- Local shared assets/logo.png copied from the user's Cargo export; all HTML Logo URLs now use it.
- Removed incorrectly extracted Logo/arrow from the eight project galleries.
- Language links now point to the same project/information/photography in the chosen language, including when JavaScript is disabled.
- localStorage reads/writes tolerate unavailable storage.
- Site header and project introduction have explicit distinct classes; project margin selectors no longer affect site navigation.
- Removed card/gallery borders and rounding; kept three header columns on narrow screens with smaller Logo/type. Browser review still required before release.
- CNAME and production branch unchanged. Remaining favicon/project media CDN dependencies intentionally reported, not silently declared solved.

## Recommended architecture
Use a small dependency-light static generator with shared templates (header, project, gallery) and structured project data keyed by stable slug. Keep English source and translations together per project, and store ordered images, captions, widths and original grid placements in data. Emit the current /en/, /zh/, /ja/, /de/ URLs as ordinary HTML so GitHub Pages remains compatible. Generate hreflang/canonical metadata and same-content language links at build time. Keep assets local; never require client JavaScript to render navigation. Choose generator only after reviewing the first visual restoration, rather than changing URLs or infrastructure now.

## Priorities and validation
P0: establish deployed SHA and Pages settings; resolve the 12 missing targets using real content or remove invalid entry links; restore actual cover images; localize all owned media; review desktop and mobile screenshots.
P1: restore original gallery layout/captions/prose and pinned frame, verify fonts; implement shared static templates; supply approved Information/Photography source and full natural translations.
P2: image dimensions/responsive sources, accessible alt text, landmarks/keyboard checks, metadata/hreflang/sitemap, documented content update command.

Checks performed: local absolute href/src target audit, source review of all page types and language code, git diff --check. Remaining broken links are baseline content gaps, recorded in JSON. No commit, push, DNS change or deployment performed.
## Design restoration update
Four Design homepages now show all nine original covers. Only the two available project details are linked; missing detail covers are preserved without invalid links. All twelve Design pages pass local link/media checks and use local assets. Both projects restore original source content across all languages, explicitly marked English until translations are prepared. Desktop homepage and 390px mobile homepage/Sequence House were visually reviewed. Photography and Information are outside this change's content scope. Production remains unchanged.

## Release preparation — 2026-10-28
Larger type and responsive two-row phone navigation implemented. Information biography verified against the original CV PDF, translated into four languages; no private address, phone or referee contact included. Viewport widths 320, 430, 768 and 1280 checked without horizontal overflow. Current whole-site internal link audit: zero missing targets. Photography content remains pending the owner's photo selection. Prepared locally for release; no production push performed.
