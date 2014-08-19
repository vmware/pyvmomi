vim.host.InternetScsiHba.DigestType
===================================
  The type of integrity checks to use. The digest setting for header and data traffic can be separately configured. prohibited : do not use digest. preferred : use digest if successfully negotiated, but skip the use of digest otherwise. discouraged : do not use digest if target allows, otherwise use digest. required : use digest strictly, and fail if target does not support digest. Defaults to preferred on first configuration if unspecified.
  :contained by: `vim.host.InternetScsiHba <vim/host/InternetScsiHba.rst>`_

  :type: `vim.host.InternetScsiHba.DigestType <vim/host/InternetScsiHba/DigestType.rst>`_

  :name: digestRequired

values:
--------

digestPreferred
   digestPreferred

digestDiscouraged
   digestDiscouraged

digestProhibited
   digestProhibited

digestRequired
   digestRequired
