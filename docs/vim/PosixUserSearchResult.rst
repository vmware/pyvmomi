
vim.PosixUserSearchResult
=========================
  Searching for users and groups on POSIX systems provides User ID and Group ID information, in addition to that defined in UserSearchResult.
:extends: vim.UserSearchResult_

Attributes:
    id (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       If the search result is for a user, then id refers to User ID. For a group, the value of Group ID is assigned to id.
    shellAccess (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If the search result is for a user, shellAccess indicates whether shell access has been granted or not.
