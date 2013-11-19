# PyLadies Stockholm: Build your own Blog with Django



#### Note for Windows' users

Windows users: first you need to figure out which system architecture you have (32-bits or 64-bits):

* Right-click on "Computer" or "My Computer"
* Choose "Properties" on the context menu
* Depending on which Windows version you have (XP, Vista, 7, or 8), you may have to click on "General" tab.
* You should see something like "... x64 Edition...", or "64-bit Operating System..." or "32-bit Operating System...".  If you see *no* numbers, then it is a 32-bit system.
* **Remember** your architecture type!

## Installation

You can either [download everything](#downloadingovertheinternet) or [copy & run everything from a USB](#usingtheusbstick) to install all the packages you need for tonight.

### Downloading over the internet

##### Step 1: VirtualBox

1. Download the VirtualBox executable file to your machine from [here](https://www.virtualbox.org/wiki/Downloads).  
2. Double-click the downloaded file to install it.  The file will end in either `.exe`, `.dmg`, `.rpm`, or `.deb` file extension depending on your operating system.

##### Step 2: Vagrant
1. Download the Vagrant executable file to your machine from [here](http://downloads.vagrantup.com/tags/v1.3.5).
2. Double-click the downloaded file to install it.  The file will end in either `.exe`, `.dmg`, `.rpm`, or `.deb` file extension depending on your operating system.


##### Step 3: Text Editor
If you don't have a text editor (like Notepad++, TextEdit, TextWrangler, Sublime Text), install Sublime Text 2. **NOTE:** Windows' users: select the downloadable file per your architecture (32-bit/64-bit).

1. download the executable file [here](http://www.sublimetext.com/2).
2. Double-click the downloaded file to install it.  The file will end in either `.exe`, `.dmg`, `.rpm`, or `.deb` file extension depending on your operating system.

##### Step 4: PyLadies prepacked Virtual Machine/Box
1. Download the `PyLadiesDjango.box` pre-packaged virtual machine from [here](https://dl.dropboxusercontent.com/u/15999054/PyLadiesDjango)
2. Save the pre-packaged virtual machine to a location you will remember for later. 
3. **DO NOT** open this file!!



**Continue to [Setup](#setup)** below when you're all set with downloading & installing.

### Using the USB stick

##### Step 1: VirtualBox

Install VirtualBox by running the `VirtualBox` executable file (`.exe`, `.dmg`, `.rpm`, or `.deb` file extension depending on your operating system) file from the USB stick.  Click through the install process, if any, like you normally would when installing a new program.

##### Step 2: Vagrant
Install Vagrant by running the `vagrant` executable (`.exe`, `.dmg`, `.rpm`, or `.deb` file extension depending on your operating system) file from the USB stick. Click through the install process, if any, like you normally would when installing a new program.

##### Step 3: Text Editor
If you don't have a text editor (like Notepad++, TextEdit, TextWrangler, Sublime Text), install Sublime Text 2.  Run the `Sublime Text` executable (`.exe`, `.dmg`, `.rpm`, or `.deb` file extension depending on your operating system) file from the USB stick.

##### Step 4: PyLadies prepacked Virtual Machine/Box
Save the pre-packaged PyLadies virtual machine titled `PyLadiesDjango.box` to some place you'll remember. **DO NOT** open this file!!

**Continue to [Setup](#setup)** below when you're all set with downloading & installing.


---

#### To read while you're waiting for everything to download.
##### What does this all mean?


* **Virtual Machine** is a computer within your computer.  You are able to create virtual machines to run many different types of operating systems, like Ubuntu, Fedora, and Debian, regardless if you own a Windows machine, a Mac, or a Linux machine. 
* In Installation Step #1, you downloaded **VirtualBox**.  VirtualBox is free software that allows you to run virtual machines on your computer. 
* For our workshop, we are running the Linux flavor called [**Ubuntu 12.04**](http://en.wikipedia.org/wiki/List_of_Ubuntu_releases#Ubuntu_12.04_LTS_.28Precise_Pangolin.29).  Why?  Because Linux-type environments make it really easy for Python development.  Also, Ubuntu is one of the most popular Linux-flavors out there within the developer circles.  It's very well supported.
* **Vagrant**, which you downloaded & installed in step 2 above, is a tool that developers often use to work with virtual machines.  It pairs nicely with the VirtualBox software that we downloaded.  
* All you need to know about Vagrant is that it makes it *very* easy to create virtual machines, so that I am able to give you an Ubuntu virtual machine that is ready to go for today's workshop.
* You may hear me refer to the PyLadiesDjango virtual machine (downloaded in step 3 above) as a "box" or a "vm".  These are the same things.
* You are able to reuse this virtual machine whenever you'd like!

##### An FYI for the not-so-n00b
##### Go ahead and skip this section if virtual machines are new to you.

* The vagrant box, "PyLadiesDjango", has python, pip, virtualenv, and virtualenvwrapper installed.  The whole system as also been updated as of Nov 18th, 2013.
* It also already as a "synced folder" setup, linked locally to `DjangoProj`, and on the VM to `/home/vagrant/DjangoProj`.  Any changes locally within `DjangoProj` will be reflected within `/home/vagrant/DjangoProj` on the VM, and vice-versa.   All code-work will be done locally within `DjangoProj`, and run within the VM. 
* The virtualenv "DjangoProj" has also already been created, with Django 1.6 installed.
* The virtual machine is setup to forward to port 8080 on the local machine from port 8000 on the vm.  Therefore, if you have a server running within the virtual machine, you will be able to see it on `localhost:8080` on the local machine.

---

## Setup

#### Setup some folders on your local machine
* Create a "pyladies" folder anywhere that you prefer.  **Take note** of _where_ you created that folder.
* Move the `PyLadiesDjango.box` virtual machine to the "pyladies" folder.
* Within the "pyladies" folder, create another folder called "DjangoProj".  **NOTE:** spelling and capitalization is important here!

#### Setup virtual machine
* Open up your command line program:
	* For **Windows**, click "Start", then select "run".  Type "cmd" and press enter.  You should see a screen with `C:\`, or `C:\Users\lynn>` prompt, where `lynn` is actually _your_ username.
	* For **Mac**, press "COMMAND+Space Bar" at the same time; you should get a "Spotlight" finder that pops up to the upper-right.  Type "terminal" and press enter.  You should just see the `$` prompt.
	* For **Linux**: I trust that you know where your terminal/shell is. :)
* Navigate to the "pyladies" folder that you created:
	* **Windows**: For instance, if you created the "pyladies" folder within "My Documents", then within the CMD/Command Prompt, type `cd C:\Documents and Settings\<username>\Desktop\My Documents\pyladies`.  Be sure to put in your own username for `<username`. The actual command/path may be different depending on capitalization, spelling, and actual location of where you put the "pyladies" folder.
	* **Mac**: For instance, if you created the "pyladies" folder within "Documents", then within your terminal, type: 	`cd Documents/pyladies`. 
	* **Linux**: Very similar to Mac, but perhaps your file heirarchy/path is different. 
* In the terminal/command line, type the following 3 commands.  **Make sure** that you are 1) within the "pyladies" directory, and 2) you moved the "PyLadiesDjango" box that you downloaded above within the "pyladies" directory. Note that each command may take a while.  You must wait for the process to finish before proceeding to the next command: 

	```bash
	vagrant box add PyLadiesVM PyLadiesDjango.box
	```

	```bash
	vagrant init
	```

	```bash
	vagrant up
	```

* You now have a virtual machine called "PyLadiesVM" using the "PyLadiesDjango" box that I gave you in step 3 of the installation process!