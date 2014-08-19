
vim.vm.Summary.ConfigSummary
============================
  A subset of virtual machine configuration.
:extends: vmodl.DynamicData_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the virtual machine.
    template (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag to determine whether or not this virtual machine is a template.
    vmPathName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Path name to the configuration file for the virtual machine
    memorySizeMB (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Memory size of the virtual machine, in megabytes.
    cpuReservation (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Configured CPU reservation in MHz
    memoryReservation (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Configured Memory reservation in MB
    numCpu (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Number of processors in the virtual machine.
    numEthernetCards (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Number of virtual network adapters.
    numVirtualDisks (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Number of virtual disks attached to the virtual machine.
    uuid (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Virtual machine BIOS identification.
    instanceUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       VC-specific identifier of the virtual machine
    guestId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Guest operating system identifier (short name).
    guestFullName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Guest operating system name configured on the virtual machine.
    annotation (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Description for the virtual machine.
    product (`vim.vApp.ProductInfo <vim/vApp/ProductInfo.rst>`_, optional):

       Product information. References to properties in the URLs are expanded.
    installBootRequired (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Whether the VM requires a reboot to finish installation. False if no vApp meta-data is configured.
    ftInfo (`vim.vm.FaultToleranceConfigInfo <vim/vm/FaultToleranceConfigInfo.rst>`_, optional):

       Fault Tolerance settings for this virtual machine. This property will be populated only for fault tolerance virtual machines and will be left unset for all other virtual machines. See `FaultToleranceConfigInfo <vim/vm/FaultToleranceConfigInfo.rst>`_ for a description.
    managedBy (`vim.ext.ManagedByInfo <vim/ext/ManagedByInfo.rst>`_, optional):

       Specifies that this VM is managed by a VC Extension. See the `managedBy <vim/vm/ConfigSpec.rst#managedBy>`_ property in the ConfigSpec for more details.
