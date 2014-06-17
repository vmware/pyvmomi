.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vim.alarm.Alarm: ../../vim/alarm/Alarm.rst

.. _vim.ManagedEntity: ../../vim/ManagedEntity.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.ManagedEntity.Status: ../../vim/ManagedEntity/Status.rst


vim.alarm.AlarmState
====================
  Information about the alarm's state.
:extends: vmodl.DynamicData_

Attributes:
    key (`str`_):

       Unique key that identifies the alarm.
    entity (`vim.ManagedEntity`_):

       Entity on which the alarm is instantiated.
    alarm (`vim.alarm.Alarm`_):

       Alarm object from which the AlarmState object is instantiated.
    overallStatus (`vim.ManagedEntity.Status`_):

       Overall status of the alarm object. This is the value of the alarm's top-level expression. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Since this property is on a DataObject, an update returned by WaitForUpdatesEx may contain values for this property when some other property on the DataObject changes. If this update is a result of a call to WaitForUpdatesEx with a non-empty version parameter, the value for this property may not be current.
    time (`datetime`_):

       Time the alarm triggered.
    acknowledged (`bool`_, optional):

       Flag to indicate if the alarm's actions have been acknowledged for the associated ManagedEntity.
    acknowledgedByUser (`str`_, optional):

       The user who acknowledged this triggering. If the triggering has not been acknowledged, then the value is not valid.
    acknowledgedTime (`datetime`_, optional):

       The time this triggering was acknowledged. If the triggering has not been acknowledged, then the value is not valid.
