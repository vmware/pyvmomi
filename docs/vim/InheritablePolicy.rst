
vim.InheritablePolicy
=====================
  The base class for any type of setting or configuration that may get a inherited value.When used in a reconfgure operation specification, if `inherited <vim/InheritablePolicy.rst#inherited>`_ is true, it specifies the intention to change the values of subclass's properties to the inhertied values from the level above. In this case, users don't need to specify the values and any set property in the subclass will be ignored. if `inherited <vim/InheritablePolicy.rst#inherited>`_ is false, it specifies the intension to explicitly set subclass's properties to user specified values. Users should set the properties in the subclass with the desired values.When used in a configuration information object, The values of the properties in the subclass are the effective values. if `inherited <vim/InheritablePolicy.rst#inherited>`_ is true, the object is getting the effective values from upper level. If false, the values are explicitly set by a user.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    inherited (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether the configuration is set to inherited value.
