.. _vim.fault.AgentInstallFailed: ../../../vim/fault/AgentInstallFailed.rst

.. _vim.fault.AgentInstallFailed.Reason: ../../../vim/fault/AgentInstallFailed/Reason.rst

vim.fault.AgentInstallFailed.Reason
===================================
  :contained by: `vim.fault.AgentInstallFailed`_

  :type: `vim.fault.AgentInstallFailed.Reason`_

  :name: UnknownInstallerError

values:
--------

NotEnoughSpaceOnDevice
   There is not enough storage space on the host to install the agent.

AgentUploadFailed
   Failed to upload the agent installer.

AgentUploadTimedout
   The agent upload took too long.

AgentNotReachable
   The agent was installed but did not respond to requests.

SignatureVerificationFailed
   The signature verification for the installer failed.

PrepareToUpgradeFailed
   Failed to initialize the upgrade directory on the host.

InstallTimedout
   The agent install took too long.

AgentNotRunning
   The agent was installed but is not running.

UnknownInstallerError
   The agent installer failed for an unknown reason.
