
vim.dvs.TrafficRuleset
======================
  This class defines a ruleset(set of rules) that will be applied to network traffic.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The key of the ruleset.
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Whether ruleset is enabled or not.
    precedence (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Precedence of the ruleset. Rulesets for a port will be executed in the order of their precedence.
    rules ([`vim.dvs.TrafficRule <vim/dvs/TrafficRule.rst>`_], optional):

       List of rules belonging to this ruleset.
