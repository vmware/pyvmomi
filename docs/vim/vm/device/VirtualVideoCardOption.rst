
vim.vm.device.VirtualVideoCardOption
====================================
  This data object type contains the options for the `VirtualVideoCard <vim/vm/device/VirtualVideoCard.rst>`_ data object type.
:extends: vim.vm.device.VirtualDeviceOption_

Attributes:
    videoRamSizeInKB (`vim.option.LongOption <vim/option/LongOption.rst>`_, optional):

       Minimum, maximum and default size of the video frame buffer.
    numDisplays (`vim.option.IntOption <vim/option/IntOption.rst>`_, optional):

       Minimum, maximum and default value for the number of displays.
    useAutoDetect (`vim.option.BoolOption <vim/option/BoolOption.rst>`_, optional):

       Flag to indicate whether the display settings of the host should be used to automatically determine the display settings of the virtual machine's video card.
    support3D (`vim.option.BoolOption <vim/option/BoolOption.rst>`_, optional):

       Flag to indicate whether the virtual video card supports 3D functions.
    use3dRendererSupported (`vim.option.BoolOption <vim/option/BoolOption.rst>`_, optional):

       Flag to indicate whether the virtual video card can specify how to render 3D graphics.
