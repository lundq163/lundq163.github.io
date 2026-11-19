# lundq163.github.io

Personal academic website of Jacob Lundquist, live at https://lundq163.github.io.

Built with [Hugo](https://gohugo.io) using a customized [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme, adapted from Pascal Michaillat's [hugo-website](https://github.com/pmichaillat/hugo-website) template.

## Layout

- `config.yml`: site settings, home-page bio, menu, and social/profile links
- `content/papers/`, `content/projects/`: the Papers and Projects pages
- `static/`: files served as-is (`cv.pdf`, `picture.jpeg`, favicons, fonts, `files/` for PDFs)
- `layouts/`, `assets/css/`: overrides of the PaperMod theme in `themes/PaperMod/`
- `archetypes/`: templates for new content (`hugo new papers/my-paper.md`)

## Local development

```sh
brew install hugo   # once
hugo server         # preview at http://localhost:1313
```

## Deployment

Pushing to `main` triggers `.github/workflows/hugo.yml`, which builds the site and deploys it to GitHub Pages. Build output (`public/`, `resources/`) is not committed; CI builds it fresh. Keep the Hugo version in the workflow in step with your local `hugo version`.
