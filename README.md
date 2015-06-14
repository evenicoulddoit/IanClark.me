#[IanClark.me](http://www.ianclark.me)#
##Django-based personal website and blog##
Thanks for checking out the codebase. I designed this site in early 2014, to create a personal blog, and document my hobbies and skills. This was my first ever Django project at the time.

##Getting Started##
The site is currently hosted on [Heroku](https://heroku.com/). To deploy, simply clone the repo into a new Heroku App, and add the following buildpacks:

1. https://github.com/heroku/heroku-buildpack-ruby.git
2. https://github.com/heroku/heroku-buildpack-nodejs.git
3. https://github.com/heroku/heroku-buildpack-python.git

The order *is* important, as Ruby is required to to provide the Sass binaries, which Node uses to compile both the CSS and JavaScript, which is then in turn collected by Django during the final stage of the deployment process.

To run locally, you should download the [Heroku Toolbelt](https://toolbelt.heroku.com/), and use Foreman to control the environment variables. By default, Postgres is used, and you will need to install a number of other dependencies, including:

* Python and packages.
  * Download PIP and then use `pip install -r requirements.txt`
* Ruby and packages.
  * `gem install bundler`
  * `bundle install`
* Node and packages:
  * `npm install`

With these dependencies installed, you can run Django's development server using `foreman start`
