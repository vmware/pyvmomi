.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.dvs.HostMember.Backing: ../../../vim/dvs/HostMember/Backing.rst


vim.host.HostProxySwitch.Specification
======================================
  This data object type describes the HostProxySwitch specification representing the properties on a HostProxySwitch that can be configured once the object exists.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    backing (`vim.dvs.HostMember.Backing`_, optional):

       The specification describes how physical network adapters are bridged to the switch.
