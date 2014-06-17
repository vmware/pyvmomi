.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.TpmEventDetails: ../../vim/host/TpmEventDetails.rst


vim.host.TpmEventLogEntry
=========================
  This data object represents a single entry of an event log created by Trusted Platform Module (TPM).An TPM event log entry represents a single change to the value of a Platform Configuration Register (PCR). It contains detailed information about the reason of PCR value change, and the specifics of the event.Multiple objects of this type form an TPM event log. This log allows for verification of the both the software stack running on a host and the attestation process itself.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    pcrIndex (`int`_):

       Index of the PCR that was affected by the event.
    eventDetails (`vim.host.TpmEventDetails`_):

       The details of the event.
