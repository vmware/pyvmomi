.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst


vim.OvfManager.CreateDescriptorResult
=====================================
  The result of creating the OVF descriptor for the entity.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    ovfDescriptor (`str`_):

       The OVF descriptor for the entity.
    error ([`vmodl.LocalizedMethodFault`_], optional):

       Errors that happened during processing.For example, unknown or unsupported devices could be found (in which case this array will contain one or more instances of Unsupported-/UnknownDevice).
    warning ([`vmodl.LocalizedMethodFault`_], optional):

       Non-fatal warnings from the processing.The result will be valid, but the user may choose to reject it based on these warnings.
    includeImageFiles (`bool`_, optional):

       Returns true if there are ISO or Floppy images attached to one or more VMs.
