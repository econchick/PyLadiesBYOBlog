PyLadiesBYOBlog
===============

Build Your Own Django Blog

PyLadiesSF workshop hosted on May 12th, 2012
PyLadiesCZ workshop hosted on November 16th, 2012

Info about [PyLadiesSF](www.meetup.com/PyLadiesSF "PyLadiesSF meetup") 

Info about [PyLadiesCZ](www.meetup.com/PyLadiesCZ "PyLadiesCZ meetup")

Info about [PyLadies](www.pyladies.com "PyLadies Main Site")

This Django-based site is the very barest of bones for a blogging site.  It uses Django's class based views as opposed to the Django tutorial's function-defined views.

For folks wanting to contribute: Anyone is welcome to contribute!  Please be excessively clear in whatever code you're adding with hyper-aware documentation.  

For ladies wanting to use this to build your own blog, here is a quick, barebones  overview of what you will need:

1. Download Git (this is not a GitHub account) found [here](http://git-scm.com/downloads "Git Downloads")
**Optional**: If you want to deploy on OpenShift:
	1. Sign up for an [OpenShift Account](https://openshift.redhat.com/app/account/new "OpenShift Acct Signup")
	2. Follow the directions to install [Red Hat tools](https://openshift.redhat.com/community/get-started "RHC install")
	3. `$ rhc setup` and follow instructions.
	4. `$ rhc app create -a {{app name}} -t python`
	5. Continue on!
	
	**Optional**: it's nice to get in the hang of using proper tools for managing web applications and projects.  Suffice it to say, it's highly recommended to use virtualenv, a tool that manages projects with their respective packages.<br />
	On a Mac: `$ sudo easy_install pip`<br />
	On Ubuntu: `$ sudo apt-get pip`<br />
	On Fedora: `$ sudo yum install pip`<br />
	On Windows: TODO <br />
	
	For Everyone:
	
	`$ pip install virtualenv` <br />
	`$ pip install virtualenvwrapper` <br />
	`$ export WORKON_HOME=~/Envs` <br />
	`$ mkdir -p $WORKON_HOME` <br />
	`$ source /usr/local/bin/virtualenvwrapper.sh` <br />
	`$ mkvirtualenv {{ prj_name }}` <br />
	`(prj_name)$ pip install django` <br />
	
	Skip to step 3.
2. Download and Install [Django](https://www.djangoproject.com/download/ "Django Download")

3. **Note**: if you created an OpenShift account, and installed the tools, fork this repo into the application directory that the `rhc app create` process did : 
	
	`$ git clone git@github.com:econchick/PyLadiesBYOBlog.git {{directory name}}`


4. For those that did not create an OpenShift account, fork this repo: `$ git clone git@github.com:econchick/PyLadiesBYOBlog.git`  

4. Edit the `settings.py` file to your own project.  You will need to make a random string of letters, numbers, and characters for `SECRET_KEY`.  Do not share your settings publically.

5. In PyLadiesBYOBlog directory from the command line, type: `python manage.py runserver`

6. Navigate to 'localhost:8000/admin' and throw up a few blog posts.

7. Navigate to 'localhost:8000' to see your posts.

If you created an OpenShift account and downloaded the Red Hat tools:

1. `$ git commit -am "your message here, e.g. 'initial commit'"`
2. `$ git push`
3. You should see it live!


=======


TODO
--------

0. Lulz openshift doesn't actually work.

1. Proper Sphinx documentation

2. Fixing the comment form to be visable & to work

3. Adding the ability to format text when blogging using a WYSIWYG editor (WYSIWYG = 'what you see is what you get')

4. Ability to upload media (e.g. images), link to other pages
