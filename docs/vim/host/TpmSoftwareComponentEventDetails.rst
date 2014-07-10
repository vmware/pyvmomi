.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _vim.host.TpmEventDetails: ../../vim/host/TpmEventDetails.rst


vim.host.TpmSoftwareComponentEventDetails
=========================================
  Details of a Trusted Platform Module (TPM) event recording a software component related event.This event is created when measuring a software component installed on the system. A software component may be a tardisk, a kernel module or any other type supported by the package system.Some software components are not packaged as VIBs (currently the package database and persistent state information of ESXi). For these components the VIB fields will contain empty strings.
:extends: vim.host.TpmEventDetails_
:since: `vSphere API 5.1`_

Attributes:
    componentName (`str`_):

       Name of the software component that caused this TPM event.
    vibName (`str`_):

       Name of the VIB containing the software component.
    vibVersion (`str`_):

       Version of the VIB containing the software component.
    vibVendor (`str`_):

       Vendor of the VIB containing the software component.
