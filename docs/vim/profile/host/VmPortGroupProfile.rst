.. _policy: ../../../vim/profile/ApplyProfile.rst#policy

.. _Network: ../../../vim/Network.rst

.. _property: ../../../vim/profile/ApplyProfile.rst#property

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _VmPortGroupProfile: ../../../vim/profile/host/VmPortGroupProfile.rst

.. _vim.profile.host.PortGroupProfile: ../../../vim/profile/host/PortGroupProfile.rst


vim.profile.host.VmPortGroupProfile
===================================
  The `VmPortGroupProfile`_ data object represents the subprofile for a port group that will be used by virtual machines. Use the `policy`_ list for access to configuration data for the virtual machine port group profile. Use the `property`_ list for access to subprofiles, if any.vSphere Servers use `Network`_ managed objects to represent virtual machine port groups in the vSphere inventory.
:extends: vim.profile.host.PortGroupProfile_
:since: `vSphere API 4.0`_

Attributes:
