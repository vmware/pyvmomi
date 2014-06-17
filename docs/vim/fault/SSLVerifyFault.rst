.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.HostConnectFault: ../../vim/fault/HostConnectFault.rst


vim.fault.SSLVerifyFault
========================
    :extends:

        `vim.fault.HostConnectFault`_

  SSLVerifyFault is thrown by the host connect method if the VC server could not verify the authenticity of the host's SSL certificate. Currently, we do not distinguish the various possible reasons why the certificate could not be verified because we don't provide a way for the user to overwrite these reasons other than turning off SSL certificate verification completely. The only exception is the case when the certificate was rejected because it was self-signed. This is the most likely case when the user may want to overwrite the behavior by specifying the certificate's thumbprint in the ConnectSpec the next time the user connects to the host.

Attributes:

    selfSigned (`bool`_)

    thumbprint (`str`_)




