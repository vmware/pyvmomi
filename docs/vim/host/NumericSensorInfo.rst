
vim.host.NumericSensorInfo
==========================
  Base class for numeric sensor information.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the physical element associated with the sensor
    healthState (`vim.ElementDescription <vim/ElementDescription.rst>`_, optional):

       The health state of the of the element indicated by the sensor. This property is populated only for sensors that support threshold settings.See `HostNumericSensorHealthState <vim/host/NumericSensorInfo/HealthState.rst>`_ 
    currentReading (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The current reading of the element indicated by the sensor. The actual sensor reading is obtained by multiplying the current reading by the scale factor.
    unitModifier (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The unit multiplier for the values returned by the sensor. All values returned by the sensor are current reading * 10 raised to the power of the UnitModifier.
    baseUnits (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The base units in which the sensor reading is specified. If rateUnits is set the units of the current reading is further qualified by the rateUnits.See `rateUnits <vim/host/NumericSensorInfo.rst#rateUnits>`_ 
    rateUnits (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The rate units in which the sensor reading is specified. For example if the baseUnits is Volts and the rateUnits is per second the value returned by the sensor are in Volts/second.
    sensorType (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The type of the sensor. If the sensor type is set to Other the sensor name can be used to further identify the type of sensor. The sensor units can also be used to further implicitly determine the type of the sensor.See `HostNumericSensorType <vim/host/NumericSensorInfo/SensorType.rst>`_ 
