import glob
import os

folders_pattern = '../../content/tutorials/*/'

## get tutorial folders
folders = glob.glob(folders_pattern)
folders.sort()

## get thumbnails
for folder in folders:
    page_name = folder.rsplit('/',2)[-2]
    old_page_name = page_name.split('-',3)[-1]
    ## get markdown file
    idx_file_path = os.path.join(folder,'index.md')
    with open(idx_file_path,'r') as f:
        markdown = f.read()

    ## add alias for old link
    markdown = markdown.replace("subtitle:",f"subtitle:\naliases: /content/{old_page_name}\n")

    ## write new markdown file
    with open(idx_file_path,'w') as f:
        f.write(markdown)
