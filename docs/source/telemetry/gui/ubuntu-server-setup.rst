.. _vm_setup:

Installing Servers on a VM
==========================

.. important:: 

    Currently SUFST doesn't provide a pre-built VM image. You'll need to manually create a Virtual Machine (VM) and install all servers on it. Don't let this scare you. The process is quite simple and documented in this guide step-by-step. 

As you'll read in this section, SUFST's software infrastructure includes two important servers than need to be runnning and configured correctly for all telemetry systems to work properly. These are the :ref:`intermediate server <inter_server>` and the :ref:`back-end server <backend_server>`. 

The simplest way to run these is to install them on a **Virtual Machine** or **VM** for short. This guide will include the following parts: 

1. :ref:`Creating a Virtual Machine using VirtualBox. <creating_vm>`
2. :ref:`Installing the Intermediate Server on the VM. <inter_install>`
3. :ref:`Installing the Back-End Server on the VM. <backend_install>`

----

.. _creating_vm:

Creating a Virtual Machine using VirtualBox. 
--------------------------------------------

.. important:: Text appearing in *italic* brackets *[]* refers to a button that must be clicked. 

For creating the Virtual Machine, we recommend using the popular software **VirtualBox**. The steps to do this are the following: 

1. Download `Ubuntu Server 18.04.5 <https://ubuntu.com/download/server>`_. This should be a ``.iso`` file. 

2. Download `VirtualBox <https://www.virtualbox.org/>`_.

3. Create a new Ubuntu 64-bit Virtual-Machine in VirtualBox. To do this: 
    1. Open VirtualBox. 
    2. Click *[Expert Mode]*.
    3. Name -> ``sufst``. 
    4. Type -> ``Linux``.
    5. Version -> ``Ubuntu 64-bit``.
    6. Memory Size -> ``>= 2048MB``. Here 2048MB is the minimum but you specify more. 
    7. Create a virtual hard disk.
    8. Click *[Create]*.
    9. File size -> ``>=10.00GB``
    10. Hard disk file type -> ``VDI``
    11. Storage on physical disk -> ``Dynmanically allocated``.
    12. Click *[Create]*.
4. Set the VM Network adapter. 
    1. Click *[Settings]* on the new VM.
    2. Click *[Network]*.
    3. Attached to -> ``Bridged Adapter``.
    4. Name -> MAKE SURE IT IS YOUR LOCAL ADAPTER.
5. Having the VM selected in the left-hand side, click *[Start]* the VM.
6. A *[Select start-up disk]* menu should appear.
    1. Chose the Ubuntu Server 18.04.5 .iso file downloaded in step 1.
7. Click *[Start]*. 
8. Go through the Ubuntu server install.
    1. Most screens are straightforward.
    2. Configure a guided storage layout -> Set up this disk as an LVM group.
    3. Profile setup -> Rest of the guide assumes you put `sufst` for all fields.
    
    .. caution:: Rest of the guide assumes you put `sufst` for all fields.
    
    4. Install OpenSSH server -> Mark to install.
    5. The install of security updates may take a while...
9. Select *[Reboot]*.  This will appear once all updates are complete. 
10. On reboot it will say ``Please remove the installation medium``.
     1. If you don't want to assign more CPU, then restart the VM by clicking *[machine]* -> *[reset]* -> *[Reset]* on the VM window top bar.
     2. If you want to assign more CPU, then close the VM -> VM Settings -> System -> Processors -> <= 4 -> Start the VM.
11. Wait for VM to start. There should be a screen that starts with ``Ubuntu 18.04.5 LTS sufst tty1``.
12. If you know the VM IP Address skip this step, if not, follow below.
     1. Log in -> ``sufst``, hit enter ``sufst``, hit enter. 
     2. You should see the VM IP address in the top of the VM screen after you login. 
     3. If you can't see the IP, run:  
     
     .. code:: bash

        sudo apt install net-tools
     
     and run ``ifconfig``
     
     .. code:: bash

        sudo apt install net-tools 
    
     The VM IP will be under an ``inet`` section on one of the adapters [should be e.g. ``192.168.1.232``].

     4. The adapter will be named e.g. ``enp0s3`` [should be of a similar form but will be different on each VM].
13. SSH into the VM.
     1. Open a terminal. *If on Windows I recommend using Windows Terminal which is available on the Windows Store*.
     2. Run: ``ssh sufst@<IP>``. For example: 

     .. code:: bash
        
        ssh sufst@192.168.1.232
        
     3. If prompted for ``yes/no`` for security then select ``yes``.


Congratulations! You now have a **fully working Ubuntu Server VM!**. You can now continue in the next steps below, installing the SUFST servers. 

----

.. _inter_install:

Installing the Intermediate Server. 
--------------------------------------------

Now you'll need to install the **SUFST intermediate server**. The repository - source for this can be found `here <https://github.com/sufst/intermediate-server>`__. To do this follow the steps below. 

1. Open the SUFST VM and SSH into it. 
2. In the home directory of the VM run: 
    .. code:: bash

        git clone https://github.com/sufst/intermediate-server.git

    .. caution:: Here you might be asked to log in to GitHub using your username and password. Please go again and login. This is to make sure that you have the right to clone this repository - which as a SUFST member you do. 
3. Install Python by running the following commands one-by-one:
    1. ``sudo apt update``
    2. ``sudo apt install software-properties-common``
    3. ``sudo add-apt-repository ppa:deadsnakes/ppa`` *[Hit enter]*
    4. ``sudo apt update``
    5. ``sudo apt install python3.7`` -> *[Hit Y]*
    6. ``sudo apt install python3-pip`` -> *[Hit Y]*
    7. ``sudo apt-get install python3-venv`` -> *[Hit Y]*
4. Set up a Virtual Environment for the Intermediate Server by running the following: 
    1. ``cd ./intermediate-server``
    2. ``python3 -m venv inter-server-venv``
5. Set up the intermediate-server python environment by running the following: 
    1. ``source inter-server-venv/bin/activate`` -> ``(inter-server-venv)`` should now be right of the terminal user account.
    2. ``pip install wheel``.
    3. ``pip install pipenv``.
    4. ``pipenv install`` -> Should install all intermediate-server dependencies.
6. Test the intermediate-server using:
    1. ``python server.py``.
    2. The Licence should appear with no errors.
    3. Hit CTRL+C to close the server.
7. Set up the intermediate-server service by running:
    1. ``sudo touch /etc/systemd/system/intermediate-server.service``.
    2. ``sudo nano /etc/systemd/system/intermediate-server.service``.
    3. Copy the following: 
    
    .. code:: bash

        [Unit]
        Description=SUFST intermediate server service
        After=network.target
        
        [Service]
        User=sufst
        Group=www-data
        WorkingDirectory=/home/sufst/intermediate-server
        ExecStart=/home/sufst/intermediate-server/inter-server-venv/bin/python3 /home/sufst/intermediate-server/server.py
        
        [Install]
        WantedBy=multi-user.target
8. Start the intermediate-server service using: 
    1. ``sudo systemctl daemon-reload``.
    2. ``sudo systemctl enable intermediate-server.service``
    3. ``sudo systemctl start intermediate-server.service``
    4. ``sudo systemctl status intermediate-server.service``
    5. There should be no errors in the status of the intermediate-server service.
9. You can now exit the Python venv using ``deactivate``.

Congratulations! You have now installed the intermediate server into the VM!

----

.. _backend_install:

Installing the Back-End Server. 
--------------------------------------------

Now you'll need to install the **SUFST back-end server**. The repository - source for this can be found `here <https://github.com/sufst/back-end>`__. To do this follow the steps below. 

1. Open the SUFST VM and SSH into it. 
2. In the home directory of the VM run: 
    .. code:: bash

        git clone https://github.com/sufst/back-end.git

    .. caution:: Here you might be asked to log in to GitHub using your username and password. Please go again and login. This is to make sure that you have the right to clone this repository - which as a SUFST member you do. 
3. Set up a Virtual Environment for the Back-End by running the following: 
    1. ``cd ./back-end``
    2. ``python3 -m venv backend-venv``
4. Set up the back-end python environment by running the following: 
    1. ``source backend-venv/bin/activate`` -> ``(backend-venv)`` should now be right of the terminal user account.
    2. ``pip install wheel``.
    3. ``pip install pipenv``.
    4. ``pipenv install`` -> Should install all back-end dependencies.
5. Test the back-end using: 
    1. ``python server.py``.
    2. The Licence should appear with no errors.
    3. Hit CTRL+C to close the server.
6. Set up the back-end server service by running:
    1. ``sudo touch /etc/systemd/system/back-end.service``.
    2. ``sudo nano /etc/systemd/system/back-end.service``.
    3. Copy the following: 
    
    .. code:: bash

        [Unit]
        Description=SUFST backend service
        After=network.target
        
        [Service]
        User=sufst
        Group=www-data
        WorkingDirectory=/home/sufst/back-end
        ExecStart=/home/sufst/back-end/backend-venv/bin/python3 /home/sufst/back-end/server.py
        
        [Install]
        WantedBy=multi-user.target
7. Start the back-end service using: 
    1. ``sudo systemctl daemon-reload``.
    2. ``sudo systemctl enable back-end.service``
    3. ``sudo systemctl start back-end.service``
    4. ``sudo systemctl status back-end.service``
    5. There should be no errors in the status of the intermediate-server service.
8. You can now exit the Python venv using ``deactivate``.
9. Test if the back-end is reachable from a local machine. On a local machine [Most likely the machine you are running the VM on] -> go to ``http://<IP>:5000/user`` e.g. ``http://192.168.1.232:5000/user`` in a browser. You should see a response message along the lines of -> ``msg: "Missing Authorization Header"``.
10. Congradulations! You have a working back-end 👍 
