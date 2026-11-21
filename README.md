# lundq163.github.io

Personal academic website of Jacob Lundquist, live at https://lundq163.github.io.

Built with [Hugo](https://gohugo.io) using a customized [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme, adapted from Pascal Michaillat's [hugo-website](https://github.com/pmichaillat/hugo-website) template.

## Layout

- `config.yml`: site settings, home-page bio, menu, and social/profile links
- `content/papers/`, `content/projects/`: the Papers and Projects pages
- `static/`: files served as-is (`cv.pdf`, `picture.jpeg`, favicons, fonts, `files/` for PDFs)
- `layouts/`, `assets/css/`: overrides of the PaperMod theme in `themes/PaperMod/`
- `archetypes/`: templates for new content (`hugo new papers/my-paper.md`)
- `data/venues.yaml`: publisher/journal logos for papers (a paper picks one with `venue:`)
- `scripts/fetch_citations.py`: pulls citation counts from OpenAlex into `data/citations.json` (gitignored)

## Local development

```sh
brew install hugo                  # once
python3 scripts/fetch_citations.py # optional: citation counts
hugo server                        # preview at http://localhost:1313
```

## Deployment

Pushing to `main` triggers `.github/workflows/hugo.yml`, which builds the site and deploys it to GitHub Pages. Build output (`public/`, `resources/`) is not committed; CI builds it fresh. The workflow also runs on the 1st of each month to refresh citation counts from OpenAlex; if OpenAlex is unreachable the site still builds, just without the counts. Keep the Hugo version in the workflow in step with your local `hugo version`.
