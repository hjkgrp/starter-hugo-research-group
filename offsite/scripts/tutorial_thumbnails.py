import glob
import os
import urllib.request
import re

old_domain = 'http://hjkgrp.mit.edu/content/'
img_extensions = ('.jpg', '.png')  # allowed thumbnail extensions
folders_pattern = '../../content/tutorials/*/'

## get tutorial folders
folders = glob.glob(folders_pattern)
folders.sort()

## get thumbnails
for folder in folders:
    page_name = folder.rsplit('/',2)[-2]
    old_page_name = page_name.split('-',3)[-1]
    old_page_url = old_domain + old_page_name
    with urllib.request.urlopen(old_page_url) as response:
        html = response.read().decode('utf-8')
    matches = re.findall('"(http://.+?thumbnail.+?)"',html)
    if len(matches) == 1:
        thumbnail_url = matches[0]
    elif len(matches) == 0:
        print(f'{old_page_name}: Thumbnail not found')
        continue
    else:
        print(f'{old_page_name}: Multiple matches found')
        continue
    ## post process url
    thumbnail_url = thumbnail_url.replace('styles/thumbnail/public/','')
    print(thumbnail_url)
    img_extension = [ext for ext in img_extensions if ext in thumbnail_url][0]
    ## save thumbnail as featured.ext
    file_dest = os.path.join(folder,f'featured{img_extension}')
    if not os.path.exists(file_dest):
        urllib.request.urlretrieve(thumbnail_url,file_dest)
