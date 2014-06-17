.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vim.HostSystem: ../../vim/HostSystem.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.cluster.HostRecommendation
==============================
  A DRS recommended host for either powering on, resuming or reverting a virtual machine, or migrating a virtual machine from outside the cluster.
:extends: vmodl.DynamicData_

Attributes:
    host (`vim.HostSystem`_):

       The recommended host.
    rating (`int`_):

       Rating for the recommendation. Ratings range from 1 to 5, and the higher the rating, the stronger DRS suggests this host is picked for the operation.
