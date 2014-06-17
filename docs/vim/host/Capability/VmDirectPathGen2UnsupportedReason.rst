.. _vim.host.Capability: ../../../vim/host/Capability.rst

.. _vmDirectPathGen2UnsupportedReason: ../../../vim/host/Capability.rst#vmDirectPathGen2UnsupportedReason

.. _vim.host.Capability.VmDirectPathGen2UnsupportedReason: ../../../vim/host/Capability/VmDirectPathGen2UnsupportedReason.rst

vim.host.Capability.VmDirectPathGen2UnsupportedReason
=====================================================
  Set of possible values for `vmDirectPathGen2UnsupportedReason`_ .
  :contained by: `vim.host.Capability`_

  :type: `vim.host.Capability.VmDirectPathGen2UnsupportedReason`_

  :name: hostNptDisabled

values:
--------

hostNptIncompatibleProduct
   The host software does not support VMDirectPath Gen 2.

hostNptIncompatibleHardware
   The host hardware does not support VMDirectPath Gen 2. Note that this is a general capability for the host and is independent of support by a given physical NIC.

hostNptDisabled
   The host is configured to disable VMDirectPath Gen 2.
