.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.PatchNotApplicable: ../../vim/fault/PatchNotApplicable.rst


vim.fault.PatchMissingDependencies
==================================
    :extends:

        `vim.fault.PatchNotApplicable`_

  This fault is thrown if a patch install fails because the patch requires other patches or libraries that are not installed on the host.

Attributes:

    prerequisitePatch (`str`_): is optional.

    prerequisiteLib (`str`_): is optional.




