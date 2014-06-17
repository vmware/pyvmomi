.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.PatchManager.Status: ../../../vim/host/PatchManager/Status.rst


vim.host.PatchManager.Result
============================
  The result of the operation. Some of the fields are only valid for specific operations.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    version (`str`_):

       The version of the scan result schema.
    status (`vim.host.PatchManager.Status`_, optional):

       The scan results for each patch.
    xmlResult (`str`_, optional):

       The scan results in XML format.
