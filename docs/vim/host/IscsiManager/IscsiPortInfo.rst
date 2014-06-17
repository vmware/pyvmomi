.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.VirtualNic: ../../../vim/host/VirtualNic.rst

.. _vim.host.PhysicalNic: ../../../vim/host/PhysicalNic.rst

.. _vim.host.IscsiManager.IscsiStatus: ../../../vim/host/IscsiManager/IscsiStatus.rst


vim.host.IscsiManager.IscsiPortInfo
===================================
  The IscsiPortInfo data object describes the Virtual NIC that are bound to an iSCSI adapter and also it describes the candidate Virtual NICs that can be bound to a given iSCSI adapter.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    vnicDevice (`str`_, optional):

       Virtual NIC Name. Contains the name of the Virtual NIC device. This may be unset in case where the bound Virtual NIC doesn't have the system object or where a candidate Physical NIC isn't associated with any Virtual NIC.
    vnic (`vim.host.VirtualNic`_, optional):

       Virtual NIC Object corresponding to the vnicDevice. May be unset if Virtual NIC object corresponding to vnicDevice doesn't exist in the system.
    pnicDevice (`str`_, optional):

       Physical NIC Name.
    pnic (`vim.host.PhysicalNic`_, optional):

       Physical NIC Object corresponding to the pnicDevice. May be unset if Physical NIC object corresponding to pnicDevice doesn't exist in the system or the vnicDevice doesn't have any Physical NIC associated with it.
    switchName (`str`_, optional):

       Name of the virtual switch this Physical/Virtual NIC belongs. May be unset if the vnicDevice and/or pnicDevice do not have a virtual switch associated with them.
    switchUuid (`str`_, optional):

       UUID of the virtual switch this Physical/Virtual NIC belongs. May be unset if the vnicDevice and/or pnicDevice do not have a virtual switch associated with them or the associated switch is not VDS.
    portgroupName (`str`_, optional):

       Name of the portgroup to which this Virtual NIC belongs. May be unset if the vnicDevice and/or pnicDevice do not have a Portgroup associated with them.
    portgroupKey (`str`_, optional):

       Portgroup key to which this Virtual NIC belongs. May be unset if the vnicDevice and/or pnicDevice do not have a Portgroup associated with them or the associated portgroup does is not of VDS type.
    portKey (`str`_, optional):

       portkey to which this Virtual NIC belongs. May be unset if the vnicDevice is not assigned to a specific port or the switch is not VDS.
    complianceStatus (`vim.host.IscsiManager.IscsiStatus`_, optional):

       Status indicating whether the Virtual NIC is compliant with the network policy that is required by iSCSI port binding. May be unset in the candidate NIC list.
    pathStatus (`str`_, optional):

       A status, as defined in PathStatus, indicating the existing storage paths dependency level on a given Virtual NIC. May be unset in the candidate NIC list.
