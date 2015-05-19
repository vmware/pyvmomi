.. _int: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _level: ../../vim/SharesInfo.rst#level

.. _shares: ../../vim/SharesInfo.rst#shares

.. _vim.SharesInfo: ../../vim/SharesInfo.rst

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.StorageResourceManager.IOAllocationInfo
===========================================
  The IOAllocationInfo specifies the shares, limit and reservation for storage I/O resource.The storage I/O resource is allocated to virtual machines based on their shares, limit and reservation. The reservation is currently exposed only at the host level for local datastores. And we do not support storage I/O resource management on resource pools.Each virtual machine has one IOAllocationInfo object per virtual disk. For example, we can specify that a virtual machine has 500 shares on the first virtual disk, 1000 shares on the second virtual disk, etc.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    limit (`long`_, optional):

       The utilization of a virtual machine will not exceed this limit, even if there are available resources. This is typically used to ensure a consistent performance of virtual machines independent of available resources. If set to -1, then there is no fixed limit on resource usage (only bounded by available resources and shares). The unit is number of I/O per second. While setting the limit for storage I/O resource, if the property is unset, it is treated as no change and the property is not updated. While reading back the limit information of storage I/O resource, if the property is unset, a default value of -1 will be returned, which indicates that there is no limit on resource usage.
    shares (`vim.SharesInfo`_, optional):

       Shares are used in case of resource contention. The value should be within a range of 200 to 4000. While setting shares for storage I/O resource, if the property is unset, it is treated as no change and the property is not updated. While reading back the shares information of storage I/O resource, if the property is unset, a default value of `level`_ = normal, `shares`_ = 1000 will be returned.
    reservation (`int`_, optional):

       Reservation control is used to provide guaranteed allocation in terms of IOPS. Large IO sizes are considered as multiple IOs using a chunk size of 32 KB as default. This control is initially supported only at host level for local datastores. It future, it may get supported on shared storage based on integration with Storage IO Control. Also right now we don't do any admission control based on IO reservation values.
