.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../vim/Task.rst

.. _vim.fault.NotFound: ../vim/fault/NotFound.rst

.. _vim.fault.AlreadyExists: ../vim/fault/AlreadyExists.rst

.. _vim.CustomizationSpecInfo: ../vim/CustomizationSpecInfo.rst

.. _vim.CustomizationSpecItem: ../vim/CustomizationSpecItem.rst

.. _vim.fault.ConcurrentAccess: ../vim/fault/ConcurrentAccess.rst

.. _vim.fault.CustomizationFault: ../vim/fault/CustomizationFault.rst

.. _vim.fault.UncustomizableGuest: ../vim/fault/UncustomizableGuest.rst

.. _vim.fault.CannotDecryptPasswords: ../vim/fault/CannotDecryptPasswords.rst

.. _vim.fault.MissingLinuxCustResources: ../vim/fault/MissingLinuxCustResources.rst

.. _vim.fault.MissingWindowsCustResources: ../vim/fault/MissingWindowsCustResources.rst


vim.CustomizationSpecManager
============================
  The CustomizationSpecManager managed object is used to manage customization specifications stored on the VirtualCenter server.




Attributes
----------
    info ([`vim.CustomizationSpecInfo`_]):
      privilege: VirtualMachine.Provisioning.ReadCustSpecs
       Gets a list of information on available specifications.
    encryptionKey ([`int`_]):
      privilege: System.View
       Gets a binary public encryption key that can be used to encrypt passwords in stored specifications.


Methods
-------


DoesCustomizationSpecExist(name):
   Whether or not a specification exists.


  Privilege:
               VirtualMachine.Provisioning.ReadCustSpecs



  Args:
    name (`str`_):




  Returns:
    `bool`_:
         


GetCustomizationSpec(name):
   Obtains a specification for the given name.


  Privilege:
               VirtualMachine.Provisioning.ReadCustSpecs



  Args:
    name (`str`_):
       Unique name identifying the requested customization specification.




  Returns:
    `vim.CustomizationSpecItem`_:
         

  Raises:

    `vim.fault.NotFound`_: 
       vim.fault.NotFound


CreateCustomizationSpec(item):
   Creates a new specification.


  Privilege:
               VirtualMachine.Provisioning.ModifyCustSpecs



  Args:
    item (`vim.CustomizationSpecItem`_):




  Returns:
    None
         

  Raises:

    `vim.fault.CustomizationFault`_: 
       vim.fault.CustomizationFault

    `vim.fault.AlreadyExists`_: 
       vim.fault.AlreadyExists

    `vim.fault.CannotDecryptPasswords`_: 
       vim.fault.CannotDecryptPasswords


OverwriteCustomizationSpec(item):
   Overwrites an existing specification, possibly after retrieving (by using 'get') and editing it. If, based on the item's changeVersion value, the overwrite process detects that the specification has changed since its retrieval, then the API uses the SpecModified exception to warn the client that he might overwrite another client's change.


  Privilege:
               VirtualMachine.Provisioning.ModifyCustSpecs



  Args:
    item (`vim.CustomizationSpecItem`_):




  Returns:
    None
         

  Raises:

    `vim.fault.CustomizationFault`_: 
       vim.fault.CustomizationFault

    `vim.fault.NotFound`_: 
       vim.fault.NotFound

    `vim.fault.ConcurrentAccess`_: 
       vim.fault.ConcurrentAccess

    `vim.fault.CannotDecryptPasswords`_: 
       vim.fault.CannotDecryptPasswords


DeleteCustomizationSpec(name):
   Deletes a specification.


  Privilege:
               VirtualMachine.Provisioning.ModifyCustSpecs



  Args:
    name (`str`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       vim.fault.NotFound


DuplicateCustomizationSpec(name, newName):
   Duplicates a specification.


  Privilege:
               VirtualMachine.Provisioning.ModifyCustSpecs



  Args:
    name (`str`_):


    newName (`str`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       vim.fault.NotFound

    `vim.fault.AlreadyExists`_: 
       vim.fault.AlreadyExists


RenameCustomizationSpec(name, newName):
   Renames a specification.


  Privilege:
               VirtualMachine.Provisioning.ModifyCustSpecs



  Args:
    name (`str`_):


    newName (`str`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       vim.fault.NotFound

    `vim.fault.AlreadyExists`_: 
       vim.fault.AlreadyExists


CustomizationSpecItemToXml(item):
   Converts a specification item to XML text


  Privilege:
               System.View



  Args:
    item (`vim.CustomizationSpecItem`_):




  Returns:
    `str`_:
         


XmlToCustomizationSpecItem(specItemXml):
   Converts an XML string to a specification item


  Privilege:
               System.View



  Args:
    specItemXml (`str`_):




  Returns:
    `vim.CustomizationSpecItem`_:
         

  Raises:

    `vim.fault.CustomizationFault`_: 
       vim.fault.CustomizationFault


CheckCustomizationResources(guestOs):
   Validate that required resources are available on the server to customize a particular guest operating system. These would include sysprep for Windows and the debugfs and changefs volume editors for Linux guests.


  Privilege:
               System.View



  Args:
    guestOs (`str`_):
       Short name from the guest OS descriptor list describing the OS we intend to customize.




  Returns:
    None
         

  Raises:

    `vim.fault.CustomizationFault`_: 
       vim.fault.CustomizationFault

    `vim.fault.MissingLinuxCustResources`_: 
       vim.fault.MissingLinuxCustResources

    `vim.fault.MissingWindowsCustResources`_: 
       vim.fault.MissingWindowsCustResources

    `vim.fault.UncustomizableGuest`_: 
       vim.fault.UncustomizableGuest


