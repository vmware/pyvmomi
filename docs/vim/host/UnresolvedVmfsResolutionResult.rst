.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.VmfsVolume: ../../vim/host/VmfsVolume.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst

.. _vim.host.UnresolvedVmfsResolutionSpec: ../../vim/host/UnresolvedVmfsResolutionSpec.rst


vim.host.UnresolvedVmfsResolutionResult
=======================================
  When an UnresolvedVmfsVolume has been resignatured or forceMounted, we want to return the original spec information along with newly created VMFS volume.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    spec (`vim.host.UnresolvedVmfsResolutionSpec`_):

       The original UnresolvedVmfsResolutionSpec which user had specified
    vmfs (`vim.host.VmfsVolume`_, optional):

       Newly created VmfsVolume
    fault (`vmodl.LocalizedMethodFault`_, optional):

       'fault' would be set if the operation was not successful
