.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _ProfileDescription: ../../../vim/profile/Profile/Description.rst

.. _vim.profile.Profile.Description.Section: ../../../vim/profile/Profile/Description/Section.rst


vim.profile.Profile.Description
===============================
  The `ProfileDescription`_ data object describes a profile. The description contains multiple sections. Each section describes a part of the profile.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    section ([`vim.profile.Profile.Description.Section`_]):

       Sections which make up the profile description.
