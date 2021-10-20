.. _backend_server:

Back-End Server
===============

This page houses all documentation for the team's **back-end server**. 

.. note:: This project is currently *under development* and it maintained over at GitHub. The link to the repository can be found `here <https://github.com/sufst/back-end>`_.


1. Project Purpose
##################

The main purpose of the Back-End server is to store all data coming from the car while testing and/or while running on competitions. It also handles all user authentication and member permissions for the telemetry GUI. 

The Back-End consists of 3 main parts: 

1. **Users** RESTful API 
2. **Sessions** RESTful API 
3. *Storage* for users & sessions. 

- Project Priority: **HIGH**

.. note:: Although not 100% crusial for the car to run - meaning that the car can run in competition without a back-end server - this project is marked as **crusial**. Without a back-end server and a RESTful API, the telemetry GUI cannot function.

1. Development
##############

All code and project management resources for this project are hosted on the `GitHub <https://github.com/sufst/back-end>`_ repository. 

Contributions to the codebase by team members need to follow the team's General GitHub Contributing Guidelines available :ref:`intermediate server <inter_server>`

2.1 Technology Stack
--------------------

The web application is developed using the **technologies listed below**: 

- Python 
- Flask
- SQL

2.2 Building & Running 
------------------------

.. note:: In order to run the Back-End you'll need to have the SUFST VM configured on your computer and the back-end installed within that. Instruction to do that are found :ref:`here <vm_setup>.

To run the Back-End server please follow the steps below: 

1. Open the SUFST. 

THAT'S IT! 

If you have followed the instructions correctly while installing the server and configuring the VM, you shouldn't have to do anything extra! The server will run automatically once you open the SUFST VM!