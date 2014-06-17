.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.InternetScsiHba.SendTarget: ../../../vim/host/InternetScsiHba/SendTarget.rst

.. _vim.host.InternetScsiHba.StaticTarget: ../../../vim/host/InternetScsiHba/StaticTarget.rst


vim.host.InternetScsiHba.TargetSet
==================================
  A collection of one or more static targets or discovery addresses. At least one of the arrays must be non-empty.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    staticTargets (`vim.host.InternetScsiHba.StaticTarget`_, optional):

    sendTargets (`vim.host.InternetScsiHba.SendTarget`_, optional):

