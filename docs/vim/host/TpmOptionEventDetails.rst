
vim.host.TpmOptionEventDetails
==============================
  Details of a Trusted Platform Module (TPM) event recording boot-time options.The boot-time options set on the system are packaged into a file that is supplied to the kernel at boot time. The boot options may be a string of key=value pairs (possibly separated by a new line) or a blob of arbitrary data.
:extends: vim.host.TpmEventDetails_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    optionsFileName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the file containing the boot options.
    bootOptions ([`int <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Options set by the boot option package.This array exposes the raw contents of the settings file (or files) that were passed to kernel during the boot up process, and, therefore, should be treated accordingly.
