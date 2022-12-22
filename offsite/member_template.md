---
# fill out fields in {}, deleting the {}
# e.g. {your name} --> John Doe
# choose one for fields with entries separated by |

# Display name
title: {your name}

# Username (this should match the folder name)
authors:
  - {kerberos}

# Role/position
role: {Graduate Student|Postdoctoral Associate|Course {MIT course numeral} UROP|Masters Student}

# Is this the primary user of the site?
superuser: false

# Organizations/Affiliations
organizations:
- name: Massachusetts Institute of Technology
  url: ""

interests:
- {interest 1}
- {interest 2}
- {interest 3}

# remove the second course if you do not have multiple degrees (i.e. are not a postdoc/do not have a Master's)
education:
  courses:
  - course: {degree title}
    institution: {degree institution}
    year: {graduation year}
  - course: {degree title}
    institution: {degree institution}
    year: {graduation year}



# Social/Academic Networking
# For available icons, see: https://sourcethemes.com/academic/docs/page-builder/#icons
#   For an email link, use "fas" icon pack, "envelope" icon, and a link in the
#   form "mailto:your-email@example.com" or "#contact" for contact widget.
social:
# - icon: envelope
#   icon_pack: fas
#   link: 'mailto:{kerberos} AT mit DOT edu'
# - icon: twitter
#   icon_pack: fab
#   link: https://twitter.com/{twitter handle}
# - icon: google-scholar
#   icon_pack: ai
#   link: https://scholar.google.com/citations?user={id}
# - icon: github
#   icon_pack: fab
#   link: https://github.com/{GitHub username}
# - icon: linkedin
#   icon_pack: fab
#   link: https://www.linkedin.com/in/{LinkedIn ID}
# Link to a PDF of your resume/CV from the About widget.
# To enable, copy your resume/CV to `static/files/cv.pdf` and uncomment the lines below.
# - icon: cv
#   icon_pack: ai
#   link: files/CV_{initials}.pdf


# Highlight the author in author lists? (true/false)
highlight_name: false

# Organizational groups that you belong to (for People widget)
#   Set this to `[]` or comment out if you are not using People widget.
user_groups:
- {Grad Students|Postdocs|Undergraduate Students|Masters Students}
---

{bio}
