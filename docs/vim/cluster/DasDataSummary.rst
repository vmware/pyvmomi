
vim.cluster.DasDataSummary
==========================
  This class contains the summary of the data that DAS needs/uses. The actual data is available in `ClusterDasDataDetails <vim/cluster/DasDataDetails.rst>`_ and can be retrieved using the `RetrieveDasData <vim/ClusterComputeResource.rst#retrieveDasData>`_ method. This class is meant for VMware internal use only.
:extends: vim.cluster.DasData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    hostListVersion (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The version corresponding to the hostList
    clusterConfigVersion (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The version corresponding to the clusterConfig
    compatListVersion (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The version corresponding to the compatList
