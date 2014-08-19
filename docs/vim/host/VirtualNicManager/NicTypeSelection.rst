
vim.host.VirtualNicManager.NicTypeSelection
===========================================
  DataObject which lets a VirtualNic be marked for use as a `HostVirtualNicManagerNicType <vim/host/VirtualNicManager/NicType.rst>`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    vnic (`vim.host.VirtualNicConnection <vim/host/VirtualNicConnection.rst>`_):

       VirtualNic for the selection is being made
    nicType ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

