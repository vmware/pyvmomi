
vim.host.ImageConfigManager
===========================
  This managed object is the interface for configuration of the ESX software image, including properties such as acceptance level. It is currently designed to be host agent specific.


:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


Attributes
----------


Methods
-------


HostImageConfigGetAcceptance():
   Queries the current host acceptance level setting.See `HostImageAcceptanceLevel <vim/host/ImageConfigManager/AcceptanceLevel.rst>`_ 


  Privilege:
               System.Read



  Args:


  Returns:
    `str <https://docs.python.org/2/library/stdtypes.html>`_:
         

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       if the host acceptance setting is invalid.See `HostImageAcceptanceLevel <vim/host/ImageConfigManager/AcceptanceLevel.rst>`_ 


HostImageConfigGetProfile():
   Queries the current host image profile information.See `HostImageProfileSummary <vim/host/ImageConfigManager/ImageProfileSummary.rst>`_ 


  Privilege:
               System.Read



  Args:


  Returns:
    `vim.host.ImageConfigManager.ImageProfileSummary <vim/host/ImageConfigManager/ImageProfileSummary.rst>`_:
         


UpdateHostImageAcceptanceLevel(newAcceptanceLevel):
   Sets the acceptance level of the host image profile.See `HostImageAcceptanceLevel <vim/host/ImageConfigManager/AcceptanceLevel.rst>`_ 


  Privilege:
               Host.Config.Image



  Args:
    newAcceptanceLevel (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       the new AcceptanceLevel to set.See `HostImageAcceptanceLevel <vim/host/ImageConfigManager/AcceptanceLevel.rst>`_ 




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       if the acceptance level is raised and there are VIB packages that are not permitted by the higher acceptance level.See `HostImageAcceptanceLevel <vim/host/ImageConfigManager/AcceptanceLevel.rst>`_ 


