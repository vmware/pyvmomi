.. _str: https://docs.python.org/2/library/stdtypes.html

.. _newName: ../../../vim/event/VmRenamedEvent.rst#newName

.. _oldName: ../../../vim/event/VmRenamedEvent.rst#oldName

.. _VmEventArgument: ../../../vim/event/Event.rst#vm

.. _VmPoweredOnEvent: ../../../vim/event/VmPoweredOnEvent.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _fullFormattedMessage: ../../../vim/event/Event.rst#fullFormattedMessage


vim.event.EventDescription.EventDetail
======================================
  Each Event object provides an automatic event message string through its `fullFormattedMessage`_ property. However, you can use the EventDetail object's properties to format an event message string that is appropriate when viewed from a specific context. The variable information (vm.name, and so on) is derived from the Event object's event arguments ( `VmEventArgument`_ , and so on).
:extends: vmodl.DynamicData_

Attributes:
    key (`str`_):

       Type of event being described.
    description (`str`_, optional):

       A string that is a short human-parseable description of the event.This is not the full message string (which may contain details of the arguments, etc.), but merely a more understandable, and localized, description of what the event stands for. It is meant for contexts where thenameof the event has to be displayed to end-users, e.g. when creating Event-based Alarms. ` *E.g., for `VmPoweredOnEvent`_ , the eventDescription in English might say "VM Powered On".
    category (`str`_):

       A category of events.
    formatOnDatacenter (`str`_):

       A string that is appropriate in the context of a specific Datacenter. For example, a renaming event in this context produces the following string:"Renamed {vm.name} from {oldName} to {newName}"where `oldName`_ and `newName`_ are properties of the VmRenamedEvent object.
    formatOnComputeResource (`str`_):

       A string that is appropriate in the context of a specific cluster. For example, a powering on event in this context produces the following string:"{vm.name} on {host.name} is powered on".
    formatOnHost (`str`_):

       A string that is appropriate in the context of a specific Host. For example, a powering on event in this context produces the following string:"{vm.name} is powered on"
    formatOnVm (`str`_):

       A string that is appropriate for the context of a specific virtual machine. For example, a powering on event in this context produces the following string:"Virtual machine on {host.name} is powered on"
    fullFormat (`str`_):

       A string whose context is not entity-specific. For example, a powering on event produces the following string:"{vm.name} on {host.name} in {datacenter.name} is powered on"
    longDescription (`str`_, optional):

       A detailed description of the event. It includes common causes and actions to remediate them. It may also include links to kb articles and other diagnostic information. For example, the BadUserNameSessionEvent may produce the following string:The user could not be logged in because of an unknown or invalid user name.The user name was unknown to the systemUse a user name known to the system user directory(On Linux) Check if the user directory is correctly configured.Check the health of the domain controller (if you are using Active Directory)The user provided an invalid passwordSupply the correct password
