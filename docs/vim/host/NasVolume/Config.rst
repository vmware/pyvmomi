.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _HostConfigChangeOperation: ../../../vim/host/ConfigChange/Operation.rst

.. _vim.host.NasVolume.Specification: ../../../vim/host/NasVolume/Specification.rst


vim.host.NasVolume.Config
=========================
  This describes the NAS Volume configuration containing the configurable properties on a NAS Volume
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    changeOperation (`str`_, optional):

       Indicates the change operation to apply on this configuration specification.See `HostConfigChangeOperation`_ 
    spec (`vim.host.NasVolume.Specification`_, optional):

       The specification volume.
