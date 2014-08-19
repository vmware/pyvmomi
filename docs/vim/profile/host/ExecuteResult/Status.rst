vim.profile.host.ExecuteResult.Status
=====================================
  Defines the result status values for a `HostProfile <vim/profile/host/HostProfile.rst>`_ . `ExecuteHostProfile <vim/profile/host/HostProfile.rst#execute>`_ operation. The result data is contained in the `ProfileExecuteResult <vim/profile/host/ExecuteResult.rst>`_ data object.
  :contained by: `vim.profile.host.ExecuteResult <vim/profile/host/ExecuteResult.rst>`_

  :type: `vim.profile.host.ExecuteResult.Status <vim/profile/host/ExecuteResult/Status.rst>`_

  :name: error

values:
--------

needInput
   Additional data is required to complete the operation. The data requirements are defined in the list of policy options for the profile ( `ApplyProfile <vim/profile/ApplyProfile.rst>`_ . `policy <vim/profile/ApplyProfile.rst#policy>`_ []).

success
   Profile execution was successful. You can use the output configuration data to apply the profile to a host.

error
   Profile execution generated an error. See `ProfileExecuteResult <vim/profile/host/ExecuteResult.rst>`_ . `error <vim/profile/host/ExecuteResult.rst#error>`_ .
