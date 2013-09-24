restorethefourth.website
========================

### About this repo:

Official repo for designing/developing the restorethe4th.com website.
For now, the basic wireframe, layout, and information will be worked on.

This repo was made in direction and response with [http://www.reddit.com/r/restorethefourth/](http://www.reddit.com/r/restorethefourth/)

# Getting up to speed.

We're using [Django](https://www.djangoproject.com). If you aren't familiar it's very well documented.

### How to run the dev site on OS X (should work on Linux as well)
This is mostly command line stuff:

If you plan on contributing code you should fork the repo, I will assume you are familiar with that process.

First, make a directory for the project

    mkdir restorethefourth

Now clone the repo, it will clone into a directory named rtf, for the sake of convenience rename this directory to fourth.

    git clone https://github.com/100010001/rtf.git
    mv rtf fourth


Make sure you've [installed virtualenv](https://jamiecurle.co.uk/blog/installing-pip-virtualenv-and-virtualenvwrapper-on-os-x/).

Now create a virtualenv:

    virtualenv venv

Install requirements:

    pip install -r fourth/requirements.txt

If you get errors about pylibmc, ensure you have libmemcached installed on your system. If you get syntax errors from Python, it probably means you're using an unsupported version of Python (some requirements only work in Python 2.x).

Create your local_settings.py file

    cp fourth/rtf/local_settings.default fourth/rtf/local_settings.py

From the "fourth" directory, create a database:

    ./manage.py createdb

Now migrate the database:

    ./manage.py migrate rtf

Now run the server:

    ./manage.py runserver

The dev site is now your browser:
[http://localhost:8000](http://localhost:8000)

You'll get a page that looks nothing like the one on restorethe4th.com. You'll need to visit [the admin panel](http://127.0.0.1:8000/admin) and add a new page. Set the slug to "/" and it should take the place of the homepage.

# FAQ, Communications, Goals and Plans

## FAQ

* Why aren't we using Google Analytics?/We shouldn't use Google Analytics/Should we use Google analytics?

This has come up several times in IRC. There is an open ticket [here](https://github.com/100010001/rtf/issues/3) and you are welcome to discuss.

* I can't code but I'm a designer/marketer/have ideas.

Great, please check [reddit.com/r/restorethefourth](https://reddit.com/r/restorethefourth) and join #restorethefourth on irc.snoonet.org.

* I have a suggestion to bring to the developers.

Great, bring it up in our irc channel #r4dev on irc.snoonet.org, if the developers think it's in scope then open or have a developer open an issue on the github repo.

* I'm new to this whole git thing, where is a good place to get started?

Github has some great tutorials that should get you up to speed [here](https://help.github.com/articles/set-up-git)

## Communication:

#### IRC Channels:

* General Discussion: http://webchat.snoonet.org/?channels=restorethefourth
* Dev Discussion: http://webchat.snoonet.org/?channels=r4dev
* Graphic Design Discussion: http://webchat.snoonet.org/?channels=r4design
* Marketing Discussion: http://webchat.snoonet.org/?channels=r4marketing

## Goals and Plans

#### What we don't want to do:

We don't want this site to become bloated or watered down. We want to keep it simple and get it up and running quickly to support what's going on in reddit. We want to chose a technology that more than one or two people know so we've got a base that can work on it.


### Current Domain Names online:

* [restorethe4th.com](http://www.restorethe4th.com/)

####Domain Names Available:

* restorethefourth.us
* restorethe4th.com
* restorethe4th.la
* restorethefourthamendment.com
* restorethefourth.net

# About Restore the Fourth

The best place to read about what restore the fourth stands for is [on reddit.](http://www.reddit.com/r/restorethefourth) We are focussed on these three things:


1. By exercising our right to vote and peaceful protest, the removal from office of any official in government who acted against our fourth amendment rights. No apologies, no amends, simply removal from office. They have betrayed their oath to protect and defend the constitution, and must be removed.

2. Repeal the patriot act and other similar laws. If our currently elected representatives will not do so (highly unlikely), than we shall in the course of time elect those who will.

3. The implementation of a transparent government which respects the fourth amendment and represents the interests of the people of the United States of America.
