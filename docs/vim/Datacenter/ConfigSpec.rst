
vim.Datacenter.ConfigSpec
=========================
  Changes to apply to the datacenter configuration.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    defaultHardwareVersionKey (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Key for Default Hardware Version to be used on this datacenter in the format of `key <vim/vm/ConfigOptionDescriptor.rst#key>`_ . Setting this field affects `defaultConfigOption <vim/vm/ConfigOptionDescriptor.rst#defaultConfigOption>`_ returned by `environmentBrowser <vim/ComputeResource.rst#environmentBrowser>`_ of all its children with this field unset.
