.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _HostImageProfileSummary: ../../vim/host/ImageConfigManager/ImageProfileSummary.rst

.. _HostImageAcceptanceLevel: ../../vim/host/ImageConfigManager/AcceptanceLevel.rst

.. _vim.fault.HostConfigFault: ../../vim/fault/HostConfigFault.rst

.. _vim.host.ImageConfigManager.ImageProfileSummary: ../../vim/host/ImageConfigManager/ImageProfileSummary.rst


vim.host.ImageConfigManager
===========================
  This managed object is the interface for configuration of the ESX software image, including properties such as acceptance level. It is currently designed to be host agent specific.


:since: `vSphere API 5.0`_


Attributes
----------


Methods
-------


HostImageConfigGetAcceptance():
   Queries the current host acceptance level setting.See `HostImageAcceptanceLevel`_ 


  Privilege:
               System.Read



  Args:


  Returns:
    `str`_:
         

  Raises:

    `vim.fault.HostConfigFault`_: 
       if the host acceptance setting is invalid.See `HostImageAcceptanceLevel`_ 


HostImageConfigGetProfile():
   Queries the current host image profile information.See `HostImageProfileSummary`_ 


  Privilege:
               System.Read



  Args:


  Returns:
    `vim.host.ImageConfigManager.ImageProfileSummary`_:
         


UpdateHostImageAcceptanceLevel(newAcceptanceLevel):
   Sets the acceptance level of the host image profile.See `HostImageAcceptanceLevel`_ 


  Privilege:
               Host.Config.Image



  Args:
    newAcceptanceLevel (`str`_):
       the new AcceptanceLevel to set.See `HostImageAcceptanceLevel`_ 




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault`_: 
       if the acceptance level is raised and there are VIB packages that are not permitted by the higher acceptance level.See `HostImageAcceptanceLevel`_ 


