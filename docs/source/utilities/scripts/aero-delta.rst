Aero Delta
===============

Aero Delta is a Python script designed to take two CFD output images as inputs and produce an output image showing the difference in various areodynamic performance measures. It has been extended to take a path to a folder of base images and compare them all to a corresponding set of images that the delta is desired for.

Instructions for Usage
######################

Follow the instructions for installation and use below. 

.. tip:: You must have Python installed and on your PATH

Installation
************
Clone the repository

.. code:: none
    
    git clone https://github.com/sufst/Aero-Visual-Delta.git

Navigate into the repository directory

.. code:: none

    cd Aero-Visual-Delta

.. tip:: It is recommended to create a virtual environment to install Python packages

Install required packages

.. code:: none

    pip install -r requirements.txt

Usage
*****

For example, consider the file structure below:

.. code:: none

    .
    └── Aero-Images
        ├── Base
        │   ├── frame000.png
        │   ├── frame001.png
        │   └── frame002.png
        └── Test
            ├── frame000.png
            ├── frame001.png
            └── frame002.png

If you wished to find the delta for the images in the *Base* directory to the images in the *Test* directory, you would run the following command 

.. code:: none

    python delta-visualise.py "Aero-Images/Base" "Aero-Images/Test"

Where the two path arguments may be either absolute paths, or relative paths from wherever you are running the script from.

.. tip:: Ensure that you wrap both path argument in double quotation marks, this prevents special characters causing problems.

The script will create a new folder called *"delta"* with the delta visualise images. The folder structure below demonstrates the output of the script:

.. code:: none

    .
    └── Aero-Images
        ├── Base
        │   ├── frame000.png
        │   ├── frame001.png
        │   └── frame002.png
        ├── Test
        │   ├── frame000.png
        │   ├── frame001.png
        │   └── frame002.png
        └── delta
            ├── delta000.png
            ├── delta001.png
            └── delta003.png


.. note::

    Should the *Base* and *Test* directories not have the same parent directory, the output *delta* directory will be in the same directory as the *Base* directory.