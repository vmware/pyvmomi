.. _str: https://docs.python.org/2/library/stdtypes.html

.. _edit: ../../../vim/ConfigSpecOperation.rst#edit

.. _scope: ../../../vim/dvs/DistributedVirtualPort/ConfigInfo.rst#scope

.. _remove: ../../../vim/ConfigSpecOperation.rst#remove

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.ManagedEntity: ../../../vim/ManagedEntity.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _DistributedVirtualPort: ../../../vim/dvs/DistributedVirtualPort.rst

.. _vim.dvs.DistributedVirtualPort.Setting: ../../../vim/dvs/DistributedVirtualPort/Setting.rst


vim.dvs.DistributedVirtualPort.ConfigSpec
=========================================
  Specification to reconfigure a `DistributedVirtualPort`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    operation (`str`_):

       The operation to remove or modify the existing ports. The valid values are:
        * `edit`_
        * `remove`_
    key (`str`_, optional):

       Key of the port to be reconfigured.
    name (`str`_, optional):

       The name of the port.
    scope ([`vim.ManagedEntity`_], optional):

       The eligible entities that can connect to the port, for detail see `scope`_ .
    description (`str`_, optional):

       The description string of the port.
    setting (`vim.dvs.DistributedVirtualPort.Setting`_, optional):

       The network setting of the port.
    configVersion (`str`_, optional):

       The version string of the configuration.
