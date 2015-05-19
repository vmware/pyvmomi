.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.RuntimeFault: ../../vmodl/RuntimeFault.rst


vim.fault.DisallowedChangeByService
===================================
    :extends:

        `vmodl.RuntimeFault`_

  Fault thrown if the disallowed operation is invoked by the client. The change is disallowed because it conflicts with target state maintained by a service. The corresponding method is usually not disabled because only a subset of changes carried out by the method is disallowed. For example, an online extend executed via virtual machine reconfigure method is not allowed if replication is enabled on a virtual machine.

Attributes:

    serviceName (`str`_)

    disallowedChange (`str`_): is optional.




