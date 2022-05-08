---
title: "BIOS 203: Useful commandline tools"
subtitle: 

# Summary for listings and search engines
summary: 

# Link this post with a project
projects: []

# Date published
date: 2013-02-19

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
  placement: 2
  preview_only: false

authors:
- admin

tags:

categories:
- tutorials

---
If you have limited experience with the command line interface (e.g. within a linux installation or Mac OS X’s terminal.app), it can be daunting to find your way around. However, once you get used to the commandline, you’ll often see you can do many things much faster than you would normally be able to with point and click alone.  Here’s a list of commands and what they are useful for in order to supplement the work that students are doing in [BIOS 203](http://bios203.stanford.edu/ "http://bios203.stanford.edu").


 


1. 1.Getting around the file system:

Here are some useful tools for manipulating files at the commandline.


 


ls: lists all visible files in the current directory.


Try: ls -ltrh


to view files with long printing (l), last modified sorting (t), in reverse (r), and human readable (h) file sizes.


Try: ls .*


to view all hidden files that start with ‘.’ such as .bashrc.


Try: ls */*


to view all files in first layer of subdirectories, etc.


Try: ls */ -d


to view all files that match a wildcard with a directory.


 


cd: change directory.


Try: cd ~/


to change directory to home


Try: cd -


to change directory to the previous one.


Try: cd ../


to move up one directory


 


mkdir: make a directory.


Try: mkdir -p path/to/directory


to simulatenously make new directory path, with a subdirectory inside to, with sub-subdirectory inside called ‘directory’


 


pwd: gets the current working directory.


 


ln: make a symbolic link for a directory.  


Say you have a long source directory like /usr/local/source/file/compiler/bin/ and want to be able to see its contents more easily.


Try: ln -s /usr/local/source/file/compiler/bin/ easydir


to make a symbolic link in your existing directory as a subdirectory called “easydir”. To remove the symbolic link, just try “rm” per below.


 


df/quota: find out how much space is free for you to use.


On any filesystem, if you want to know how much free space there is, 


Try: df -h


for human units (GB/MB/KB) to see how much space is free on all drives.


If your system has a quota set up (e.g. on a cluster for many users)


Try: quota -v


to find out if there’s a quota set up for you and how close you are to any existing limits.


 


cp/mv: copy or move files from one place to another. You may want to copy or move files around from one place to another.  Here are some examples of copying or moving the old file apples.txt to oranges.txt.


Try: cp -i apples.txt oranges.txt


“i” for interactive means that if oranges.txt already exists, it will ask you if you want to overwrite.


Try: mv -i apples.txt oranges.txt


“i” for interactive means that if oranges.txt already exists, it will ask you if you want to overwrite the existing oranges.txt.


Try: mv -f apples.txt oranges.txt


“f” forces the move even if an existing oranges.txt is already there.


Try: cp -p apples.txt oranges.txt


“p” means that permissions and timestamps will be preserved.


Try:  cp -r apples/ oranges/


“r” means that you’re recursively copying all the files in a directory. You need to do this if you’re trying to copy a directory.


 


rm: remove a file. 


Much like cp and mv, you can remove files (be careful with this) using a couple different flags.


Try: rm -i apples.txt


to interactively ”i” remove a file (i.e. get a y/n statement)


Try: rm -v apples.txt


to get a verbose listing of the files removed.


Try: rm -r apples/


to recursively remove an entire directory.


 


chown/chmod: to change permissions of files.


Try: chown <user> apples.txt


to make the <user> an owner of the file apples.txt if it is not already the owner.


Try: chmod  a+rw apples.txt


to make the file apples.txt readable and writeable by all.  You can also rescind read or write access in the same way but using a ‘-’. 


 


vi/nano/more/less: to edit or view a file.


Try: vi apples.txt


to open the files apple.txt with a text editor. Nano provides an easy text editing interface. And the other commands more/less can be used to view the file a page at a time but not to edit them.  Check out these resources for [vi](http://acms.ucsd.edu/info/vi_tutorial.html "http://acms.ucsd.edu/info/vi_tutorial.html")and [nano](http://www.gentoo.org/doc/en/nano-basics-guide.xml "http://www.gentoo.org/doc/en/nano-basics-guide.xml") for more info.


 


locate: check a database of indexed files 


Try: locate apples


to find all paths and files that have the phrase apples somewhere in them. You can also use wildcards.


 


tar: compress and uncompress files.


Try: tar cvzf apples.tgz apples.txt


to create an archive of files. You can also use wildcards or a long list of files.


Try: tar zxvf apples.tgz


to expand an existing archive of files.


 


1. 2. Getting connected:

Here are some useful tips for how to get started connecting to other machines.


 


ssh: secure shell remote login to a machine.


Try: ssh cardinal1.stanford.edu


to login to the machine cardinal1.stanford.edu. This will work if your username on the current computer is the same as the login for your destination. 


Otherwise try: ssh -l usernew cardinal1.stanford.edu


 


Note: a handy trick is to alias common logins in your .bashrc or .profile (depending on what gets sourced when you open a new terminal).


As an example you could set an alias:


alias scard=”ssh -l usernew cardinal1.stanford.edu”


this would allow you to type scard to login rather than that whole long thing. Note you can use alias in your .bashrc/.profile to shorten all of your most common commands.


 


scp: secure copy 


Try: scp -pr cardinal1.stanford.edu:/path/to/remotefile ./localfile


to secure copy a file from the cardinal1 filesystem to a local spot recursively and with preserved permissions and timestamps.


Try: scp -pr localfile cardinal1.stanford.edu:/path/to/


to secure copy a file from the local host to the cardinal1 filesystem.


 


sleep: sleep to keep the system waiting.


It may be useful to you to execute several commands and then sleep before executing more. Or you may find it useful to keep a connection alive to a server.


Try: sleep 5


to sleep at the command line for five seconds.


 


time: time how long it takes to execute a command.


Try: time <command> to see how long it takes to execute a command.


 


ps: list the running processes


Try: ps aux


to see all the running processes.


 


kill: kill a process


Try: kill -9 <process id>


to kill a process with one of the highest priorities.


 


wget: download a file from the web.


wget <http://www.example.com/file.zip>


 


1. 3.Parsing data at the commandline.

It’s often useful to be able to manipulate data at the commandline. We’ll learn a few ways to do that here.


 


grep: find regular expressions


Try: grep ‘apple’ apples.txt


to see if the phrase ‘apple’ appears in apples.txt and how many times.


Try: grep -l ‘apple’ *.*


to return a list of files that have the phrase ‘apple’ in them.


 


awk: a more complicated regular expression tool.


Try: awk ‘/apple/ { print $2 }’ apples.txt


to return the 2nd record in any line that has the word ‘apple’ in it.


 


tail: get the tail of a file.


Starting from the bottom you can get the last N lines with ‘tail -N file’.


Try: tail -f myfile.txt


if you are running a program that is writing to myfile.txt, tail -f will update with the newly written lines from the file.


 


cat: show the file.


Try: cat myfile.txt


to cat all of the contents of the file to standard out.


Try: cat myfile.txt >> apples.txt


to add all the contents of myfile.txt to the end of apples.txt.


 


uniq: identify unique items in a list of items.


Try: cat apples.txt | uniq


to get all unique instances of lines in apples.txt. For instance if the word ‘apples’ appears twice on two separate lines, you’ll only get one result.


 


sort: sort items in a list.


Try: cat apples.txt | sort


to get everything sorted alphabetically.


Try: cat apples.txt | sort -n


to get everything sorted numerically.


Try: cat apples.txt | sort -rn


to reverse the numerical sort.


 


echo: send a phrase to standard out consisting of text or variables


You can specify a variable:


apples=”oranges”


And try using echo: echo $apples


the result will be: oranges


 


wc: word count


Try: cat apples.txt | wc 


to return the number of lines, words, and characters in the file.


Note: wc -l returns only the number of lines.


 


bc: calculator


Try: bc -l


to enter an interactive calculator to do math in.


Or try: echo “3+2” | bc 


to add and return the resulting number to the standard out.


 


diff: identify line by line differences in a file.


Try: diff apples.txt oranges.txt


to get the line by line differences between two files.


 


sed: this line editor can allow you some useful ways to change lines in a file.


Say you want to get all of the lines from your file except those that start with ‘orange’.


Try: cat apples.txt | sed ‘/orange/d’ > applesnew.txt


where the ‘d’ stands for deleting all matching cases of that regular expression.


 


I hope you found this linux mini-tutorial helpful. If you’re at Stanford and would like to take the course or just in the Bay area and would be interested in popping in or giving a guest lecture, please [email me](mailto:hjkulik@mit.edu?subject=Questions%20about%20BIOS%20203%20linux%20tutorial "mailto:hjkulik@mit.edu?subject=Questions about BIOS 203 linux tutorial")!


