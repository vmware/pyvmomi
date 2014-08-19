
vim.ComputeResource.ConfigInfo
==============================
  Configuration of the compute resource; applies to both standalone hosts and clusters.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    vmSwapPlacement (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Swapfile placement policy for virtual machines within this compute resource. Any policy except for "inherit" is a valid value for this property; the default is "vmDirectory". This setting will be honored for each virtual machine within the compute resource for which the following is true:
        * The virtual machine is executing on a host that has the
        * `perVmSwapFiles <vim/host/Capability.rst#perVmSwapFiles>`_
        * capability.
        * The virtual machine configuration's
        * `swapPlacement <vim/vm/ConfigInfo.rst#swapPlacement>`_
        * property is set to "inherit".See `VirtualMachineConfigInfoSwapPlacementType <vim/vm/ConfigInfo/SwapPlacementType.rst>`_ 
    spbmEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag indicating whether or not the SPBM(Storage Policy Based Management) feature is enabled on this compute resource
    defaultHardwareVersionKey (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Key for Default Hardware Version used on this compute resource in the format of `key <vim/vm/ConfigOptionDescriptor.rst#key>`_ . This field affects `defaultConfigOption <vim/vm/ConfigOptionDescriptor.rst#defaultConfigOption>`_ returned by `environmentBrowser <vim/ComputeResource.rst#environmentBrowser>`_ of this object and all its children with this field unset.
