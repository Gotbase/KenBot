.. role:: raw-html-m2r(raw)
   :format: html


Troubleshoot
============

Cannot connect to host www.tentacles.kenbot.online:443
-------------------------------------------------------

.. image:: https://raw.githubusercontent.com/gotbase/kenbot/assets/wiki_resources/troubleshoot-tentacles-url-error.png
   :target: https://raw.githubusercontent.com/gotbase/kenbot/assets/wiki_resources/troubleshoot-tentacles-url-error.png
   :alt: tentacles url error

.. code-block:: bash

    kenbot_tentacles_manager.api.util.tentacles_management Exception during InstallWorker processing: Cannot connect to host www.tentacles.kenbot.online:443 ssl:default [No address associated with hostname] (ClientConnectorError)

The tentacles server URL has changed, there is no more leading "www". Starting from 0.4.0b6, kenbot uses the latest URL.
To use kenbot previous versions, please first set this environment variable before downloading tentacles:

On Unix systems

.. code-block:: bash

   $ export TENTACLES_URL="https://tentacles.kenbot.online/repository/tentacles/officials/packages/full/base/0.4.0b4/any_platform.zip"
   $ python3 start.py tentacles --install --all

On Windows systems

.. code-block:: bash

   $ SET TENTACLES_URL=https://tentacles.kenbot.online/repository/tentacles/officials/packages/full/base/0.4.0b4/any_platform.zip
   $ python3 start.py tentacles --install --all

Using Docker

.. code-block:: bash

   $ docker run -itd --name kenbot -p 80:5001 -e TENTACLES_URL="https://tentacles.kenbot.online/repository/tentacles/officials/packages/full/base/0.4.0b4/any_platform.zip" -v $(pwd)/user:/kenbot/user -v $(pwd)/tentacles:/kenbot/tentacles -v $(pwd)/logs:/kenbot/logs gotbase/kenbot:stable

Where 0.4.0b4 is your kenbot version.

Windows
-------

Time synchronization
^^^^^^^^^^^^^^^^^^^^

This issue happens when error messages such as ``'recvWindow' must be less than ...`` appear.

Open an administrator terminal (``Win + X`` then ``A``) and type:

.. code-block:: bash

   net stop w32time
   net start w32time
   w32tm /resync
   w32tm /query /status

Code from `serverfault.com <https://serverfault.com/questions/294787/how-do-i-force-sync-the-time-on-windows-workstation-or-server>`_

Another solution found by @alpi on discord channel : `timesynctool.com <http://www.timesynctool.com>`_

kenbot freeze
^^^^^^^^^^^^^^

When running kenbot on Windows, clicking into the kenbot terminal (Powershell or Cmd) can freeze the log output and therefore freeze kenbot execution (kenbot will be waiting for the log to be published to continue).

To fix this issue, untick the "QuickEdit Mode" in your terminal properties and restart it.


.. image:: https://raw.githubusercontent.com/gotbase/kenbot/assets/wiki_resources/powerShellEditMode.jpg
   :width: 400 px
   :target: https://raw.githubusercontent.com/gotbase/kenbot/assets/wiki_resources/powerShellEditMode.jpg
   :alt: Powershell


.. image:: https://raw.githubusercontent.com/gotbase/kenbot/assets/wiki_resources/cmdQuickEdit.jpg
   :width: 400 px
   :target: https://raw.githubusercontent.com/gotbase/kenbot/assets/wiki_resources/cmdQuickEdit.jpg
   :alt: Cmd


To open the properties menu, right click on the terminal window header and select "properties".

Linux
-----

Time synchronization
^^^^^^^^^^^^^^^^^^^^

This issue happens when error messages such as ``'recvWindow' must be less than ...`` appear.

On Debian or Ubuntu, open a terminal and type:

.. code-block:: bash

   sudo service ntp stop
   sudo ntpd -gq
   sudo service ntp start

Requires ``ntp`` package installation ``sudo apt-get install ntp``.

Code from `askubuntu.com <https://askubuntu.com/questions/254826/how-to-force-a-clock-update-using-ntp#256004>`_.

Installation
^^^^^^^^^^^^

During pip install if you have SSL problems, open a terminal and type

.. code-block:: bash

   pip3 install service_identity --force --upgrade
