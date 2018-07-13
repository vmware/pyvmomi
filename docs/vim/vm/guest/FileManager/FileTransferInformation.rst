.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../../vim/version.rst#vimversionversion7

.. _GuestFileManager: ../../../../vim/vm/guest/FileManager.rst

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst

.. _InitiateFileTransferFromGuest: ../../../../vim/vm/guest/FileManager.rst#initiateFileTransferFromGuest

.. _vim.vm.guest.FileManager.FileAttributes: ../../../../vim/vm/guest/FileManager/FileAttributes.rst


vim.vm.guest.FileManager.FileTransferInformation
================================================
  Represents the information about a `InitiateFileTransferFromGuest`_ operation of `GuestFileManager`_ object.The user can use the URL provided in url property to transfer the file from the guest. The user should send a HTTP GET request to the URL. Entire file content will be returned in the body of the response message.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    attributes (`vim.vm.guest.FileManager.FileAttributes`_):

       File attributes of the file that is being transferred from the guest.
    size (`long`_):

       Total size of the file in bytes.
    url (`str`_):

       Specifies the URL to which the user has to send HTTP GET request. Multiple GET requests cannot be sent to the URL simultaneously. URL will become invalid once a successful GET request is sent. The host part of the URL is returned as '*' if the hostname to be used is the name of the server to which the call was made. For example, if the call is made to esx-svr-1.domain1.com, and the file is available for download from http://esx-svr-1.domain1.com/guestFile?id=1=1234, the URL returned may be http:///guestFile?id=1=1234. The client replaces the asterisk with the server name on which it invoked the call.
