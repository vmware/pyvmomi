.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.PlugStoreTopology.Path: ../../vim/host/PlugStoreTopology/Path.rst

.. _vim.host.PlugStoreTopology.Device: ../../vim/host/PlugStoreTopology/Device.rst

.. _vim.host.PlugStoreTopology.Target: ../../vim/host/PlugStoreTopology/Target.rst

.. _vim.host.PlugStoreTopology.Plugin: ../../vim/host/PlugStoreTopology/Plugin.rst

.. _vim.host.PlugStoreTopology.Adapter: ../../vim/host/PlugStoreTopology/Adapter.rst


vim.host.PlugStoreTopology
==========================
  This data object represents the plug-store topology on a host system. Through this data object, the storage structure of a system that utilizes the plug-store architecture can be presented.The object entity-relationship diagram is modeled below:0..N 0..N 0..N Plugin -----> Device ------> Path<------ Adapter<------ | ------> 0,1 | 1 | | 0,1 \|/ TargetDescription and reasoning behind the relationships:When a storage device driver is loaded, it claims a PCI device as a host bus adapter. This host bus adapter is represented as an Adapter. The PCI device identifier is a property on the HostBusAdapter in the Adapter.Once the host bus adapter is on the system, the hardware bus is scanned. If a storage Device is found on the bus, the communication path to the Device from the the host bus adapter is represented by a Path. A Device may have more than one Path. How those Paths are composed to create a Device is determined by a storage Plugin.When a storage Plugin is loaded, it claims a set of Paths. It groups these Paths into a set of Devices. Devices are hence associated with a set of Paths that might be used to provide a single logical device such as in the case of multipathing. Devices may be also composed of zero Paths meaning that they do not directly use a host bus adapter for communication with underlying storage.The purpose of this data object is to represent the topology of storage as seen by the base plug-store system. There is some overlap with information in other objects such as ScsiTopology which is only applicable when a particular "native multipathing" plugin is used. This data object provides the complete inventory of Devices and Paths. Hence it provides a superset of Device mappings over data object such as ScsiTopology and MultipaThe use cases that this data object accommodates includes the following non-exhaustive list:
   * Enumerate paths on a host bus adapter.
   * Enumerate paths on a storage device.
   * Conveniently access the devices a host bus adapter is associated with by traversing the path.
   * Determine which plugin a device belongs.
   * Determine which paths are claimed by a plugin by accumulating the paths of all device of the plugin.
   * Determine which plugin a path belongs to by accessing its device and finding that device in the Plugin list.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    adapter (`vim.host.PlugStoreTopology.Adapter`_, optional):

       List of host bus adapters in the plug store inventory.
    path (`vim.host.PlugStoreTopology.Path`_, optional):

       List of paths in the plug store inventory.
    target (`vim.host.PlugStoreTopology.Target`_, optional):

       Partial list of targets as seen by the host. The list of targets may not be exhaustive on the host.
    device (`vim.host.PlugStoreTopology.Device`_, optional):

       List of devices in the plug store inventory.
    plugin (`vim.host.PlugStoreTopology.Plugin`_, optional):

       List of plugins in the plug store inventory.
