vim.host.UnresolvedVmfsResolutionSpec.VmfsUuidResolution
========================================================
  :contained by: `vim.host.UnresolvedVmfsResolutionSpec <vim/host/UnresolvedVmfsResolutionSpec.rst>`_

  :type: `vim.host.UnresolvedVmfsResolutionSpec.VmfsUuidResolution <vim/host/UnresolvedVmfsResolutionSpec/VmfsUuidResolution.rst>`_

  :name: forceMount

values:
--------

resignature
   Resignature the Unresolved VMFS volume.In the event the volume to be resignatured contains multiple extents but only a single copy of each extent exists, only the head extent needs to be specified.

forceMount
   Keep the original Uuid of the VMFS volume and mount itIn the event the volume to be force mounted contains multiple extents but only a single copy of each extent exists, only the head extent needs to be specified.
