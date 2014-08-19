
vim.host.PhysicalNic.LldpInfo
=============================
  The Link Layer Discovery Protocol information.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    chassisId (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       ChassisId represents the chassis identification for the device that transmitted the LLDP frame. The receiving LLDP agent combines the Chassis ID and portId to represent the entity connected to the port where the frame was received.
    portId (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       This property identifies the specific port that transmitted the LLDP frame. The receiving LLDP agent combines the Chassis ID and Port to represent the entity connected to the port where the frame was received.
    timeToLive (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       It is the duration of time in seconds for which information contained in the received LLDP frame shall be valid. If a value of zero is sent it can also identify a device that has shut down or is no longer transmitting, prompting deletion of the record from the local database.
    parameter ([`vmodl.KeyAnyValue <vmodl/KeyAnyValue.rst>`_], optional):

       LLDP parameters
