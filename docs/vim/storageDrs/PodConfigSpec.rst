
vim.storageDrs.PodConfigSpec
============================
  The `StorageDrsPodConfigSpec <vim/storageDrs/PodConfigSpec.rst>`_ data object provides a set of update specifications for pod-wide storage DRS configuration. To support incremental changes, these properties are all optional.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag indicating whether or not storage DRS is enabled.
    ioLoadBalanceEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag indicating whether or not storage DRS takes into account storage I/O workload when making load balancing and initial placement recommendations.
    defaultVmBehavior (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Specifies the pod-wide default storage DRS behavior for virtual machines. For currently supported storage DRS behavior, see `StorageDrsPodConfigInfoBehavior <vim/storageDrs/PodConfigInfo/Behavior.rst>`_ . You can override the default behavior for a virtual machine by using the `StorageDrsVmConfigInfo <vim/storageDrs/VmConfigInfo.rst>`_ object.
    loadBalanceInterval (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Specify the interval that storage DRS runs to load balance among datastores within a storage pod.
    defaultIntraVmAffinity (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Specifies whether or not each virtual machine in this pod should have its virtual disks on the same datastore by default.
    spaceLoadBalanceConfig (`vim.storageDrs.SpaceLoadBalanceConfig <vim/storageDrs/SpaceLoadBalanceConfig.rst>`_, optional):

       The configuration settings for load balancing storage space.
    ioLoadBalanceConfig (`vim.storageDrs.IoLoadBalanceConfig <vim/storageDrs/IoLoadBalanceConfig.rst>`_, optional):

       The configuration settings for load balancing I/O workload. This takes effect only if `ioLoadBalanceEnabled <vim/storageDrs/PodConfigInfo.rst#ioLoadBalanceEnabled>`_ istrue.
    rule ([`vim.cluster.RuleSpec <vim/cluster/RuleSpec.rst>`_], optional):

       Changes to the set of rules.
    option ([`vim.storageDrs.OptionSpec <vim/storageDrs/OptionSpec.rst>`_], optional):

       Changes to advance settings.
