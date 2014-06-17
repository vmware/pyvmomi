.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _vSphere API 5.5: ../../vim/version.rst#vimversionversion9

.. _vim.host.VsanInternalSystem.CmmdsQuery: ../../vim/host/VsanInternalSystem/CmmdsQuery.rst


vim.host.VsanInternalSystem
===========================
  The VsanInternalSystem exposes low level access to CMMDS, as well as draft versions of VSAN object and disk management APIs that are subject to change in future releases. No compatibility is guaranteed on any of the APIs, including their prototype, behavior or result encoding.


:since: `vSphere API 5.5`_


Attributes
----------


Methods
-------


QueryCmmds(queries):
   Query CMMDS directly. The list of given queries is executed and all results are returned in a flat list. No attempt is made to de-dupe results in the case of overlapping query results.


  Privilege:
               System.Read



  Args:
    queries (`vim.host.VsanInternalSystem.CmmdsQuery`_):
       List of CMMDS query specs.




  Returns:
    `str`_:
         JSON string with the results


QueryPhysicalVsanDisks(props):
   Query statistics about physical VSAN disks. Using the props parameter the caller can control which properties are returned. Requesting only the required properties is encouraged to reduce server load, response time and client load.


  Privilege:
               System.Read



  Args:
    props (`str`_, optional):
       List of properties to gather. Not specifying a list will fetch all properties.




  Returns:
    `str`_:
         JSON string with the results


QueryVsanObjects(uuids):
   Query information about VSAN DOM objects. Retrieves information about the given set of DOM object UUIDs. In order to make this API efficient, the output of this API contains the found DOM_OBJECT, and referenced LSOM_OBJECT and DISK entries.


  Privilege:
               System.Read



  Args:
    uuids (`str`_, optional):
       List of VSAN/DOM object UUIDs.




  Returns:
    `str`_:
         JSON string with the results


QueryObjectsOnPhysicalVsanDisk(disks):
   Query DOM objects on a given set of physical disks. Finds all DOM objects that have at least one component on the given physical disks. In order to make this API efficient, the output of this API contains the found DOM_OBJECT, and referenced LSOM_OBJECT and DISK entries.


  Privilege:
               System.Read



  Args:
    disks (`str`_):
       List of VSAN disk UUIDs.




  Returns:
    `str`_:
         JSON string with the results


