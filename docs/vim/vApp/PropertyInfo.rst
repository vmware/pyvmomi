
vim.vApp.PropertyInfo
=====================
  A vApp Property description, including deployment values
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    key (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       A unique integer key for the property.
    classId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       class name for this propertyValid values for classId: Any string except any white-space charactersReconfigure privilege: VApp.ApplicationConfig
    instanceId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       class name for this propertyValid values for instanceId: Any string except any white-space charactersReconfigure privilege: VApp.ApplicationConfig
    id (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Name of property. In the OVF environment, the property is listed as [classId.]id[.instanceId]. The [classId.]name[.instanceId] must be unique.This field cannot be empty for a property. Thus, it must be specified at creation and cannot be set to the empty string.Valid values for id: Any string except any white-space charactersReconfigure privilege: VApp.ApplicationConfig
    category (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       A user-visible description the category the property belongs to.Reconfigure privilege: VApp.ApplicationConfig
    label (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The display name for the property.Reconfigure privilege: VApp.ApplicationConfig
    type (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Describes the valid format of the property.A type must be one of:
        * string : A generic string. Max length 65535 (64k).
        * string(x..) : A string with minimum character length x.
        * string(..y) : A string with maximum character length y.
        * string(x..y) : A string with minimum character length x and maximum character length y.
        * string["choice1", "choice2", "choice3"] : A set of choices. " inside a choice must be either \" or ' e.g "start\"middle\"end" or "start'middle'end" and a \ inside a string choice must be encoded as \\ e.g. "start\\end".
        * int : An integer value. Is semantically equivalent to int(-2147483648..2147483647) e.g. signed int32.
        * int(x..y): An integer value with a minimum size x and a maximum size y. For example int(0..255) is a number between 0 and 255 both incl. This is also a way to specify that the number must be a uint8. There is always a lower and lower bound. Max number of digits is 100 including any sign. If exported to OVF the value will be truncated to max of uint64 or int64.
        * real : IEEE 8-byte floating-point value.
        * real(x..y) : IEEE 8-byte floating-point value with a minimum size x and a maximum size y. For example real(-1.5..1.5) must be a number between -1.5 and 1.5. Because of the nature of float some conversions can truncate the value. Real must be encoded acording to CIM: RealValue = [ "+" | "-" } *decimalDigit "." 1*decimalDigit [ ("e" | "E" ) [ "+" | "-" ] 1*decimalDigit ] ]
        * boolean : A boolean. The value can be True or False
        * password : A generic string. Max length 65535 (64k).
        * password(x..) : A string with minimum character length x.
        * password(..y) : A string with maximum character length y.
        * password(x..y) : A string with minimum character length x and maximum character length y.
        * ip : An IPv4 address in dot-decimal notation or an IPv6 address in colon-hexadecimal notation.
        * ip:network : An IP address in dot-notation (IPv4) and colon-hexadecimal (IPv6) on a particular network. The behavior of this type depends on the ipAllocationPolicy. See below.
        * expression: The default value specifies an expression that is calculated by the system.
        * For properties of type 'password', the value field and default value field will always be returned as an empty string when queried. Thus, it is a write-only property. Typically, a client application will also render these as a text field with hidden text and double prompting.
        * An expression follows the general patterns of either ${arg} or ${cmd:arg}. The list of supported expressions are listed below:
        * 
        * ${
        * name
        * } : This expression evaluates to the same value as the named property in the parent vApp. A parent vApp is the first vApp in the ancestry chain (resource pools are skipped). If no parent vApp exists or the property is not defined on the parent vApp, the expression evaluates to the empty value.
        * ${subnet:
        * network
        * } : The subnet value of the given network.
        * ${netmask:
        * network
        * } : The netmask value of the given network.
        * ${gateway:
        * network
        * } : The gateway value of the given network.
        * ${autoIp:
        * network
        * } : An auto-assigned network address on the given network
        * ${net:
        * network
        * } : The name of the network
        * ${domainName:
        * network
        * } : The DNS domain name, e.g., vmware.com, of the given network.
        * ${searchPath:
        * network
        * } : The DNS search path, e.g., eng.vmware.com;vmware.com, of the given network.
        * ${hostPrefix:
        * network
        * }: The host prefix on a given network, e.g., "voe-"
        * ${dns:network}: A comma-separated string of configured network addresses
        * ${httpProxy:network}: The hostname:port for a proxy on the network
        * ${vimIp:} : The IP address of the VIM API provider server. This would typical be an ESX Server or VirtualCenter Server.
        * A vApp will fail to start if any of the properties cannot be computed. For example, if a property reference a gateway on a network, for which is has not been specified. The value of the computed computation is assigned to the 'value' field upon start of the vApp or virtual machine. The value is cleared once the vApp or virtual machine is not-running.
        * The system provides three ways of specifying IP addresses:
        * 
        * ip,
        * ip:network type,
        * ${ip:network} expression.Theiptypes are typically used to specify an IP addressed to an external system. Thus, these are not used by a virtual ethernet adapter within the guest itself. Both the ip:network expression and the ${ip:network} expression are intended as a way to obtain an IP address for a virtual machine in a vApp.The behavior of ip:network type is controlled by the ipAssignPolicy, as described in the following table:Policyip:networktypeDHCPThe user is not prompted to enter a value. The variable is set to the empty string during power-on, and later updated with the IP value reported by the guest software.TransientThe user is not prompted to enter a value. An IP address is allocated by the platform and is assigned to the variable which is available to the guest. The IP address is released at power-off.FixedThe user is prompted to enter a value. This value is available to the guest.Fixed AllocatedThe user is not prompted to enter a value. An IP address is allocated by the platform and is assigned to the variable which is available to the guest. The IP address remains allocated at power-off, and are only released if the property is deleted or the vApp is destroyed.Reconfigure privilege: VApp.ApplicationConfig
    typeReference (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Contains extra configuration data depending on the property type. For types that refer to network names the type reference is the managed object reference of the network.
    userConfigurable (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Whether the property is user-configurable or a system property. This is not used if the type is expression.Reconfigure privilege: VApp.ApplicationConfig
    defaultValue (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       This either contains the default value of a field (used if value is empty string), or the expression if the type is "expression". See comment for the
    value (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The value of the field at deployment time. For expressions, this will contain the value that has been computed.Reconfigure privilege: VApp.InstanceConfig
    description (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       A description of the field.Reconfigure privilege: VApp.ApplicationConfig
