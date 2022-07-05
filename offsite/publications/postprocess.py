import glob
import os
import re


# paths
basepath = os.getcwd()
# search for content folder
for i in range(2):
    content_folder = os.path.join(basepath,'content')
    if os.path.exists(content_folder):
        break
    else:
        basepath = basepath = os.path.dirname(basepath)

authors_folder = os.path.join(content_folder,'authors')
author_mds = glob.glob(os.path.join(authors_folder,"*","_index.md"))
pub_folder = os.path.join(content_folder,'publication')
pub_mds = glob.glob(os.path.join(pub_folder,"*","index.md"))

# initialize dictionary for mapping author names to usernames
author_dict = {"first": {}, "last": {}}
name_re = re.compile("title: (.+?)\n")

for author_md in author_mds:
    # get username from folder name
    author = os.path.basename(os.path.dirname(author_md))
    with open(author_md,'r') as f:
        markdown = f.read()
    # search markdown for actual name
    names = name_re.search(markdown).group(1).split()
    # save in dictionary
    first_name = names[0]
    last_name = names[-1]
    author_dict['first'][first_name] = author
    author_dict['last'][last_name] = author

# define alternate first name for Heather
author_dict['first']['H.'] = 'admin'
# save dictionaries separately
first_names = author_dict['first']
last_names = author_dict['last']


# postprocess markdown files
for pub_md in pub_mds:
    with open(pub_md,'r') as f:
        markdown = f.readlines()
    # flag for if in the authors section
    in_authors = False
    for i, line in enumerate(markdown):
        if 'authors:' in line:
            in_authors = True
            continue
        if not(in_authors):
            continue
        if ":" in line:
            break
        # get name currently entered
        name = line.split()
        last_name = name[-1]
        first_name = name[1]
        # check if in author dict
        if not last_name in last_names:
            continue
        if not first_name in first_names:
            continue
        # if first and last name both match a username
        if first_names[first_name] == last_names[last_name]:
            # replace name with username
            markdown[i] = f"- {first_names[first_name]}\n"
    with open(pub_md,'w') as f:
        f.writelines(markdown)