.. _vim.fault.VimFault: ../../vim/fault/VimFault.rst


vim.fault.OvfFault
==================
    :extends:

        `vim.fault.VimFault`_

  A common base type fault for all Ovf related faults. The structure of OvfFault is as listed.
   * OvfFault
   * OvfInvalidPackage
   * OvfXmlFormat
   * OvfWrongNamespace
   * OvfElement
   * OvfElementInvalidValue
   * OvfUnexpectedElement
   * OvfDuplicateElement
   * OvfMissingElement
   * OvfMissingElementNormalBoundary
   * OvfDuplicatedElementBoundary
   * OvfAttribute
   * OvfMissingAttribute
   * OvfInvalidValue
   * OvfInvalidValueFormatMalformed
   * OvfInvalidValueConfiguration
   * OvfInvalidValueReference
   * OvfInvalidValueEmpty
   * OvfProperty
   * OvfPropertyType
   * OvfPropertyValue
   * OvfPropertyNetwork
   * OvfPropertyQualifier
   * OvfPropertyQualifierWarning
   * OvfConstraint
   * OvfDiskOrderConstraint
   * OvfHostResourceConstraint
   * OvfUnsupportedPackage
   * OvfNoHostNic
   * OvfInvalidVmName
   * OvfUnsupportedAttribute
   * OvfUnsupportedAttributeValue
   * OvfUnsupportedElement
   * OvfUnsupportedElementValue
   * OvfUnsupportedSection
   * OvfNoSpaceOnController
   * OvfUnsupportedType
   * OvfUnsupportedSubType
   * OvfHardwareCheck
   * OvfNoSupportedHardwareFamily
   * OvfExport
   * OvfExportFailed
   * OvfHardwareExport
   * OvfUnsupportedDeviceExport
   * OvfUnknownDeviceBacking
   * OvfConnectedDevice
   * OvfConnectedDeviceISO
   * OvfUnableToExportDisk
   * OvfPropertyExport
   * OvfPropertyNetworkExport
   * OvfDuplicatedPropertyIdExport
   * OvfImport (these are typically returned as warnings)
   * OvfImportFailed
   * OvfHardwareCheck
   * OvfMissingHardware
   * OvfCpuCompatibility
   * OvfCpuCompatibilityCheckNotSupported
   * OvfUnsupportedDiskProvisioning
   * OvfDuplicatedPropertyIdImport
   * OvfNetworkMappingNotSupported
   * OvfSystemFault
   * OvfDiskMappingNotFound
   * OvfHostValueNotParsed
   * OvfInternalError
   * OvfUnsupportedDeviceBackingOption
   * OvfUnsupportedDeviceBackingInfo
   * OvfToXmlUnsupportedElement
   * OvfUnknownDevice
   * OvfUnknownEntity
   * OvfConsumerCallbackFault
   * OvfConsumerFault
   * OvfConsumerCommunicationError
   * OvfConsumerInvalidSection
   * OvfConsumerUndeclaredSection
   * OvfConsumerUndefinedPrefixAll messages go into the vimlocale

Attributes:




