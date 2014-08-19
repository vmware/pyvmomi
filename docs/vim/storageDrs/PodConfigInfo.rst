
vim.storageDrs.PodConfigInfo
============================
  The `StorageDrsPodConfigInfo <vim/storageDrs/PodConfigInfo.rst>`_ data object contains pod-wide configuration information for the storage DRS service.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether or not storage DRS is enabled.
    ioLoadBalanceEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether or not storage DRS takes into account storage I/O workload when making load balancing and initial placement recommendations.
    defaultVmBehavior (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Specifies the pod-wide default storage DRS behavior for virtual machines. For currently supported storage DRS behavior, see Behavior. You can override the default behavior for a virtual machine by using the `StorageDrsVmConfigInfo <vim/storageDrs/VmConfigInfo.rst>`_ object.
    loadBalanceInterval (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Specify the interval that storage DRS runs to load balance among datastores within a storage pod.Unit: minute. The valid values are from 60 (1 hour) to 43200 (30 days). If not specified, the default value is 480 (8 hours).
    defaultIntraVmAffinity (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Specifies whether or not each virtual machine in this pod should have its virtual disks on the same datastore by default. If set to true, virtual machines will have all their virtual disks on the same datastore. If set to false, the virtual disks of a virtual machine may or may not be placed on the same datastore. If not set, the default value is true. You can override the default behavior for a virtual machine by using the `StorageDrsVmConfigInfo <vim/storageDrs/VmConfigInfo.rst>`_ object.
    spaceLoadBalanceConfig (`vim.storageDrs.SpaceLoadBalanceConfig <vim/storageDrs/SpaceLoadBalanceConfig.rst>`_, optional):

       The configuration settings for load balancing storage space.
    ioLoadBalanceConfig (`vim.storageDrs.IoLoadBalanceConfig <vim/storageDrs/IoLoadBalanceConfig.rst>`_, optional):

       The configuration settings for load balancing I/O workload. This takes effect only if `ioLoadBalanceEnabled <vim/storageDrs/PodConfigInfo.rst#ioLoadBalanceEnabled>`_ istrue.
    rule ([`vim.cluster.RuleInfo <vim/cluster/RuleInfo.rst>`_], optional):

       Pod-wide rules.
    option ([`vim.option.OptionValue <vim/option/OptionValue.rst>`_], optional):

       Advanced settings.
