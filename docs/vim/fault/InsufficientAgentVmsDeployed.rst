
vim.fault.InsufficientAgentVmsDeployed
======================================
    :extends:

        `vim.fault.InsufficientResourcesFault <vim/fault/InsufficientResourcesFault.rst>`_

  This fault is returned when the required number of deployed agent virtual machines is not currently deployed on a host and hence the host cannot be used to run client virtual machines.

Attributes:

    hostName (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    requiredNumAgentVms (`int <https://docs.python.org/2/library/stdtypes.html>`_)

    currentNumAgentVms (`int <https://docs.python.org/2/library/stdtypes.html>`_)




