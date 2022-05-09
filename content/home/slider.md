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
  - title: The Group
    content: 'Summer 2021'
    # Choose `center`, `left`, or `right` alignment.
    align: right
    # Overlay a color or image (optional).
    #   Deactivate an option by commenting out the line, prefixing it with `#`.
    overlay_color: '#666'  # An HTML color value.
    overlay_img: kulikgroup_Jun2021_v2.png  # Image path relative to your `assets/media/` folder
    overlay_filter: 0.2  # Darken the image. Value in range 0-1.
    # Call to action button (optional).
    #   Activate the button by specifying a URL and button label below.
    #   Deactivate by commenting out parameters, prefixing lines with `#`.
    #cta_label: Download my app
    #cta_url: 'https://example.org'
    #cta_icon_pack: fas
    #cta_icon: graduation-cap
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
  - title: ML
    content: "What's needed for intelligent workflows"
    align: right
    overlay_color: '#333'
    overlay_img: robot_and_layer_from_wide_fin_rgb.png
    overlay_filter: 0.2
    # Call to action button (optional).
    #   Activate the button by specifying a URL and button label below.
    #   Deactivate by commenting out parameters, prefixing lines with `#`.
    cta_label: Read the paper
    cta_url: 'publication/duan-learning-2019'
    cta_icon_pack: fas
    cta_icon: graduation-cap
  - title: Biochemistry
    content: "Non-heme iron enzymes and their vanadyl mimics"
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
---
