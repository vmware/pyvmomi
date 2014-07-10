.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.host.DigestInfo: ../../vim/host/DigestInfo.rst


vim.host.TpmDigestInfo
======================
  This data object type describes the digest values in the Platform Configuration Register (PCR) of a Trusted Platform Module (TPM) device.
:extends: vim.host.DigestInfo_
:since: `vSphere API 4.0`_

Attributes:
    pcrNumber (`int`_):

       Index of the PCR that stores the TPM digest value.
