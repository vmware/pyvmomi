.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _rateUnits: ../../vim/host/NumericSensorInfo.rst#rateUnits

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _HostNumericSensorType: ../../vim/host/NumericSensorInfo/SensorType.rst

.. _vim.ElementDescription: ../../vim/ElementDescription.rst

.. _HostNumericSensorHealthState: ../../vim/host/NumericSensorInfo/HealthState.rst


vim.host.NumericSensorInfo
==========================
  Base class for numeric sensor information.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    name (`str`_):

       The name of the physical element associated with the sensor
    healthState (`vim.ElementDescription`_, optional):

       The health state of the of the element indicated by the sensor. This property is populated only for sensors that support threshold settings.See `HostNumericSensorHealthState`_ 
    currentReading (`long`_):

       The current reading of the element indicated by the sensor. The actual sensor reading is obtained by multiplying the current reading by the scale factor.
    unitModifier (`int`_):

       The unit multiplier for the values returned by the sensor. All values returned by the sensor are current reading * 10 raised to the power of the UnitModifier.
    baseUnits (`str`_):

       The base units in which the sensor reading is specified. If rateUnits is set the units of the current reading is further qualified by the rateUnits.See `rateUnits`_ 
    rateUnits (`str`_, optional):

       The rate units in which the sensor reading is specified. For example if the baseUnits is Volts and the rateUnits is per second the value returned by the sensor are in Volts/second.
    sensorType (`str`_):

       The type of the sensor. If the sensor type is set to Other the sensor name can be used to further identify the type of sensor. The sensor units can also be used to further implicitly determine the type of the sensor.See `HostNumericSensorType`_ 
