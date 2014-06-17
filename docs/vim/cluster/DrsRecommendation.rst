.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.cluster.DrsMigration: ../../vim/cluster/DrsMigration.rst


vim.cluster.DrsRecommendation
=============================
  DrsRecommendation describes a recommendation to migrate one or more virtual machines.
:extends: vmodl.DynamicData_
**deprecated**


Attributes:
    key (`str`_):

       Key to identify the recommendation when calling applyRecommendation.
    rating (`int`_):

       A rating of the recommendation. Valid values range from 1 (lowest confidence) to 5 (highest confidence).
    reason (`str`_):

       A reason code explaining why this set of migrations is being suggested.
    reasonText (`str`_):

       Text that provides more information about the reason code for the suggested set of migrations.
    migrationList (`vim.cluster.DrsMigration`_):

