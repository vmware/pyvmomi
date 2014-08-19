vim.fault.DeviceNotSupported.Reason
===================================
  Reasons why a virtual device would not be supported on a host.
  :contained by: `vim.fault.DeviceNotSupported <vim/fault/DeviceNotSupported.rst>`_

  :type: `vim.fault.DeviceNotSupported.Reason <vim/fault/DeviceNotSupported/Reason.rst>`_

  :name: guest

values:
--------

host
   The host does not support this virtual device at all.

guest
   The device is supported by the host in general, but not for the specific guest OS the virtual machine is using.
