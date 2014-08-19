
vim.dvs.VmwareDistributedVirtualSwitch.VspanConfigSpec
======================================================
  This class defines the configuration of a Distributed Port Mirroring session. A Distributed Port Mirroring session
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    vspanSession (`vim.dvs.VmwareDistributedVirtualSwitch.VspanSession <vim/dvs/VmwareDistributedVirtualSwitch/VspanSession.rst>`_):

       The Distributed Port Mirroring session to be reconfigured.
    operation (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Operation type, see `ConfigSpecOperation <vim/ConfigSpecOperation.rst>`_ for valid values.
