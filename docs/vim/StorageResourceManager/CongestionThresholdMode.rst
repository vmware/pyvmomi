.. _congestionThreshold: ../../vim/StorageResourceManager/IORMConfigInfo.rst#congestionThreshold

.. _vim.StorageResourceManager: ../../vim/StorageResourceManager.rst

.. _vim.StorageResourceManager.CongestionThresholdMode: ../../vim/StorageResourceManager/CongestionThresholdMode.rst

vim.StorageResourceManager.CongestionThresholdMode
==================================================
  User specification of congestion threshold mode on a given datastoreFor more information, see `congestionThreshold`_ 
  :contained by: `vim.StorageResourceManager`_

  :type: `vim.StorageResourceManager.CongestionThresholdMode`_

  :name: manual

values:
--------

manual
   Use user specified Storage IO Control congestion threshold value

automatic
   Storagage IO Control will choose appropriate congestion threshold value for that datastore to operate at given percentage of peak throughput. This is the default setting
