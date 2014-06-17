.. _NotFound: ../../../vim/fault/NotFound.rst

.. _vim.host.ConfigChange: ../../../vim/host/ConfigChange.rst

.. _vim.host.ConfigChange.Operation: ../../../vim/host/ConfigChange/Operation.rst

vim.host.ConfigChange.Operation
===============================
  This list indicates the operation that should be performed for a network entity.
  :contained by: `vim.host.ConfigChange`_

  :type: `vim.host.ConfigChange.Operation`_

  :name: edit

values:
--------

edit
   Indicates changes on the network entity. The entity must exist or a `NotFound`_ error will be thrown.

add
   Indicates the addition of a network entity to the configuration.

remove
   Indicates the removal of a network entity from the configuration.
