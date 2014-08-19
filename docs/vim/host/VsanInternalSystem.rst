
vim.host.VsanInternalSystem
===========================
  The VsanInternalSystem exposes low level access to CMMDS, as well as draft versions of VSAN object and disk management APIs that are subject to change in future releases. No compatibility is guaranteed on any of the APIs, including their prototype, behavior or result encoding.


:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_


Attributes
----------


Methods
-------


QueryCmmds(queries):
   Query CMMDS directly. The list of given queries is executed and all results are returned in a flat list. No attempt is made to de-dupe results in the case of overlapping query results.


  Privilege:
               System.Read



  Args:
    queries (`vim.host.VsanInternalSystem.CmmdsQuery <vim/host/VsanInternalSystem/CmmdsQuery.rst>`_):
       List of CMMDS query specs.




  Returns:
    `str <https://docs.python.org/2/library/stdtypes.html>`_:
         JSON string with the results


QueryPhysicalVsanDisks(props):
   Query statistics about physical VSAN disks. Using the props parameter the caller can control which properties are returned. Requesting only the required properties is encouraged to reduce server load, response time and client load.


  Privilege:
               System.Read



  Args:
    props (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       List of properties to gather. Not specifying a list will fetch all properties.




  Returns:
    `str <https://docs.python.org/2/library/stdtypes.html>`_:
         JSON string with the results


QueryVsanObjects(uuids):
   Query information about VSAN DOM objects. Retrieves information about the given set of DOM object UUIDs. In order to make this API efficient, the output of this API contains the found DOM_OBJECT, and referenced LSOM_OBJECT and DISK entries.


  Privilege:
               System.Read



  Args:
    uuids (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       List of VSAN/DOM object UUIDs.




  Returns:
    `str <https://docs.python.org/2/library/stdtypes.html>`_:
         JSON string with the results


QueryObjectsOnPhysicalVsanDisk(disks):
   Query DOM objects on a given set of physical disks. Finds all DOM objects that have at least one component on the given physical disks. In order to make this API efficient, the output of this API contains the found DOM_OBJECT, and referenced LSOM_OBJECT and DISK entries.


  Privilege:
               System.Read



  Args:
    disks (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       List of VSAN disk UUIDs.




  Returns:
    `str <https://docs.python.org/2/library/stdtypes.html>`_:
         JSON string with the results


