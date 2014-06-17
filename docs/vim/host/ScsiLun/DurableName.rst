.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.ScsiLun.DurableName
============================
  This data object type represents an SMI-S "Correlatable and Durable Name" which is an identifier for a logical unit number (LUN) that is generated using a common algorithm. The algorithm divides the identifier into multiple namespaces where each namespace uses a different set of properties of the LUN to generate the identifier. The namespace itself is encoded in the identifier.
:extends: vmodl.DynamicData_

Attributes:
    namespace (`str`_):

       The string describing the namespace used for the durable name.
    namespaceId (`int`_):

       The byte used by the ESX Server product to represent the namespace.
    data (`int`_, optional):

       The variable length byte array containing the namespace-specific data. For a SCSI-3 compliant device this field is the descriptor header along with the payload for data obtained from page 83h, and is the payload for data obtained from page 80h of the Vital Product Data (VPD).
