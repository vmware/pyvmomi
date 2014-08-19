
vim.vApp.CloneSpec.NetworkMappingPair
=====================================
  Maps one network to another as part of the clone process.Instances of this class are used in the field `networkMapping <vim/vApp/CloneSpec.rst#networkMapping>`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    source (`vim.Network <vim/Network.rst>`_):

       The source network
    destination (`vim.Network <vim/Network.rst>`_, privilege: Network.Assign):

       The destination network
