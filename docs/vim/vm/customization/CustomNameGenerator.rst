.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.vm.customization.NameGenerator: ../../../vim/vm/customization/NameGenerator.rst


vim.vm.customization.CustomNameGenerator
========================================
  Specifies that the VirtualCenter server will launch an external application to generate the (hostname/IP). The command line for this application must be specified in the server configuration file (vpxd.cfg) in the vpxd/name-ip-generator key.
:extends: vim.vm.customization.NameGenerator_

Attributes:
    argument (`str`_, optional):

       An optional argument that is passed to the utility for this IP address. The meaning of this field is user-defined in the script.
