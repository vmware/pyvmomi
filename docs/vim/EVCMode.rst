.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _track: ../vim/EVCMode.rst#track

.. _label: ../vim/Description.rst#label

.. _summary: ../vim/Description.rst#summary

.. _EVCMode: ../vim/EVCMode.rst

.. _vendorTier: ../vim/EVCMode.rst#vendorTier

.. _maxEVCModeKey: ../vim/host/Summary.rst#maxEVCModeKey

.. _vSphere API 4.0: ../vim/version.rst#vimversionversion5

.. _HostListSummary: ../vim/host/Summary.rst

.. _currentEVCModeKey: ../vim/host/Summary.rst#currentEVCModeKey

.. _vim.host.CpuIdInfo: ../vim/host/CpuIdInfo.rst

.. _vim.host.FeatureMask: ../vim/host/FeatureMask.rst

.. _guaranteedCPUFeatures: ../vim/EVCMode.rst#guaranteedCPUFeatures

.. _minRequiredEVCModeKey: ../vim/vm/RuntimeInfo.rst#minRequiredEVCModeKey

.. _vim.ElementDescription: ../vim/ElementDescription.rst

.. _vim.vm.FeatureRequirement: ../vim/vm/FeatureRequirement.rst

.. _VirtualMachineRuntimeInfo: ../vim/vm/RuntimeInfo.rst

.. _vim.host.FeatureCapability: ../vim/host/FeatureCapability.rst

.. _ClusterComputeResourceSummary: ../vim/ClusterComputeResource/Summary.rst


vim.EVCMode
===========
  The `EVCMode`_ data object describes an Enhanced vMotion Compatibility mode. An EVC mode is associated with a set of CPU features. A vCenter Server defines the available EVC modes. You use them to establish a common set of features for compatibility between hosts in a cluster. An EVC-enabled cluster supports safe vMotion of virtual machines across a range of CPU generations. You must use the vSphere Client to configure EVC.When you add a host to an EVC-enabled cluster, the vCenter Server determines the CPU compatibility to preserve vMotion compatibility within the cluster. If the host CPU is compatible with those already in the cluster, the Server adds the host to the cluster and configures it for compatible operation. Hosts that are not compatible are not allowed to join the cluster.The inherited `key`_ property is a string value that uniquely identifies an EVC mode. The vCenter Server assigns the key value; the vSphere API uses the key to identify modes in summary and information objects:
   * `ClusterComputeResourceSummary`_
   * .
   * `currentEVCModeKey`_
   * `HostListSummary`_
   * .
   * `currentEVCModeKey`_
   * `HostListSummary`_
   * .
   * `maxEVCModeKey`_
   * `VirtualMachineRuntimeInfo`_
   * .
   * `minRequiredEVCModeKey`_The inherited `label`_ and `summary`_ properties are human-readable strings.You can use the `track`_ and `vendorTier`_ properties to determine feature-superset relationships between modes without examining the individual feature bits in `guaranteedCPUFeatures`_ . The CPU feature baseline of mode A is a superset of mode B's baseline if and only if:
   * modeA.track is the same as or a superset of modeB.track
   * modeA.vendorTier is equal to or greater than modeB.vendorTierUse the `track`_ and `vendorTier`_ properties only for the purpose of feature-superset calculations as described above. Do not use them to infer the presence or absence of specific features. The property values for a given mode may change across releases as the set of available EVC modes changes, to better represent mode relationships.
:extends: vim.ElementDescription_
:since: `vSphere API 4.0`_

Attributes:
    guaranteedCPUFeatures (`vim.host.CpuIdInfo`_, optional):

       Describes the CPU feature baseline associated with the EVC mode. On the cluster where a particular EVC mode is configured, those CPU features are guaranteed, either because the host hardware naturally matches those features or because CPU feature override is used to mask out differences and enforce a match.
    featureCapability (`vim.host.FeatureCapability`_, optional):

       Describes the feature capability baseline associated with the EVC mode. On the cluster where a particular EVC mode is configured, these features capabilities are guaranteed, either because the host hardware naturally matches those features or because feature masks are used to mask out differences and enforce a match.
    featureMask (`vim.host.FeatureMask`_, optional):

       The masks (modifications to a host's feature capabilities) that limit a host's capabilities to that of the EVC mode baseline.
    featureRequirement (`vim.vm.FeatureRequirement`_, optional):

       The conditions that must be true of a host's feature capabilities in order for the host to meet the minimum requirements of the EVC mode baseline.
    vendor (`str`_):

       CPU hardware vendor required for this mode.
    track (`str`_):

       Identifiers for feature groups that are at least partially present in the `guaranteedCPUFeatures`_ array for this mode. Use this property to compare track values from two modes. Do not use this property to determine the presence or absence of specific features.
    vendorTier (`int`_):

       Index for ordering the set of modes that apply to a given CPU vendor. Use this property to compare vendor tier values from two modes. Do not use this property to determine the presence or absence of specific features.
