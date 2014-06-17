.. _RFC 2396: http://www.ietf.org/rfc/rfc2396.txt

.. _proxyURI: ../../../../vim/vm/device/VirtualDevice/URIBackingInfo.rst#proxyURI

.. _direction: ../../../../vim/vm/device/VirtualDevice/URIBackingInfo.rst#direction

.. _serviceURI: ../../../../vim/vm/device/VirtualDevice/URIBackingInfo.rst#serviceURI

.. _vSphere API 4.1: ../../../../vim/version.rst#vimversionversion6

.. _OpenSSL ciphers: http://www.openssl.org/docs/apps/ciphers.rst

.. _VirtualSerialPort: ../../../../vim/vm/device/VirtualSerialPort.rst

.. _Authentication Parameters: ../../../../#authparam

.. _VirtualSerialPortURIBackingInfo: ../../../../vim/vm/device/VirtualSerialPort/URIBackingInfo.rst

.. _vim.vm.device.VirtualDevice.URIBackingInfo: ../../../../vim/vm/device/VirtualDevice/URIBackingInfo.rst


vim.vm.device.VirtualSerialPort.URIBackingInfo
==============================================
  The `VirtualSerialPortURIBackingInfo`_ data object specifies network backing for a `VirtualSerialPort`_ . You can use URI backing to create a network serial port on the virtual machine, supporting connections between the virtual machine and remote systems.When a virtual machine establishes a connection with a remote system on the network, the virtual machine can act as a server or a client. When the virtual machine acts as a server, it accepts a connection. When the virtual machine acts as a client, it initiates the connection.You can configure the virtual serial port for communication through a virtual serial port concentrator that acts as a proxy between the virtual machine and the network. When you specify a `proxyURI`_ , the virtual machine initiates the connection with the concentrator and forwards the `direction`_ and `serviceURI`_ to the concentrator. For information about using a virtual serial port concentrator, seeUsing a Proxy with vSphere Virtual Serial Ports.ESX hosts support different protocols depending on your virtual serial port configuration.
   * If the virtual machine is handling the network connection directly (no
   * `proxyURI`_
   * specified), you can use telnet, TCP, and SSL protocols. The
   * `serviceURI`_
   * must use one of the following URI schemes:
   * 
   * host
   * :
   * port
   * - this is the equivalent of
   * tcp://
   * host
   * :
   * port
   * .
   * tcp://
   * host
   * :
   * port
   * - unencrypted TCP connection (IPv4 or IPv6).
   * tcp4://
   * host
   * :
   * port
   * - unencrypted TCP connection (IPv4 only).
   * tcp6://
   * host
   * :
   * port
   * - unencrypted TCP connection (IPv6 only).
   * ssl://
   * host
   * :
   * port
   * - this is the equivalent of
   * tcp+ssl://
   * host
   * :
   * port
   * .
   * tcp+ssl://
   * host
   * :
   * port
   * - encrypted SSL over TCP.
   * tcp4+ssl://
   * host
   * :
   * port
   * - SSL over TCP over IPv4.
   * tcp6+ssl://
   * host
   * :
   * port
   * - SSL over TCP over IPv6.
   * telnet://
   * host
   * :
   * port
   * - telnet over TCP. The virtual machine and remote system can negotiate and use SSL if the remote system supports the telnet authentication option; if not, the connection uses unencrypted text (plaintext).
   * telnets://
   * host
   * :
   * port
   * - telnet over SSL over TCP. In this case, SSL negotiation begins immediately and you cannot use the telnet authentication option.
   * As of vSphere 5.1 you can specify authentication parameters to support an encrypted connection with a remote system using SSL over telnet or telnets. The connection will fail if the peer does not support the protocols. You cannot use certificate verification when you specify
   * tcp
   * ,
   * tcp4
   * , or
   * tcp6
   * schemas. For information about parameter specification, see
   * `Authentication Parameters`_
   * below.
   * 
   * If you are using a
   * `proxyURI`_
   * to connect to a virtual serial port concentrator, the URI scheme for the communication between the remote system on the network and the concentrator depends on the concentrator implementation. The connection between the concentrator and the virtual serial port must use telnet or secure telnet (telnets). The proxy URI must use one of the following URI schemes. You cannot specify a username and password in the proxy URI.
   * 
   * telnet://
   * host
   * :
   * port
   * - telnet over TCP. The virtual machine and remote system can negotiate and use SSL if the remote system supports the telnet authentication option; if not, the connection uses unencrypted text (plaintext).
   * telnets://
   * host
   * :
   * port
   * - telnet over SSL over TCP. In this case, SSL negotiation starts immediately and you cannot use the telnet authentication option.
   * As of vSphere 5.1 you can specify authentication parameters to support an encrypted connection with a concentrator using SSL over telnet or telnets. The connection will fail if the concentrator does not support the protocols. For information about parameter specification, see
   * `Authentication Parameters`_
   * below.
   * 
   * 
   * 
   * Authentication Parameters
   * For an encrypted connection, the URI includes a set of authentication parameters. The parameters are specified as key words or key/value pairs. The following syntax description uses
   * telnet
   * ; you can also specify authentication parameters for secure telnet (
   * telnets
   * ).
   * 
   * telnet://
   * host
   * :
   * port
   * key[=value][
   * key[=value] ...]
   * 
   * The first parameter must have a number sign (
   * ) prefix. Additional parameters must have an ampersand (
   * ) prefix. The following list shows the valid parameters.
   * 
   * thumbprint=value
   * - Specifies a certificate thumbprint against which the peer certificate thumbprint is compared. When you specify a thumbprint, certificate verification is automatically enabled. See the description of the
   * verify
   * parameter below.
   * peerName=value
   * - Specifies the peer name that will be used to validate the peer certificate. When you specify a peer name, certificate verification is automatically enabled. See the description of the
   * verify
   * parameter below.
   * verify
   * - Forces certificate verification. The virtual machine will verify that the peer certificate subject matches the specified
   * peerName
   * and that it was signed by a certificate authority known to the ESXi host. Verification is automatically enabled if you specify a
   * thumbprint
   * or
   * peerName
   * .
   * cipherList=value
   * - Specifies a list of SSL ciphers. See
   * `OpenSSL ciphers`_
   * . The ciphers are specified as a list separated by colons, spaces, or commas.For information about URI format, see `RFC 2396`_ .
:extends: vim.vm.device.VirtualDevice.URIBackingInfo_
:since: `vSphere API 4.1`_

Attributes:
