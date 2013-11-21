=======
Pykaboo
=======

A convenient command line tool to check python source code from the python standard library and user installed packages.

Running Pykaboo opens a new tab in your browser listing your python standard library modules folder and user installed packages folder. New paths can also be added to this list. 

When clicking on a .py file, python syntax is highlighted and lines are numbered. 

Typical usage::

    $ pykaboo

Pykaboo shows only '.py' files and directories by default. But you can also allow files with other extensions to be viewed::

    $ pykaboo allow .css

Or you can add custom directories next to the default links to the standard library modules and user installed packages::

    $ pykaboo add ~/Documents/my_python_projects

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

     To use Pykaboo just run the following command in Cygwin::

         $ pykaboo

     In case you get errors, try `rebasing Cygwin <http://cygwin.wikia.com/wiki/Rebaseall>`_ .

* Using a virtual machine:

  `Here <http://www.psychocats.net/ubuntu/virtualbox>`_ you can find a tutorial to install the Linux distro Ubuntu on the virtual box virtual machine. Once installed see the Linux users section.

Support & bug reports
=====================
If you need support or if you spot bugs send a mail to *robrecht.de.rouck at gmail.com*. If you have a github account opening an issue or making a poll request is appreciated in case of bugs.

Note about usage
================
Shortly after it's last release **I stopped using Pykaboo for what it was intended**. At the time I made it I still worked with `Gedit <http://www.python.org/>`_ as my main editor, need I say more? 
It is **still convenient however in case I would want to print out a significant amount of specific files in a repository**.   

If you are wondering I now use `Vim <http://www.vim.org/>`_ as my editor and in case I'd want to find only Python files or a file with a specific name I would just use `find <http://linux.die.net/man/1/find>`_.
