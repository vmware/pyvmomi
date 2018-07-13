.. _str: https://docs.python.org/2/library/stdtypes.html

.. _Task: ../../vim/Task.rst

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _PatchInstallFailed: ../../vim/fault/PatchInstallFailed.rst

.. _vim.fault.NoDiskSpace: ../../vim/fault/NoDiskSpace.rst

.. _vim.fault.InvalidState: ../../vim/fault/InvalidState.rst

.. _vim.fault.TaskInProgress: ../../vim/fault/TaskInProgress.rst

.. _vim.fault.RebootRequired: ../../vim/fault/RebootRequired.rst

.. _vmodl.fault.RequestCanceled: ../../vmodl/fault/RequestCanceled.rst

.. _vim.host.PatchManager.Result: ../../vim/host/PatchManager/Result.rst

.. _vim.fault.PatchNotApplicable: ../../vim/fault/PatchNotApplicable.rst

.. _vim.host.PatchManager.Status: ../../vim/host/PatchManager/Status.rst

.. _vim.fault.PatchInstallFailed: ../../vim/fault/PatchInstallFailed.rst

.. _vim.fault.PlatformConfigFault: ../../vim/fault/PlatformConfigFault.rst

.. _vim.host.PatchManager.Locator: ../../vim/host/PatchManager/Locator.rst

.. _vim.fault.PatchMetadataInvalid: ../../vim/fault/PatchMetadataInvalid.rst

.. _vim.fault.PatchBinariesNotFound: ../../vim/fault/PatchBinariesNotFound.rst

.. _vim.host.PatchManager.PatchManagerOperationSpec: ../../vim/host/PatchManager/PatchManagerOperationSpec.rst


vim.host.PatchManager
=====================
  This managed object is the interface for scanning and patching an ESX server. VMware publishes updates through its external website. A patch update is synonymous with a bulletin. An update may contain many individual patch binaries, but its installation and uninstallation are atomic.




Attributes
----------


Methods
-------


CheckHostPatch(metaUrls, bundleUrls, spec):
   Check the list of metadata and returns the dependency, obsolete and conflict information The operation is cancelable through the returned `Task`_ object. No integrity checks are performed on the metadata.
  since: `vSphere API 4.0`_


  Privilege:
               System.Read



  Args:
    metaUrls (`str`_, optional):
       a list of urls pointing to metadata.zip.


    bundleUrls (`str`_, optional):
       a list of urls pointing to an "offline" bundle. It is not supported in 5.0 or later.


    spec (`vim.host.PatchManager.PatchManagerOperationSpec`_, optional):




  Returns:
     `vim.Task`_:


  Raises:

    `vmodl.fault.RequestCanceled`_:
       if the operation is canceled.

    `vim.fault.InvalidState`_:
       If the feature cannot be supported on the platform, potentially because the hardware configuration does not support it.

    `vim.fault.TaskInProgress`_:
       if there is already a patch installation in progress.

    `vim.fault.PlatformConfigFault`_:
       if any error occurs during the operation. More detailed information will be returned within the payload of the exception as xml string.


ScanHostPatch(repository, updateID):
   Scan the host for the patch status. The operation is cancelable through the returned `Task`_ object. Integrity checks are performed on the metadata only during the scan operation.


  Privilege:
               System.Read



  Args:
    repository (`vim.host.PatchManager.Locator`_):
       Location of the repository that contains the bulletin depot. The depot must be organized as a flat collection of bulletins with each one being a folder named after the bulletin ID. Each folder must contain the full update metadata.


    updateID (`str`_, optional):
       The updates to scan. Wildcards can be used to specify the update IDs. The wildcards will be expanded to include all updates whose IDs match the specified wildcard and whose metadata is available in the repository. Specifying no update is equivalent to a wildcard "*". In this case all updates available in the repository will be scanned.




  Returns:
     `vim.Task`_:


  Raises:

    `vmodl.fault.RequestCanceled`_:
       if the operation is canceled.

    `vim.fault.PatchMetadataInvalid`_:
       if query required metadata is invalid--for example, it is not found in the repository, is corrupted and so on. Typically a more specific subclass of PatchMetadataInvalid is thrown.

    `vim.fault.PlatformConfigFault`_:
       if there is any error in the repository access, metadata download, repository level integrity check, or reading the metadata. See `text`_ for specific details.


ScanHostPatchV2(metaUrls, bundleUrls, spec):
   Scan the host for the patch status. The operation is cancelable through the returned `Task`_ object. Integrity checks are performed on the metadata only during the scan operation.
  since: `vSphere API 4.0`_


  Privilege:
               System.Read



  Args:
    metaUrls (`str`_, optional):
       a list of urls pointing to metadata.zip.


    bundleUrls (`str`_, optional):
       a list of urls pointing to an "offline" bundle. It is not supported in 5.0 or later.


    spec (`vim.host.PatchManager.PatchManagerOperationSpec`_, optional):




  Returns:
     `vim.Task`_:


  Raises:

    `vmodl.fault.RequestCanceled`_:
       if the operation is canceled.

    `vim.fault.InvalidState`_:
       If the feature cannot be supported on the platform, potentially because the hardware configuration does not support it.

    `vim.fault.TaskInProgress`_:
       if there is already a patch installation in progress.

    `vim.fault.PlatformConfigFault`_:
       if there is any error in the repository access, metadata download, repository level integrity check, or reading the metadata. See `text`_ for specific details.


StageHostPatch(metaUrls, bundleUrls, vibUrls, spec):
   Stage the vib files to esx local location and possibly do some run time check.
  since: `vSphere API 4.0`_


  Privilege:
               Host.Config.Patch



  Args:
    metaUrls (`str`_, optional):
       A list of urls pointing to metadata.zip.


    bundleUrls (`str`_, optional):
       a list of urls pointing to an "offline" bundle. It is not supported in 5.0 or later.


    vibUrls (`str`_, optional):
       The urls of update binary files to be staged.


    spec (`vim.host.PatchManager.PatchManagerOperationSpec`_, optional):




  Returns:
     `vim.Task`_:


  Raises:

    `vmodl.fault.RequestCanceled`_:
       if the operation is canceled.

    `vim.fault.InvalidState`_:
       If the feature cannot be supported on the platform, potentially because the hardware configuration does not support it.

    `vim.fault.TaskInProgress`_:
       if there is already a patch installation in progress.

    `vim.fault.PlatformConfigFault`_:
       if any error occurs during the operation. More detailed information will be returned within the payload of the exception as xml string.


InstallHostPatch(repository, updateID, force):
   Patch the host. The operation is not cancelable. If the patch installation failed, an atomic rollback of the installation will be attempted. Manual rollback is required if the atomic rollback failed, see `PatchInstallFailed`_ for details.


  Privilege:
               Host.Config.Patch



  Args:
    repository (`vim.host.PatchManager.Locator`_):
       Location of the repository that contains the bulletin depot. The depot must be organized as a flat collection of bulletins with each one being a folder named after the bulletin ID. Each folder must contain both update metadata and required binaries.


    updateID (`str`_):
       The update to be installed on the host.


    force (`bool`_, optional):
       Specify whether to force reinstall an update. By default, installing an already-installed update would fail with the `PatchAlreadyInstalled`_ fault. If force is set to true, the update will be forcefully reinstalled, thus overwriting the already installed update.




  Returns:
     `vim.Task`_:


  Raises:

    `vim.fault.PatchMetadataInvalid`_:
       if the required metadata is invalid--for example, it is not found in the repository, is corrupted and so on. Typically a more specific subclass of PatchMetadataInvalid is thrown.

    `vim.fault.PatchBinariesNotFound`_:
       if required update related binaries were not available.

    `vim.fault.PatchNotApplicable`_:
       if the patch is not applicable. Typically a more specific subclass of PatchNotApplicable is thrown to indicate a specific problem--for example, PatchSuperseded if the patch is superseded, MissingDependency if required patch or libraries are not installed, AlreadyInstalled if the patch is already installed.

    `vim.fault.NoDiskSpace`_:
       if the update can not be installed because there is insufficient disk space for the installation, including temporary space used for rollback.

    `vim.fault.PatchInstallFailed`_:
       if the installation failed, `text`_ has details of the failure. Automatic rollback might have succeeded or failed.

    `vim.fault.RebootRequired`_:
       if the update cannot be installed without restarting the host. This might occur on account of a prior update installation which needed to be installed separately from other updates.

    `vim.fault.InvalidState`_:
       if the host is not in maintenance mode but the patch install requires all virtual machines to be powered off.

    `vim.fault.TaskInProgress`_:
       if there is already a patch installation in progress.


InstallHostPatchV2(metaUrls, bundleUrls, vibUrls, spec):
   Patch the host. The operation is not cancelable. If the patch installation failed, an atomic rollback of the installation will be attempted. Manual rollback is required if the atomic rollback failed, see `PatchInstallFailed`_ for details.
  since: `vSphere API 4.0`_


  Privilege:
               Host.Config.Patch



  Args:
    metaUrls (`str`_, optional):
       A list of urls pointing to metadata.zip.


    bundleUrls (`str`_, optional):
       a list of urls pointing to an "offline" bundle. It is not supported in 5.0 or later.


    vibUrls (`str`_, optional):
       The urls of update binary files to be installed.


    spec (`vim.host.PatchManager.PatchManagerOperationSpec`_, optional):




  Returns:
     `vim.Task`_:


  Raises:

    `vmodl.fault.RequestCanceled`_:
       Thrown if the operation is canceled.

    `vim.fault.InvalidState`_:
       If the feature cannot be supported on the platform, potentially because the hardware configuration does not support it.

    `vim.fault.TaskInProgress`_:
       if there is already a patch installation in progress.

    `vim.fault.PlatformConfigFault`_:
       vim.fault.PlatformConfigFault


UninstallHostPatch(bulletinIds, spec):
   Uninstall patch from the host. The operation is not cancelable.
  since: `vSphere API 4.0`_


  Privilege:
               Host.Config.Patch



  Args:
    bulletinIds (`str`_, optional):
       A list of bulletin IDs to be removed.


    spec (`vim.host.PatchManager.PatchManagerOperationSpec`_, optional):




  Returns:
     `vim.Task`_:


  Raises:

    `vim.fault.InvalidState`_:
       If the feature cannot be supported on the platform, potentially because the hardware configuration does not support it.

    `vim.fault.TaskInProgress`_:
       if there is already a patch installation in progress.

    `vim.fault.PlatformConfigFault`_:
       vim.fault.PlatformConfigFault


QueryHostPatch(spec):
   Query the host for installed bulletins.
  since: `vSphere API 4.0`_


  Privilege:
               System.Read



  Args:
    spec (`vim.host.PatchManager.PatchManagerOperationSpec`_, optional):




  Returns:
     `vim.Task`_:


  Raises:

    `vmodl.fault.RequestCanceled`_:
       vmodl.fault.RequestCanceled

    `vim.fault.InvalidState`_:
       If the bulletin ID did not exist.

    `vim.fault.TaskInProgress`_:
       if there is already a patch installation in progress.

    `vim.fault.PlatformConfigFault`_:
       vim.fault.PlatformConfigFault
