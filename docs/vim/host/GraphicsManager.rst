
vim.host.GraphicsManager
========================
  This managed object manages the graphics state of the host.


:extends: vim.ExtensibleManagedObject_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_


Attributes
----------
    graphicsInfo ([`vim.host.GraphicsInfo <vim/host/GraphicsInfo.rst>`_]):
      privilege: System.Read
       Array of graphics information


Methods
-------


RefreshGraphicsManager():
   Refresh the available graphics information.


  Privilege:
               Host.Config.Settings



  Args:


  Returns:
    None
         


IsSharedGraphicsActive():
   Indicate if shared graphics device is active on the host.


  Privilege:
               System.Read



  Args:


  Returns:
    `bool <https://docs.python.org/2/library/stdtypes.html>`_:
         


