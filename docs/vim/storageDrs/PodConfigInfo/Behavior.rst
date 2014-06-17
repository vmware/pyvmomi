.. _vim.storageDrs.PodConfigInfo: ../../../vim/storageDrs/PodConfigInfo.rst

.. _vim.storageDrs.PodConfigInfo.Behavior: ../../../vim/storageDrs/PodConfigInfo/Behavior.rst

vim.storageDrs.PodConfigInfo.Behavior
=====================================
  Storage DRS behavior.
  :contained by: `vim.storageDrs.PodConfigInfo`_

  :type: `vim.storageDrs.PodConfigInfo.Behavior`_

  :name: automated

values:
--------

manual
   Specifies that VirtualCenter should generate recommendations for virtual disk migration and for placement with a datastore, but should not execute the recommendations automatically.

automated
   Specifies that VirtualCenter should generate recommendations for virtual disk migration and for placement with a datastore. The recommendations for virtual disk migrations will be executed automatically, but the placement recommendations will be done manually.
