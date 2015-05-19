.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.TpmDigestInfo: ../../vim/host/TpmDigestInfo.rst

.. _vim.host.TpmEventLogEntry: ../../vim/host/TpmEventLogEntry.rst


vim.host.TpmAttestationReport
=============================
  This class is used to report Trusted Platform Module (TPM) attestation information - values of the Platform Configuration Registers (PCRs) and the TPM event log to the external clients.This information can be used to determine the integrity of the software stack running as reported by the platform.The TPM stores digests (hashes) of the software stack components running on the host. Both binary modules and configuration information can be hashed. The calculated hash values are stored in special-purpose hardware registers called PCRs. Each PCR is defined to hold cumulative digest(s) of specific part(s) of the software stack.Due to the limited amount of PCRs available a hash-chaining scheme is implemented. When adding new information to a PCR the new value of hash is computed according to the following formula: NewHash = hash_function(OldHash + hash_function(NewData)) This scheme allows storing measurements of an unlimited amount of components.The TPM event log provides an exact sequence of the events that contributed to the value of a PCR. It contains information about the type of the event and event-specific information. The presence of the log allows verification of both the final PCR state and the entire attestation path that formed it.It is possible for this report to be unreliable. This could be due to missing package information in the host database, errors in creation of the events. Only first 1000 events are recorded by the kernel. Further events will not be recorded in the log and will cause the log to be marked as incomplete.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    tpmPcrValues ([`vim.host.TpmDigestInfo`_]):

       The array of PCR digest values stored in the TPM device since the last host boot time.
    tpmEvents ([`vim.host.TpmEventLogEntry`_]):

       Log of TPM software stack attestation events.
    tpmLogReliable (`bool`_):

       This flag indicates whether the provided TPM events are a complete and reliable information about host boot status.TPM event log may be incomplete (and therfore unreliable) if certain modules have inappropriate origin or if the package information is incomplete. Only first 1000 events are recorded by the kernel. Further events will not be recorded in the log and will cause the log to be marked as unreliable.
