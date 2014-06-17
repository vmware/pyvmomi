.. _vim.host.NumericSensorInfo: ../../../vim/host/NumericSensorInfo.rst

.. _vim.host.NumericSensorInfo.HealthState: ../../../vim/host/NumericSensorInfo/HealthState.rst

vim.host.NumericSensorInfo.HealthState
======================================
  Health state of the numeric sensor as reported by the sensor probes.
  :contained by: `vim.host.NumericSensorInfo`_

  :type: `vim.host.NumericSensorInfo.HealthState`_

  :name: red

values:
--------

unknown
   The implementation cannot report on the current health state of the physical element

green
   The sensor is operating under normal conditions

red
   The sensor is operating under critical or fatal conditions. This may directly affect the functioning of both the sensor and related components.

yellow
   The sensor is operating under conditions that are non-critical.
