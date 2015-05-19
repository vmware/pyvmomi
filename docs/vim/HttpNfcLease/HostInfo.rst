.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.HttpNfcLease.HostInfo
=========================
  Contains information about how to connect to a given host.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    url (`str`_):

       The host url will be of the formhttps://hostname/nfc/ticket id/The url can be used for both POST requests to a single device and for multi-POST requests to multiple devices. A single-POST URL is formed by adding the target id to the hostUrl:https://hostname/nfc/ticket id/target ida multi-POST URL looks likehttps://hostname/nfc/ticket id/multi?targets=id1,id2,id3,...
    sslThumbprint (`str`_):

       SSL thumbprint for the host the URL refers to. Empty if no SSL thumbprint is available or needed.
