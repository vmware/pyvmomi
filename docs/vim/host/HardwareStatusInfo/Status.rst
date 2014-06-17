.. _vim.host.HardwareStatusInfo: ../../../vim/host/HardwareStatusInfo.rst

.. _vim.host.HardwareStatusInfo.Status: ../../../vim/host/HardwareStatusInfo/Status.rst

vim.host.HardwareStatusInfo.Status
==================================
  The current status of the hardware
  :contained by: `vim.host.HardwareStatusInfo`_

  :type: `vim.host.HardwareStatusInfo.Status`_

  :name: Red

values:
--------

Unknown
   The implementation cannot report on the current status of the physical element

Green
   The physical element is functioning as expected

Red
   The physical element is failing. It is possible that some or all functionalities of this physical element is degraded or not working.

Yellow
   All functionality is available but some might be degraded.
