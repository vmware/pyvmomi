
vim.profile.cluster.ClusterProfile.CompleteConfigSpec
=====================================================
  DataObject completely specifying the configuration of the profile.
:extends: vim.profile.cluster.ClusterProfile.ConfigSpec_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    complyProfile (`vim.profile.ComplianceProfile <vim/profile/ComplianceProfile.rst>`_, optional):

       User defined compliance profile for the cluster. If unset, clear the complyProfile.
