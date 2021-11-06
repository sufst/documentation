Getting Started
===============

This **Getting Started** page will walk you through installing all the necessary pieces of software and creating all needed accounts to work with *SUFST's* version control system. 

As a team we use ``git``, the popular version control software, for managing source code, as well as `GitHub <https://github.com/>`_ for storing the ``git`` repositories online. For this we have set up a a **SUFST Organisation** within GitHub that serves as a central place for all the team's code repositories. The link for the organisation can be found `here <https://github.com/sufst>`__.  

.. attention:: If you already have git installed, have a GitHub account and have configured git to work with GitHub, feel free to skip this page. 

----

1. Installing git
-----------------

This wholy depends on your operating system, so jump in the right section according to what matches your personal device. We currently provide instructions for **Microsoft Windows** and **macOS**. 

Microsoft Windows
~~~~~~~~~~~~~~~~~

The easiest way to install ``git`` is straight from the Git website. Just go to https://git-scm.com/download/win and the download will start automatically. 

Run the installer that was downloaded and simply hit ``Next`` through the pages. The default settings are the recommended. 

After the installation is complete, a new program called **Git Bash** should appear in your computer. This is the default git shell. 

.. seealso:: Prefer written or video instructions? 
   - `Written <https://phoenixnap.com/kb/how-to-install-git-windows>`__
   - `Video <https://www.youtube.com/watch?v=2j7fD92g-gE&ab_channel=Simplilearn>`_

macOS
~~~~~

If you are on a macOS machine, installing ``git`` might not be needed as it could have been installed with some other software without you knowing. To check if you have ``git`` already installed, open a terminal window and type the following: 

.. code:: none

   git --version

If ``git`` is installed it should print something like: 

.. code:: none

   git version 2.30.1 (Apple Git-130)

If it isn't installed it will prompt you to install it using the Xcode Command Line tools. Follow the instructions presented and you should be all ready and set. To verify it worked, you can simply run ``git --version`` again using a terminal window.

.. seealso:: Prefer written instructions? 
   - `Written <https://www.atlassian.com/git/tutorials/install-git>`__


----

2. Creating a GitHub account
----------------------------

As mentioned, the team uses **GitHub** as a place to store all source code. To get you up and running with GitHub and the team's organisation, you first need to have a GitHub account. 

You can very easily sign up for an account `here <https://www.github.com/signup>`__. 

.. tip:: Although **not mandatory**, we strongly advise you to enable 2FA (2-Factor Authentication) on your GitHub account (as for every other important online account you have.)

----

3. Configuring GitHub to work with Git
--------------------------------------

Lastly, you'll need to link your GitHub account you just created with ``git`` that you installed earlier on. This is so all commits you create, code you write and later push onto the team's account is linked with correct GitHub account - in this case your account. 

Do to so open ``Git Bash`` if you're on Windows or a terminal window if you're on macOS and run the following 2 commands. 

.. code:: none

   git config ––global user.name “github_username”

.. code:: none

   git config ––global user.email “email_address”


.. tip:: Here you have to replace `github_username` and `email_address` with the ones you provided when you signed up to GitHub. For example, if your name was John Doe and your email was john@johndoe.com you'll need to run ``git config ––global user.name “John Doe”`` and ``git config ––global user.email “john@johndoe.com”``

.. admonition:: Not part of the SUFST GitHub Organisation?

   If you are not a member of the SUFST GitHub Organisation, please inform a Committee member so they can send you an invite to join! 

This is it! Congratulations. You have successfully configured all required pieces of software to start writing code for **SUFST**!
