
vim.DistributedVirtualSwitch.Summary
====================================
  Summary of the distributed switch configuration.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the switch.
    uuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The generated UUID of the switch.
    numPorts (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Current number of ports, not including conflict ports.
    productInfo (`vim.dvs.ProductSpec <vim/dvs/ProductSpec.rst>`_, optional):

       The product information for the implementation of the switch.
    hostMember ([`vim.HostSystem <vim/HostSystem.rst>`_], optional):

       The names of the hosts that join the switch.
    vm ([`vim.VirtualMachine <vim/VirtualMachine.rst>`_], optional):

       The Virtual Machines with Virtual NICs that connect to the switch. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Since this property is on a DataObject, an update returned by WaitForUpdatesEx may contain values for this property when some other property on the DataObject changes. If this update is a result of a call to WaitForUpdatesEx with a non-empty version parameter, the value for this property may not be current.
    host ([`vim.HostSystem <vim/HostSystem.rst>`_], optional):

       The hosts with Virtual NICs that connect to the switch.
    portgroupName ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       The names of the portgroups that are defined on the switch.
    description (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       A description string of the switch.
    contact (`vim.DistributedVirtualSwitch.ContactInfo <vim/DistributedVirtualSwitch/ContactInfo.rst>`_, optional):

       The human operator contact information.
    numHosts (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The number of hosts in the switch. The value of this property is not affected by the privileges granted to the current user.
