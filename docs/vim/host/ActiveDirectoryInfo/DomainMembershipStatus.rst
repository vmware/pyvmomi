.. _vim.host.ActiveDirectoryInfo: ../../../vim/host/ActiveDirectoryInfo.rst

.. _vim.host.ActiveDirectoryInfo.DomainMembershipStatus: ../../../vim/host/ActiveDirectoryInfo/DomainMembershipStatus.rst

vim.host.ActiveDirectoryInfo.DomainMembershipStatus
===================================================
  :contained by: `vim.host.ActiveDirectoryInfo`_

  :type: `vim.host.ActiveDirectoryInfo.DomainMembershipStatus`_

  :name: otherProblem

values:
--------

ok
   No problems with the domain membership.

clientTrustBroken
   The client side of the trust relationship is broken.

unknown
   The Active Directory integration provider does not support domain trust checks.

otherProblem
   There's some problem with the domain membership.

noServers
   The host thinks it's part of a domain, but no domain controllers could be reached to confirm.

serverTrustBroken
   The server side of the trust relationship is broken (or bad machine password).

inconsistentTrust
   Unexpected domain controller responded.
