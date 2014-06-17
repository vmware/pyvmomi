.. _str: https://docs.python.org/2/library/stdtypes.html

.. _int: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _managedBy: ../../../vim/vm/ConfigSpec.rst#managedBy

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.vApp.ProductInfo: ../../../vim/vApp/ProductInfo.rst

.. _vim.ext.ManagedByInfo: ../../../vim/ext/ManagedByInfo.rst

.. _FaultToleranceConfigInfo: ../../../vim/vm/FaultToleranceConfigInfo.rst

.. _vim.vm.FaultToleranceConfigInfo: ../../../vim/vm/FaultToleranceConfigInfo.rst


vim.vm.Summary.ConfigSummary
============================
  A subset of virtual machine configuration.
:extends: vmodl.DynamicData_

Attributes:
    name (`str`_):

       Name of the virtual machine.
    template (`bool`_):

       Flag to determine whether or not this virtual machine is a template.
    vmPathName (`str`_):

       Path name to the configuration file for the virtual machine
    memorySizeMB (`int`_, optional):

       Memory size of the virtual machine, in megabytes.
    cpuReservation (`int`_, optional):

       Configured CPU reservation in MHz
    memoryReservation (`int`_, optional):

       Configured Memory reservation in MB
    numCpu (`int`_, optional):

       Number of processors in the virtual machine.
    numEthernetCards (`int`_, optional):

       Number of virtual network adapters.
    numVirtualDisks (`int`_, optional):

       Number of virtual disks attached to the virtual machine.
    uuid (`str`_, optional):

       Virtual machine BIOS identification.
    instanceUuid (`str`_, optional):

       VC-specific identifier of the virtual machine
    guestId (`str`_, optional):

       Guest operating system identifier (short name).
    guestFullName (`str`_, optional):

       Guest operating system name configured on the virtual machine.
    annotation (`str`_, optional):

       Description for the virtual machine.
    product (`vim.vApp.ProductInfo`_, optional):

       Product information. References to properties in the URLs are expanded.
    installBootRequired (`bool`_, optional):

       Whether the VM requires a reboot to finish installation. False if no vApp meta-data is configured.
    ftInfo (`vim.vm.FaultToleranceConfigInfo`_, optional):

       Fault Tolerance settings for this virtual machine. This property will be populated only for fault tolerance virtual machines and will be left unset for all other virtual machines. See `FaultToleranceConfigInfo`_ for a description.
    managedBy (`vim.ext.ManagedByInfo`_, optional):

       Specifies that this VM is managed by a VC Extension. See the `managedBy`_ property in the ConfigSpec for more details.
