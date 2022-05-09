---
widget: slider
headless: true  # This file represents a page section.

# ... Put Your Section Options Here (section position etc.) ...
# Activate this widget? true/false
active: true

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 15

# Slide interval.
# Use `false` to disable animation or enter a time in ms, e.g. `5000` (5s).
interval: 4000

# Minimum slide height.
# Specify a height to ensure a consistent height for each slide.
# CSS hack from Taneda example site
height: '400px; background-position:left; background-repeat: no-repeat'

spacing:
  # Customize the section spacing. Order is top, right, bottom, left.
  #padding: ["0px", "0", "0px", "0"]

item:
  - title: Meet the group
    content: 'October 2021'
    # Choose `center`, `left`, or `right` alignment.
    align: right
    # Overlay a color or image (optional).
    #   Deactivate an option by commenting out the line, prefixing it with `#`.
    overlay_color: '#666'  # An HTML color value.
    overlay_img: group_photo_oct2021_v2.png  # Image path relative to your `assets/media/` folder
    overlay_filter: 0.2  # Darken the image. Value in range 0-1.
    # Call to action button (optional).
    #   Activate the button by specifying a URL and button label below.
    #   Deactivate by commenting out parameters, prefixing lines with `#`.
    cta_label: Meet the team
    cta_url: 'people'
    cta_icon_pack: fas
    cta_icon: people-group
    #- title: Left
    #content: 'I am left aligned 😄'
    #align: left
    #overlay_color: '#555'
    #overlay_img: logo.png
    #overlay_filter: 0.1
    #- title: Right
    #content: 'I am right aligned 😄'
    #align: right
    #overlay_color: '#333'
    #overlay_img: 'logo.png'
    #overlay_filter: 0.1
  - title: Biochemistry
    content: "Non-heme iron vs vanadyl mimics"
    align: right
    overlay_color: '#333'
    overlay_img: vanadium_splash_figure.png
    overlay_filter: 0.2
    # Call to action button (optional).
    #   Activate the button by specifying a URL and button label below.
    #   Deactivate by commenting out parameters, prefixing lines with `#`.
    cta_label: Read the paper
    cta_url: 'publication/vennelakanti-arevanadium-2022'
    cta_icon_pack: fas
    cta_icon: graduation-cap
  - title: ML & catalysis
    content: "Sifting through 16M catalysts with ML"
    align: right
    overlay_color: '#333'
    overlay_img: splash.png
    overlay_filter: 0.2
    # Call to action button (optional).
    #   Activate the button by specifying a URL and button label below.
    #   Deactivate by commenting out parameters, prefixing lines with `#`.
    cta_label: Read the paper
    cta_url: 'publication/nandy-new-2022'
    cta_icon_pack: fas
    cta_icon: graduation-cap
  - title: ML & theory
    content: "Detecting imbalances in MR character"
    align: right
    overlay_color: '#333'
    overlay_img: TOC_v2.png
    overlay_filter: 0.2
    # Call to action button (optional).
    #   Activate the button by specifying a URL and button label below.
    #   Deactivate by commenting out parameters, prefixing lines with `#`.
    cta_label: Read the paper
    cta_url: 'publication/duan-detection-2022'
    cta_icon_pack: fas
    cta_icon: graduation-cap
  - title: Text mining MOFs
    content: "MOFSimplify: engineering MOF stability"
    align: right
    overlay_color: '#333'
    overlay_img: MOFSimplify_long_final_0.png
    overlay_filter: 0.2
    # Call to action button (optional).
    #   Activate the button by specifying a URL and button label below.
    #   Deactivate by commenting out parameters, prefixing lines with `#`.
    cta_label: Read the paper
    cta_url: 'publication/nandy-mofsimplify-2022'
    cta_icon_pack: fas
    cta_icon: graduation-cap
  - title: Catalysis
    content: "Unraveling bioinspired catalyst design"
    align: right
    overlay_color: '#333'
    overlay_img: rectangle.png
    overlay_filter: 0.2
    # Call to action button (optional).
    #   Activate the button by specifying a URL and button label below.
    #   Deactivate by commenting out parameters, prefixing lines with `#`.
    cta_label: Read the paper
    cta_url: 'publication/liu-largescale-2022'
    cta_icon_pack: fas
    cta_icon: graduation-cap
  - title: ML & MOFs
    content: "Using literature data to engineer MOF stability"
    align: right
    overlay_color: '#333'
    overlay_img: Splash-2.png
    overlay_filter: 0.2
    # Call to action button (optional).
    #   Activate the button by specifying a URL and button label below.
    #   Deactivate by commenting out parameters, prefixing lines with `#`.
    cta_label: Read the paper
    cta_url: 'publication/nandy-using-2021'
    cta_icon_pack: fas
    cta_icon: graduation-cap
  - title: ML & DFT
    content: "Universal design rules from 23 DFT functionals"
    align: right
    overlay_color: '#333'
    overlay_img: TOC_v5-min-2.png
    overlay_filter: 0.2
    # Call to action button (optional).
    #   Activate the button by specifying a URL and button label below.
    #   Deactivate by commenting out parameters, prefixing lines with `#`.
    cta_label: Read the paper
    cta_url: 'publication/duan-machine-2021'
    cta_icon_pack: fas
    cta_icon: graduation-cap
  - title: Biochemistry
    content: "The importance of substrate positioning"
    align: right
    overlay_color: '#333'
    overlay_img: halogenases_toc.png
    overlay_filter: 0.2
    # Call to action button (optional).
    #   Activate the button by specifying a URL and button label below.
    #   Deactivate by commenting out parameters, prefixing lines with `#`.
    cta_label: Read the paper
    cta_url: 'publication/mehmood-spectroscopically-2021'
    cta_icon_pack: fas
    cta_icon: graduation-cap
  - title: Materials
    content: "Mapping the surface of InP QD materials"
    align: right
    overlay_color: '#333'
    overlay_img: InPQDDoping_Slide.png
    overlay_filter: 0.2
    # Call to action button (optional).
    #   Activate the button by specifying a URL and button label below.
    #   Deactivate by commenting out parameters, prefixing lines with `#`.
    cta_label: Read the paper
    cta_url: 'publication/taylor-mapping-2021'
    cta_icon_pack: fas
    cta_icon: graduation-cap
  - title: Biochemistry
    content: "Harder,better,faster,stronger:large-scale QM/MM"
    align: right
    overlay_color: '#333'
    overlay_img: cosb_website_pic_v3.png
    overlay_filter: 0.2
    # Call to action button (optional).
    #   Activate the button by specifying a URL and button label below.
    #   Deactivate by commenting out parameters, prefixing lines with `#`.
    cta_label: Read the opinion
    cta_url: 'publication/vennelakanti-harder-2022'
    cta_icon_pack: fas
    cta_icon: graduation-cap
  - title: DFT & catalysis
    content: "The influence of DFT functional on catalysis"
    align: right
    overlay_color: '#333'
    overlay_img: tic_website_pic_v2.png
    overlay_filter: 0.2
    # Call to action button (optional).
    #   Activate the button by specifying a URL and button label below.
    #   Deactivate by commenting out parameters, prefixing lines with `#`.
    cta_label: Read the paper
    cta_url: 'publication/vennelakanti-effect-2022'
    cta_icon_pack: fas
    cta_icon: graduation-cap
  - title: ML
    content: "Chem. Rev. on ML for transition metals is out!"
    align: right
    overlay_color: '#333'
    overlay_img: religious_molecule_wide.png
    overlay_filter: 0.2
    # Call to action button (optional).
    #   Activate the button by specifying a URL and button label below.
    #   Deactivate by commenting out parameters, prefixing lines with `#`.
    cta_label: Read the review
    cta_url: 'publication/nandy-computational-2021'
    cta_icon_pack: fas
    cta_icon: graduation-cap
  - title: Biochemistry
    content: "Electronic allostery in protein dynamics"
    align: right
    overlay_color: '#333'
    overlay_img: charge_coupling_web.png
    overlay_filter: 0.2
    # Call to action button (optional).
    #   Activate the button by specifying a URL and button label below.
    #   Deactivate by commenting out parameters, prefixing lines with `#`.
    cta_label: Read the paper
    cta_url: 'publication/yang-quantifying-2021'
    cta_icon_pack: fas
    cta_icon: graduation-cap
  - title: ML
    content: "What's needed for intelligent workflows"
    align: right
    overlay_color: '#333'
    overlay_img: robot_and_layer_from_wide_fin_rgb.png
    overlay_filter: 0.2
    # Call to action button (optional).
    #   Activate the button by specifying a URL and button label below.
    #   Deactivate by commenting out parameters, prefixing lines with `#`.
    cta_label: Read the perspective
    cta_url: 'publication/duan-putting-2021'
    cta_icon_pack: fas
    cta_icon: graduation-cap
  - title: DFT
    content: "Molecular DFT+U for delocalization error"
    align: right
    overlay_color: '#333'
    overlay_img: modftu_slide_v1.jpg
    overlay_filter: 0.2
    # Call to action button (optional).
    #   Activate the button by specifying a URL and button label below.
    #   Deactivate by commenting out parameters, prefixing lines with `#`.
    cta_label: Read the perspective
    cta_url: 'publication/bajaj-molecular-2021'
    cta_icon_pack: fas
    cta_icon: graduation-cap
  - title: ML
    content: "Where are the stars in chemical space?"
    align: right
    overlay_color: '#333'
    overlay_img: acc_chem_res_splash.png
    overlay_filter: 0.2
    # Call to action button (optional).
    #   Activate the button by specifying a URL and button label below.
    #   Deactivate by commenting out parameters, prefixing lines with `#`.
    cta_label: Read the account
    cta_url: 'publication/janet-navigating-2021'
    cta_icon_pack: fas
    cta_icon: graduation-cap
  - title: ML & theory
    content: "Semi-supervised learning for MR detection"
    align: right
    overlay_color: '#333'
    overlay_img: semisupervised.png
    overlay_filter: 0.2
    # Call to action button (optional).
    #   Activate the button by specifying a URL and button label below.
    #   Deactivate by commenting out parameters, prefixing lines with `#`.
    cta_label: Read the paper
    cta_url: 'publication/duan-semi-supervised-2020' 
    cta_icon_pack: fas
    cta_icon: graduation-cap
  - title: ML
    content: "Accelerating practical materials design"
    align: right
    overlay_color: '#333'
    overlay_img: janet2020_rfb_toc.png
    overlay_filter: 0.2
    # Call to action button (optional).
    #   Activate the button by specifying a URL and button label below.
    #   Deactivate by commenting out parameters, prefixing lines with `#`.
    cta_label: Read the paper
    cta_url: 'publication/janet-accurate-2020'
    cta_icon_pack: fas
    cta_icon: graduation-cap
---
