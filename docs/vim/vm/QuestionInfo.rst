.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.vm.Message: ../../vim/vm/Message.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.option.ChoiceOption: ../../vim/option/ChoiceOption.rst


vim.vm.QuestionInfo
===================
  This data object type describes the question that is currently blocking a virtual machine.
:extends: vmodl.DynamicData_

Attributes:
    id (`str`_):

       Identifier with an opaque value that specifies the pending question.
    text (`str`_):

       Text that describes the pending question.
    choice (`vim.option.ChoiceOption`_):

       List of key-value pairs that specify possible answers.
    message (`vim.vm.Message`_, optional):

       The message data for the individual messages that comprise the question. Only available on servers that support localization.
