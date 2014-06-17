.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _HostActiveDirectorySpec: ../../../vim/host/ActiveDirectorySpec/Specification.rst


vim.host.ActiveDirectorySpec.Specification
==========================================
  The `HostActiveDirectorySpec`_ data object defines properties for Active Directory domain access.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    domainName (`str`_, optional):

       Domain name.
    userName (`str`_, optional):

       Name of an Active Directory account with the authority to add a host to the domain.
    password (`str`_, optional):

       Password for the Active Directory account.
    camServer (`str`_, optional):

       If set, the CAM server will be used to join the domain and theuserNameandpasswordfields will be ignored.
    thumbprint (`str`_, optional):

       Thumbprint for the SSL certficate of CAM server
