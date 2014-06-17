.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.InsufficientResourcesFault: ../../vim/fault/InsufficientResourcesFault.rst


vim.fault.InsufficientAgentVmsDeployed
======================================
    :extends:

        `vim.fault.InsufficientResourcesFault`_

  This fault is returned when the required number of deployed agent virtual machines is not currently deployed on a host and hence the host cannot be used to run client virtual machines.

Attributes:

    hostName (`str`_)

    requiredNumAgentVms (`int`_)

    currentNumAgentVms (`int`_)




