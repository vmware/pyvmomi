
vim.cluster.DrsRecommendation
=============================
  DrsRecommendation describes a recommendation to migrate one or more virtual machines.
:extends: vmodl.DynamicData_
**deprecated**


Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Key to identify the recommendation when calling applyRecommendation.
    rating (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       A rating of the recommendation. Valid values range from 1 (lowest confidence) to 5 (highest confidence).
    reason (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       A reason code explaining why this set of migrations is being suggested.
    reasonText (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Text that provides more information about the reason code for the suggested set of migrations.
    migrationList ([`vim.cluster.DrsMigration <vim/cluster/DrsMigration.rst>`_]):

