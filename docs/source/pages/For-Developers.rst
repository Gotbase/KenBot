Developer installation
================================

Requirements
-------------------------------


* Python 3.8 (\ `download <https://www.python.org/downloads/>`_\ )
* Git (\ `Download <https://git-scm.com/downloads>`_\ )

Instructions
-------------------------------

Windows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Python3.8 has to be in environment variable** :

During `python install <https://www.python.org/downloads>`_ check *add to environment var* checkbox.

Open a command line and type :

.. code-block:: bash

   git clone https://github.com/gotbase/kenbot -b dev
   cd kenbot
   python3 -m pip install -Ur requirements.txt
   python3 start.py tentacles --install --all

There **python3** is refering to your **Python3.8.X** installation, just adapt the commands to match your setup if any different (might be python, python3, python3.8, etc: it depends on your environment).

Note that python3.8 might be available under the name **python3.8** after this installation.

Update kenbot with python only when using kenbot code directly from dev branch
--------------------------------------------------------------------------------

Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Python3.8.X**\ , **git** and an installed and **functional kenbot setup** cloned from `kenbot github repository <https://github.com/gotbase/kenbot>`

.. code-block:: bash

   $ git pull origin dev
   $ python3 -m pip install -Ur requirements.txt
   $ python3 start.py tentacles --install --all

Python3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There **python3** is refering to your **Python3.8.X** installation, just adapt the commands to match your setup if any different (might be python, python3, python3.8, etc: it depends on your environment).


With Repo
-------------------------------
Repo is a tool built on top of Git. Repo helps manage many Git repositories.

To create a development kenbot environment, repo can be used as following :

- `Install repo <https://source.android.com/setup/build/downloading#installing-repo>`_
- Create a directory for the kenbot environment
- Create kenbot developer environment by running

.. code-block:: bash

   repo init -u https://github.com/gotbase/kenbot-Repo-Manifest.git

- Synchronize repositories

.. code-block:: bash

   repo sync

All required kenbot projects are now available in the current directory :

.. code-block:: bash

    Async-Channel
    kenbot
    kenbot-Backtesting
    kenbot-Commons
    kenbot-Evaluators
    kenbot-Services
    kenbot-Tentacles
    kenbot-Tentacles-Manager
    kenbot-Trading
