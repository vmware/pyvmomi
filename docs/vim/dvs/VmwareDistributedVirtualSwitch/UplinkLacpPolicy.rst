
vim.dvs.VmwareDistributedVirtualSwitch.UplinkLacpPolicy
=======================================================
  This class defines VMware specific Link Aggregation Control Protocol policy.
:extends: vim.InheritablePolicy_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_
**deprecated**


Attributes:
    enable (`vim.BoolPolicy <vim/BoolPolicy.rst>`_, optional):

       The flag to indicate whether or not Link Aggregation Control Protocol is enabled. It can be set to true if the value of `lacpApiVersion <vim/dvs/VmwareDistributedVirtualSwitch/ConfigInfo.rst#lacpApiVersion>`_ is LacpApiVersion#singleLag, else an exception ConflictingConfiguration will be thrown.
    mode (`vim.StringPolicy <vim/StringPolicy.rst>`_, optional):

       The mode of Link Aggregation Control Protocol. See UplinkLacpMode for valid values.
