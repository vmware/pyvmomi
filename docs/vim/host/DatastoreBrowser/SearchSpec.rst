.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.DatastoreBrowser.Query: ../../../vim/host/DatastoreBrowser/Query.rst

.. _vim.host.DatastoreBrowser.FileInfo.Details: ../../../vim/host/DatastoreBrowser/FileInfo/Details.rst


vim.host.DatastoreBrowser.SearchSpec
====================================
  The data object type describes a search for files in one or more datastores. The properties do not include the starting datastore path because that path is a separate parameter to the search method.A SearchSpec contains the query parameters and some global search modifiers.
:extends: vmodl.DynamicData_

Attributes:
    query ([`vim.host.DatastoreBrowser.Query`_], optional):

       The set of file types to match, search criteria specific to the file type, and the amount of detail for a file. These search parameters are specific to a file type, meaning that they can be specified only if the file type to which they are associated is in the set. A file type cannot appear more than once in the set.If this query object is not present, then all files providing only file level details are matched.
    details (`vim.host.DatastoreBrowser.FileInfo.Details`_, optional):

       This object comprises a set of booleans that describe what details to return for each file. The file level details apply globally to all matched files.
    searchCaseInsensitive (`bool`_, optional):

       This flag indicates whether or not to search using a case insensitive match on type. In general the algorithm used to match file types relies on file extensions. Although the specific file extensions used are encapsulated by this API, clients are still allowed to modify the filtering behavior.By default, the DatastoreBrowser uses a platform-consistent algorithm to determine if a file is of a type. Specifically on Linux, where case is important, the search is case sensitive. On Windows, case is not important, so the search is case insensitive.In an environment with heterogenous platforms, being platform-consistent may not be desirable. As a result, the default behavior can be overridden by setting this optional flag.
    matchPattern ([`str`_], optional):

       Specifies a list of file patterns that must match for a file to be returned. This search property is a filter that applies globally so that only files matching the specified patterns are returned, regardless of the other search parameters.
    sortFoldersFirst (`bool`_, optional):

       By default, files are sorted in alphabetical order regardless of file type. If this flag is set to "true", folders are placed at the start of the list of results in alphabetical order. The remaining files follow in alphabetical order.
