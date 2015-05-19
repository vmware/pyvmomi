.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _ConfigSpecOperation: ../../../vim/ConfigSpecOperation.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.VspanSession: ../../../vim/dvs/VmwareDistributedVirtualSwitch/VspanSession.rst


vim.dvs.VmwareDistributedVirtualSwitch.VspanConfigSpec
======================================================
  This class defines the configuration of a Distributed Port Mirroring session. A Distributed Port Mirroring session
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    vspanSession (`vim.dvs.VmwareDistributedVirtualSwitch.VspanSession`_):

       The Distributed Port Mirroring session to be reconfigured.
    operation (`str`_):

       Operation type, see `ConfigSpecOperation`_ for valid values.
