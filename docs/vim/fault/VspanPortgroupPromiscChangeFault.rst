.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.DvsFault: ../../vim/fault/DvsFault.rst


vim.fault.VspanPortgroupPromiscChangeFault
==========================================
    :extends:

        `vim.fault.DvsFault`_

  Thrown when changing a non-promiscous portgroup to promiscuous mode if any port in this portgroup is used as tranmistted source or dest ports in vspan session.

Attributes:

    portgroupName (`str`_)




