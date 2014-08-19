
vim.host.GraphicsInfo
=====================
  This data object type describes information about a single graphics device.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    deviceName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The device name.
    vendorName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The vendor name.
    pciId (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       PCI ID of this device composed of "bus:slot.function".
    graphicsType (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Graphics type (@see GraphicsType).
    memorySizeInKB (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Memory capacity of graphics device or zero if not available.
    vm ([`vim.VirtualMachine <vim/VirtualMachine.rst>`_], optional):

       Virtual machines using this graphics device.
