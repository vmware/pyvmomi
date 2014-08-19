vim.StorageResourceManager.CongestionThresholdMode
==================================================
  User specification of congestion threshold mode on a given datastoreFor more information, see `congestionThreshold <vim/StorageResourceManager/IORMConfigInfo.rst#congestionThreshold>`_ 
  :contained by: `vim.StorageResourceManager <vim/StorageResourceManager.rst>`_

  :type: `vim.StorageResourceManager.CongestionThresholdMode <vim/StorageResourceManager/CongestionThresholdMode.rst>`_

  :name: manual

values:
--------

manual
   Use user specified Storage IO Control congestion threshold value

automatic
   Storagage IO Control will choose appropriate congestion threshold value for that datastore to operate at given percentage of peak throughput. This is the default setting
