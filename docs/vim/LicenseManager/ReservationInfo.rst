.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.LicenseManager.ReservationInfo.State: ../../vim/LicenseManager/ReservationInfo/State.rst


vim.LicenseManager.ReservationInfo
==================================
  A reservation describes how many licenses of a particular feature are being used by a particular feature.
:extends: vmodl.DynamicData_

Attributes:
    key (`str`_):

       Key of the License Feature.See `key`_ 
    state (`vim.LicenseManager.ReservationInfo.State`_):

       Describes the reservation state of a license.
    required (`int`_):

       Contains the required number of licenses of the particular type that the product needs in its current configuration.Licenses are normally allocated at the same time as they are needed, so the value of required is set at the time the license is needed. For example, in the case of the number of licenses based on virtual machines, the required count is set at the time a virtual machine is powered on, just before the license is checked out.
