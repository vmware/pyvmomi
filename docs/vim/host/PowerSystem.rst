
vim.host.PowerSystem
====================
  Managed object responsible for getting and setting host power management policies.


:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_


Attributes
----------
    capability (`vim.host.PowerSystem.Capability <vim/host/PowerSystem/Capability.rst>`_):
      privilege: Host.Config.Power
       Power system capabilities object.
    info (`vim.host.PowerSystem.Info <vim/host/PowerSystem/Info.rst>`_):
      privilege: Host.Config.Power
       Power system state info object.


Methods
-------


ConfigurePowerPolicy(key):
   Configure host power policy.


  Privilege:
               Host.Config.Power



  Args:
    key (`int <https://docs.python.org/2/library/stdtypes.html>`_):
       A key from one of the policies in `availablePolicy <vim/host/PowerSystem/Capability.rst#availablePolicy>`_ .




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for any other failure.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if an invalid power policy key is provided.


