.. _DvsFilterConfig: ../../../vim/dvs/DistributedVirtualPort/FilterConfig.rst

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vim.InheritablePolicy: ../../../vim/InheritablePolicy.rst

.. _DvsTrafficFilterConfig: ../../../vim/dvs/DistributedVirtualPort/TrafficFilterConfig.rst

.. _DvsTrafficFilterConfigSpec: ../../../vim/dvs/DistributedVirtualPort/TrafficFilterConfigSpec.rst

.. _vim.dvs.DistributedVirtualPort.FilterConfig: ../../../vim/dvs/DistributedVirtualPort/FilterConfig.rst


vim.dvs.DistributedVirtualPort.FilterPolicy
===========================================
  This class defines Network Filter Policy.
:extends: vim.InheritablePolicy_
:since: `vSphere API 5.5`_

Attributes:
    filterConfig (`vim.dvs.DistributedVirtualPort.FilterConfig`_, optional):

       List of Network Filter Configurations. In an update operation, the array can contain all `DvsTrafficFilterConfigSpec`_ objects or all `DvsFilterConfig`_ and `DvsTrafficFilterConfig`_ object, but not mixed of Config and Spec objects. If array of FilterConfigSpec and TrafficFilterConfigSpec is used for updating Network Filter then only the Network Filters matching `key`_ / `key`_ is updated. If array of `DvsFilterConfig`_ and `DvsTrafficFilterConfig`_ is used for updating port settings, the Network Filter settings will be overridden with the new array specified. The specified array should only contain FilterConfig and TrafficFilterConfig objects with FilterConfig#inherited / TrafficFilterConfig#inherited set to false. FilterConfig/TrafficFilterConfig objects with FilterConfig#inherited/TrafficFilterConfig#inherited as true in the specified array will be ignored. The updated result will include FilterConfig/TrafficFilterConfig objects inherited from parent, if any.
