
vim.host.NasVolume.Config
=========================
  This describes the NAS Volume configuration containing the configurable properties on a NAS Volume
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    changeOperation (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates the change operation to apply on this configuration specification.See `HostConfigChangeOperation <vim/host/ConfigChange/Operation.rst>`_ 
    spec (`vim.host.NasVolume.Specification <vim/host/NasVolume/Specification.rst>`_, optional):

       The specification volume.
