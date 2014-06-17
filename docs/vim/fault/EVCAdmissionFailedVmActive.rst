.. _maxEVCModeKey: ../../vim/host/Summary.rst#maxEVCModeKey

.. _vim.fault.EVCAdmissionFailed: ../../vim/fault/EVCAdmissionFailed.rst


vim.fault.EVCAdmissionFailedVmActive
====================================
    :extends:

        `vim.fault.EVCAdmissionFailed`_

  An attempt to move or add a host into an Enhanced VMotion Compatibility cluster has failed for the following reason:
   * The host exposes additional compatibility-relevant CPU features beyond those present in the baseline mandated by the cluster's EVC mode.
   * The host has powered-on or suspended virtual machines.
   * Therefore the host may not be admitted into the cluster, since its virtual machines may be using CPU features suppressed in the cluster.
   * Note that in rare cases, this may occur even if the host's
   * `maxEVCModeKey`_
   * corresponds to the EVC mode of the cluster. This means that even though that EVC mode is the best match for the host's hardware, the host still has some features beyond those present in the baseline for that EVC mode.

Attributes:




