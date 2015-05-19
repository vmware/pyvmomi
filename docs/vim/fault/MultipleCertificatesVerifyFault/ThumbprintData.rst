.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.fault.MultipleCertificatesVerifyFault.ThumbprintData
========================================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    port (`int`_):

       The port used by the service.
    thumbprint (`str`_):

       The SSL thumbprint of the host's certificate used by the service.
