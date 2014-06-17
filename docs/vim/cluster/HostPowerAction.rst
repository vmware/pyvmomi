.. _int: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.cluster.Action: ../../vim/cluster/Action.rst

.. _vim.cluster.HostPowerAction.OperationType: ../../vim/cluster/HostPowerAction/OperationType.rst


vim.cluster.HostPowerAction
===========================
  Describes a single host power action.
:extends: vim.cluster.Action_
:since: `VI API 2.5`_

Attributes:
    operationType (`vim.cluster.HostPowerAction.OperationType`_):

       Specify whether the action is power on or power off
    powerConsumptionWatt (`int`_, optional):

       Estimated power consumption of the host. In case of power-on, this is the projected increase in the cluster's power consumption. In case of power off, this is the projected decrease in the cluster's power consumption
    cpuCapacityMHz (`int`_, optional):

       CPU capacity of the host in units of MHz. In case of power-on action, this is the projected increase in the cluster's CPU capacity. In case of power off, this is the projected decrease in the cluster's CPU capacity.
    memCapacityMB (`int`_, optional):

       Memory capacity of the host in units of MM. In case of power-on action, this is the projected increase in the cluster's memory capacity. In case of power off, this is the projected decrease in the cluster's memory capacity.
