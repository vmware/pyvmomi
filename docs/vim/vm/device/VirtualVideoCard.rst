
vim.vm.device.VirtualVideoCard
==============================
  The VirtualVideoCard data object type represents a video card in a virtual machine.
:extends: vim.vm.device.VirtualDevice_

Attributes:
    videoRamSizeInKB (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The size of the framebuffer for a virtual machine.
    numDisplays (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates the number of supported monitors. The number of displays X the maximum resolution of each display is bounded by the video RAM size of the virtual video card. This property can only be updated when the virtual machine is powered off.
    useAutoDetect (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate whether the display settings of the host on which the virtual machine is running should be used to automatically determine the display settings of the virtual machine's video card. This setting takes effect at virtual machine power-on time. If this value is set to TRUE, numDisplays will be ignored.
    enable3DSupport (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate whether the virtual video card supports 3D functions. This property can only be updated when the virtual machine is powered off.
    use3dRenderer (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicate how the virtual video device renders 3D graphics.The virtual video device can use hardware acceleration and software rendering. By default, VMware products determine whether or not to use hardware acceleration based on the availability of physical graphics devices. Certain workloads can benefit from explicitly specifying if hardware acceleration is required. For example, 3D intensive workloads may indicate to run on systems with graphics hardware.There are three settings.(automatic) - The virtual device chooses how to render 3D graphics (default). (software) - The virtual device will use software rendering and will not attempt to use hardware acceleration. (hardware) - The virtual device will use hardware acceleration and will not activate without it.
