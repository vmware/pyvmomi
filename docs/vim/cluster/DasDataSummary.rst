.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _RetrieveDasData: ../../vim/ClusterComputeResource.rst#retrieveDasData

.. _vim.cluster.DasData: ../../vim/cluster/DasData.rst

.. _ClusterDasDataDetails: ../../vim/cluster/DasDataDetails.rst


vim.cluster.DasDataSummary
==========================
  This class contains the summary of the data that DAS needs/uses. The actual data is available in `ClusterDasDataDetails`_ and can be retrieved using the `RetrieveDasData`_ method. This class is meant for VMware internal use only.
:extends: vim.cluster.DasData_
:since: `vSphere API 5.0`_

Attributes:
    hostListVersion (`long`_):

       The version corresponding to the hostList
    clusterConfigVersion (`long`_):

       The version corresponding to the clusterConfig
    compatListVersion (`long`_):

       The version corresponding to the compatList
