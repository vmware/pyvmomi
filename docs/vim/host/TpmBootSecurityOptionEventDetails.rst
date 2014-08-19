
vim.host.TpmBootSecurityOptionEventDetails
==========================================
  Details of a Trusted Platform Module (TPM) event recording kernel security option passed at boot time and currently in effect.This event type exists to simplify parsing of the security-related information by internal and third-party solutions. Each boot option may be passed to kernel multiple times and/or in different forms. Replicating the parsing logic of the kernel would be neither convinient, nor secure for the client applications.Each instance of this event reports details of a single security-related boot option, as set in the kernel.
:extends: vim.host.TpmEventDetails_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    bootSecurityOption (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Security-related options string, reflecting the state of an option set in the kernel.This string is in the form of a KEY=VALUE pair.
