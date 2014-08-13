.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../vmodl/DynamicData.rst

.. _vim.ElementDescription: ../vim/ElementDescription.rst


vim.EnumDescription
===================
  Static strings used for describing an enumerated type.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    key (`str`_):

       Type of enumeration being described.
    tags ([`vim.ElementDescription`_]):

       Element descriptions of all the tags for that enumerated type.
