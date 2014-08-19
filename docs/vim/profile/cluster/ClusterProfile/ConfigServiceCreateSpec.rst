
vim.profile.cluster.ClusterProfile.ConfigServiceCreateSpec
==========================================================
  DataObject which allows reconfiguration of a profile based on services that will be available on the cluster.
:extends: vim.profile.cluster.ClusterProfile.ConfigSpec_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    serviceType ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Type of the service for which the ClusterProfile is being requested. If more than one service is specified, the created ClusterProfile will cater for all the services. Possible values are specified by `ClusterProfileServiceType <vim/profile/cluster/ClusterProfile/ServiceType.rst>`_ . If unset, clear the compliance expressions on the profile.
