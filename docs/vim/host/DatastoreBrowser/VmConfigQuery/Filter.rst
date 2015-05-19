.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst


vim.host.DatastoreBrowser.VmConfigQuery.Filter
==============================================
  The filter for the virtual machine configuration file.
:extends: vmodl.DynamicData_

Attributes:
    matchConfigVersion ([`int`_], optional):

       If this property is set, only the virtual machine configuration files that match one of the specified configuration versions are selected. If no versions are specified, this search criteria is ignored.
