vim.option.ArrayUpdateSpec.Operation
====================================
  This list specifies the type of operation being performed on the array.
  :contained by: `vim.option.ArrayUpdateSpec <vim/option/ArrayUpdateSpec.rst>`_

  :type: `vim.option.ArrayUpdateSpec.Operation <vim/option/ArrayUpdateSpec/Operation.rst>`_

  :name: edit

values:
--------

edit
   indicates changes to an element in the array.

add
   indicates an addition to the array.

remove
   indicates the removal of an element in the array. In this case the key field must contain the key of the element to be removed.
