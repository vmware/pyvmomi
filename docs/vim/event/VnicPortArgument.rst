.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.dvs.PortConnection: ../../vim/dvs/PortConnection.rst


vim.event.VnicPortArgument
==========================
  This argument records a Virtual NIC device that connects to a DVPort.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    vnic (`str`_):

       The Virtual NIC devices that were using the DVports.
    port (`vim.dvs.PortConnection`_):

       The DVPorts that were being used.
