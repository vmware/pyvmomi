.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vmodl.KeyAnyValue: ../../../vmodl/KeyAnyValue.rst


vim.host.PhysicalNic.LldpInfo
=============================
  The Link Layer Discovery Protocol information.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    chassisId (`str`_):

       ChassisId represents the chassis identification for the device that transmitted the LLDP frame. The receiving LLDP agent combines the Chassis ID and portId to represent the entity connected to the port where the frame was received.
    portId (`str`_):

       This property identifies the specific port that transmitted the LLDP frame. The receiving LLDP agent combines the Chassis ID and Port to represent the entity connected to the port where the frame was received.
    timeToLive (`int`_):

       It is the duration of time in seconds for which information contained in the received LLDP frame shall be valid. If a value of zero is sent it can also identify a device that has shut down or is no longer transmitting, prompting deletion of the record from the local database.
    parameter (`vmodl.KeyAnyValue`_, optional):

       LLDP parameters
