.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.VimFault: ../../vim/fault/VimFault.rst


vim.fault.PatchNotApplicable
============================
    :extends:

        `vim.fault.VimFault`_

  This fault is thrown if a patch install fails because the patch is not applicable to the host. Typically, a subclass of this exception is thrown, indicating a problem such as the patch is superseded, already installed, or has dependencies missing, and so on.

Attributes:

    patchID (`str`_)




