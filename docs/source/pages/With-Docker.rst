With Docker
===========
.. WARNING:: For unix distribution only

Installing docker
-----------------

Please follow the instructions `here <https://docs.docker.com/install/linux/docker-ce/debian/>`_ for a debian computer.

For a raspberry installation please follow `this guide <https://phoenixnap.com/kb/docker-on-raspberry-pi>`_.

.. note:: Don't forget to run the following command at the end of the installation (and logout)

    .. code-block:: bash

        sudo usermod -aG docker $USER

    so you don't have this permission denied error each time you use a docker command : `permission denied while trying to connect to daemon socket`.


Running stable kenbot
----------------------

1. Download kenbot stable

.. code-block:: bash

   docker pull gotbase/kenbot:stable

2. Start kenbot (for linux x64/x86 and raspberry linux arm64/arm32)

.. code-block:: bash

   docker run -itd --name kenbot -p 80:5001 -v $(pwd)/user:/kenbot/user -v $(pwd)/tentacles:/kenbot/tentacles -v $(pwd)/logs:/kenbot/logs gotbase/kenbot:stable

Running latest kenbot image build (may be unstable)
----------------------------------------------------

1. Download kenbot latest

.. code-block:: bash

   docker pull gotbase/kenbot:latest

2. Start kenbot (for linux x64/x86 and raspberry linux arm64/arm32)

.. code-block:: bash

   docker run -itd --name kenbot -p 80:5001 -v $(pwd)/user:/kenbot/user -v $(pwd)/tentacles:/kenbot/tentacles -v $(pwd)/logs:/kenbot/logs gotbase/kenbot:latest

How to look at kenbot logs ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   docker logs kenbot -f

How to stop kenbot ?
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   docker stop kenbot

How to restart kenbot ?
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   docker restart kenbot

How to update kenbot ?
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   docker pull gotbase/kenbot:stable
   docker stop kenbot
   docker rm kenbot
   docker run -itd --name kenbot -p 80:5001 -v $(pwd)/user:/kenbot/user -v $(pwd)/tentacles:/kenbot/tentacles -v $(pwd)/logs:/kenbot/logs gotbase/kenbot:stable

Running with docker-compose
---------------------------

A simple way to run a docker image is to use docker-compose : 


* Install `docker-compose <https://docs.docker.com/compose/install/>`_
* Download the `docker-compose.yml file <https://github.com/gotbase/kenbot/blob/master/docker-compose.yml>`_
* Create a `.env` file in the current folder
* Add `HOST=YOUR_IP_ADDRESS` in the newly created `.env` file. (where YOUR_IP_ADDRESS is the ip address of the computer, can be replaced by `localhost` if it's a local computer)
* Start kenbot with docker-compose (with the previous file `docker-compose.yml` in the current folder) :

  .. code-block:: bash

     docker-compose up -d

You can now open the kenbot web interface at https://YOUR_IP_ADDRESS.

Start multiple kenbots with docker
---------------------------------------

To run a second kenbot on the same computer :

1. Create a new directory and enter it

2. Start kenbot's web interface on a new port by changing "-p" option

.. code-block:: bash

   docker run -itd --name kenbot -p 8000:5001 -v $(pwd)/user:/kenbot/user -v $(pwd)/tentacles:/kenbot/tentacles -v $(pwd)/logs:/kenbot/logs gotbase/kenbot:stable

In this example, the second kenbot's web interface is accessible at http://127.0.0.1:8000.

Any port can be used except those already used by another kenbot or any software on your system.

Start kenbot with docker managed files
---------------------------------------
.. WARNING:: It's easier to use but it will not be possible to update it without deleting its files.

-v arguments can be removed from previous start commands but kenbot's local files will then be managed by docker (and not directly visible).

.. code-block:: bash

   docker run -itd --name kenbot -p 80:5001 gotbase/kenbot:stable

Local kenbot files path are located in /var/lib/docker and can be listed with the following command

.. code-block:: bash

   docker inspect -f '{{ .Mounts }}' kenbot

To copy files of a directory outside the kenbot container, for example for logs files :

.. code-block:: bash

   docker cp kenbot:/kenbot/logs/. .

Wherer "kenbot" is your container name
