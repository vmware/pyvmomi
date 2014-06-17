.. _vim.HostSystem: ../../../../vim/HostSystem.rst

.. _vSphere API 5.0: ../../../../vim/version.rst#vimversionversion7

.. _HostProfileSerializedHostProfileSpec: ../../../../vim/profile/host/HostProfile/SerializedHostProfileSpec.rst

.. _vim.profile.Profile.SerializedCreateSpec: ../../../../vim/profile/Profile/SerializedCreateSpec.rst


vim.profile.host.HostProfile.SerializedHostProfileSpec
======================================================
  The `HostProfileSerializedHostProfileSpec`_ data object contains a string representation of a host profile. Use this object when you create a host profile from a file.
:extends: vim.profile.Profile.SerializedCreateSpec_
:since: `vSphere API 5.0`_

Attributes:
    validatorHost (`vim.HostSystem`_, optional):

       Host for profile validation. This can be a host on which the profile is intended to be used.
