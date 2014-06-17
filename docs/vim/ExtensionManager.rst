.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../vim/Task.rst

.. _VI API 2.5: ../vim/version.rst#vimversionversion2

.. _vim.Extension: ../vim/Extension.rst

.. _IpPoolManager: ../vim/IpPoolManager.rst

.. _vSphere API 4.0: ../vim/version.rst#vimversionversion5

.. _vSphere API 5.1: ../vim/version.rst#vimversionversion8

.. _vSphere API 5.0: ../vim/version.rst#vimversionversion7

.. _vim.ManagedEntity: ../vim/ManagedEntity.rst

.. _vim.fault.NotFound: ../vim/fault/NotFound.rst

.. _LoginExtensionByCertificate: ../vim/SessionManager.rst#loginExtensionByCertificate

.. _vmodl.fault.InvalidArgument: ../vmodl/fault/InvalidArgument.rst

.. _vim.fault.NoClientCertificate: ../vim/fault/NoClientCertificate.rst

.. _vim.ExtensionManager.IpAllocationUsage: ../vim/ExtensionManager/IpAllocationUsage.rst


vim.ExtensionManager
====================
  This managed object type provides directory and basic management services for all registered extensions.Clients use the ExtensionManager, available in `ServiceInstance`_ , to access extension objects.While several authentication methods are available for extension servers to use (see `SessionManager`_ ), only one authentication method is valid for an extension at any given time.


:since: `VI API 2.5`_


Attributes
----------
    extensionList (`vim.Extension`_):
      privilege: System.View
       The list of currently registered extensions.


Methods
-------


UnregisterExtension(extensionKey):
   Unregisters the specified extension if it exists.


  Privilege:
               Extension.Unregister



  Args:
    extensionKey (`str`_):
       Unique name of extension to unregister.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       if the specified extension is not registered.


FindExtension(extensionKey):
   Returns extension with the given key, if any.


  Privilege:
               System.View



  Args:
    extensionKey (`str`_):
       Key to search for.




  Returns:
    `vim.Extension`_:
         Extension that matches given key, if any.


RegisterExtension(extension):
   Registers extension.


  Privilege:
               Extension.Register



  Args:
    extension (`vim.Extension`_):
       Extension description to register.




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       if the Extension description is incomplete or an extension is already registered with the given unique key, or if the extension is an OVF extension and its section types overlap with other registered OVF extensions.


UpdateExtension(extension):
   If the key specified in the extension exists, the existing record is updated.If thesubjectNameproperty of the Extension object has a value, and it is different from the existing value, this method will unset any public key or certificate associated with the extension.


  Privilege:
               Extension.Update



  Args:
    extension (`vim.Extension`_):
       Updated extension description.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       if the specified extension key is not registered.

    `vmodl.fault.InvalidArgument`_: 
       if the Extension description is incomplete or invalid, or if the extension is an OVF extension and its section types overlap with other registered OVF extensions.


GetPublicKey():
   Returns VirtualCenter Server public key.


  Privilege:
               System.View



  Args:


  Returns:
    `str`_:
         Public key of VirtualCenter Server, encoded in PEM (privacy-enhanced mail) format.


SetPublicKey(extensionKey, publicKey):
   Sets extension's public key.This method will unset any subject name or certificate associated with the extension.


  Privilege:
               Extension.Update



  Args:
    extensionKey (`str`_):
       Key of extension to update.


    publicKey (`str`_):
       Public key of extension, encoded in PEM (privacy-enhanced mail) format.




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       if the public key is invalid.


SetExtensionCertificate(extensionKey, certificatePem):
   Update the stored authentication certificate for a specified extension. Updates the registration of the specified extension with the thumbprint of the X.509 client certificate provided over SSL handshake, or by thecertificatePemargument. The thumbprint will be used to authenticate the extension during invocations of `LoginExtensionByCertificate`_ .NOTE: No verification is performed on the received certificate, such as expiry or revocation.This method will unset any public key or subject name associated with the extension.
  since: `vSphere API 4.0`_


  Privilege:
               Extension.Update



  Args:
    extensionKey (`str`_):
       Key of extension to update.


    certificatePem (`str`_, optional):
       PEM encoded certificate. If not specified, the certificate passed over SSL handshake is used.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       if an extension specified byextensionKeyis not registered.

    `vim.fault.NoClientCertificate`_: 
       if certificatePem is not specified, and no certificate was passed over SSL handshake.

    `vmodl.fault.InvalidArgument`_: 
       if the certificate described bycertificatePemis not in PEM format, or could not be decoded to an X.509 certificate.


QueryManagedBy(extensionKey):
   Find entities managed by an extension. These can be either virtual machines or vApps.
  since: `vSphere API 5.0`_


  Privilege:
               System.View



  Args:
    extensionKey (`str`_):
       Key of the extension to find managed entities for.




  Returns:
    `vim.ManagedEntity`_:
         List of entities managed by the extension.


QueryExtensionIpAllocationUsage(extensionKeys):
   Query statistics about IP allocation usage, either system wide or for specified extensions.Refer to `IpPoolManager`_ for details.
  since: `vSphere API 5.1`_


  Privilege:
               System.View



  Args:
    extensionKeys (`str`_, optional):
       List of extensions whose IP allocation is being queried. If no extension keys are specified then allocation data for all registered extensions are returned.




  Returns:
    `vim.ExtensionManager.IpAllocationUsage`_:
         List of IP allocation usage.


