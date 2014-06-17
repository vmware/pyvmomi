.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vim.fault.HostConfigFault: ../../vim/fault/HostConfigFault.rst

.. _vim.host.PowerSystem.Info: ../../vim/host/PowerSystem/Info.rst

.. _vmodl.fault.InvalidArgument: ../../vmodl/fault/InvalidArgument.rst

.. _vim.host.PowerSystem.Capability: ../../vim/host/PowerSystem/Capability.rst


vim.host.PowerSystem
====================
  Managed object responsible for getting and setting host power management policies.


:since: `vSphere API 4.1`_


Attributes
----------
    capability (`vim.host.PowerSystem.Capability`_):
      privilege: Host.Config.Power
       Power system capabilities object.
    info (`vim.host.PowerSystem.Info`_):
      privilege: Host.Config.Power
       Power system state info object.


Methods
-------


ConfigurePowerPolicy(key):
   Configure host power policy.


  Privilege:
               Host.Config.Power



  Args:
    key (`int`_):
       A key from one of the policies in `availablePolicy`_ .




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault`_: 
       for any other failure.

    `vmodl.fault.InvalidArgument`_: 
       if an invalid power policy key is provided.


