## Based on Wowchemy's Research Group Template for [Hugo](https://github.com/gohugoio/hugo)

The [Research Group Template](https://github.com/wowchemy/starter-hugo-research-group) empowers your research group to easily create a beautiful website with a stunning homepage, news, academic publications, events, team profiles, and a contact form.

[Check out the latest demo](https://research-group.netlify.app/) of what you'll get in less than 5 minutes, or [view the showcase](https://wowchemy.com/user-stories/).

_[**Wowchemy**](https://wowchemy.com) makes it easy to create a beautiful website for free. Edit your site in Markdown, Jupyter, or RStudio (via Blogdown), generate it with Hugo, and deploy with GitHub or Netlify. Customize anything on your site with widgets, themes, and language packs._

# Contributing
For group members who would like to add/update content
1. Check existing branches for contribution category
2. Create or switch to branch
3. Edit/preview any Markdown (.md) files directly on GitHub (or clone the branch to your local machine and make edits there)
4. Once changes are committed, open a pull request
5. View website preview via Netlify build on your pull request
6. Assign a reviewer

## Advanced Contributing
For group members who would like to make larger edits
1. [Install hugo extended](https://wowchemy.com/docs/getting-started/install-hugo-extended/)
2. Clone the repository to your local machine
3. Make edits locally
4. Run `hugo server` in the top-level directory to run an interactive website server locally
5. Double check edits by running `hugo` in the top-level directory, change into `public/` folder, and run `python -m http.server` to run a local website server

For website maintainers, to finalize updates:
```bash
ssh <user>@athena.dialup.mit.edu
ssh root@hjkgrp
bash /var/www/update.sh
```
