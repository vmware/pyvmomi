.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.SystemIdentificationInfo: ../../vim/host/SystemIdentificationInfo.rst


vim.host.SystemInfo
===================
  Information about the system as a whole.
:extends: vmodl.DynamicData_

Attributes:
    vendor (`str`_):

       Hardware vendor identification.
    model (`str`_):

       System model identification.
    uuid (`str`_):

       Hardware BIOS identification.
    otherIdentifyingInfo (`vim.host.SystemIdentificationInfo`_, optional):

       Other System identification information. This information may be vendor specific
