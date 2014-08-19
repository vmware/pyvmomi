
vim.host.PowerSystem.Info
=========================
  Power System Info data object. Shows current state of power management system.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    currentPolicy (`vim.host.PowerSystem.PowerPolicy <vim/host/PowerSystem/PowerPolicy.rst>`_):

       Currently selected host power management policy. This property can have one of the values from `availablePolicy <vim/host/PowerSystem/Capability.rst#availablePolicy>`_ .
