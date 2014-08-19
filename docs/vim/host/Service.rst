
vim.host.Service
================
  Data object that describes a single service that runs on the host.
:extends: vmodl.DynamicData_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Brief identifier for the service.
    label (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Display label for the service.
    required (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether the service is required and cannot be disabled.
    uninstallable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether the service can be uninstalled.
    running (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether the service is currently running.
    ruleset ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       List of firewall rulesets used by this service. Must come from the list of rulesets in `ruleset <vim/host/FirewallInfo.rst#ruleset>`_ .
    policy (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Service activation policy.See Policy
    sourcePackage (`vim.host.Service.SourcePackage <vim/host/Service/SourcePackage.rst>`_, optional):

       The source package associated with the service
