
vim.fault.PatchMissingDependencies
==================================
    :extends:

        `vim.fault.PatchNotApplicable <vim/fault/PatchNotApplicable.rst>`_

  This fault is thrown if a patch install fails because the patch requires other patches or libraries that are not installed on the host.

Attributes:

    prerequisitePatch (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.

    prerequisiteLib (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.




