.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _green: ../../../vim/ManagedEntity/Status.rst#green

.. _vSphere API 4.1: ../../../vim/version.rst#vimversionversion6

.. _ManagedEntityStatus: ../../../vim/ManagedEntity/Status.rst

.. _vmDirectPathGen2Active: ../../../vim/vm/DeviceRuntimeInfo/VirtualEthernetCardRuntimeState.rst#vmDirectPathGen2Active

.. _vmDirectPathGen2Supported: ../../../vim/host/Capability.rst#vmDirectPathGen2Supported

.. _vmDirectPathGen2InactiveReasonVm: ../../../vim/vm/DeviceRuntimeInfo/VirtualEthernetCardRuntimeState.rst#vmDirectPathGen2InactiveReasonVm

.. _vmDirectPathGen2InactiveReasonOther: ../../../vim/vm/DeviceRuntimeInfo/VirtualEthernetCardRuntimeState.rst#vmDirectPathGen2InactiveReasonOther

.. _vmDirectPathGen2InactiveReasonExtended: ../../../vim/vm/DeviceRuntimeInfo/VirtualEthernetCardRuntimeState.rst#vmDirectPathGen2InactiveReasonExtended

.. _vim.vm.DeviceRuntimeInfo.DeviceRuntimeState: ../../../vim/vm/DeviceRuntimeInfo/DeviceRuntimeState.rst


vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState
========================================================
  Runtime state of a virtual ethernet card device.
:extends: vim.vm.DeviceRuntimeInfo.DeviceRuntimeState_
:since: `vSphere API 4.1`_

Attributes:
    vmDirectPathGen2Active (`bool`_):

       Flag to indicate whether VMDirectPath Gen 2 is active on this device. If false, the reason(s) for inactivity will be provided in one or more of `vmDirectPathGen2InactiveReasonVm`_ , `vmDirectPathGen2InactiveReasonOther`_ , and `vmDirectPathGen2InactiveReasonExtended`_ .
    vmDirectPathGen2InactiveReasonVm ([`str`_], optional):

       If `vmDirectPathGen2Active`_ is false, this array will be populated with reasons for the inactivity that are related to virtual machine state or configuration (chosen from VmDirectPathGen2InactiveReasonVm). Other reasons for inactivity will be provided in `vmDirectPathGen2InactiveReasonOther`_ . If there is a reason for inactivity that cannot be described by the available constants, `vmDirectPathGen2InactiveReasonExtended`_ will be populated with an additional explanation provided by the platform.Note that this list of reasons is not guaranteed to be exhaustive.
    vmDirectPathGen2InactiveReasonOther ([`str`_], optional):

       If `vmDirectPathGen2Active`_ is false, this array will be populated with reasons for the inactivity that are not related to virtual machine state or configuration (chosen from VmDirectPathGen2InactiveReasonOther). Virtual machine related reasons for inactivity will be provided in `vmDirectPathGen2InactiveReasonVm`_ . If there is a reason for inactivity that cannot be described by the available constants, `vmDirectPathGen2InactiveReasonExtended`_ will be populated with an additional explanation provided by the platform.Note that this list of reasons is not guaranteed to be exhaustive.See `vmDirectPathGen2Supported`_ 
    vmDirectPathGen2InactiveReasonExtended (`str`_, optional):

       If `vmDirectPathGen2Active`_ is false, this property may contain an explanation provided by the platform, beyond the reasons (if any) enumerated in `vmDirectPathGen2InactiveReasonVm`_ and/or `vmDirectPathGen2InactiveReasonOther`_ .
    reservationStatus (`str`_, optional):

       The status indicating whether network reservation requirement is violated or not on the virtual network adapter. See `ManagedEntityStatus`_ for possible values. `red`_ indicates that reservation specified on the virtual network adapter is not being fulfilled. This can happen if the reservation requested is greater than the available capacity reserved for virtual machine traffic on the host. `green`_ indicates that the reservation specified on the virtual network adapter is being fulfilled.
