
vim.host.SystemInfo
===================
  Information about the system as a whole.
:extends: vmodl.DynamicData_

Attributes:
    vendor (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Hardware vendor identification.
    model (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       System model identification.
    uuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Hardware BIOS identification.
    otherIdentifyingInfo ([`vim.host.SystemIdentificationInfo <vim/host/SystemIdentificationInfo.rst>`_], optional):

       Other System identification information. This information may be vendor specific
