=======
Pykaboo
=======

A convenient command line tool to check python source code from the python standard library and user installed packages.

Running Pykaboo opens a new tab in your browser listing your python standard library modules folder and user installed packages folder. New paths can also be added to this list. 

When clicking on a .py file, python syntax is highlighted and lines are numbered. 

Typical usage::

    $ pykaboo

For a list of commands::

    $ pykaboo help

Installation
============
Linux and OS X users
--------------------
First install `pip <http://guide.python-distribute.org/installation.html#installing-pip>`_. Then::

    $ pip install pykaboo

Windows users
-------------
Use Cygwin or use a Linux distro on a virtual machine.

* Using Cygwin:

  1. Install `Cygwin <http://www.cygwin.com/>`_. During the installation, also mark the ``bins`` of ``Python`` (under Interpreters) and ``wget`` (under Web) for installation. 

  2. In the Cygwin terminal run the following commands::
    
         $ wget http://peak.telecommunity.com/dist/ez_setup.py
         $ python ez_setup.py
         $ easy_install pip
         $ pip install pykaboo

     To use Pyakboo just run the following command in Cygwin::

         $ pykaboo

     In case you get errors, try `rebasing Cygwin <http://cygwin.wikia.com/wiki/Rebaseall>`_ .

* Using a virtual machine:

  `Here <http://www.psychocats.net/ubuntu/virtualbox>`_ you can find a tutorial to install the Linux distro Ubuntu on the virtual box virtual machine. Once installed see the Linux users section.

Support & bug reports
=====================
If you need support or if you spot bugs send a message to *robrecht.de.rouck at gmail.com*. If you have a github account opening an issue or making a poll request is appreciated in case of bugs.
