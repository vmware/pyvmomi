.. _long: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _CreateVApp: ../vim/ResourcePool.rst#createVApp

.. _ImportVApp: ../vim/ResourcePool.rst#importVApp

.. _reservation: ../vim/ResourceAllocationInfo.rst#reservation

.. _ResourcePool: ../vim/ResourcePool.rst

.. _vim.SharesInfo: ../vim/SharesInfo.rst

.. _vmodl.DynamicData: ../vmodl/DynamicData.rst

.. _CreateResourcePool: ../vim/ResourcePool.rst#createResourcePool

.. _expandableReservation: ../vim/ResourceAllocationInfo.rst#expandableReservation


vim.ResourceAllocationInfo
==========================
  The ResourceAllocationInfo data object specifies the reserved resource requirement as well as the limit (maximum allowed usage) for a given kind of resource. This is specified for both memory allocation (specified in MB) and CPU allocation (specified in MHz).For a `ResourcePool`_ , the ResourceAllocationInfo object describes both the guaranteed amount of the resource ( `reservation`_ ) and whether or not it is expandable ( `expandableReservation`_ ). If expandableReservation is true, then the resource pool can grow its reservation dynamically by borrowing unreserved resources from its parent resource pool. For the methods `CreateResourcePool`_ , `CreateVApp`_ and `ImportVApp`_ , you must provide values for all properties except overheadLimit; they are not optional. (Currently, overheadLimit is for vCenter Server use only.)If the limit is configured, it must be greater than or equal to the reservation.
:extends: vmodl.DynamicData_

Attributes:
    reservation (`long`_, optional):

       Amount of resource that is guaranteed available to the virtual machine or resource pool. Reserved resources are not wasted if they are not used. If the utilization is less than the reservation, the resources can be utilized by other running virtual machines. Units are MB for memory, MHz for CPU.
    expandableReservation (`bool`_, optional):

       In a resource pool with an expandable reservation, the reservation on a resource pool can grow beyond the specified value, if the parent resource pool has unreserved resources. A non-expandable reservation is called a fixed reservation. This property is ignored for virtual machines.
    limit (`long`_, optional):

       The utilization of a virtual machine/resource pool will not exceed this limit, even if there are available resources. This is typically used to ensure a consistent performance of virtual machines / resource pools independent of available resources. If set to -1, then there is no fixed limit on resource usage (only bounded by available resources and shares). Units are MB for memory, MHz for CPU.
    shares (`vim.SharesInfo`_, optional):

       Memory shares are used in case of resource contention.
    overheadLimit (`long`_, optional):

       The maximum allowed overhead memory. For a powered on virtual machine, the overhead memory reservation cannot be larger than its overheadLimit. This property is only applicable to powered on virtual machines and is not persisted across reboots. This property is not applicable for resource pools. If set to -1, then there is no limit on reservation. Units are MB.Note: For vCenter Server use only. Not available for other clients at this time. The server will throw an exception if you attempt to set this property.
