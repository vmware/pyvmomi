.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.cluster.Action: ../../vim/cluster/Action.rst

.. _vmodl.ManagedObject: ../../vim.ExtensibleManagedObject.rst


vim.cluster.Recommendation
==========================
  Recommendation is the base class for any packaged group of actions that are intended to take the system from one state to another one.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    key (`str`_):

       Key to identify the recommendation when calling applyRecommendation.
    type (`str`_):

       Type of the recommendation. This differentiates between various of recommendations aimed at achieving different goals.
    time (`datetime`_):

       The time this recommendation was computed.
    rating (`int`_):

       A rating of the recommendation. Valid values range from 1 (lowest confidence) to 5 (highest confidence).
    reason (`str`_):

       A reason code explaining why this set of migrations is being suggested.
    reasonText (`str`_):

       Text that provides more information about the reason code for the suggested set of migrations.
    prerequisite (`str`_, optional):

       This recommendation may depend on some other recommendations. The prerequisite recommendations are listed by their keys.
    action (`vim.cluster.Action`_, optional):

       List of actions that are executed as part of this recommendation
    target (`vmodl.ManagedObject`_, optional):

       The target object of this recommendation.
