
vim.Datacenter.ConfigInfo
=========================
  Configuration of the datacenter.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    defaultHardwareVersionKey (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Key for Default Hardware Version used on this datacenter in the format of `key <vim/vm/ConfigOptionDescriptor.rst#key>`_ . This field affects `defaultConfigOption <vim/vm/ConfigOptionDescriptor.rst#defaultConfigOption>`_ returned by `environmentBrowser <vim/ComputeResource.rst#environmentBrowser>`_ of all its children with this field unset.
