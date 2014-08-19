
vim.Extension
=============
  This data object type contains all information about an extension. An extension may contain zero or more server interfaces and zero or more clients.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    description (`vim.Description <vim/Description.rst>`_):

       Description of extension.
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Extension key. Should follow java package naming conventions for uniqueness (e.g. "com.example.management").Extension names can only contain characters belonging to the lower ASCII character set (UTF-7) with the exception of the following characters:
        * All whitespace characters ("space" - ascii character 0x20 is allowed)
        * Control characters
        * Comma (ascii 0x2c), Forward slash (ascii 0x2f), Backward slash (ascii 0x5c), Hash/Pound (ascii 0x23), Plus (ascii 0x2b), Greater (ascii 0x3e), Lesser (ascii 0x3c), Equals (ascii 0x3d), Semi-colon (ascii 0x3b) and Double quote (ascii 0x22).
    company (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Company information.
    type (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Type of extension (example may include CP-DVS, NUOVA-DVS, etc.).
    version (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Extension version number as a dot-separated string. For example, "1.0.0"
    subjectName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Subject name from client certificate.
    server ([`vim.Extension.ServerInfo <vim/Extension/ServerInfo.rst>`_], optional):

       Servers for this extension.
    client ([`vim.Extension.ClientInfo <vim/Extension/ClientInfo.rst>`_], optional):

       Clients for this extension.
    taskList ([`vim.Extension.TaskTypeInfo <vim/Extension/TaskTypeInfo.rst>`_], optional):

       Definitions of tasks defined by this extension.
    eventList ([`vim.Extension.EventTypeInfo <vim/Extension/EventTypeInfo.rst>`_], optional):

       Definitions of events defined by this extension.
    faultList ([`vim.Extension.FaultTypeInfo <vim/Extension/FaultTypeInfo.rst>`_], optional):

       Definitions of faults defined by this extension.
    privilegeList ([`vim.Extension.PrivilegeInfo <vim/Extension/PrivilegeInfo.rst>`_], optional):

       Definitions privileges defined by this extension.
    resourceList ([`vim.Extension.ResourceInfo <vim/Extension/ResourceInfo.rst>`_], optional):

       Resource data for all locales
    lastHeartbeatTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):

       Last extension heartbeat time.
    healthInfo (`vim.Extension.HealthInfo <vim/Extension/HealthInfo.rst>`_, optional):

       Health specification provided by this extension.
    ovfConsumerInfo (`vim.Extension.OvfConsumerInfo <vim/Extension/OvfConsumerInfo.rst>`_, optional):

       OVF consumer specification provided by this extension.
    extendedProductInfo (`vim.ext.ExtendedProductInfo <vim/ext/ExtendedProductInfo.rst>`_, optional):

       Extended product information, such as URLs to vendor, product, etc.
    managedEntityInfo ([`vim.ext.ManagedEntityInfo <vim/ext/ManagedEntityInfo.rst>`_], optional):

       Information about entities managed by this extension. An extension can register virtual machines as managed by itself, by setting the `managedBy <vim/vm/ConfigSpec.rst#managedBy>`_ property of the virtual machine.
    shownInSolutionManager (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Opt-in to the Solution Manager. If set to true, this extension will be shown in the Solution Manager. If not set, or set to false, this extension is not shown in the Solution Manager.
    solutionManagerInfo (`vim.ext.SolutionManagerInfo <vim/ext/SolutionManagerInfo.rst>`_, optional):

       Solution Manager configuration for this extension.
