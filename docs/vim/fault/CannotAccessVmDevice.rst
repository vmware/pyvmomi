.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.CannotAccessVmComponent: ../../vim/fault/CannotAccessVmComponent.rst


vim.fault.CannotAccessVmDevice
==============================
    :extends:

        `vim.fault.CannotAccessVmComponent`_

  One of the virtual machine's devices uses a backing that is not accessible on the host.Following is a discussion of this fault's use in migration validation.This is an error if the device is currently connected and a warning otherwise. Devices that can be disconnected can only be connected if the virtual machine is powered on.The usage of this fault is slightly different if the backing of a device is inherently host-local, and therefore not shared or globally named among hosts. (Examples of such backings: physical CD-ROM drive, physical serial port.) If a device with such a backing is currently connected, that will be a migration error. If the device is disconnected, there will be a warning if no backing with the same name exists on the destination host. If the device is disconnected and a backing with the same name exists on the destination host, this is neither a warning nor an error case, even though the destination host's backing is not the same instance as the source host's. It is assumed that use of the host-local backing is what is desired for the device.

Attributes:

    device (`str`_)

    backing (`str`_)

    connected (`bool`_)




