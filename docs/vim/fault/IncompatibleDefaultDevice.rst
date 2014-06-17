.. _str: https://docs.python.org/2/library/stdtypes.html

.. _defaultDevice: ../../vim/vm/ConfigOption.rst#defaultDevice

.. _videoRamSizeInKB: ../../vim/vm/device/VirtualVideoCard.rst#videoRamSizeInKB

.. _vim.fault.MigrationFault: ../../vim/fault/MigrationFault.rst


vim.fault.IncompatibleDefaultDevice
===================================
    :extends:

        `vim.fault.MigrationFault`_

  A default device (see `defaultDevice`_ for a definition) which the virtual machine is using is incompatible with the corresponding default device which will be created on the target host.This is an issue with powered-on or suspended migration under some circumstances. The problem is that in cases where the virtual machine must be recreated, it will have the default device created with default settings that are appropriate for the target host. If those are not compatible with the settings for that device that the virtual machine is currently using, then resuming the virtual machine on the target host might fail.This might happen if the device in question were reconfigured or the default is different between the source and the destination host. An example of a default device and associated setting which might cause this is `videoRamSizeInKB`_ . This is an error.

Attributes:

    device (`str`_)




