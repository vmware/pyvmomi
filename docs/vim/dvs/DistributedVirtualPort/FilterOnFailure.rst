.. _vim.dvs.DistributedVirtualPort: ../../../vim/dvs/DistributedVirtualPort.rst

.. _vim.dvs.DistributedVirtualPort.FilterOnFailure: ../../../vim/dvs/DistributedVirtualPort/FilterOnFailure.rst

vim.dvs.DistributedVirtualPort.FilterOnFailure
==============================================
  Network Filter on Failure Type. It specifies whether all the packets will be allowed or all the packets will be denied when Filter fails to configure.
  :contained by: `vim.dvs.DistributedVirtualPort`_

  :type: `vim.dvs.DistributedVirtualPort.FilterOnFailure`_

  :name: failClosed

values:
--------

failOpen
   Allows all the packets when the Filter fails to configure.

failClosed
   Denies all the packets when the Filter fails to configure.
