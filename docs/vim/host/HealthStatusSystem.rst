.. _vim.Task: ../../vim/Task.rst

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.host.HealthStatusSystem.Runtime: ../../vim/host/HealthStatusSystem/Runtime.rst


vim.host.HealthStatusSystem
===========================
  This managed object manages the health state of the host.


:since: `VI API 2.5`_


Attributes
----------
    runtime (`vim.host.HealthStatusSystem.Runtime`_):
       


Methods
-------


RefreshHealthStatusSystem():
   Refresh the available runtime hardware health information.


  Privilege:
               System.Read



  Args:


  Returns:
    None
         


ResetSystemHealthInfo():
   Resets the state of the sensors of the IPMI subsystem. On certain types of hardware IPMI sensor states latch onto unhealthy states and will stay in an unhealth state until the sensor state is reset. This method will explicitly reset the sensors state.


  Privilege:
               Host.Config.Settings



  Args:


  Returns:
    None
         


