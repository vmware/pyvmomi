
vim.fault.DisallowedOperationOnFailoverHost
===========================================
    :extends:

        `vmodl.RuntimeFault <vmodl/RuntimeFault.rst>`_

  Fault thrown when an attempt is made to perform a disallowed operation on a host that has been configured as a failover host in an cluster that has High Availability enabled. See `ClusterFailoverHostAdmissionControlPolicy <vim/cluster/FailoverHostAdmissionControlPolicy.rst>`_ . Examples of such operations are destroying a host, moving a host out of a cluster, or powering on a virtual machine on a specific host.

Attributes:

    host (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    hostname (`str <https://docs.python.org/2/library/stdtypes.html>`_)




