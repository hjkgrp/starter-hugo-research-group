---
title: "Installing molSimplify"
subtitle:
aliases: /content/installing-molsimplify
 

# Summary for listings and search engines
summary: 

# Link this post with a project
projects: []

# Date published
date: 2021-10-27

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
- molsimplify

categories:
- molsimplify-tutorials
- tutorials

---
**Install recommendations**: For users who intend to develop (i.e., change the source code) with molSimplify, we recommend an install from source. If you have difficulties installing from source, we recommend Docker or Conda, where we maintain a static image of molSimplify that includes machine learning models that we have published. If you have a Mac with an M1 chip, you must install from source.


**System requirements:** The code should work on any recent OS supporting Python 3. These include Windows 7 to 10, OS X 10.10 to 10.13 and Ubuntu 14.14. There are no specific memory or processor requirements, but we recommend disabling the force field (`-ffoption B`) or switching to UFF from the default MMFF94 (`-ff uff`) if poor performance is observed.


**Special Instructions for M1 Mac:** For M1 Macs, please use [miniforge](https://github.com/conda-forge/miniforge) for Mac OSX arm64 instead of the normal Anaconda installation. A prebuilt conda environment and script to download an M1-compatible copy of Tensorflow is present in our Github instructions to build molSimplify from source. Please follow the [instructions on Github](https://github.com/hjkgrp/molSimplify#readme) for installation details.


**Installation from Source:** molSimplify can also be installed from [source](https://github.com/hjkgrp/molSimplify/tree/master) using Git. This is the best option if you would like to modify the source code or get the most up to date code and features. The detailed instruction is on our github page (<https://github.com/hjkgrp/molSimplify>, section titled "Installation via Conda"). In this installation method, we build molSimplify from source, but get all other dependencies from conda.


**Installation via Conda:** [Conda](https://docs.conda.io/en/latest/) is the recommended mode of installation for our package when you do not want to install from source. Conda is a package and environment manager application that lets users easily download and install python, R, C, Scala, Java and other programs, without needing to worry about dependencies. First install Conda from the link above if you do not already have it. We recommend using the Anaconda version with Python 3 since Python 2 is no longer maintained. **Note: our conda image will not work for Mac computers with an M1 chip, and you will need to install from source following our instructions above.**


1. Once Conda is installed, create a new environment with:


`$ conda create -n molSimplify python=3.6`


2. Activate this newly created environment with the command:


`$ conda activate molSimplify`


**NOTE: Whenever you want to run molSimplify in a new terminal window, remember first to activate the environment as shown above!** 


3. Add package channels that molSimplify depends on.

``` bash
(molSimplify)$ conda config --add channels hjkgroup
(molSimplify)$ conda config --add channels conda-forge
(molSimplify)$ conda config --add channels defaults
```

4. Inside this new environment, you can install molSimplify using (**NOTE: case sensitive**):

``` bash
(molSimplify)$ conda install -c hjkgroup molSimplify
```


Here, the `-c` indicates that the package will come from the Anaconda cloud and `hjkgroup` indicates our cloud account. All required dependencies, including OpenBabel and SciPy, will also be automatically installed. This will download a static image from conda that gets periodically updated. You can visit this link: [https://anaconda.org/hjkgroup/molsimplify](https://anaconda.org/hjkgroup/molsimplify ) which will give you the details of our conda image.


When you use conda environments, you must activate your molSimplify environment before use (and again every time you close your terminal session or deactivate the environment). This environment will prevent the installation from conflicting with other Python-based software on your computer. Note that if you would like to use the molSimplify GUI, PyQt5 needs to be installed separately (see below).


**NOTE on debugging:**If you encounter a tensorflow error, it is likely that your hardware is not compatible with the version of tensorflow (1.14.0) pre-installed and shipped with molSimplify. In this case, we suggest you to downgrade your tensorflow to an older version (e.g., 1.12.0). You can do this within conda.  If you have the `core dumped` error, it is likely that the OpenMP tries to run it with multiple treads and errors out. You can try doing `export OMP_NUM_THREADS=1` to fix it.


**Running the GUI (only OS X and Linux supported):**


PyQt5 is required for our GUI. If you don't already have it, you can install it using the command:


`(molSimplify)$ conda install pyqt=5`


Now you can launch the GUI by calling molSimplify without any arguments (the command line version will still work as usual):


`(molSimplify)$ molsimplify`


**OS X 10.12 or older:** OpenBabel 2.4.1 may not be compatible with OS X 10.12 or older. If you encounter OpenBabel errors, you can get an older version by running


`conda install -c hjkgroup openbabel=2.3.2`


**Installation via Docker:**[Docker](https://hub.docker.com/) is the recommended mode of install for easy use of molSimplify without making any modifications. This version is platform independent, and will run as long as you can install docker. Following the exact instructions below step by step should allow you to get molSimplify running on your machine.


1. Make a free account with docker: <https://hub.docker.com/>.
2. Install docker for your OS. After you install docker correctly and open the application, **there should be a whale icon in your navigation bar.**
3. Open up the docker application and sign in with your free account credentials. It may take some time to start.
4. You can test that your docker works by typing the following in a terminal: `docker run hello-world`
	1. Running this will result in something that says: "Hello from Docker! This message shows that your installation appears to be working correctly."
5. Make the folder where you want your molSimplify to dump the files (a folder to place geometries and input files outputted by molSimplify.). Pick an easy to find location. Find the path of this folder, you will use it in the following step. I am going to dump my files at `/Users/molSimplifyUser/Desktop/dockertest` --> which I will call **MYFILEPATH.**
	1. You can open up a terminal and use bash commands like `mkdir` to make a directory where you want your files dumped. You can then use `cd` to go to the directory where you want those files dumped (aka **MYFILEPATH**). Use `pwd` to get the path (which would replace **MYFILEPATH**).
6. Next, run the following command, which should give you the molsimplify container. Replace the section that says **MYFILEPATH** with your path for where you want to dump your structures and input files. The below command will make a container that is titled "my\_container." Keep the part that says hjkgroup/ after the -it flag... that is our dockerhub account.
	1. `docker run --name my_container -v MYFILEPATH:/root/Runs/ -it hjkgroup/molsimplify:latest`
7. At this step, make sure you have the `-it` flag on. If you do not, then it cannot make the interactive docker environment that you want! You should copy the above line directly (starting from `docker`) and only replace **MYFILEPATH**.
8. <---- Will download the docker container --->
9. After this download is complete, the docker container is going to be running interactively.
10. You will notice that you are in an environment with (molSimplify) on the left, followed by root@... This is good! You can use molsimplify now. Any files you make will show up in **MYFILEPATH** specified earlier. At this point, try building a structure. We can build our favorite Fe(II)(NH3)6 complex:
	1. `molsimplify -core fe -lig ammonia -ligocc 6 -ligloc True -oxstate II -spin 5`
	2. Check if the files are present in **MYFILEPATH**!
11. If you are done with the container and want to leave, simply type exit. This halts all running processes.
	1. You have now left the container, but you can always restart it.
12. You can type docker ps -a to see your existing containers. If you want to re-start and re-enter the container, type the following:
	1. `docker start my_container`
	2. `docker attach my_container`
	3. You're back in the container. That's it!
13. If you want to remove a container, you can get the names from `docker ps -a` , and then do `docker rm <CONTAINERNAME>` where CONTAINERNAME can be identified from the `ps -a` command.
14. If you want to stop docker from running completely, go to the whale in your navigation bar and quit docker. Once you open it back up, you can reattach to your old containers.

If you have any issues with the installation process, please [email us](mailto:molsimplify@mit.edu?subject=molsimplify%20installation%20issues)!


