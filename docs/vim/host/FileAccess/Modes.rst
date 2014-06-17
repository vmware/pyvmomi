.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.FileAccess.Modes
=========================
  The FileAccess.Modes data object type defines the known access modes for a datastore. The property values specify how to interpret the "what" property for a FileAccess object.
:extends: vmodl.DynamicData_

Attributes:
    browse (`str`_, optional):

       Can see the existence of a file.
    read (`str`_):

       Can read a file.
    modify (`str`_):

       Can read and write a file.
    use (`str`_):

       Can execute or operate a file or look inside a directory.
    admin (`str`_, optional):

       Can change permissions for a file.
    full (`str`_):

       Can do anything to a file, including change permissions.
