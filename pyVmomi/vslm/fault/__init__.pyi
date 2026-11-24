# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.vmodl
import pyVmomi.vim.vslm



class VslmFault(pyVmomi.vmodl.MethodFault):
   """
   The super class for all VSLM Faults.
   
   Attributes:
       msg: The fault message if available.
   """
   msg: _typing.Optional[str] = None


class SyncFault(VslmFault):
   """
   An SyncFault fault is thrown when there is a failure to synchronize
   the FCD global catalog information with the local catalog information.
   
   Pandora synchronizes the datastore periodically in the background, it
   recovers from any transient failures affecting the datastore or
   individual FCDs. In cases where the sync fault needs to be resolved
   immediately, explicitly triggering a
   `pyVmomi.vslm.StorageLifecycleManager.syncDatastore` should resolve the
   issue, unless there are underlying infrastructure issues affecting the
   datastore or FCD. If the fault is ignored there is
   a possibility that the FCD is unrecognized by Pandora or Pandora
   DB having stale information, consequently, affecting the return of
   `pyVmomi.vslm.vso.VStorageObjectManager.listVStorageObjectsForSpec` and
   `pyVmomi.vslm.vso.VStorageObjectManager.retrieveVStorageObjects` APIs.
   In cases where the `pyVmomi.vslm.fault.SyncFault.id` is specified,
   the client can explicitly trigger
   `pyVmomi.vslm.StorageLifecycleManager.syncDatastore` to resolve
   the issue, else, could ignore the fault in anticipation of Pandora
   automatically resolving the error.
   """
   id: _typing.Optional[pyVmomi.vim.vslm.ID] = None
