.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../vim/Task.rst

.. _VI API 2.5: ../vim/version.rst#vimversionversion2

.. _AddLicense: ../vim/LicenseManager.rst#addLicense

.. _vim.KeyValue: ../vim/KeyValue.rst

.. _RemoveLicense: ../vim/LicenseManager.rst#removeLicense

.. _vim.HostSystem: ../vim/HostSystem.rst

.. _vSphere API 4.0: ../vim/version.rst#vimversionversion5

.. _SetLicenseEdition: ../vim/LicenseManager.rst#setEdition

.. _vim.fault.InvalidState: ../vim/fault/InvalidState.rst

.. _vim.fault.InvalidLicense: ../vim/fault/InvalidLicense.rst

.. _vmodl.fault.InvalidArgument: ../vmodl/fault/InvalidArgument.rst

.. _vim.LicenseAssignmentManager: ../vim/LicenseAssignmentManager.rst

.. _vmodl.fault.NotEnoughLicenses: ../vmodl/fault/NotEnoughLicenses.rst

.. _vim.LicenseManager.LicenseInfo: ../vim/LicenseManager/LicenseInfo.rst

.. _vim.LicenseManager.FeatureInfo: ../vim/LicenseManager/FeatureInfo.rst

.. _vim.LicenseManager.LicenseSource: ../vim/LicenseManager/LicenseSource.rst

.. _vim.LicenseManager.DiagnosticInfo: ../vim/LicenseManager/DiagnosticInfo.rst

.. _vim.LicenseManager.EvaluationInfo: ../vim/LicenseManager/EvaluationInfo.rst

.. _vim.fault.CannotAccessLocalSource: ../vim/fault/CannotAccessLocalSource.rst

.. _vim.fault.LicenseServerUnavailable: ../vim/fault/LicenseServerUnavailable.rst

.. _vim.LicenseManager.AvailabilityInfo: ../vim/LicenseManager/AvailabilityInfo.rst

.. _vim.LicenseManager.LicenseUsageInfo: ../vim/LicenseManager/LicenseUsageInfo.rst


vim.LicenseManager
==================
  This managed object type controls entitlements for a given VMware platform. VMware platforms include VirtualCenter, ESX Server, VMware Server, Workstation and Player. Entitlements define what software capabilities this host may use.Entitlements are identified by a short string 'key'. Keys can represent either a particular edition (Full, Starter) or a particular feature/function (featureKey) (backup, nas). An edition implies zero one or more functions which are express, denied or optional. For example a 'Full' edition includes 'iscsi' function but a Starter edition might disallow it.Which edition a given VMware platform uses can be defined at any time. Generally this is done right after first install and boot as installation software may not set it. For editions that are similar in nature, any future changes to edition type will only impact future requests for functionality. Current functionality is left unaffected. The same is true for optional functions enabled/disabled after some period of time. For dissimilar editions, such transitions may require entering maintenance mode first else an exception of InvalidState will be thrown.To specify the edition type and any optional functions, use updateLicense for ESX Server and addLicense follow by LicenseAssingmentManager.updateAssignedLicense for VirtualCenter.When an edition is specified for a given host, the cost of that edition (how many licenses are needed) is determined. The cost is computed using the license's CostUnit value multiplied by the number of units activated. For example, when a VMware platform is set to an edition which uses a 'cpuPackage' on a two socket server, two licenses would be needed to successfully install that edition.Here is a diagram of the unit costs supported by this API and their relationships.+------------------------------+ +--------+ +-------+ | +-----------+ +-----------+ | | Server | | Host | | | | | | | +--------+ +-------+ | | cpuCore | | cpuCore | | +-------+ | +-----------+ +-----------+ | +--------+ | Host | | cpuPackage | | VM | +-------+ +------------------------------+ +--------+




Attributes
----------
    source (`vim.LicenseManager.LicenseSource`_):
       Set or return a data object type of LocalLicense or LicenseServer.
    sourceAvailable (`bool`_):
       Current state of the license source. License sources that are LocalSource are always available.
    diagnostics (`vim.LicenseManager.DiagnosticInfo`_):
       Return current diagnostic information.
    featureInfo (`vim.LicenseManager.FeatureInfo`_):
       The list of features that can be licensed.
    licensedEdition (`str`_):
       The product's license edition. The edition defines which product license the server requires. This, in turn, determines the core set of functionalities provided by the product and the additional features that can be licensed. If no edition is set the property is set to the empty string (""). To set the edition use `SetLicenseEdition`_ .
    licenses (`vim.LicenseManager.LicenseInfo`_):
      privilege: dynamic
       Get information about all the licenses avaiable.
    licenseAssignmentManager (`vim.LicenseAssignmentManager`_):
      privilege: System.View
       License Assignment Manager
    evaluation (`vim.LicenseManager.EvaluationInfo`_):
      privilege: System.Read
       


Methods
-------


QuerySupportedFeatures(host):
   Queries the current license source for a list of available licenses that can be licensed from this system.
  since: `VI API 2.5`_


  Privilege:
               Global.Licenses



  Args:
    host (`vim.HostSystem`_, optional):
       Use the license source of the specified host.




  Returns:
    `vim.LicenseManager.FeatureInfo`_:
         


QueryLicenseSourceAvailability(host):
   Queries the current license source for total and available licenses available for each feature known to this system.


  Privilege:
               Global.Licenses



  Args:
    host (`vim.HostSystem`_, optional):
       Use the license source of the specified host.




  Returns:
    `vim.LicenseManager.AvailabilityInfo`_:
         


QueryLicenseUsage(host):
   Returns the license usage. The license usage is a list of supported features and the number of licenses that have been reserved.PLATFORM Specific Notes:VirtualCenter - Empty string returns the usage of non-host specific features. Must specify managed host to query. ESX Server - Host argument ignored.


  Privilege:
               System.Read



  Args:
    host (`vim.HostSystem`_, optional):
       Host to query for usage. If missing, query the server the `LicenseManager`_ is on.




  Returns:
    `vim.LicenseManager.LicenseUsageInfo`_:
         


SetLicenseEdition(host, featureKey):
   Defines the product's license edition. The edition defines which product license the server requires. This, in turn, determines the core set of functionality provided by the product and the additional features that can be licensed.To determine what featureKey the current platform will accept, use querySourceAvailablity() at runtime, or consult the documentation for the current platform.


  Privilege:
               Global.Licenses



  Args:
    host (`vim.HostSystem`_, optional):
       Host to act on if LicenseManager is not on a host.


    featureKey (`str`_, optional):
       Name of edition feature to select. If featureKey is not set or set to empty string, the product becomes unlicensed.




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState`_: 
       If the feature cannot be supported on the platform, potentially because the hardware configuration does not support it.

    `vim.fault.LicenseServerUnavailable`_: 
       If the license server is unavailable.

    `vmodl.fault.InvalidArgument`_: 
       If a feature key is not an edition feature key.


CheckLicenseFeature(host, featureKey):
   Returns whether or not a given feature is enabled.


  Privilege:
               System.Read



  Args:
    host (`vim.HostSystem`_, optional):
       Host to act on if LicenseManager is not on a host.


    featureKey (`str`_):
       Name of the feature to enable.




  Returns:
    `bool`_:
         Returns true if the feature is enabled and false if it is not.

  Raises:

    `vim.fault.InvalidState`_: 
       If the feature cannot be supported on the platform, potentially because the hardware configuration does not support it.

    `vmodl.fault.InvalidArgument`_: 
       If a feature name is not found.


EnableFeature(host, featureKey):
   Enable a feature that has an optional state.


  Privilege:
               Global.Licenses



  Args:
    host (`vim.HostSystem`_, optional):
       Host to act on if LicenseManager is not on a host.


    featureKey (`str`_):
       Name of the feature to enable.




  Returns:
    `bool`_:
         Returns true if enabling the feature was successful, false otherwise.

  Raises:

    `vim.fault.InvalidState`_: 
       If the feature cannot be supported on the platform, potentially because the hardware configuration does not support it.

    `vim.fault.LicenseServerUnavailable`_: 
       If the license server is unavailable.

    `vmodl.fault.InvalidArgument`_: 
       If a feature name is not found or it is not optional.


DisableFeature(host, featureKey):
   Release licenses for an optional feature.


  Privilege:
               Global.Licenses



  Args:
    host (`vim.HostSystem`_, optional):
       Host to act on if LicenseManager is not on a host.


    featureKey (`str`_):
       key of the feature to disable.




  Returns:
    `bool`_:
         Returns true if the feature was disabled and false if not.

  Raises:

    `vim.fault.InvalidState`_: 
       If the feature is in use.

    `vim.fault.LicenseServerUnavailable`_: 
       If the license server is unavailable.

    `vmodl.fault.InvalidArgument`_: 
       If a feature name is not found or it is not optional.


ConfigureLicenseSource(host, licenseSource):
   Allows for reconfiguration of the License Manager license source.This changes the licensing source to be either served or local. Before changing the license source location, the API checks the number of licenses available at the new potential source to ensure there are at least as many licenses there as have been issued by the current source. If there are an equal or greater number of licenses at the new source, all licenses on the current source are released and then reacquired from the new source. If there are not enough licenses available on the new source to reissue all licenses, the operation fails.This is used to configure the license source on an individual host.PLATFORM Specific Notes:VirtualCenter - only supports a served source. the host parameter is mandatory. ESX Server - the host parameter is optional.


  Privilege:
               Global.Licenses



  Args:
    host (`vim.HostSystem`_, optional):
       Host for which the license manager should be reconfigured.


    licenseSource (`vim.LicenseManager.LicenseSource`_):
       ServedSource or LocalSource.




  Returns:
    None
         

  Raises:

    `vim.fault.CannotAccessLocalSource`_: 
       if the local source cannot be accessed.

    `vim.fault.InvalidLicense`_: 
       if the new license source is LocalLicenseSource and the license file is not valid.

    `vim.fault.LicenseServerUnavailable`_: 
       if the license server is unreachable.

    `vmodl.fault.NotEnoughLicenses`_: 
       if the new license source does not have enough licenses.


UpdateLicense(licenseKey, labels):
   Updates the available licenses to the one provided in licenseKey. This is the same as removing all the licenses using `RemoveLicense`_ and adding licenseKey using `AddLicense`_ If the optional parameter labels is specify this is the same as calling updateLicense without the optioal parameter and calling updateLabel for each pair in the labels array.
  since: `vSphere API 4.0`_


  Privilege:
               Global.Licenses



  Args:
    licenseKey (`str`_):
       A license. E.g. a serial license.


    labels (`vim.KeyValue`_, optional):
       array of key-value labels.




  Returns:
    `vim.LicenseManager.LicenseInfo`_:
         Returns information about the license specified in licenseKey.


AddLicense(licenseKey, labels):
   Adds a license to the inventory of available licenses.
  since: `vSphere API 4.0`_


  Privilege:
               Global.Licenses



  Args:
    licenseKey (`str`_):
       A license. E.g. a serial license.


    labels (`vim.KeyValue`_, optional):
       array of key-value labels. Ignored by ESX Server.




  Returns:
    `vim.LicenseManager.LicenseInfo`_:
         Returns information about the license specified in licenseKey.


RemoveLicense(licenseKey):
   Remove license from the available set.
  since: `vSphere API 4.0`_


  Privilege:
               Global.Licenses



  Args:
    licenseKey (`str`_):
       A licenses. E.g. a serial license.




  Returns:
    None
         


DecodeLicense(licenseKey):
   Decodes licensing information on the license specified.
  since: `vSphere API 4.0`_


  Privilege:
               Global.Licenses



  Args:
    licenseKey (`str`_):
       A license. E.g. a serial license.




  Returns:
    `vim.LicenseManager.LicenseInfo`_:
         Returns information about the license specified in licenseKey.


UpdateLicenseLabel(licenseKey, labelKey, labelValue):
   Update a license's label. It creates a label entry if the labelKey doesn't already exist
  since: `vSphere API 4.0`_


  Privilege:
               Global.Licenses



  Args:
    licenseKey (`str`_):
       A license.


    labelKey (`str`_):
       A label key.


    labelValue (`str`_):
       Value for the label.




  Returns:
    None
         


RemoveLicenseLabel(licenseKey, labelKey):
   Removed a license's label.
  since: `vSphere API 4.0`_


  Privilege:
               Global.Licenses



  Args:
    licenseKey (`str`_):
       A license.


    labelKey (`str`_):
       A label key.




  Returns:
    None
         


