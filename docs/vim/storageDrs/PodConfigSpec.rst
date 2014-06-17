.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _ioLoadBalanceEnabled: ../../vim/storageDrs/PodConfigInfo.rst#ioLoadBalanceEnabled

.. _vim.cluster.RuleSpec: ../../vim/cluster/RuleSpec.rst

.. _StorageDrsVmConfigInfo: ../../vim/storageDrs/VmConfigInfo.rst

.. _StorageDrsPodConfigSpec: ../../vim/storageDrs/PodConfigSpec.rst

.. _vim.storageDrs.OptionSpec: ../../vim/storageDrs/OptionSpec.rst

.. _StorageDrsPodConfigInfoBehavior: ../../vim/storageDrs/PodConfigInfo/Behavior.rst

.. _vim.storageDrs.IoLoadBalanceConfig: ../../vim/storageDrs/IoLoadBalanceConfig.rst

.. _vim.storageDrs.SpaceLoadBalanceConfig: ../../vim/storageDrs/SpaceLoadBalanceConfig.rst


vim.storageDrs.PodConfigSpec
============================
  The `StorageDrsPodConfigSpec`_ data object provides a set of update specifications for pod-wide storage DRS configuration. To support incremental changes, these properties are all optional.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    enabled (`bool`_, optional):

       Flag indicating whether or not storage DRS is enabled.
    ioLoadBalanceEnabled (`bool`_, optional):

       Flag indicating whether or not storage DRS takes into account storage I/O workload when making load balancing and initial placement recommendations.
    defaultVmBehavior (`str`_, optional):

       Specifies the pod-wide default storage DRS behavior for virtual machines. For currently supported storage DRS behavior, see `StorageDrsPodConfigInfoBehavior`_ . You can override the default behavior for a virtual machine by using the `StorageDrsVmConfigInfo`_ object.
    loadBalanceInterval (`int`_, optional):

       Specify the interval that storage DRS runs to load balance among datastores within a storage pod.
    defaultIntraVmAffinity (`bool`_, optional):

       Specifies whether or not each virtual machine in this pod should have its virtual disks on the same datastore by default.
    spaceLoadBalanceConfig (`vim.storageDrs.SpaceLoadBalanceConfig`_, optional):

       The configuration settings for load balancing storage space.
    ioLoadBalanceConfig (`vim.storageDrs.IoLoadBalanceConfig`_, optional):

       The configuration settings for load balancing I/O workload. This takes effect only if `ioLoadBalanceEnabled`_ istrue.
    rule (`vim.cluster.RuleSpec`_, optional):

       Changes to the set of rules.
    option (`vim.storageDrs.OptionSpec`_, optional):

       Changes to advance settings.
