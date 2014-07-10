.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vim.cluster.RuleInfo: ../../vim/cluster/RuleInfo.rst


vim.storageDrs.VirtualDiskAntiAffinityRuleSpec
==============================================
  Pod-wide anit-affinity rule for virtual disks. The set of virtual disks should be placed on different datastores.
:extends: vim.cluster.RuleInfo_
:since: `vSphere API 5.0`_

Attributes:
    diskId (`int`_):

       The list of virtual disks.
