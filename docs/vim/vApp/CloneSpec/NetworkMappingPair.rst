.. _vim.Network: ../../../vim/Network.rst

.. _networkMapping: ../../../vim/vApp/CloneSpec.rst#networkMapping

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.vApp.CloneSpec.NetworkMappingPair
=====================================
  Maps one network to another as part of the clone process.Instances of this class are used in the field `networkMapping`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    source (`vim.Network`_):

       The source network
    destination (`vim.Network`_, privilege: Network.Assign):

       The destination network
