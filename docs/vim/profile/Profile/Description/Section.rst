
vim.profile.Profile.Description.Section
=======================================
  The `ProfileDescriptionSection <vim/profile/Profile/Description/Section.rst>`_ data object contains a profile element description and any messages that may be associated with the profile section.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    description (`vim.ExtendedElementDescription <vim/ExtendedElementDescription.rst>`_):

       Localized message data.
    message ([`vmodl.LocalizableMessage <vmodl/LocalizableMessage.rst>`_], optional):

       List of messages that make up the section.
