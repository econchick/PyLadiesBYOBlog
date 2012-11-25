PyLadiesBYOBlog
===============

Build Your Own Django Blog

PyLadiesSF workshop hosted on May 12th, 2012<br />
PyLadiesCZ workshop hosted on November 16th, 2012<br />
PyLadiesHR workshop hosted on December 15/16th, 2012<br />

Info about [PyLadiesSF](www.meetup.com/PyLadiesSF "PyLadiesSF meetup") <br />
Info about [PyLadiesCZ](www.meetup.com/PyLadiesCZ "PyLadiesCZ meetup")<br />
Info about [PyLadies](www.pyladies.com "PyLadies Main Site")

This Django-based site is the very barest of bones for a blogging site.  It uses Django's function-defined views as opposed to Django's Class-Based-Views.

<b>For folks wanting to contribute:</b> Anyone is welcome to contribute!  Please be excessively clear in whatever code you're adding with hyper-aware documentation.  

<b>For ladies wanting to use this to build your own blog, </b>here is a quick, barebones  overview of what you will need:

1. Download Git (this is not a GitHub account) found [here](http://git-scm.com/downloads "Git Downloads")<br /><br />
	**Optional**: it's nice to get in the hang of using proper tools for managing web applications and projects.  Suffice it to say, it's highly recommended to use virtualenv, a tool that manages projects with their respective packages.<br /><br />
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
	
	Skip step 2.
2. Download and Install [Django](https://www.djangoproject.com/download/ "Django Download")
3. **OPTIONAL** If you want comments on your blog, I'd suggest using [Disqus](http://disqus.com).  A free account is required.  We _could_ build our own comment system pretty easily within the blog, but we would not have spam filters setup properly.  To set up comments, follow the template portion of the [slides](ineedtoputthelinkehere) (refer to notes of the second template slide, where you copy HTML files).

**NOTE** If you want to work through the workshop again yourself (which I highly suggest), please take a look at the [slides](ineedtoputthelinkhere) to walk you through, and skip these next steps until #6: Deployment.  

You can poke around at my code as you go along in this repository. 

**NOTE** the following steps use _my_ code, which is already a complete blog application.  

**A complete blog: **

4. Now, fork this repo: `$ git clone git@github.com:econchick/PyLadiesBYOBlog.git`  

4. Edit the `settings.py` file to your own project.  You will need to make a random string of letters, numbers, and characters for `SECRET_KEY`.  Do not share your settings publically.

5. In PyLadiesBYOBlog directory from the command line, type: `python manage.py runserver`

6. Navigate to `localhost:8000/admin` and throw up a few blog posts.

7. Navigate to `localhost:8000` to see your posts.

8. Deployment: **OPTIONAL**  If you want folks to see your blog, then I'd suggest deploying on [Heroku](http://heroku.com) or [OpenShift](http://openshift.redhat.com) (be wary, I had a difficult time deploying on OpenShift).  You will need an account with either, but due to the small size of your application, it will be free to put up online.  <br /><br />
Heroku has a great [how-to Deploy Django](https://devcenter.heroku.com/articles/django) using their services. 

ADDITIONAL RESOURCES
--------------------
1. [The main Django Tutorial](https://docs.djangoproject.com/en/1.4/intro/tutorial01/)
2. [Learn Python the Hard Way](http://learnpythonthehardway.com): A great way to practice Python for brand new folks.
3. [Boston Python Workshop Tutorial](https://openhatch.org/wiki/Boston_Python_Workshop_6/Friday/Tutorial) This site goes into more detail regarding Python data structures.
4. [CodingBat](http://codingbat.com/python) Practice small Python exercises.
5. [More Simple Django Project Tutorials](http://lightbird.net/dbe/) Where this blog application got its inspiration!

=======


TODO
----

0. Get OpenShift to work.

1. Adding Disqus comments (account required).

3. Adding the ability to format text when blogging using a WYSIWYG editor (WYSIWYG = 'what you see is what you get').

4. Ability to upload media (e.g. images) - may be just adding another application to the Project Site.
