PyLadiesBYOBlog
===============

Build Your Own Django Blog

PyLadiesSF workshop hosted on May 12th, 2012

Info about PyLadiesSF: www.meetup.com/PyLadiesSF

Info about PyLadies: www.pyladies.com


This Django-based site is the very barest of bones for a blogging site.  It uses Django's class based views as opposed to the Django tutorial's function-defined views.

For folks wanting to contribute: Anyone is welcome to contribute!  Please be excessively clear in whatever code you're adding with hyper-aware documentation.  

For ladies wanting to use this to build your own blog, here is a quick, barebones  overview of what you will need:

1) Download Git (this is not a GitHub account)

2) Create a GitHub account

3) Fork this repo (follow the GitHub directions on how to Fork a repo).  You will have a new folder called PyLadiesBYOBlog with the files we created at the workshop.

4) Make sure you have Django on your system.
	
	a) If you successfully got virtualenv/virtualenv wrapper, create a new virtual environment within the newly forked directory, PyLadiesBYOBlog
	b) Within your new virtualenv on your terminal/command line, type: pip install django

	c) If you do not have virtualenv, navitage to the newly forked directory from step 3 in your command line.
	d) In your command line, type: easy_install django
5) In PyLadiesBYOBlog directory from the command line, type: python manage.py runserver

6) Navigate to 'localhost:8000/admin' and throw up a few blog posts.

7) Navigate to 'localhost:8000' to see your posts.


On my TODO/wish list:

1) Proper Sphinx documentation

2) Fixing the comment form to be visable & to work

3) Adding the ability to format text when blogging using a WYSIWYG editor (WYSIWYG = 'what you see is what you get')

4) Ability to upload media (e.g. images), link to other pages