.. _ElementDescription: ../../vim/ElementDescription.rst

.. _vim.option.OptionType: ../../vim/option/OptionType.rst

.. _vim.ElementDescription: ../../vim/ElementDescription.rst


vim.option.OptionDef
====================
  Describes a user-defined option. The name of each option is identified by the "key" property, inherited from the `ElementDescription`_ data object type. You can indicate the property's position in a hierarchy by using a dot-separated notation. The string preceding the first dot is the top of the hierarchy. The hierarchy descends to a new sublevel with each dot. For example, "Ethernet.NetworkConnection.Bridged".
:extends: vim.ElementDescription_

Attributes:
    optionType (`vim.option.OptionType`_):

       The option type which defines allowed values.
