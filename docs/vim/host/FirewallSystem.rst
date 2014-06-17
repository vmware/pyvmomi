.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vim.fault.NotFound: ../../vim/fault/NotFound.rst

.. _vim.host.FirewallInfo: ../../vim/host/FirewallInfo.rst

.. _vim.fault.HostConfigFault: ../../vim/fault/HostConfigFault.rst

.. _vim.ExtensibleManagedObject: ../../vim/ExtensibleManagedObject.rst

.. _vim.host.Ruleset.RulesetSpec: ../../vim/host/Ruleset/RulesetSpec.rst

.. _vim.host.FirewallInfo.DefaultPolicy: ../../vim/host/FirewallInfo/DefaultPolicy.rst


vim.host.FirewallSystem
=======================
  The FirewallSystem managed object describes the firewall configuration of the host.The firewall should be configured first by setting the default policy and then by making exceptions to the policy to get the desired openness.


:extends: vim.ExtensibleManagedObject_


Attributes
----------
    firewallInfo (`vim.host.FirewallInfo`_):
       Firewall configuration.


Methods
-------


UpdateDefaultPolicy(defaultPolicy):
   Updates the default firewall policy; unset fields are left unchanged.


  Privilege:
               Host.Config.NetService



  Args:
    defaultPolicy (`vim.host.FirewallInfo.DefaultPolicy`_):




  Returns:
    None
         


EnableRuleset(id):
   Opens the firewall ports belonging to the specified ruleset. If the ruleset has a managed service with a policy of 'auto' that is not running, starts the service.


  Privilege:
               Host.Config.NetService



  Args:
    id (`str`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       if the ruleset ID is unknown.

    `vim.fault.HostConfigFault`_: 
       if an internal error happend when reconfigure the ruleset.


DisableRuleset(id):
   Blocks the firewall ports belonging to the specified ruleset. If the ruleset has a managed service with a policy of 'auto' and all other rulesets used by the service are blocked, stops the service.


  Privilege:
               Host.Config.NetService



  Args:
    id (`str`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       if the ruleset ID is unknown.

    `vim.fault.HostConfigFault`_: 
       if an internal error happend when reconfigure the ruleset.


UpdateRuleset(id, spec):
   Update the firewall ruleset specification.
  since: `vSphere API 5.0`_


  Privilege:
               Host.Config.NetService



  Args:
    id (`str`_):


    spec (`vim.host.Ruleset.RulesetSpec`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       if the ruleset ID is unknown

    `vim.fault.HostConfigFault`_: 
       if the update of the ruleset failed.


RefreshFirewall():
   Refresh the firewall information and settings to pick up any changes made directly on the host.


  Privilege:
               Host.Config.NetService



  Args:


  Returns:
    None
         


