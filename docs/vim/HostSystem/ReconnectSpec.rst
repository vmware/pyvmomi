.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.HostSystem.ReconnectSpec
============================
  Specifies the parameters needed to merge vCenter Server settings and host settings on reconnect.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    syncState (`bool`_, optional):

       This flag should be set if on a host reconnect, state such as virtual machine state in vCenter Server e.g. the virtual machine inventory and autostart rules, has to be propogated to the host. Any virtual machines that may have been unregistered or orphaned will be reregistered according to the vCenter Server inventory. Any autostart rules that may have changed on the host will be similarly restored. This flag is primarily intended for stateless hosts to enable vCenter Server to resync these hosts after a reboot.
