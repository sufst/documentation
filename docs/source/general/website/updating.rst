Updating
========

.. note:: This page describes the process to update the SUFST website hosted at ``www.sufst.co.uk``.

Guide: 
######

1. Ensure the **latest code is pushed** to the ``main`` branch on the Github repo.
   
You'll need to have your PR approved by a Committee member for this. 

2. SSH into the Digital Ocean server. 

This requires **SSH access and a valid SSH key** so please ask committee if you feel you need to do work on the production server.

.. warning:: The username and IP address of the Digital Ocean server will not be published here. Please ask a Committee member for this information. 


3. From the home directory of the Digital Ocean server, run ``cd website-frontend``.

4. Run ``git pull``. 

This should pull the latest version from the ``main`` branch. You'll either need a GitHub SSH key or Personal Access Token for this. 

5. Run ``npm run-script build``.

**This should be it!!**

.. note:: Verifying it worked. ``/var/www/sufst.co.uk/html`` should now contain simlinks to the build folder within the sufst home directory. 

.. uml:: diagram.uml

   

