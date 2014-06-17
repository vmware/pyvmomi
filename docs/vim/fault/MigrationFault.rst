.. _vim.fault.VimFault: ../../vim/fault/VimFault.rst


vim.fault.MigrationFault
========================
    :extends:

        `vim.fault.VimFault`_

  Base object type for issues that can occur when reassigning the execution host of a virtual machine using migrate or relocate. These issues are typically used as argument in the MigrationEvent. When a MigrationFault is used as a value in a MigrationEvent, the type of MigrationEvent determines if the issue is a warning or an error (for example, MigrationHostWarningEvent or MigrationHostErrorEvent). When thrown as an exception, the fault is an error.Issues are categorized as errors or warnings according to the following criteria:If the virtual machine is powered on:
   * Error for fatal problems with the VMotion interfaces or licensing.
   * Error if VMotion would fail.
   * Error if VMotion would in any way interrupt the continuous and consistent operation of the virtual machine.
   * Warning for potential performance or connectivity problems between the source and destination VMotion interfaces.
   * Warning if the virtual machine's currently disconnected devices may not be connectable after VMotion.If the virtual machine is powered off or suspended:
   * Error if the destination host cannot access all the files that comprise the virtual machine (including virtual disks).
   * Error if aspects of the virtual machine are not supported by the destination host's hardware or software.
   * Warning if problems would occur when powering on or resuming the virtual machine, if the usage/configuration of the destination host were to remain in its current state.

Attributes:




