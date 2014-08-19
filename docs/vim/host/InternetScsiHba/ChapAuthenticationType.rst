vim.host.InternetScsiHba.ChapAuthenticationType
===============================================
  The type of CHAP authentication setting to use. prohibited : do not use CHAP. preferred : use CHAP if successfully negotiated, but allow non-CHAP connections as fallback discouraged : use non-CHAP, but allow CHAP connectsion as fallback required : use CHAP for connection strictly, and fail if CHAP negotiation fails. Defaults to preferred on first configuration if unspecified.
  :contained by: `vim.host.InternetScsiHba <vim/host/InternetScsiHba.rst>`_

  :type: `vim.host.InternetScsiHba.ChapAuthenticationType <vim/host/InternetScsiHba/ChapAuthenticationType.rst>`_

  :name: chapRequired

values:
--------

chapPreferred
   chapPreferred

chapDiscouraged
   chapDiscouraged

chapProhibited
   chapProhibited

chapRequired
   chapRequired
