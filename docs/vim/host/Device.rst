
vim.host.Device
===============
  This data object type defines a device on the host.
:extends: vmodl.DynamicData_

Attributes:
    deviceName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the device on the host. For example, /dev/cdrom or \\serverX\device_name.
    deviceType (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Device type when available: floppy, mouse, cdrom, disk, scsi device, or adapter.
