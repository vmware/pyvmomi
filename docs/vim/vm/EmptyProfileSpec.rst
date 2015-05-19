.. _vSphere API 5.5: ../../vim/version.rst#vimversionversion9

.. _vim.vm.ProfileSpec: ../../vim/vm/ProfileSpec.rst


vim.vm.EmptyProfileSpec
=======================
  Specifies an empty Storage Policy for a Virtual Machine Home or a Virtual Disk object.The object is left without any profile association, and hence has no explicit policy driven requirements. This implies that object's policy driven SLAs are always met trivially.
:extends: vim.vm.ProfileSpec_
:since: `vSphere API 5.5`_

Attributes:
