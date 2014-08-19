
vim.host.FileAccess.Modes
=========================
  The FileAccess.Modes data object type defines the known access modes for a datastore. The property values specify how to interpret the "what" property for a FileAccess object.
:extends: vmodl.DynamicData_

Attributes:
    browse (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Can see the existence of a file.
    read (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Can read a file.
    modify (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Can read and write a file.
    use (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Can execute or operate a file or look inside a directory.
    admin (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Can change permissions for a file.
    full (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Can do anything to a file, including change permissions.
