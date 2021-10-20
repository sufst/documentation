Wireless Telemetry GUI 
======================

This page houses all documentation for the team's real-time **Wireless Telemetry GUI**. 

.. note:: This project is currently *under development* and it maintained over at GitHub. The link to the repository can be found `here <https://github.com/sufst/wireless-telemetry-gui>`_.


1. Project Purpose
##################

The main purpose of the Telemetry GUI is to provide the team with a **real-time telemetry system** that can be used to access and validate car performance during testing and/or competitions. 

Data coming from the sensors placed in the car need to be *wirelessly transmitted* to the GUI and then *graphed in real-time* with a small - or close to zero - delay. 

- Project Priority: **HIGH**

.. note:: Although not 100% crusial for the car to run - meaning that the car can run in competition without a telemetry GUI - this project is marked as **crusial** since it is essential that team members and Tier 1 are able to view that the car behaves as expected while running. 


2. Development
##############

All code and project management resources for this project are hosted on the `GitHub <https://github.com/sufst/wireless-telemetry-gui>`_ repository. 

Contributions to the codebase by team members need to follow the team's General GitHub Contributing Guidelines available :ref:`intermediate server <inter_server>`

2.1 Technology Stack
--------------------

The web application is developed using the **technologies listed below**: 

- TypeScript - JavaScript 
- React.js 
- Redux 
- Material UI

2.2 Building & Running 
------------------------

.. note:: In order to run the Telemetry GUI you'll need to have both the :ref:`intermediate server <inter_server>` and :ref:`intermediate server <backend_server>` running on the **SUFST VM** or your local computer. 

To run the Telemetry GUI please follow the steps below: 

1. Open the SUFST VM and run ``ifconfig``. 

Note the IP of the VM down, you'll need this later. 

2. Clone the from GitHub. 

You do this by running ``https://github.com/sufst/wireless-telemetry-gui.git`` on an directory. 

3. Move into the ``wireless-telemetry-gui`` folder

You do this by running ``cd wireless-telemetry-gui``. 

4. Open ``src/config.ts``.

Replace line 25 by the VM IP you noted down earlier in the following format: ``<ip>:5000``

5. Run the app from the command line. 

Being in the ``wireless-telemetry-gui`` folder, run ``npm run start``. A browser window should appear with the telemetry app running on ``localhost:3000``. 







