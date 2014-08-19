
vim.alarm.AlarmState
====================
  Information about the alarm's state.
:extends: vmodl.DynamicData_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Unique key that identifies the alarm.
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):

       Entity on which the alarm is instantiated.
    alarm (`vim.alarm.Alarm <vim/alarm/Alarm.rst>`_):

       Alarm object from which the AlarmState object is instantiated.
    overallStatus (`vim.ManagedEntity.Status <vim/ManagedEntity/Status.rst>`_):

       Overall status of the alarm object. This is the value of the alarm's top-level expression. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Since this property is on a DataObject, an update returned by WaitForUpdatesEx may contain values for this property when some other property on the DataObject changes. If this update is a result of a call to WaitForUpdatesEx with a non-empty version parameter, the value for this property may not be current.
    time (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):

       Time the alarm triggered.
    acknowledged (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate if the alarm's actions have been acknowledged for the associated ManagedEntity.
    acknowledgedByUser (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The user who acknowledged this triggering. If the triggering has not been acknowledged, then the value is not valid.
    acknowledgedTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The time this triggering was acknowledged. If the triggering has not been acknowledged, then the value is not valid.
