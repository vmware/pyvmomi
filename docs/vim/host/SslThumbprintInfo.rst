.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.host.SslThumbprintInfo
==========================
  The SSL thumbprint information for a host managed by a vCenter Server or a vCenter extension to login into other hosts without username/password authentication.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    principal (`str`_):

       The principal used for the login session
    ownerTag (`str`_):

       The tag associated with this registration. Owner tags allow multiple entities to register the same thumbprint without interfering with each other on the life cycle of the thumbprint with their unique tags. Each solution should use a unique tag to identify itself.
    sslThumbprints ([`str`_], optional):

       Specify the SSL thumbprints to register on the host.
