
vim.ComputeResource.ConfigSpec
==============================
  Changes to apply to the compute resource configuration.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    vmSwapPlacement (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       New setting for the swapfile placement policy. Any change to this policy will affect virtual machines that subsequently power on or resume from a suspended state in this compute resource, or that migrate to a host in this compute resource while powered on; virtual machines that are currently powered on in this compute resource will not yet be affected.See `VirtualMachineConfigInfoSwapPlacementType <vim/vm/ConfigInfo/SwapPlacementType.rst>`_ 
    spbmEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag indicating whether or not the SPBM(Storage Policy Based Management) feature is enabled on this compute resource
    defaultHardwareVersionKey (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Key for Default Hardware Version to be used on this compute resource in the format of `key <vim/vm/ConfigOptionDescriptor.rst#key>`_ . Setting this field affects `defaultConfigOption <vim/vm/ConfigOptionDescriptor.rst#defaultConfigOption>`_ returned by `environmentBrowser <vim/ComputeResource.rst#environmentBrowser>`_ of this object and all its children with this field unset.
