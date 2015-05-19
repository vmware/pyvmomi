.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../vim/Task.rst

.. _VirtualMachine: ../vim/VirtualMachine.rst

.. _vSphere API 4.1: ../vim/version.rst#vimversionversion6

.. _vSphere API 4.0: ../vim/version.rst#vimversionversion5

.. _vmodl.MethodFault: ../vmodl/MethodFault.rst

.. _vim.fault.Timedout: ../vim/fault/Timedout.rst

.. _vim.HttpNfcLease.Info: ../vim/HttpNfcLease/Info.rst

.. _vim.fault.InvalidState: ../vim/fault/InvalidState.rst

.. _vim.HttpNfcLease.State: ../vim/HttpNfcLease/State.rst

.. _vmodl.LocalizedMethodFault: ../vmodl/LocalizedMethodFault.rst

.. _vim.HttpNfcLease.ManifestEntry: ../vim/HttpNfcLease/ManifestEntry.rst


vim.HttpNfcLease
================
  Represents a lease on a `VirtualMachine`_ or a `VirtualApp`_ , which can be used to import or export disks for the entity. While the lease is held, operations that alter the state of the virtual machines covered by the lease are blocked. Examples of blocked operations are PowerOn, Destroy, Migrate, etc.A lease is in one of four states:InitializingThis is the initial state. The lease remains in this state while the corresponding import/export task is preparing the objects. In an import session, this involves creating inventory objects.ReadyThe lease changes to this state once the corresponding import/export task is done preparing the lease. The leased objects are now ready, and the client can use the information provided in the `info`_ property to determine where to up/download disks. The client must call `HttpNfcLeaseProgress`_ periodically to keep the lease alive and report progress to the corresponding import/export task. Failure to do so causes the lease to time out and enter the error state.DoneWhen the client is done transferring disks, it calls `HttpNfcLeaseComplete`_ to signal the end of the import/export session. This causes the corresponding import/export task to complete successfully.ErrorIf an error occurs during initialization or the lease times out, it will change to this state. The client can also abort the lease manually by calling `HttpNfcLeaseAbort`_ . In this state, the `error`_ property can be read to determine the cause. If the lease belongs to an import session, all objects created during the import are removed when the lease enters this state.The import/export task corresponding to the lease continues running while the lease is held.


:since: `vSphere API 4.0`_


Attributes
----------
    initializeProgress (`int`_):
       Provides progress information (0-100 percent) for the initializing state of the lease. Clients can use this to track overall progress.
    info (`vim.HttpNfcLease.Info`_):
       Provides information on the objects contained in this lease. The info property is only valid when the lease is in the ready state.
    state (`vim.HttpNfcLease.State`_):
       The current state of the lease.
    error (`vmodl.LocalizedMethodFault`_):
       If the lease is in the error state, this property contains the error that caused the lease to be aborted.


Methods
-------


HttpNfcLeaseGetManifest():
   Gets the download manifest for this lease.
  since: `vSphere API 4.1`_


  Privilege:



  Args:


  Returns:
    [`vim.HttpNfcLease.ManifestEntry`_]:
         

  Raises:

    `vim.fault.Timedout`_: 
       vim.fault.Timedout

    `vim.fault.InvalidState`_: 
       vim.fault.InvalidState


HttpNfcLeaseComplete():
   Completes the import/export and releases this lease. Operations on the objects contained in this lease will no longer be blocked. After calling this method, this lease will no longer be valid.Clients should call this method when they are done accessing the disks for the `VirtualMachine`_ s in this lease. The status of the corresponding task will be set to success.


  Privilege:



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.Timedout`_: 
       if the lease has timed out before this call.

    `vim.fault.InvalidState`_: 
       if the lease has already been completed or aborted.


HttpNfcLeaseAbort(fault):
   Aborts the import/export and releases this lease. Operations on the objects contained in this lease will no longer be blocked. After calling this method, this lease will no longer be valid.Clients should call this method if an error occurs while accessing the disks, or if the operation is cancelled. The client can report the cause of the abort to other clients listening on the task with the fault parameter.


  Privilege:



  Args:
    fault (`vmodl.MethodFault`_, optional):
       [in] The fault that caused the abort, if any.




  Returns:
    None
         

  Raises:

    `vim.fault.Timedout`_: 
       if the lease has timed out before this call.

    `vim.fault.InvalidState`_: 
       if the lease has already been aborted.


HttpNfcLeaseProgress(percent):
   Sets the disk up/download progress, and renews this lease. A lease will time out automatically after a while. If the client wishes to continue using it, for example if it is not done accessing the disks, this method must be called periodically.


  Privilege:



  Args:
    percent (`int`_):
       [in] Completion status represented as an integer in the 0-100 range.




  Returns:
    None
         

  Raises:

    `vim.fault.Timedout`_: 
       if the lease has timed out.


