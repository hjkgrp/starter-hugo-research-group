#######################################################################################################
# run with python 3 from /content/tutorials/ to produce commit 6405576
# https://github.com/hjkgrp/starter-hugo-research-group/commit/6405576a971490b2ef75d2991fbffc1113e6919a
#######################################################################################################
import glob
import os
from urllib.request import urlretrieve
import re

img_extensions = ('jpeg', 'gif', 'png', 'apng', 'svg', 'bmp')

## get molsimplify tutorial folders
folders = glob.glob('*molsimplify*')
folders.sort()

for folder in folders:
    ## get markdown file
    idx_file_path = os.path.join(folder,'index.md')
    with open(idx_file_path,'r') as f:
        markdown = f.read()
    ## add molSimplify tag and category
    markdown = markdown.replace('tags:','tags:\n- molsimplify')
    markdown = markdown.replace('categories:','categories:\n- molsimplify-tutorials')
    
    ## get standard files 
    files = re.findall("(/sites.*?)\)",markdown)
    ## retrieve files
    for file in files:
        file_name = file.rsplit('/',1)[-1]
        file_url = 'http://hjkgrp.mit.edu/' + file
        file_dest = os.path.join(folder,file_name)
        if not os.path.exists(file_dest):
            urlretrieve(file_url,file_dest)
        ## update markdown string
        markdown = markdown.replace(file,file_name)
    
    ## add script downloads to the end of the file
    scripts = [file for file in files if not file.endswith(img_extensions)]
    if len(scripts) > 0:
        markdown += '**Scripts:**\n\n'
        for script in scripts:
            script_name = script.rsplit('/',1)[-1]
            markdown += f'[{script_name}]({script_name})'
    
    ## get embedded pngs
    embedded_urls = re.findall("\((data:image/png.*?)\)",markdown)
    for i, url in enumerate(embedded_urls):
        file_name = f'image_{i}.png'
        file_dest = os.path.join(folder,file_name)
        if not os.path.exists(file_dest):
            urlretrieve(url,file_dest)
        markdown = markdown.replace(url,file_name)
        
    ## write new markdown file
    with open(idx_file_path,'w') as f:
        f.write(markdown)