#[IanClark.me](http://www.ianclark.me)#
##Django-based personal website and blog##
Thanks for checking out the codebase. I designed this site both to create blog articles and to document my hobbies and skills. 

##Getting Started##
This project has a number of dependencies. Noteably, these include: 
* Python 2 and PIP for Django and additional libraries (Use VirtualEnv) - `requirements/requirements.pip.txt`
    * Once complete you can launch a local HTTP server using `python manage.py runserver`
* Ruby for Sass (Use Bundler) - `Gemfile`
    * Once complete you can have Compass poll for changes using `compass watch`
* Node for automatic Closure compilation (via grunt) - `requirements/requirements.npm.txt`
    * Once complete you can have grunt poll for changes using `grunt watch`
