
vim.Capability
==============
  A particular product may or may not support certain features. This data object indicates whether or not a service instance implements these features. This data object type indicates the circumstances under which an operation throws a `NotSupported <vmodl/fault/NotSupported.rst>`_ fault.Support for some features is indicated by the presence or absence of the manager object from the service instance. For example, the AlarmManager manager object indicates collecting alarms is supported. Other features indicate whether or not a given operation on an object throws a `NotSupported <vmodl/fault/NotSupported.rst>`_ fault.Some capabilities depend on the host or virtual machine version. These are specified by using the vim.host.Capability and vim.vm.Capability objects.
:extends: vmodl.DynamicData_

Attributes:
    provisioningSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether or not the service instance supports provisioning. For example, the `CloneVM <vim/VirtualMachine.rst#clone>`_ operation.
    multiHostSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether or not the service instance supports multiple hosts.
    userShellAccessSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether host user accounts should have the option to be granted shell access
    supportedEVCMode ([`vim.EVCMode <vim/EVCMode.rst>`_], optional):

       All supported Enhanced VMotion Compatibility modes.
    networkBackupAndRestoreSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether network backup and restore feature is supported.
