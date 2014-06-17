.. _int: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.option.OptionValue: ../../vim/option/OptionValue.rst

.. _ClusterDpmHostConfigInfo: ../../vim/cluster/DpmHostConfigInfo.rst

.. _vim.cluster.DpmConfigInfo.DpmBehavior: ../../vim/cluster/DpmConfigInfo/DpmBehavior.rst


vim.cluster.DpmConfigInfo
=========================
  Configuration of the VMware DPM service.All fields are defined as optional. In case of a reconfiguration, unset fields are not changed.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    enabled (`bool`_, optional):

       Flag indicating whether or not the service is enabled. This service can not be enabled, unless DRS is enabled as well.
    defaultDpmBehavior (`vim.cluster.DpmConfigInfo.DpmBehavior`_, optional):

       Specifies the default VMware DPM behavior for hosts. This default behavior can be overridden on a per host basis using the `ClusterDpmHostConfigInfo`_ object.
    hostPowerActionRate (`int`_, optional):

       DPM generates only those recommendations that are above the specified rating. Ratings vary from 1 to 5. This setting applies to both manual and automated (@link DpmBehavior) DPM clusters.
    option (`vim.option.OptionValue`_, optional):

       Advanced settings.
