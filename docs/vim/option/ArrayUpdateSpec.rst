
vim.option.ArrayUpdateSpec
==========================
  An ArrayUpdateSpec data object type is a common superclass for supporting incremental updates to arrays.The common code pattern is:class MyTypeSpec extrends ArrayUpdateSpec { MyTypeInfo info; }The ArrayUpdateSpec contains the following:
   * operation
   * : the type of operation being performed.
   * removeKey
   * : In the case of a remove operation, the key value that identifies the array to be removed.
   * 
:extends: vmodl.DynamicData_

Attributes:
    operation (`vim.option.ArrayUpdateSpec.Operation <vim/option/ArrayUpdateSpec/Operation.rst>`_):

       The type of operation being performed on the specified virtual device.
    removeKey (`object <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Key for the element to be removed. Only used if the operation is "remove".
