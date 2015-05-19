.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst


vim.OvfManager.ValidateHostResult
=================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    downloadSize (`long`_, optional):

       The total amount of data that must be transferred to download the entity.This may be inaccurate due to disk compression etc.
    flatDeploymentSize (`long`_, optional):

       The total amount of space required to deploy the entity if using flat disks.
    sparseDeploymentSize (`long`_, optional):

       The total amount of space required to deploy the entity using sparse disks, if known.
    error ([`vmodl.LocalizedMethodFault`_], optional):

       Errors that happened during validation. The presence of faults in this list indicates that the validation failed.
    warning ([`vmodl.LocalizedMethodFault`_], optional):

       Non-fatal warnings from the validation.
    supportedDiskProvisioning ([`str`_], optional):

       An array of the disk provisioning type supported by the target host system.
