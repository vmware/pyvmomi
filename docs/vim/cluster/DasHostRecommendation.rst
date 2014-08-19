
vim.cluster.DasHostRecommendation
=================================
  A host recommendation for a virtual machine managed by the VMware HA Service.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    host (`vim.HostSystem <vim/HostSystem.rst>`_):

       The recommended host.
    drsRating (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Rating as computed by DRS for a DRS-enabled cluster. Rating range from 1 to 5, and the higher the rating, the stronger DRS suggests this host is picked for the operation.
