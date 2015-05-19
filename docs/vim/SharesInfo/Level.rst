.. _level: ../../vim/SharesInfo.rst#level

.. _shares: ../../vim/SharesInfo.rst#shares

.. _vim.SharesInfo: ../../vim/SharesInfo.rst

.. _vim.SharesInfo.Level: ../../vim/SharesInfo/Level.rst

.. _networkResourcePoolHighShareValue: ../../vim/DistributedVirtualSwitch/FeatureCapability.rst#networkResourcePoolHighShareValue

vim.SharesInfo.Level
====================
  Simplified shares notation. These designations have different meanings for different resources.
  :contained by: `vim.SharesInfo`_

  :type: `vim.SharesInfo.Level`_

  :name: custom

values:
--------

high
   For CPU: Shares = 2000 * nmumber of virtual CPUsFor Memory: Shares = 20 * virtual machine memory size in megabytesFor Disk: Shares = 2000For Network: Shares = `networkResourcePoolHighShareValue`_ 

custom
   If you specifycustomfor the `level`_ property, when there is resource contention the Server uses the `shares`_ value to determine resource allocation.

low
   For CPU: Shares = 500 * number of virtual CPUsFor Memory: Shares = 5 * virtual machine memory size in megabytesFor Disk: Shares = 500For Network: Shares = 0.25 * `networkResourcePoolHighShareValue`_ 

normal
   For CPU: Shares = 1000 * number of virtual CPUsFor Memory: Shares = 10 * virtual machine memory size in megabytesFor Disk: Shares = 1000For Network: Shares = 0.5 * `networkResourcePoolHighShareValue`_ 
