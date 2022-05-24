---
title: "Ten research tools and shortcuts"
subtitle:
aliases: /content/ten-research-tools-and-shortcuts
 

# Summary for listings and search engines
summary: 

# Link this post with a project
projects: []

# Date published
date: 2013-05-21

# Date updated
lastmod: 

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: 
  focal_point: ""
  placement: 1
  preview_only: false

authors:
- admin

tags:

categories:
- tutorials

---
While this month’s tutorial is currently stuck in debugging, here is a list of ten useful things I’ve learned or used in the past few months.  Why not [share some useful tips](mailto:hjkulik@mit.edu?subject=My%20top%20tip "mailto:hjkulik@mit.edu?subject=My top tip") you’ve learned with me? I’ll post the best suggestions on this site. In no particular order, here they are:


 


10. Generating random numbers

Sometimes, e.g. when starting an MD run, you may want to see with a random number.  It’s as simple as `$RANDOM`! Put it in your bash scripts or try it at the commandline.


 


9. Add a line number to the start of your file in vi


Maybe you have a bunch of ‘y’ column data but you need a series of integers in your first column as your ‘x’ data for plotting software.  You can do this in vi using a command of the following structure:

```
:%s/^/\=line('.') . ' '/
```

where the first bit indicates the substitution is on all lines. If you want to adjust the line number, you can try `line(‘.’)-<offset>`. The second bit is a string. In my case, I wanted to add a space but you may want a comma or any number of other characters.


 


8. Upgrade your excel graphs

Excel - love it or hate it, take it or leave it...sometimes it’s just more convenient to use.  For instance, I find I like to make bar graphs in excel, and they don’t look that bad.  Still there are a few things you can do (get rid of that annoying outline, tweak your colors, change your fonts, etc) to hide the obvious “excel”-ness of them.  But did you know if you copy an excel graph and paste it into photoshop, it will paste as a vector smart object that you can then edit further in adobe illustrator? This is handy for fine-tuning and tweaking shadows and other features as well as for ensuring that the resolution of that graph is maintained for publication.


 


7. Keep that Ångström symbol handy


Not really a brand-new-to-me tip but here are some ways to keep that Å handy: In xmgrace, you can add it to your legends with the code: `\cE\C`. In microsoft programs, try `alt-shift-A`. In latex, it’s `\AA`.


 


6. Know your colors

Whether you’re designing a new webpage, a brochure or just trying to make presentations that pop, it can’t hurt to learn a little color theory.  [This site is really handy](http://colorschemedesigner.com/ "http://colorschemedesigner.com/") for putting together complementary colors and accents. Note the RGB % at the bottom left corner. You can match that against a color in something else you’re working on.  You can also check out color blind settings and export as a photoshop palette.


5. Digitize graphs from papers

Find some experimental data you’d like to compare your theory to? There are a number of ways to digitize that data. Most are still tedious and involve you clicking on each data point and then defining the axes. The one I like to use is called Plot Digitizer. Go ahead and [download it here](http://plotdigitizer.sourceforge.net/ "http://plotdigitizer.sourceforge.net/")


4. Use Avogadro to rapidly build and optimize molecules


I learned this one belatedly from someone else in my postdoc group! If you use Avogrado, you can use force fields to optimize your structure as you build it. This is handy when you want to build a structure but aren’t sure exactly how long your bonds should be. [Download Avogadro here](http://avogadro.openmolecules.net/wiki/Main_Page "http://avogadro.openmolecules.net/wiki/Main_Page").



3. Drag files into terminal to get paths.

This is an old one but still handy. Did you know you can drag a file you search for in Finder on the mac onto a terminal window? Once you’ve done that, you’ll see the whole path for the file.  This is handy for then manipulating that file at the commandline.


 
2. Use Acrobat to reduce the file size of PDFs and to watermark them.


Faced with a choice that your PDF is just a little too big? If you’re on a mac, don’t bother with the reduce file size quartz filter in preview. Skip right to Acrobat and choose “Reduce file size” (I always find it using the help menu).  You can also use Acrobat to add watermarks and save preset watermarks (e.g. “All Rights Reserved”) at the top of your PDFs.


 


1. Use evernote to take screenshots easily.


Although your computer probably takes screenshots at the OS level, Evernote has really handy controls for screenshots. In fact, all of the window screenshots I use in my tutorials are made with evernote. From the menubar item, you can “Clip rectangle or window to Evernote...” a crosshairs comes up. Either click on the window to get the whole thing or drag across part of a window to get just part of it. Once this is clipped in evernote, you can rightclick and save to an image to insert into presentations and more.  


 


Got any tips of your own, please [email them to me](mailto:hjkulik@mit.edu?subject=More%20tips%20and%20tricks%20suggestion "mailto:hjkulik@mit.edu?subject=More tips and tricks suggestion")!


