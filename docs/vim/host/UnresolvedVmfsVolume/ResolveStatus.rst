
vim.host.UnresolvedVmfsVolume.ResolveStatus
===========================================
  Data object that describes the resolvability of a volume.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    resolvable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Can this volume be resolved? There may be other reasons a volume cannot be resolved other than the fact that it is incomplete. This boolean will authoritatively indicate if the server can resolve this volume.
    incompleteExtents (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Is the list of extents for the volume a partial list? A volume can only be resignatured if all extents composing that volume are available. Hence, a volume with a partial extent list cannot be resignatured.In cases where this information is not known for a volume, this property will be unset.
    multipleCopies (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Are there multiple copies of extents for this volume? If any extent of the volume has multiple copies then the extents to be resolved must be explicitly specified when resolving this volume.In cases where this information is not known for a volume, this property will be unset.
