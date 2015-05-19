.. _str: https://docs.python.org/2/library/stdtypes.html

.. _string: ../../str

.. _vmodl.RuntimeFault: ../../vmodl/RuntimeFault.rst

.. _ClusterFailoverHostAdmissionControlPolicy: ../../vim/cluster/FailoverHostAdmissionControlPolicy.rst


vim.fault.DisallowedOperationOnFailoverHost
===========================================
    :extends:

        `vmodl.RuntimeFault`_

  Fault thrown when an attempt is made to perform a disallowed operation on a host that has been configured as a failover host in an cluster that has High Availability enabled. See `ClusterFailoverHostAdmissionControlPolicy`_ . Examples of such operations are destroying a host, moving a host out of a cluster, or powering on a virtual machine on a specific host.

Attributes:

    host (`str`_)

    hostname (`str`_)




