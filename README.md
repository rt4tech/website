# RestoreThe4th.com

### About this project:

Official repo for designing/developing the restorethe4th.com website.

We're using [Django](https://www.djangoproject.com) and several other technologies/projects. A full list can be found in the `requirements.txt` file.

**If you plan on contributing code you should fork the repo and submit pull requests.**

# Prepare for Local Development

Most instructions here are specifically tailored to OS X and [homebrew](http://brew.sh), though you should have little trouble getting things to work on Linux using your distro's package manager.

### Get the code

First, clone the repo to your local development directory. Using the example below, it will clone into a directory named `rt4-site`. 

    $ git clone https://github.com/rt4tech/website rt4-site

If you prefer a different name, just alter that after the repo URL when you use `git clone`.  Directory structure really doesn't matter. Just move/clone things to whatever suits your development style.

**From here, it is expected that the next several steps are executed from inside the cloned repo. Please make sure you've changed directories before proceeding.**

    $ cd rt4-site

### Install system requirements

There are a few packages you'll need to have installed to ensure you can run the app successfully in an environment that closely matches the production server. These packages are `postgresql`, `memcached`, and `libmemcached`. On OS X, [Homebrew is your friend](http://brew.sh):

    $ brew install postgresql libmemcached
    
This should install postgres, libmemcached, memcached, and libevent when finished. **Before moving on, you should read the instructions printed after `postgres` & `memcached` install that tell you how to start up the applications. If you do not start them, you will run into problems later when you need to use them.

**NOTE: Do not skip this step. The project will not successfully run.**

### Install Python/Django requirements

Make sure you've [installed virtualenv](http://www.virtualenv.org/en/latest/virtualenv.html#installation). Assuming you have `pip` installed, it should be as simple as:

    $ sudo pip install virtualenv

Now, for least amount of hassle, you can take advantage of the existing `.gitignore` file and create a virtualenv at `/path/to/rt4-site/.env`. One nice advantage to this approach is that it places the `virtualenv` in a *hidden* directory, which means less clutter when working with the project on the command line.

    $ virtualenv -p python2.7 .env
    
Now, activate the new `virtualenv`:

    $ source .env/bin/activate

Install the project's requirements with `pip`:

    $ pip install -r requirements.txt

If you get errors about `pylibmc`, you do not have libmemcached correctly installed on your system.

### Configuring the project

Create your local `config.yml` file. **You should still be inside the rt4-site directory**.

    $ cp config/config.yml.example config/config.yml

Create a local postgres database. **You should have postgres running at this time.**

    $ createdb rtf
    
Tell Django to sync the database schema:

    $ ./manage.py syncdb

Apply the database schema migrations:

    $ ./manage.py migrate rtf

Run the server:

    ./manage.py runserver
    
### Import data

Coming soon

### View the site

The dev site should now be viewable in your browser:
[http://localhost:8000](http://localhost:8000)

You'll get a page that looks nothing like the one on restorethe4th.com. You'll need to visit [the admin panel](http://127.0.0.1:8000/admin) and add a new page. Set the slug to "/" and it should take the place of the homepage.