## Onboarding
1. Download/copy the `member_template.md` file in this folder
    1. Fill out the fields in curly braces, e.g. {example}
    2. The {bio} field should be a few sentences about yourself. Click on anyone's page on [our website](http://hjkgrp.mit.edu/people/) to see an example.
    3. Social links are optional
2. Pick a picture of yourself to display on the website
3. Optionally, prepare a PDF of your CV.

Once you have everything ready, open a pull request to upload your files to this GitHub. Your profile picture and markdown file should go in a new folder [here](../content/authors) labeled with your username, titled `avatar.jpg` (or `avatar.png`) and `_index.md` respectively. If you upload a CV, it should go [here](../static/files/).

This is easier to do via a local clone if you are familiar with git and GitHub, but can be done entirely via GitHub's web interface.
Step-by-step instructions on how to do this are as follows:
1. Click "Add file"->"Create new file" [here](../content/authors).
2. In the "Name your file..." field, enter your username followed by `/_index.md`.
3. Paste the contents of your filled out `member_template.md` file here.
4. Propose the changes in a new branch. To do so:
    1. At the bottom of the page, click "Create a new branch for this commit and start a pull request."
    2. Give the branch an informative name (e.g. `ppl-add-john` to indicate this is an update to people, adding John to the website)
    3. Click the "Propose new file" button.
This will take you to the "Open a pull request" page, but do not create the pull request for now.
5. Click on the name of your branch [here](https://github.com/hjkgrp/starter-hugo-research-group/branches).
6. Navigate to your newly created folder (in `content/authors/`) and upload your profile picture ("Add file"->"Upload files").
7. Optionally navigate to `static/files/` and upload your CV.
8. Open a pull request ("Compare & pull request" button) to merge your branch to the `main` branch and let the website manager know.

## Publication updates
1. Download/export (Better) BibTex citations to `publications/publications.bib` (recommended to use Zotero + manually add preprints w/o arXiv)
2. From top-level directory
    1. Run `academic import --bibtex offsite/publications/publications.bib` from top-level directory (using [Hugo Academic CLI](https://github.com/wowchemy/hugo-academic-cli/))
    2. Run `python offsite/publications/postprocess.py`
3. Manually adjust `index.md` files
    1. Change `publication_types` of preprints to `'3'`
    2. Add issue, pages, and year to `publication` such that it reads `'*journal*, **issue**, pages, (year)'`
