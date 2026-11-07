# Oxis Landing Page (Cloned from Agen AI Framer)

A cloned and extracted asset bundle of the [Agen AI Framer site](https://agen-ai.framer.website/).

## Project Structure
- `cloned_site/index.html`: Interactive web showcase featuring all extracted graphics, icons, and components.
- `cloned_site/index_original.html`: Complete original snapshot of the Framer DOM and layout.
- `cloned_site/index_offline.html`: Localized offline version linking directly to downloaded assets.
- `extracted_assets/images/`: Extracted high-resolution PNG & JPG mockups and graphics.
- `extracted_assets/icons_svg/`: Extracted SVG icons, badges, and brand vectors.
- `extracted_assets/fonts/`: Web fonts (.woff2) extracted from the site.
- `cloned_site/assets/`: Mirrored CDN bundle with modules, scripts, and stylesheets.

## Running Locally
To launch the preview server:
```bash
python -m http.server 8080
```
Then visit:
- Showcase: [http://localhost:8080/cloned_site/](http://localhost:8080/cloned_site/)
- Direct Framer Page: [http://localhost:8080/cloned_site/index_original.html](http://localhost:8080/cloned_site/index_original.html)

