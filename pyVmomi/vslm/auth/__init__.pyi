# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import pyVmomi.VmomiSupport



class SessionManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   `pyVmomi.vslm.auth.SessionManager` managed object manages client sessions.
   
   Login to VSLM service is done through this interface.
   It is SSO enabled so only login by using SamlToken is allowed.
   This API is intended for internal use only.
   """
   def LoginByToken(self, delegatedTokenXml: str) -> None:
      """
      Login to the VSLM service by using SSO token.
      
      VSLM will validate the user
      token from the context. The delegated token passed as a parameter will be
      used by VSLM to login to VC for authorization purposes.
      Once login successfully returns, a new session is established for the
      client. This session is only valid for the lifetime of the supplied
      delegated token. Any calls made on a session which exceeds this lifetime
      will result in a SecurityError. The client is expected to logout of the
      current session and subsequently re-login with a new delegated token to
      establish a new session.
      
      Args:
          delegatedTokenXml: The delegated token will be retrieved by the
              client and delegated to VSLM. VSLM will use this token, on user's
              behalf, to login to VC for authorization purposes. It is necessary
              to convert the token to XML because the SAML token itself is
              not a VMODL Data Object and cannot be used as a parameter.
      
      Raises:
          pyVmomi.vim.fault.InvalidLogin: if there is no token provided or the token
              could not be validated.
      """
      ...
   def Logout(self) -> None:
      """Logs out of the VSLM Service."""
      ...
