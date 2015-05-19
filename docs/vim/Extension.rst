.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _managedBy: ../vim/vm/ConfigSpec.rst#managedBy

.. _VI API 2.5: ../vim/version.rst#vimversionversion2

.. _vim.Description: ../vim/Description.rst

.. _vmodl.DynamicData: ../vmodl/DynamicData.rst

.. _vim.Extension.ServerInfo: ../vim/Extension/ServerInfo.rst

.. _vim.Extension.HealthInfo: ../vim/Extension/HealthInfo.rst

.. _vim.Extension.ClientInfo: ../vim/Extension/ClientInfo.rst

.. _vim.ext.ManagedEntityInfo: ../vim/ext/ManagedEntityInfo.rst

.. _vim.Extension.ResourceInfo: ../vim/Extension/ResourceInfo.rst

.. _vim.Extension.TaskTypeInfo: ../vim/Extension/TaskTypeInfo.rst

.. _vim.ext.ExtendedProductInfo: ../vim/ext/ExtendedProductInfo.rst

.. _vim.Extension.EventTypeInfo: ../vim/Extension/EventTypeInfo.rst

.. _vim.ext.SolutionManagerInfo: ../vim/ext/SolutionManagerInfo.rst

.. _vim.Extension.PrivilegeInfo: ../vim/Extension/PrivilegeInfo.rst

.. _vim.Extension.FaultTypeInfo: ../vim/Extension/FaultTypeInfo.rst

.. _vim.Extension.OvfConsumerInfo: ../vim/Extension/OvfConsumerInfo.rst


vim.Extension
=============
  This data object type contains all information about an extension. An extension may contain zero or more server interfaces and zero or more clients.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    description (`vim.Description`_):

       Description of extension.
    key (`str`_):

       Extension key. Should follow java package naming conventions for uniqueness (e.g. "com.example.management").Extension names can only contain characters belonging to the lower ASCII character set (UTF-7) with the exception of the following characters:
        * All whitespace characters ("space" - ascii character 0x20 is allowed)
        * Control characters
        * Comma (ascii 0x2c), Forward slash (ascii 0x2f), Backward slash (ascii 0x5c), Hash/Pound (ascii 0x23), Plus (ascii 0x2b), Greater (ascii 0x3e), Lesser (ascii 0x3c), Equals (ascii 0x3d), Semi-colon (ascii 0x3b) and Double quote (ascii 0x22).
    company (`str`_, optional):

       Company information.
    type (`str`_, optional):

       Type of extension (example may include CP-DVS, NUOVA-DVS, etc.).
    version (`str`_):

       Extension version number as a dot-separated string. For example, "1.0.0"
    subjectName (`str`_, optional):

       Subject name from client certificate.
    server ([`vim.Extension.ServerInfo`_], optional):

       Servers for this extension.
    client ([`vim.Extension.ClientInfo`_], optional):

       Clients for this extension.
    taskList ([`vim.Extension.TaskTypeInfo`_], optional):

       Definitions of tasks defined by this extension.
    eventList ([`vim.Extension.EventTypeInfo`_], optional):

       Definitions of events defined by this extension.
    faultList ([`vim.Extension.FaultTypeInfo`_], optional):

       Definitions of faults defined by this extension.
    privilegeList ([`vim.Extension.PrivilegeInfo`_], optional):

       Definitions privileges defined by this extension.
    resourceList ([`vim.Extension.ResourceInfo`_], optional):

       Resource data for all locales
    lastHeartbeatTime (`datetime`_):

       Last extension heartbeat time.
    healthInfo (`vim.Extension.HealthInfo`_, optional):

       Health specification provided by this extension.
    ovfConsumerInfo (`vim.Extension.OvfConsumerInfo`_, optional):

       OVF consumer specification provided by this extension.
    extendedProductInfo (`vim.ext.ExtendedProductInfo`_, optional):

       Extended product information, such as URLs to vendor, product, etc.
    managedEntityInfo ([`vim.ext.ManagedEntityInfo`_], optional):

       Information about entities managed by this extension. An extension can register virtual machines as managed by itself, by setting the `managedBy`_ property of the virtual machine.
    shownInSolutionManager (`bool`_, optional):

       Opt-in to the Solution Manager. If set to true, this extension will be shown in the Solution Manager. If not set, or set to false, this extension is not shown in the Solution Manager.
    solutionManagerInfo (`vim.ext.SolutionManagerInfo`_, optional):

       Solution Manager configuration for this extension.
