
vim.host.ActiveDirectorySpec.Specification
==========================================
  The `HostActiveDirectorySpec <vim/host/ActiveDirectorySpec/Specification.rst>`_ data object defines properties for Active Directory domain access.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    domainName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Domain name.
    userName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Name of an Active Directory account with the authority to add a host to the domain.
    password (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Password for the Active Directory account.
    camServer (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If set, the CAM server will be used to join the domain and theuserNameandpasswordfields will be ignored.
    thumbprint (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Thumbprint for the SSL certficate of CAM server
