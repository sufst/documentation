Read the Docs Setup
===================

The aim of this page is to document the Read the Docs setup primarily for any
future maintainers.

The `SUFST Documentation project
<https://readthedocs.org/projects/sufst-documentation/>`_ on Read the Docs is
the home of all the documentation. It is linked to the `SUFST Documentation
repository <https://github.com/sufst/documentation>`_ on GitHub through a
``Webhook`` that has been set up.

.. danger::

   Do not link the webhook URL here as this would allow external parties to
   submit a webhook on our repository which could be bad.

The Read the Docs page is setup so that on a commit to the ``main`` branch an
automated build will occur. This will take a few minutes to process and will be
served as the ``lastest`` 'version'. Currently, it is setup to only build
``HTML`` and to ignore the option of creating an ``EPUB`` or a ``PDF``.

Other 'versions' are also made for every branch that exists within the
repository. This is done to allow people to test their changes before they
submit a pull request to the main branch. These are set to automatically be
'activated' and set to 'hidden' on branch creation and to be deleted when the
branch is deleted.

Read the Docs is also setup to use a custom sub-domain of ``docs.sufst.co.uk``.
This is done through ``CNAME`` record on the ``sufst.co.uk`` domain and is
further described on the website page.

.. note::
   Link to website page written above when the page is created

The site currently uses the `Furo theme <https://pradyunsg.me/furo/>`_ which
was chosen for it's clean interface and easy customization. The customizations
made are mainly to have the SUFST image shown in the sidebar as well as changing
the primary colours to be the SUFST blue. The changes are made in the
``conf.py`` file for the project and are shown below:

.. code:: python

   html_logo = "_img/stag.svg"

   html_theme_options = {
     "light_css_variables": {
       "color-brand-primary": "#0066cc",
       "color-brand-content": "#0066cc",
     },
     "dark_css_variables": {
       "color-brand-primary": "#0066cc",
       "color-brand-content": "#0066cc",
     },
   }

The Furo theme also has good integration with some common Sphinx packages like
`Sphinx Inline Tabs <https://github.com/pradyunsg/sphinx-inline-tabs>`_ and
`Sphinx Copybutton <https://github.com/executablebooks/sphinx-copybutton>`_ and
was another reason it was chosen.
