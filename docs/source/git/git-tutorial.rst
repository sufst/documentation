Git & GitHub Tutorial
=====================

.. attention:: If you already have experience using git from the command line, making commits, pushing changes and working around the GitHub interface, feel free to skip this page. 

.. admonition:: Never used ``git``? We strongly recommend watching a video instead of reading this document. 
   
   You can watch one (or more) of the following videos. Most of them do a much better job at describing the topics than what I have done in this document. 

   * `Git and GitHub for Beginners - Crash Course <https://www.youtube.com/watch?v=RGOj5yH7evk&ab_channel=freeCodeCamp.org>`_. (Recommended - Long Video)
   * `Learn Git In 15 Minutes <https://www.youtube.com/watch?v=USjZcfj8yxE&t=1s&ab_channel=ColtSteele>`_. (Short Video)


.. caution:: Please take this guide as a reference / cheat-sheet. The main purpose of this document is NOT to teach someone Git & GitHub from scratch, but to provide reference for useful command and concepts should they need in the future. 

----

What is Git?
------------

According to their official `website <https://git-scm.com/>`_, ``git`` is described as: 

   Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

**But what does this mean?**

This basically means that ``git`` is a *software tool* that allows programmers to keep track of versions of their codebase, on an easy manner. Think about how many times you have needed to name files ``Essay.V01`` and then ``Essay.V02`` and then ``Essay.V03`` and then ``Essay.Vdon't-even-know-anymore``. Well, ``git`` saves you from doing that by keeping a history of every file you have created and allowing you to **revert back to any previous version** at any time. 

.. seealso:: 
   I won't go into to much technical detail in this section, however if you are interested you are encouraged to read more about the innerworkings of ``git`` from `here <https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F>`_.

----

What is GitHub?
---------------

**GitHub** is a remote version control system that allows users to **host their Git repositories online.** It is that simple! Basically, all ``git`` repositories that someone might have on their computer can be *pushed* (stored) to GitHub. This allows users to have a remote back-up of their codebase in case something goes wrong but most importantly GitHub allows **seemless collaboration** between developers on any project. 

.. seealso:: 

   A very good guide describing the differences between GitHub & Git as well as showing the GitHub interface can be found `here <https://kinsta.com/knowledgebase/what-is-github/>`_.


----

Git Commands
------------

1. ``git add``
~~~~~~~~~~~~~~

``git add`` is the command to use in order to **add** some (or even all) files you are working on into the git staging area. 

It can be run using: 

.. code:: none

   git add . 

or 

.. code:: none

   git add <filename>

This basically tell git to add these files into version control.  ``git add .`` adds **ALL** files into version control and ``git add <filename>`` adds only the specified file into version control. 

2. ``git commit``
~~~~~~~~~~~~~~~~~

``git commit`` commits all your working files into under a new **commit**. You will then be able to revert to any previously made commit if something goes wrong or should you need to. It is run using: 

.. code:: none

   git commit -m "<commit_message>"

For example: 

.. code:: none

   git commit -m "Added car sensors & graphs to dashboard"

3. ``git push``
~~~~~~~~~~~~~~~

As the name suggests, ``git push`` pushes your local changes and commits to the remote repository hosted on  GitHub. It works simply by running: 

.. code:: none

   git push

.. caution:: When pushing to a new branch you might be ask run ``git push --set-upstream origin <new_branch_name>``. 

Optionally, (although 99% of the time this won't be needed for SUFST work), you can specify to which remote to push and to which branch. This is done using: 

.. code:: none

   git push <remote_name> <branch_name> 

For Example: 
   
.. code:: none

   git push heroku main

4. ``git branch`` & ``git checkout``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To make a **new branch** in ``git`` and switch to it you must use the following 2 commands. 

.. code:: none

   git branch <branch_name>
   git checkout <branch_name>

There is a shorthand for these 2 by running: 

.. code:: none

   git checkout -b <branch_name>

To simply **list all branches** on a git repository you run: 

.. code:: none

   git branch

.. note:: According to your terminal shell, after running ``git branch`` the branch you are currently on could be highlighted. 


----

.. admonition:: SOMETHING WENT WRONG?

   Don't worry! Things go wrong with ``git`` and GitHub all the time. You can use `this site <https://ohshitgit.com/>`_ to check a list of possible things that could go wrong and a handy command list to fix the issue. Otherwise, as with everything in software development, the answer to your problems is simply a StackOverflow search away. 