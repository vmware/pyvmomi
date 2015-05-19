.. _str: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../vmodl/DynamicData.rst


vim.CustomizationSpecInfo
=========================
  Information about a specification.
:extends: vmodl.DynamicData_

Attributes:
    name (`str`_):

       Unique name of the specification.
    description (`str`_):

       Description of the specification.
    type (`str`_):

       Guest operating system for this specification (Linux or Windows).
    changeVersion (`str`_, optional):

       The changeVersion is a unique identifier for a given version of the configuration. Each change to the configuration will update this value. This is typically implemented as an ever increasing count or a time-stamp. However, a client should always treat this as an opaque string.If specified when updating a specification, the changes will only be applied if the current changeVersion matches the specified changeVersion. This field can be used to guard against updates that has happened between the configInfo was read and until it is applied.
    lastUpdateTime (`datetime`_, optional):

       Time when the specification was last modified. This time is ignored when the CustomizationSpecItem containing this is used as an input to CustomizationSpecManager.create.
