.. _str: https://docs.python.org/2/library/stdtypes.html

.. _edit: ../../../vim/ConfigSpecOperation.rst#edit

.. _remove: ../../../vim/ConfigSpecOperation.rst#remove

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _ConfigSpecOperation: ../../../vim/ConfigSpecOperation.rst

.. _vim.dvs.DistributedVirtualPort.TrafficFilterConfig: ../../../vim/dvs/DistributedVirtualPort/TrafficFilterConfig.rst


vim.dvs.DistributedVirtualPort.TrafficFilterConfigSpec
======================================================
  The specification to reconfigure Traffic Filter. This specification allows the user to do fine-grained updates for the Traffic Filter in the port settings. If the operation is `remove`_ , only the TrafficFilterConfigSpec#key needs to be specified. If other fields are specified, they will be ignored. We cannot remove an inherited element. Only when the inherited flag is set to false and parent does not have an element with same key this operation succeeds. If the operation is `add`_ , then TrafficFilterConfigSpec#key should not be specified and other fields need to be specified. The inherited flag should be set to false. If the operation is `edit`_ , then TrafficFilterConfigSpec#key needs be specified and specify the other properties that need modification. If the inherited flag is set to true, a TrafficFilterConfig object of same key must exist at the parent's level. The property values in the spec object will be ignored and use the values from the parent's TrafficFilterConfig object instead. If inherited flag is set to false, then the new modifications will be applied.
:extends: vim.dvs.DistributedVirtualPort.TrafficFilterConfig_
:since: `vSphere API 5.5`_

Attributes:
    operation (`str`_):

       Operation type. See `ConfigSpecOperation`_ for valid values.
