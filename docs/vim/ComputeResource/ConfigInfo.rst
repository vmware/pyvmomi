.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _swapPlacement: ../../vim/vm/ConfigInfo.rst#swapPlacement

.. _perVmSwapFiles: ../../vim/host/Capability.rst#perVmSwapFiles

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _environmentBrowser: ../../vim/ComputeResource.rst#environmentBrowser

.. _defaultConfigOption: ../../vim/vm/ConfigOptionDescriptor.rst#defaultConfigOption

.. _VirtualMachineConfigInfoSwapPlacementType: ../../vim/vm/ConfigInfo/SwapPlacementType.rst


vim.ComputeResource.ConfigInfo
==============================
  Configuration of the compute resource; applies to both standalone hosts and clusters.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    vmSwapPlacement (`str`_):

       Swapfile placement policy for virtual machines within this compute resource. Any policy except for "inherit" is a valid value for this property; the default is "vmDirectory". This setting will be honored for each virtual machine within the compute resource for which the following is true:
        * The virtual machine is executing on a host that has the
        * `perVmSwapFiles`_
        * capability.
        * The virtual machine configuration's
        * `swapPlacement`_
        * property is set to "inherit".See `VirtualMachineConfigInfoSwapPlacementType`_ 
    spbmEnabled (`bool`_, optional):

       Flag indicating whether or not the SPBM(Storage Policy Based Management) feature is enabled on this compute resource
    defaultHardwareVersionKey (`str`_, optional):

       Key for Default Hardware Version used on this compute resource in the format of `key`_ . This field affects `defaultConfigOption`_ returned by `environmentBrowser`_ of this object and all its children with this field unset.
