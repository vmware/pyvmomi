
vim.OvfManager.ValidateHostResult
=================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    downloadSize (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The total amount of data that must be transferred to download the entity.This may be inaccurate due to disk compression etc.
    flatDeploymentSize (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The total amount of space required to deploy the entity if using flat disks.
    sparseDeploymentSize (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The total amount of space required to deploy the entity using sparse disks, if known.
    error ([`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_], optional):

       Errors that happened during validation. The presence of faults in this list indicates that the validation failed.
    warning ([`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_], optional):

       Non-fatal warnings from the validation.
    supportedDiskProvisioning ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       An array of the disk provisioning type supported by the target host system.
