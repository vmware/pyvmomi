vim.host.MountInfo.InaccessibleReason
=====================================
  A datastore can become inaccessible due to a number of reasons as defined in this enum InaccessibleReason. The reason for a datastore being inaccessibile is reported in `inaccessibleReason <vim/host/MountInfo.rst#inaccessibleReason>`_ . APD ("All Paths Down") is a condition where a SAN or NFS storage has become inaccessible for unknown reasons. It only indicates loss of connectivity and does not indicate storage device failure or LUN removal (Permanent Device Loss or PDL) A difference between APD and PDL is that APD may recover in which case all use cases will start to work as before. In case of PDL the failed datastore/device is unlikely to recover and hence the device path information and data cache will be emptied. If the PDL condition recovers, the failed datastores have to be added back to the host. Once in PDL a datastore cannot be added back until there are no longer any open files on the datastore. PDL is not linked to the APD and can happen at any time with or without APD preceding. If APD and PDL occur at the same time, APD will be reported first. Once (and if) the APD condition clears, PermanentDataLoss will be reported if PDL condition still exists.
  :contained by: `vim.host.MountInfo <vim/host/MountInfo.rst>`_

  :type: `vim.host.MountInfo.InaccessibleReason <vim/host/MountInfo/InaccessibleReason.rst>`_

  :name: PermanentDeviceLoss

values:
--------

AllPathsDown_Start
   AllPathsDown_Start value is reported when all paths down state is detected

PermanentDeviceLoss
   A PDL condition is reported as PermanentDeviceLoss.

AllPathsDown_Timeout
   After a wait for a system default time (which is user modifiable) to ascertain the state is indeed an APD, AllPathsDown_Timeout property is reported. The host advanced option used to set timeout period is "/Misc/APDTimeout" After the datastore property is set to AllPathsDown_Timeout, all data i/o to the datastore will be fast-failed (failed immediately).
