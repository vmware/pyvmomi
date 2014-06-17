.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _ruleset: ../../vim/host/FirewallInfo.rst#ruleset

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.Service.SourcePackage: ../../vim/host/Service/SourcePackage.rst


vim.host.Service
================
  Data object that describes a single service that runs on the host.
:extends: vmodl.DynamicData_

Attributes:
    key (`str`_):

       Brief identifier for the service.
    label (`str`_):

       Display label for the service.
    required (`bool`_):

       Flag indicating whether the service is required and cannot be disabled.
    uninstallable (`bool`_):

       Flag indicating whether the service can be uninstalled.
    running (`bool`_):

       Flag indicating whether the service is currently running.
    ruleset (`str`_, optional):

       List of firewall rulesets used by this service. Must come from the list of rulesets in `ruleset`_ .
    policy (`str`_):

       Service activation policy.See Policy
    sourcePackage (`vim.host.Service.SourcePackage`_, optional):

       The source package associated with the service
