Contributing
============

The following extract is taken from the `Media Wiki Documentation
<https://www.mediawiki.org/wiki/Help:Editing_pages>`_ and does a good job at
summarizing contributing to our documentation.

    The number one rule of wiki editing is to **be bold**. Go ahead - make
    changes. Other people can correct any mistakes you make, so have confidence,
    and give it a try! There are all kinds of editing conventions, rules, and
    philosophies for the editing of wiki pages, but the **be bold** rule is the
    most important of these!
    
    An edit can contribute whole new paragraphs or pages of information, or it
    can be as simple as fixing a typo or a spelling mistake. In general, try to
    add or edit text so that it is clear and concise. Most importantly, make
    sure you are always aiming to do something which improves the contents of
    the wiki.
    
The important takeaway from this is that you shouldn't be afraid to contribute
anything to the documentation.

In order to contribute, you will need to edit the contents of the `SUFST
documentation repository <https://github.com/sufst/documentation>`_ on GitHub.
As mentioned in the GitHub documentation, you will only be able to push changes
to the ``main`` branch through a pull request which then gets approved by a
member of the committee **but please don't let this put you off contributing!**

How to write documentation
--------------------------

As mentioned above, you shouldn't be afraid to contribute to the documentation
and as such, there is no wrong way to write documentation. However, there are
some best practices.

This is a tricky topic to cover well so we would encourage you to visit and read
through some of `Write the Docs <https://www.writethedocs.org/guide/>`_ which is
a brilliant resource on writing technical documentation. It covers topics such
as style, mindset as well as linking to examples of good documentation. It may
be that after reading through the site you come back to our documentation and
find areas you think could be improved. If this is the case **we would encourage
you to contribute** and make the documentation better.

What to write documentation on
------------------------------

The question of what you should be writing about is often brought up. In general
documentation on this site should be related to a specific project from either a
top-level view or from a hardware view. Any documentation that is related to
software should be written on a wiki page on GitHub for that particular
repository.
   
.. important::

  The idea of splitting hardware and software documentation is because of
  peoples familiarity with documentation. People who are writing code and
  pushing to GitHub have likely used GitHub flavoured markdown before and so
  have a lower barrier of entry and are more likely to be able to quickly
  contribute to documentation about their code directly on the GitHub.

  On the other hand, for those people working on hardware, whilst they may have
  some experience with markdown, keeping documentation that is from a hardware /
  top level view with the other SUFST documentation is more important than it
  having a slightly lower barrier to entry. Primarily this is because as someone
  flicks through documentation for the first time on this site they are more
  likely to be able to find something of interest relating to a specific project
  than reading through software documentation buried within a specific GitHub
  repository.

Syntax
------

Many of you will be familiar with the ``Markdown`` syntax used for things like
GitHub README files. We use `reStructuredText
<https://docutils.sourceforge.io/rst.html>`_ for our syntax. It is similar in
many aspects but was chosen because it provides features like tables
'out-of-the-box'. This means that guides are easier to follow and there is a
standard syntax.

This syntax has been written about many times before and in far more depth than
we will cover within this documentation. Links to some sources which cover this
can be found on the :ref:`references page <doc_references>`. However, for ease
of access, linked here are the `Furo Theme Demo
<https://pradyunsg.me/furo/kitchen-sink/demo/>`_ as well as the `Furo Theme
Reference section <https://pradyunsg.me/furo/reference/>`_ guides which provide
a good reference and showcase many of the features available within
reStructuredText using the same theme that we use for SUFST.

.. tip::
   
   At the bottom of the demo pages linked above a ``View Source`` button can be
   found which will show you the raw reStructuredText without any formatting
   which may help you in writing.

   This is also true for the page you are currently reading as well as any page
   on the SUFST documentation.

Another good source of information is `our own repository
<https://github.com/sufst/documentation>`_ for documentation which could be used
to find a certain element from reStructuredText.

Downloadable PDF Files
^^^^^^^^^^^^^^^^^^^^^^

You can also add downloadable PDF files in the source code and link them from the documentation using the ``:download`` directive in Sphinx. 

All PDF files should live under the ``resources/pdfs`` folder and linked from that location to each ``.rst`` file they need to be accessed from. 

**Example:**

.. code-block::
   
   Please check the :download:`FSG 2022 Rules <path_to_file.pdf>`.


Folder Structure
----------------

The folder / file structure of the documentation is outlined in the
:ref:`structure page <doc_structure>`.

The most important part is that the files you will most likely interact with are
in ``docs/source/...`` from the base of the `documentation repository
<https://github.com/sufst/documentation>`_. From here documentation is split
into sub-folders which correspond to the links in the left sidebar.

.. note::
   
   The actual structure of the sidebar isn't controlled by the directory
   structure directly, but is instead controlled through the use of ``..
   toctree::`` directives.

   See the :ref:`structure page <doc_structure>` for more information or
   alternatively, see the :ref:`references page <doc_references>` for external
   links on where to find more detail about this.

Within these sub-folders are other ``*.rst`` files which make up the main
content of the site. You will also see a ``img`` folder for some sub-folders.
In this folder lies images or assets that are applicable for that particular
folder. If an asset is needed in more than one place, it should be in more than
one ``img`` folder.


Assets / Images
^^^^^^^^^^^^^^^

When including assets or images in the documentation, thought should be taken as
to whether the asset should be placed directly into the appropriate ``img``
folder and subsequently stored on the GitHub or if it should be placed within
the `SUFST Sharepoint <https://sotonac.sharepoint.com/teams/sufst>`_.

The choice can often be made for you. If the asset / file you are wanting to
include is 'sensitive' and should only be accessible to members of SUFST and not
to the public, it should be placed within the Sharepoint. This is becacuse both
the GitHub repository and the documentation site itself are public and viewable
by anyone with the link. As such, placing a file within the Sharepoint will
require the user to sign in to their ``@soton.ac.uk`` email and will have to be
a member of the SUFST group on Sharepoint in order to view the file.

The other reason you may choose to put a file on the Sharepoint as opposed to
the GitHub is if the file could warrent having a local copy. An example may be a
datasheet for a product we use. If we only linked to the manufactures website,
there is nothing to say that file may not exist in the future and we would then
need to find a new datasheet. Putting the file on GitHub would also work,
however, in the case of a datasheet, having access to it from Sharepoint would
be beneficial since it is likely the rest of the project files will also be put
in a similar place.

Defining exact rules for this is difficult and would probably cause more
problems that is solves so if you are unsure, make your best guess and run it
past the committee when you are making you pull request.

.. hint::
  Some examples of files you may commonly come across and where best to put
  them:

  **Images** related to the content in the documentation
     In the appropriate ``img`` folder within the GitHub

  **Datasheets**
     Placed in the folder on Sharepoint which relates to that particular item
     (motor, inverter etc...) or project (BSPD, pre-charge etc...)

  **Schematics**
     Stored on GitHub but only within the repository they relate to.

     If you wish to include the full schematic, include a link to the repository
     and possibly an exported PDF from either the Sharepoint or the GitHub
     repository for that project.

     If you wish to include a small sub-section of a schematic to explain it in
     further detail, this can be an image that is stored in the appropriate
     ``img`` folder on the GitHub. If you choose this method, ensure it is of
     high enough resolution that it is clear, but not so large that it has a
     large file size.

  **Block Diagrams**
     If the block diagrams have been made using a tool like `draw.io
     <https://app.diagrams.net/>`_ (which we recommended), the source file
     (``*.drawio``) should be stored on the Sharepoint within the appropriate
     project folder.

     If you wish to include an actual image of the diagram rather than just a
     link to the ``*.drawio`` file, this image can be stored in the appropriate
     ``img`` folder within the GitHub. Ideally the format of the image would be
     a ``*.svg`` since is a vector format and will mean the diagram is clear at
     any size and draw.io can export this format. If you cannot use the
     ``*.svg`` format, using either a ``*.jpeg`` or a ``*.png`` (when
     transparency is needed) is the next best. As a reminder, try to keep the
     file sizes to a minimum.

Testing
-------

Automated
^^^^^^^^^

The easiest way to test your changes is through the automated setup that is
running in Read the Docs. When you make a branch on the `documentation
repository <https://github.com/sufst/documentation>`_ and push a commit to it,
your changes will automatically be built into your own version of the
documentation site. This version will be found at:
``https://docs.sufst.co.uk/en/<your-branch-name>`` where ``<your-branch-name>``
is the name of your branch.

.. note::
   This is not the 'live' version of the docs that everyone can see. This is
   simply a version that will exist for as long as your branch exists and whilst
   anyone can theoretically view it, it should only be used for testing before
   pushing to the ``main`` branch.

Local
^^^^^
   
The other option to test your changes is to test locally. This involves
installing Sphinx on your local machine and running the ``make html`` in
``/docs/``. This will cause a local version of the documentation to be built to
``/docs/build`` and the site can then be launched by opening
``/docs/build/html/index.html``.

To setup Sphinx locally you will need to run the following commands.

.. code:: bash

    git clone https://github.com/sufst/documentation.git
    cd documentation/docs
    pip install -r requirements.txt

Following this you will be able to run the make procedure above to build the
documentation locally. Any files you build will not be pushed to GitHub.

To run a local server that renders any changes to the source automatically, run the following command from within the ``docs/`` directory.

.. code:: bash

    make live

You can view the result using your browser by navigating to http://localhost:8081.
When you make any changes to the documentation, this will update automatically to include them.

