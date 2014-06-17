.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _negate: ../vim/NegatableExpression.rst#negate

.. _vSphere API 5.5: ../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../vmodl/DynamicData.rst


vim.NegatableExpression
=======================
  The base class for any type of setting or configuration to which negation can be applied. When used in a configuration information object: if `negate`_ is true, then ~(objectValue) will be used for the configuration. If false, then objectValue will be used as it is.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    negate (`bool`_, optional):

       Whether the configuration needs to be negated or not.
