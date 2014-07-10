.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.VimFault: ../../vim/fault/VimFault.rst


vim.fault.PatchMetadataInvalid
==============================
    :extends:

        `vim.fault.VimFault`_

  This fault is thrown if a patch query or installation operation fails because of a problem with the metadata associated with the patch. Typically, a subclass of this exception is thrown, indicating a problem such as the metadata is not found or the metadata is corrupted.

Attributes:

    patchID (`str`_)

    metaData (`str`_): is optional.




