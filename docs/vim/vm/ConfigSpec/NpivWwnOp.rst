.. _vim.vm.ConfigSpec: ../../../vim/vm/ConfigSpec.rst

.. _vim.vm.ConfigSpec.NpivWwnOp: ../../../vim/vm/ConfigSpec/NpivWwnOp.rst

vim.vm.ConfigSpec.NpivWwnOp
===========================
  The root WWN operation mode.
  :contained by: `vim.vm.ConfigSpec`_

  :type: `vim.vm.ConfigSpec.NpivWwnOp`_

  :name: extend

values:
--------

extend
   Generate a new set of WWNs and append them to the existing list

set
   Take a client-specified set of WWNs (specified in "wwn" property) and assign them to the virtual machine. If the new WWN quntity are more than existing then we will append them to the existing list of WWNs.

generate
   Generate a new set of WWNs and assign it to the virtual machine.

remove
   Remove the currently assigned WWNs from the virtual machine.
