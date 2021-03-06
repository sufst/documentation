.. _doc_structure:

Folder / File Structure
=======================

The structure of the documentation repository is described below with reference
to the root directory ``/``. It mainly follows the standard layout described in
the `Read the Docs documentation
<https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html>`_
but is outlined below for convenience.

- ``README.md``
- ``.readthedocs.yml`` -- Configuration file for Read the Docs
- ``docs/``  
  
  - ``Makefile`` -- Generated by Sphinx. Build docs locally with ``make html``
  - ``make.bat`` -- Windows 'Makefile' script
  - ``requirements.txt`` -- Python requirements file specifying Sphinx and theme version
  - ``source/`` -- Sources for the documentation
    
    - ``_img/`` -- Images related to main index page (favicon, SUFST logo)
    - ``conf.py`` -- Configuration file for Sphinx
    - ``index.rst`` -- Homepage for documentation
    - ``robots.txt`` -- Defines how search engine crawlers should treat the site
    - ``...`` -- Files and folders for the rest of the documentation

Documentation Source
--------------------

The majority of the source for the documentation is within the ``source/``
folder as outlined above. However, it is the structure within this folder that
should have some more explanation.

In the root of the folder is the ``index.rst`` file. This is the file that is
read when you first visit the documentation - this means it has basic blocks
like a title and text. However, this file also contains some ``.. toctree::``
directives. These define items in the sidebar - both sections (seen in a grey
colour and that don't have a link in the sidebar) as well as pages directly. If
you view this file you will notice that only the top level links are defined and
that they link to the index page within sub directories. It is these sub-index
pages that define the sidebar links for these sections.

The sub-pages' index file (normally within a sub-folder for example
`documentation/`) behaves in a similar way to the main index file in that it has
a title and content, however, it's ``.. toctree::`` directive also defines the
sub-items within the sidebar.

From here, the rest of the strucutre is probably best understood simply by
looking inside the repository. Files are given an appropriate name with the
``*.rst`` extension and placed inside a folder which acts as a grouping for the
sidebar links.

.. admonition:: Help! I still don't understand
  :class: caution
	  
  If you still don't understand the structure, a small example may help. Let's
  look at the following structure:

  - ``source/``
     
    - ``index.rst``
    - ``documentation/``

      - ``index.rst``
      - ``contributing.rst``
      - ``references.rst``
      - ``structure.rst``

    - ``website/``
      
      - ``...``
	  
  Here the ``index.rst`` file within the ``source/`` folder defines the top
  level sidebar content through the use of ``.. toctree::`` directives.

  The ``index.rst`` file within the ``documentation/`` folder defines the
  sidebar links to the *contributing*, *references* and *structure* pages. This
  should line up with what you see in the sidebar on your screen now.

  The other ``*.rst`` files are just regular reStructuredText files with related
  content.

  Finally the ``website/`` folder is an example of another top level in the
  sidebar and contains it's own content.
