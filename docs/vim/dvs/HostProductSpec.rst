.. _str: https://docs.python.org/2/library/stdtypes.html

.. _AboutInfo: ../../vim/AboutInfo.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.dvs.HostProductSpec
=======================
  This data object type is a subset of `AboutInfo`_ . An object of this type can be used to describe the specification for a host.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    productLineId (`str`_, optional):

       The product-line name.
    version (`str`_, optional):

       Dot-separated version string. For example, "1.2".
