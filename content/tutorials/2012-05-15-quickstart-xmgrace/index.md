---
title: "Quickstart with xmgrace"
subtitle:
aliases: /content/quickstart-xmgrace
 

# Summary for listings and search engines
summary: 

# Link this post with a project
projects: []

# Date published
date: 2012-05-15

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
There are a lot of tools you can use to graph your data.  For graphing curves, I think [xmgrace](http://plasma-gate.weizmann.ac.il/Grace/ "http://plasma-gate.weizmann.ac.il/Grace/") is one of the most versatile tools.  Today I’ll go over some handy tips and tricks I’ve learned with [xmgrace](http://plasma-gate.weizmann.ac.il/Grace/ "http://plasma-gate.weizmann.ac.il/Grace/").  If you use a mac, you may want to download a binary that you can get access to [at the bottom of this page](http://hpc.sourceforge.net/ "http://hpc.sourceforge.net/").  Today, I’ll only go over the basics needed to get started. If you’d like more detailed and advanced information, check out the xmgrace tutorials [here](http://plasma-gate.weizmann.ac.il/Grace/doc/Tutorial.html "http://plasma-gate.weizmann.ac.il/Grace/doc/Tutorial.html").


 


**1. Knowing your data.**

You can launch xmgrace from the commandline. If you have homebrew running on your computer and use it to install xmgrace, your xmgrace installation will be located in /usr/local/bin.


If you’re running the binary linked to in this tutorial in mac os x, you’ll want to add an alias like this to your .profile:

```
alias xmgrace='/Applications/Grace.app/Contents/Resources/grace/bin/xmgrace'
```

If you're not sure where your xmgrace installation is, you can try `which xmgrace` at the commandline.


When you launch xmgrace on any column-based data, e.g. `xmgrace mydata.dat`, your x values get read in from the first column and y values from the second column. 


If you have multiple y columns with the same x values, you instead want to use `xmgrace -nxy mydata.dat`

If you have multiple files with multiple y columns each, you need to remember to use `xmgrace -nxy mydata1.dat -nxy mydata2.dat` ...etc.  Wildcards will get all of the matching files but all but the first one will default to just standard x-y instead of nxy.

Note, by default it will autoscale to all the loaded data. If you want to only look at some of your loaded data sets at a time, you can always hide them.  The fastest way to do that is to go to `Edit>Data sets...` and you’ll see all the loaded in data sets. You can right click on one and then hide or kill or edit the data.

You can also see statistics here about your data set - the max and min values and where those occur in both x and y, for instance.



**2. Manipulating your data.**

I think one of the most powerful features of xmgrace is that it allows you to quickly do mathematical operations on your data sets. Say you imported a bunch of energies in Ry but want to show them in kcal/mol.  You can quickly multiply all your data by the conversion factor between Ry and kcal/mol.  The quickest way to get started manipulating your data through addition, subtraction, multiplication and division is under `Data>Transformations>Evaluate` expression.

Here you choose a source for your data that you’re operating on and a destination. They can be the same or you can duplicate your current data set to avoid overwriting. Then you write expressions in the formula box such as:

```
s0.y = s0.y +3
```

Here we add 3 to every y value in your data set.  You can also do this on x values if you need to shift your x axis by manipulating s0.x.


Importantly, the formula recognizes avg(s0.y), min(s0.y), max(s0.y) so you can easily shift your data such that the minimum of the curve is set to zero:

```
s0.y=s0.y-min(s0.y)
```
or subtract the average to only look at fluctuations.  

Under `Data>Transformations` you can also calculate averages, numerical derivatives, and integrate.  Check out the [main xmgrace tutorial](http://plasma-gate.weizmann.ac.il/Grace/doc/Tutorial.html "http://plasma-gate.weizmann.ac.il/Grace/doc/Tutorial.html") if you’d like to learn more about those tools.  

**3. Choosing your data.**

Even though we may import a large amount of data, we may only wish to manipulate or to focus on a small subset of that data.


One of the handiest things we can do is hide sets we don’t want to look at. You can do this by going to Edit>Data Sets and right clicking on any data set to Hide, Kill, or Duplicate. Hide is safest. You can use the bar on the left with Z and z to zoom in and out of your data. Autoscale (As) will autoscale to all non-hidden data sets. And when you import data you can choose whether or not to autoscale to XY, X-only, Y-only or not at all.  

Finally, you can select regions (horiz. rang and vert. range work best). This is handy for getting the derivative of only part of your curve (e.g. for a tangent) or finding a fit of just part of the data.  


**4. Presenting it well.**

There’s not enough time to go over how to make beautiful graphs in xmgrace - some of that will come with practice, but here are a few quick tips:

Increase line thickness and symbol size in `Plot>Set Appearance`. For publication ready graphs, a line thickness of at least 3 is recommended and symbols should be at least 150 or larger. Clicking to the left or right of any sliderbar will automatically increment the size in units of 25. I find this handy for getting precise size increases quickly. You can set your symbol outline and line color on the first tab, but set symbol fill to be different if you’d like on the Symbols tab. Remember to “Apply” your changes.  

Increase the fonts on your axes to at least 150 size font as well.  You can also change them to Helvetica or Helvetica-Bold for easier reading.  Double click on your axes and modify the font and size of tick labels and axis labels on the Main, Axis Label & Bar, and Tick Labels tabs for each axis.  Always be sure to label your axes, it will help in understanding your data later. 

(Tip: Don’t know where to find your symbol? Check out `Window>Font` tool to find and insert your missing font.)



**5. Saving your data for next time.**

Now that we’ve visualized and analyzed our data, we should save it for later. Be aware that as you save, it will show the default format for how your data gets written to the grace file (*.agr).  This defaults to %.8g so you may want to change it if you have large numbers where you also care about the decimal information (e.g. total energies). Try increasing to %16.8g, for instance. Also, note you can leave some information for yourself in Project description in case you forget about what you were working on when you look at this data months later.

Another key point is that when we save xmgrace files, we’re really generating a text file that tells us how to visualize all the key aspects such as axes and fonts and symbols in addition to our data and a timestamp indicating when the file was created. I recommend you familiarize yourself with what this looks like by opening up one of your .agr files.  You may find it’s useful to modify properties of grace just by editing the text in your .agr file.

Finally, if you settle on a style of grace that you like a lot, e.g. custom fonts and certain symbol sizes and line thickness, you can save a template that will make these settings defaults.  Make a grace file called Defaults.agr and put it in the folder `~/.grace/templates/` (may vary based on distribution).  


I hope that you’ve learned or re-learned a few things about using xmgrace to plot your data today. Please [email me](mailto:hjkulik@mit.edu?subject=Questions%20about%20xmgrace%20quickstart "mailto:hjkulik@mit.edu?subject=Questions about xmgrace quickstart") if you have any additional questions not answered here!


