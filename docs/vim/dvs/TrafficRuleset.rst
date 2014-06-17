.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.dvs.TrafficRule: ../../vim/dvs/TrafficRule.rst


vim.dvs.TrafficRuleset
======================
  This class defines a ruleset(set of rules) that will be applied to network traffic.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    key (`str`_, optional):

       The key of the ruleset.
    enabled (`bool`_, optional):

       Whether ruleset is enabled or not.
    precedence (`int`_, optional):

       Precedence of the ruleset. Rulesets for a port will be executed in the order of their precedence.
    rules (`vim.dvs.TrafficRule`_, optional):

       List of rules belonging to this ruleset.
