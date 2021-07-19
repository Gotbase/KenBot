
Tests
=====

Requirements
------------

To run kenbot's tests, an kenbot development environment is necessary, development environment setup is described `here <Developer-Guide.html#environment-setup>`_

kenbot engine
--------------

To run kenbot's engine tests, use the *pytest tests* in kenbot's root folder :

.. code-block:: bash

   pytest tests

This will run all tests in the test folder.

Tentacles
---------

To run kenbot's tentacles tests, use the *pytest tentacles* command in kenbot's root folder :

.. code-block:: bash

   pytest tentacles

This will run all tests in the **tentacles** folder.
Testing tentacles works only if tentacles are installed on the tested kenbot. See `kenbot's tentacle manager <Tentacle-Manager.html>`_ to install tentacles.
