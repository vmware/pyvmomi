
vim.dvs.DistributedVirtualPort.TrafficFilterConfigSpec
======================================================
  The specification to reconfigure Traffic Filter. This specification allows the user to do fine-grained updates for the Traffic Filter in the port settings. If the operation is `remove <vim/ConfigSpecOperation.rst#remove>`_ , only the TrafficFilterConfigSpec#key needs to be specified. If other fields are specified, they will be ignored. We cannot remove an inherited element. Only when the inherited flag is set to false and parent does not have an element with same key this operation succeeds. If the operation is `add <vim/ConfigSpecOperation.rst#add>`_ , then TrafficFilterConfigSpec#key should not be specified and other fields need to be specified. The inherited flag should be set to false. If the operation is `edit <vim/ConfigSpecOperation.rst#edit>`_ , then TrafficFilterConfigSpec#key needs be specified and specify the other properties that need modification. If the inherited flag is set to true, a TrafficFilterConfig object of same key must exist at the parent's level. The property values in the spec object will be ignored and use the values from the parent's TrafficFilterConfig object instead. If inherited flag is set to false, then the new modifications will be applied.
:extends: vim.dvs.DistributedVirtualPort.TrafficFilterConfig_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    operation (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Operation type. See `ConfigSpecOperation <vim/ConfigSpecOperation.rst>`_ for valid values.
