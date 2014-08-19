
vim.host.PatchManager
=====================
  This managed object is the interface for scanning and patching an ESX server. VMware publishes updates through its external website. A patch update is synonymous with a bulletin. An update may contain many individual patch binaries, but its installation and uninstallation are atomic.




Attributes
----------


Methods
-------


CheckHostPatch(metaUrls, bundleUrls, spec):
   Check the list of metadata and returns the dependency, obsolete and conflict information The operation is cancelable through the returned `Task <vim/Task.rst>`_ object. No integrity checks are performed on the metadata.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               System.Read



  Args:
    metaUrls (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       a list of urls pointing to metadata.zip.


    bundleUrls (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       a list of urls pointing to an "offline" bundle. It is not supported in 5.0 or later.


    spec (`vim.host.PatchManager.PatchManagerOperationSpec <vim/host/PatchManager/PatchManagerOperationSpec.rst>`_, optional):




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vmodl.fault.RequestCanceled <vmodl/fault/RequestCanceled.rst>`_: 
       if the operation is canceled.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       If the feature cannot be supported on the platform, potentially because the hardware configuration does not support it.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if there is already a patch installation in progress.

    `vim.fault.PlatformConfigFault <vim/fault/PlatformConfigFault.rst>`_: 
       if any error occurs during the operation. More detailed information will be returned within the payload of the exception as xml string.


ScanHostPatch(repository, updateID):
   Scan the host for the patch status. The operation is cancelable through the returned `Task <vim/Task.rst>`_ object. Integrity checks are performed on the metadata only during the scan operation.


  Privilege:
               System.Read



  Args:
    repository (`vim.host.PatchManager.Locator <vim/host/PatchManager/Locator.rst>`_):
       Location of the repository that contains the bulletin depot. The depot must be organized as a flat collection of bulletins with each one being a folder named after the bulletin ID. Each folder must contain the full update metadata.


    updateID (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       The updates to scan. Wildcards can be used to specify the update IDs. The wildcards will be expanded to include all updates whose IDs match the specified wildcard and whose metadata is available in the repository. Specifying no update is equivalent to a wildcard "*". In this case all updates available in the repository will be scanned.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vmodl.fault.RequestCanceled <vmodl/fault/RequestCanceled.rst>`_: 
       if the operation is canceled.

    `vim.fault.PatchMetadataInvalid <vim/fault/PatchMetadataInvalid.rst>`_: 
       if query required metadata is invalid--for example, it is not found in the repository, is corrupted and so on. Typically a more specific subclass of PatchMetadataInvalid is thrown.

    `vim.fault.PlatformConfigFault <vim/fault/PlatformConfigFault.rst>`_: 
       if there is any error in the repository access, metadata download, repository level integrity check, or reading the metadata. See `text <vim/fault/PlatformConfigFault.rst#text>`_ for specific details.


ScanHostPatchV2(metaUrls, bundleUrls, spec):
   Scan the host for the patch status. The operation is cancelable through the returned `Task <vim/Task.rst>`_ object. Integrity checks are performed on the metadata only during the scan operation.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               System.Read



  Args:
    metaUrls (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       a list of urls pointing to metadata.zip.


    bundleUrls (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       a list of urls pointing to an "offline" bundle. It is not supported in 5.0 or later.


    spec (`vim.host.PatchManager.PatchManagerOperationSpec <vim/host/PatchManager/PatchManagerOperationSpec.rst>`_, optional):




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vmodl.fault.RequestCanceled <vmodl/fault/RequestCanceled.rst>`_: 
       if the operation is canceled.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       If the feature cannot be supported on the platform, potentially because the hardware configuration does not support it.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if there is already a patch installation in progress.

    `vim.fault.PlatformConfigFault <vim/fault/PlatformConfigFault.rst>`_: 
       if there is any error in the repository access, metadata download, repository level integrity check, or reading the metadata. See `text <vim/fault/PlatformConfigFault.rst#text>`_ for specific details.


StageHostPatch(metaUrls, bundleUrls, vibUrls, spec):
   Stage the vib files to esx local location and possibly do some run time check.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               Host.Config.Patch



  Args:
    metaUrls (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       A list of urls pointing to metadata.zip.


    bundleUrls (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       a list of urls pointing to an "offline" bundle. It is not supported in 5.0 or later.


    vibUrls (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       The urls of update binary files to be staged.


    spec (`vim.host.PatchManager.PatchManagerOperationSpec <vim/host/PatchManager/PatchManagerOperationSpec.rst>`_, optional):




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vmodl.fault.RequestCanceled <vmodl/fault/RequestCanceled.rst>`_: 
       if the operation is canceled.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       If the feature cannot be supported on the platform, potentially because the hardware configuration does not support it.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if there is already a patch installation in progress.

    `vim.fault.PlatformConfigFault <vim/fault/PlatformConfigFault.rst>`_: 
       if any error occurs during the operation. More detailed information will be returned within the payload of the exception as xml string.


InstallHostPatch(repository, updateID, force):
   Patch the host. The operation is not cancelable. If the patch installation failed, an atomic rollback of the installation will be attempted. Manual rollback is required if the atomic rollback failed, see `PatchInstallFailed <vim/fault/PatchInstallFailed.rst>`_ for details.


  Privilege:
               Host.Config.Patch



  Args:
    repository (`vim.host.PatchManager.Locator <vim/host/PatchManager/Locator.rst>`_):
       Location of the repository that contains the bulletin depot. The depot must be organized as a flat collection of bulletins with each one being a folder named after the bulletin ID. Each folder must contain both update metadata and required binaries.


    updateID (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The update to be installed on the host.


    force (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       Specify whether to force reinstall an update. By default, installing an already-installed update would fail with the `PatchAlreadyInstalled <vim/fault/PatchAlreadyInstalled.rst>`_ fault. If force is set to true, the update will be forcifully reinstalled, thus overwriting the already installed update.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.PatchMetadataInvalid <vim/fault/PatchMetadataInvalid.rst>`_: 
       if the requried metadata is invalid--for example, it is not found in the repository, is corrupted and so on. Typically a more specific subclass of PatchMetadataInvalid is thrown.

    `vim.fault.PatchBinariesNotFound <vim/fault/PatchBinariesNotFound.rst>`_: 
       if required update related binaries were not available.

    `vim.fault.PatchNotApplicable <vim/fault/PatchNotApplicable.rst>`_: 
       if the patch is not applicable. Typically a more specific subclass of PatchNotApplicable is thrown to indicate a specific problem--for example, PatchSuperseded if the patch is superseded, MissingDependency if required patch or libraries are not installed, AlreadyInstalled if the patch is already installed.

    `vim.fault.NoDiskSpace <vim/fault/NoDiskSpace.rst>`_: 
       if the update can not be installed because there is insufficent disk space for the installation, including temporary space used for rollback.

    `vim.fault.PatchInstallFailed <vim/fault/PatchInstallFailed.rst>`_: 
       if the installation failed, `text <vim/fault/PlatformConfigFault.rst#text>`_ has details of the failure. Automatic rollback might have succeeded or failed.

    `vim.fault.RebootRequired <vim/fault/RebootRequired.rst>`_: 
       if the update cannot be installed without restarting the host. This might occur on account of a prior update installation which needed to be installed separately from other updates.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the host is not in maintenance mode but the patch install requires all virtual machines to be powered off.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if there is already a patch installation in progress.


InstallHostPatchV2(metaUrls, bundleUrls, vibUrls, spec):
   Patch the host. The operation is not cancelable. If the patch installation failed, an atomic rollback of the installation will be attempted. Manual rollback is required if the atomic rollback failed, see `PatchInstallFailed <vim/fault/PatchInstallFailed.rst>`_ for details.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               Host.Config.Patch



  Args:
    metaUrls (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       A list of urls pointing to metadata.zip.


    bundleUrls (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       a list of urls pointing to an "offline" bundle. It is not supported in 5.0 or later.


    vibUrls (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       The urls of update binary files to be installed.


    spec (`vim.host.PatchManager.PatchManagerOperationSpec <vim/host/PatchManager/PatchManagerOperationSpec.rst>`_, optional):




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vmodl.fault.RequestCanceled <vmodl/fault/RequestCanceled.rst>`_: 
       Thrown if the operation is canceled.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       If the feature cannot be supported on the platform, potentially because the hardware configuration does not support it.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if there is already a patch installation in progress.

    `vim.fault.PlatformConfigFault <vim/fault/PlatformConfigFault.rst>`_: 
       vim.fault.PlatformConfigFault


UninstallHostPatch(bulletinIds, spec):
   Uninstall patch from the host. The operation is not cancelable.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               Host.Config.Patch



  Args:
    bulletinIds (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       A list of bulletin IDs to be removed.


    spec (`vim.host.PatchManager.PatchManagerOperationSpec <vim/host/PatchManager/PatchManagerOperationSpec.rst>`_, optional):




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       If the feature cannot be supported on the platform, potentially because the hardware configuration does not support it.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if there is already a patch installation in progress.

    `vim.fault.PlatformConfigFault <vim/fault/PlatformConfigFault.rst>`_: 
       vim.fault.PlatformConfigFault


QueryHostPatch(spec):
   Query the host for installed bulletins.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               System.Read



  Args:
    spec (`vim.host.PatchManager.PatchManagerOperationSpec <vim/host/PatchManager/PatchManagerOperationSpec.rst>`_, optional):




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vmodl.fault.RequestCanceled <vmodl/fault/RequestCanceled.rst>`_: 
       vmodl.fault.RequestCanceled

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       If the bulletin ID did not exist.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if there is already a patch installation in progress.

    `vim.fault.PlatformConfigFault <vim/fault/PlatformConfigFault.rst>`_: 
       vim.fault.PlatformConfigFault


