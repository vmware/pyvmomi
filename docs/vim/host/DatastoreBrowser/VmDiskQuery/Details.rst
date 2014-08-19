
vim.host.DatastoreBrowser.VmDiskQuery.Details
=============================================
  Details for the virtual disk primary file.
:extends: vmodl.DynamicData_

Attributes:
    diskType (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The flag to indicate whether the type of the physical disk backing the virtual disk is returned.
    capacityKb (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The flag to indicate whether the capacity of the virtual disk from the point of view of a virtual machine is returned.
    hardwareVersion (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The flag to indicate whether the hardware version of the virtual disk file is returned.
    controllerType (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The flag to indicate whether or not the controller type of the virtual disk file is returned.
    diskExtents (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The flag to indicate whether or not the disk extents of the virtual disk are returned.
    thin (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The flag to indicate whether the thin-ness of the disk is returned.
