.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.AutoStartManager.SystemDefaults
========================================
  Defines the system default auto-start/auto-stop values.
:extends: vmodl.DynamicData_

Attributes:
    enabled (`bool`_, optional):

       Indicates whether or not auto-start manager is enabled.
    startDelay (`int`_, optional):

       System-default autoStart delay in seconds. The default is 120 seconds.
    stopDelay (`int`_, optional):

       System-default autoStop delay in seconds. The default is 120 seconds.
    waitForHeartbeat (`bool`_, optional):

       System-default waitForHeartbeat setting.
    stopAction (`str`_, optional):

       System-default power-off action. Used if the stopAction string in the AutoPowerInfo object for a particular machine is set to systemDefault. If stopAction and startAction for a virtual machine are both set to none, that virtual machine is removed from the AutoStart sequence.
