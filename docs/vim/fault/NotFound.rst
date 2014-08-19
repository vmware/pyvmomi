
vim.fault.NotFound
==================
    :extends:

        `vim.fault.VimFault <vim/fault/VimFault.rst>`_

  A NotFound error occurs when a referenced component of a managed object cannot be found. The referenced component can be a data object type (such as a role or permission) or a primitive (such as a string).For example, if the missing referenced component is a data object, such as VirtualSwitch, the NotFound error is thrown. The NotFound error is also thrown if the data object is found, but the referenced name (for example, "vswitch0") is not.

Attributes:




