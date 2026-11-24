# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import fault as fault
from . import query as query

import typing as _typing
import pyVmomi.VmomiSupport



class DynamicArray(pyVmomi.VmomiSupport.DataObject):
   """
   DynamicArray is a data object type that represents an array of dynamically-typed
   objects.
   
   A client should only see a DynamicArray object when the element type
   is unknown (meaning the type is newer than the client). Otherwise, a client would
   see the type as T[] where T is known.
   
   Attributes:
       dynamicType: Reserved.
       val: Array of dynamic values.
   """
   dynamicType: _typing.Optional[str] = None
   val: list[object] = []


class DynamicData(pyVmomi.VmomiSupport.DataObject):
   """
   DynamicData is a builtin object model data object type for manipulating data
   properties dynamically.
   
   The primary usage is as a base class for types that may
   be extended with subtypes in the future, where new properties should be sent to
   old clients as a set of dynamic properties.
   
   Attributes:
       dynamicType: Reserved.
       dynamicProperty: Set of dynamic properties.
           
           This property is optional because only the
           properties of an object that are unknown to a client will be part of this set.
           This property is not readonly just in case we want to send such properties
           from a client in the future.
   """
   dynamicType: _typing.Optional[str] = None
   dynamicProperty: list[DynamicProperty] = []


class DynamicProperty(pyVmomi.VmomiSupport.DataObject):
   """
   The DynamicProperty data object type represents a name-value pair.
   
   Attributes:
       name: Path to the property.
       val: Value of the property.
   """
   name: pyVmomi.VmomiSupport.PropertyPath
   val: object

class KeyAnyValue(DynamicData):
   """
   Non-localized key/value pair in which the
   the value can be of any type.
   
   Attributes:
       key: the key
       value: the value
   """
   key: str
   value: object


class LocalizableMessage(DynamicData):
   """
   Message data which is intended to be displayed according
   to the locale of a client.
   
   A `pyVmomi.vmodl.LocalizableMessage` contains both a formatted, localized
   version of the text and the data needed to perform localization in
   conjunction with localization catalogs.
   
   Clients of the VIM API may use vim.SessionManager.setLocale()
   to cause the server to emit a localized `pyVmomi.vmodl.LocalizableMessage.message`, or may perform
   client-side localization based on message catalogs provided by the
   server.
   - If the substition variable is a string, no further lookup is required.
     - `pyVmomi.vmodl.LocalizableMessage.arg` = [(\"address\" = \"127.0.0.1\")]
     - CATALOG(locmsg, `pyVmomi.vmodl.LocalizableMessage.key`) = \"IP address is {address}\"
     - \\==> `pyVmomi.vmodl.LocalizableMessage.message` = \"IP address is 127.0.0.1\"
   - If the substitution variable is an integer, value is a lookup key.
     - `pyVmomi.vmodl.LocalizableMessage.arg` = [(\"1\" = \"button.cancel\"), (\"2\" = \"msg.revert\")]
     - CATALOG(locmsg, `pyVmomi.vmodl.LocalizableMessage.key`) = \"Select '{1}' to {2}\"
     - CATALOG(locmsg, button.cancel) = \"Cancel\"
     - CATALOG(locmsg, msg.revert) = \"revert\"
     - \\==> `pyVmomi.vmodl.LocalizableMessage.message` = \"Select 'Cancel' to revert\"
   - If the variable contains '@', value is a label lookup in another
     catalog, where {name.@CATALOG.prefix} looks up prefix.`pyVmomi.vmodl.LocalizableMessage.arg`[name].label
     in CATALOG.
     - `pyVmomi.vmodl.LocalizableMessage.arg` = [(\"field\" = \"queued\")]
     - CATALOG(locmsg, `pyVmomi.vmodl.LocalizableMessage.key`) = \"State is {field.@enum.TaskInfo.State}\"
     - CATALOG(enum, TaskInfo.State.queued.label) is \"Queued\"
     - \\==> `pyVmomi.vmodl.LocalizableMessage.message` = \"State is Queued\"
   
   Attributes:
       key: Unique key identifying the message in the localized message catalog.
       arg: Substitution arguments for variables in the localized message.
       message: Message in session locale.
           
           Use vim.SessionManager.setLocale() to change the session locale.
   """
   key: str
   arg: list[KeyAnyValue] = []
   message: _typing.Optional[str] = None


class LocalizedMethodFault(DynamicData):
   """
   A wrapper class used to pass MethodFault data objects over the wire
   along with a localized display message for the fault.
   
   Attributes:
       localizedMessage: The localized message that would be sent in the faultstring element
           of the SOAP Fault.
           
           It is optional so that clients are not required
           to send a localized message to the server, but servers are required
           to send the localized message to clients.
   """
   fault: MethodFault
   localizedMessage: _typing.Optional[str] = None


class MethodFault(DynamicData, Exception):
   """
   The base data object type for all the object model faults
   that an application might handle.
   
   Attributes:
       msg: Message describing the fault. Unlike this class's other attributes, this one isn't part of the API schema: pyVmomi's SOAP response deserializer populates it from the SOAP fault's faultstring. It is None only in rare cases, such as when the fault is instantiated directly rather than received from the server, e.g. err = vim.fault.NotFound().
       faultCause: Fault which is the cause of this fault.
       faultMessage: Message which has details about the error
           Message can also contain a key to message catalog which
           can be used to generate better localized messages.
   """
   msg: _typing.Optional[str] = None
   faultCause: _typing.Optional[MethodFault] = None
   faultMessage: list[LocalizableMessage] = []

class RuntimeFault(MethodFault):
   """
   The base data object type for all runtime faults that can be
   thrown by a method.
   """
   pass
