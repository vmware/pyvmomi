
vim.ResourceAllocationInfo
==========================
  The ResourceAllocationInfo data object specifies the reserved resource requirement as well as the limit (maximum allowed usage) for a given kind of resource. This is specified for both memory allocation (specified in MB) and CPU allocation (specified in MHz).For a `ResourcePool <vim/ResourcePool.rst>`_ , the ResourceAllocationInfo object describes both the guaranteed amount of the resource ( `reservation <vim/ResourceAllocationInfo.rst#reservation>`_ ) and whether or not it is expandable ( `expandableReservation <vim/ResourceAllocationInfo.rst#expandableReservation>`_ ). If expandableReservation is true, then the resource pool can grow its reservation dynamically by borrowing unreserved resources from its parent resource pool. For the methods `CreateResourcePool <vim/ResourcePool.rst#createResourcePool>`_ , `CreateVApp <vim/ResourcePool.rst#createVApp>`_ and `ImportVApp <vim/ResourcePool.rst#importVApp>`_ , you must provide values for all properties except overheadLimit; they are not optional. (Currently, overheadLimit is for vCenter Server use only.)If the limit is configured, it must be greater than or equal to the reservation.
:extends: vmodl.DynamicData_

Attributes:
    reservation (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Amount of resource that is guaranteed available to the virtual machine or resource pool. Reserved resources are not wasted if they are not used. If the utilization is less than the reservation, the resources can be utilized by other running virtual machines. Units are MB for memory, MHz for CPU.
    expandableReservation (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       In a resource pool with an expandable reservation, the reservation on a resource pool can grow beyond the specified value, if the parent resource pool has unreserved resources. A non-expandable reservation is called a fixed reservation. This property is ignored for virtual machines.
    limit (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The utilization of a virtual machine/resource pool will not exceed this limit, even if there are available resources. This is typically used to ensure a consistent performance of virtual machines / resource pools independent of available resources. If set to -1, then there is no fixed limit on resource usage (only bounded by available resources and shares). Units are MB for memory, MHz for CPU.
    shares (`vim.SharesInfo <vim/SharesInfo.rst>`_, optional):

       Memory shares are used in case of resource contention.
    overheadLimit (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The maximum allowed overhead memory. For a powered on virtual machine, the overhead memory reservation cannot be larger than its overheadLimit. This property is only applicable to powered on virtual machines and is not persisted across reboots. This property is not applicable for resource pools. If set to -1, then there is no limit on reservation. Units are MB.Note: For vCenter Server use only. Not available for other clients at this time. The server will throw an exception if you attempt to set this property.
