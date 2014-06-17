.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _HostConfigChangeOperation: ../../../vim/host/ConfigChange/Operation.rst

.. _vim.host.VirtualSwitch.Specification: ../../../vim/host/VirtualSwitch/Specification.rst


vim.host.VirtualSwitch.Config
=============================
  This data object type describes the VirtualSwitch configuration containing both the configurable properties on a VirtualSwitch and identification information.
:extends: vmodl.DynamicData_

Attributes:
    changeOperation (`str`_, optional):

       This property indicates the change operation to apply on this configuration specification.See `HostConfigChangeOperation`_ 
    name (`str`_):

       The name of the virtual switch. Maximum length is 32 characters.
    spec (`vim.host.VirtualSwitch.Specification`_, optional):

       The specification of the VirtualSwitch.
