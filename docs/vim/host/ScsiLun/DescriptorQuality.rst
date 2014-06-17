.. _vim.host.ScsiLun: ../../../vim/host/ScsiLun.rst

.. _vim.host.ScsiLun.DescriptorQuality: ../../../vim/host/ScsiLun/DescriptorQuality.rst

vim.host.ScsiLun.DescriptorQuality
==================================
  An indicator of the utility of Descriptor in being used as an identifier that is stable, unique, and correlatable.
  :contained by: `vim.host.ScsiLun`_

  :type: `vim.host.ScsiLun.DescriptorQuality`_

  :name: unknownQuality

values:
--------

mediumQuality
   The Descriptor has an identifier that may be used for identification and correlation across hosts.

unknownQuality
   The Descriptor has an identifier that may or may not be useful for identification and correlation across hosts.

highQuality
   The Descriptor has an identifier that is useful for identification and correlation across hosts.

lowQuality
   The Descriptor has an identifier that should not be used for identification and correlation across hosts.
