.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.HostSystem: ../../../../vim/HostSystem.rst

.. _vSphere API 4.0: ../../../../vim/version.rst#vimversionversion5

.. _HostProfileHostBasedConfigSpec: ../../../../vim/profile/host/HostProfile/HostBasedConfigSpec.rst

.. _vim.profile.host.HostProfile.ConfigSpec: ../../../../vim/profile/host/HostProfile/ConfigSpec.rst


vim.profile.host.HostProfile.HostBasedConfigSpec
================================================
  The `HostProfileHostBasedConfigSpec`_ data object specifies the host from which configuration data is to be extracted and the profile(s) to be created or updated.
:extends: vim.profile.host.HostProfile.ConfigSpec_
:since: `vSphere API 4.0`_

Attributes:
    host (`vim.HostSystem`_):

       ESX host.
    useHostProfileEngine (`bool`_, optional):

       Flag indicating if the Profile Engine should use the profile plug-ins present on the host to create the profile. Iftrue, the host Profile Engine uses the vSphere 5.0 (or later) profile plug-ins. The resulting profile is not compatible with legacy hosts (pre 5.0). Iffalseor not specified, the Profile Engine creates a legacy host profile.
