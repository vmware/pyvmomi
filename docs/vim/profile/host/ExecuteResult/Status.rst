.. _error: ../../../../vim/profile/host/ExecuteResult.rst#error

.. _policy: ../../../../vim/profile/ApplyProfile.rst#policy

.. _HostProfile: ../../../../vim/profile/host/HostProfile.rst

.. _ApplyProfile: ../../../../vim/profile/ApplyProfile.rst

.. _ExecuteHostProfile: ../../../../vim/profile/host/HostProfile.rst#execute

.. _ProfileExecuteResult: ../../../../vim/profile/host/ExecuteResult.rst

.. _vim.profile.host.ExecuteResult: ../../../../vim/profile/host/ExecuteResult.rst

.. _vim.profile.host.ExecuteResult.Status: ../../../../vim/profile/host/ExecuteResult/Status.rst

vim.profile.host.ExecuteResult.Status
=====================================
  Defines the result status values for a `HostProfile`_ . `ExecuteHostProfile`_ operation. The result data is contained in the `ProfileExecuteResult`_ data object.
  :contained by: `vim.profile.host.ExecuteResult`_

  :type: `vim.profile.host.ExecuteResult.Status`_

  :name: error

values:
--------

needInput
   Additional data is required to complete the operation. The data requirements are defined in the list of policy options for the profile ( `ApplyProfile`_ . `policy`_ []).

success
   Profile execution was successful. You can use the output configuration data to apply the profile to a host.

error
   Profile execution generated an error. See `ProfileExecuteResult`_ . `error`_ .
