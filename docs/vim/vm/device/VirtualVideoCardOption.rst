.. _VirtualVideoCard: ../../../vim/vm/device/VirtualVideoCard.rst

.. _vim.option.IntOption: ../../../vim/option/IntOption.rst

.. _vim.option.BoolOption: ../../../vim/option/BoolOption.rst

.. _vim.option.LongOption: ../../../vim/option/LongOption.rst

.. _vim.vm.device.VirtualDeviceOption: ../../../vim/vm/device/VirtualDeviceOption.rst


vim.vm.device.VirtualVideoCardOption
====================================
  This data object type contains the options for the `VirtualVideoCard`_ data object type.
:extends: vim.vm.device.VirtualDeviceOption_

Attributes:
    videoRamSizeInKB (`vim.option.LongOption`_, optional):

       Minimum, maximum and default size of the video frame buffer.
    numDisplays (`vim.option.IntOption`_, optional):

       Minimum, maximum and default value for the number of displays.
    useAutoDetect (`vim.option.BoolOption`_, optional):

       Flag to indicate whether the display settings of the host should be used to automatically determine the display settings of the virtual machine's video card.
    support3D (`vim.option.BoolOption`_, optional):

       Flag to indicate whether the virtual video card supports 3D functions.
    use3dRendererSupported (`vim.option.BoolOption`_, optional):

       Flag to indicate whether the virtual video card can specify how to render 3D graphics.
