.. _vSphere API 4.0: ../../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst

.. _vmodl.LocalizableMessage: ../../../../vmodl/LocalizableMessage.rst

.. _ProfileDescriptionSection: ../../../../vim/profile/Profile/Description/Section.rst

.. _vim.ExtendedElementDescription: ../../../../vim/ExtendedElementDescription.rst


vim.profile.Profile.Description.Section
=======================================
  The `ProfileDescriptionSection`_ data object contains a profile element description and any messages that may be associated with the profile section.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    description (`vim.ExtendedElementDescription`_):

       Localized message data.
    message ([`vmodl.LocalizableMessage`_], optional):

       List of messages that make up the section.
