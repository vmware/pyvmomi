.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _HostVirtualNicManagerNicType: ../../../vim/host/VirtualNicManager/NicType.rst

.. _vim.host.VirtualNicConnection: ../../../vim/host/VirtualNicConnection.rst


vim.host.VirtualNicManager.NicTypeSelection
===========================================
  DataObject which lets a VirtualNic be marked for use as a `HostVirtualNicManagerNicType`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    vnic (`vim.host.VirtualNicConnection`_):

       VirtualNic for the selection is being made
    nicType ([`str`_], optional):

