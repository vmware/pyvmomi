
vim.vApp.EntityConfigInfo
=========================
  This object type describes the behavior of an entity (virtual machine or sub-vApp container) in a vApp container.The auto-start/auto-stop configurations control the behavior of the start/stop vApp operations.An virtual machine entity can be configured to wait for a period of time before starting or to wait to receive a successful heartbeat from a virtual machine before starting the next virtual machine in the sequence.
   * For a power-on operation, if waitForHeartbeat is true, then the power-on sequence continues after the the first heartbeat has been received. If waitingForGuest is false, the system waits for the specified delay and then continues the power-on sequence.
   * For a power-off operation, if delay is non-zero, the requested power-off action is invoked (powerOff, suspend, guestShutdown) on the virtual machine and the system waits until the number of seconds specified in the delay have passed.
   * If startAction and stopAction for an entity are both set to none, that entity does not participate in the sequence.
   * The start/stop delay and waitingForGuest is not used if the entity is a vApp container. For a vApp the only value values for startAction is none or powerOn, and the valid values for stopAction is none or powerOff.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    key (`vim.ManagedEntity <vim/ManagedEntity.rst>`_, optional):

       Entity to power on or power off. This can be a virtual machine or a vApp.
    tag (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Tag for entity.Reconfigure privilege: VApp.ApplicationConfig
    startOrder (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Specifies the start order for this entity. Entities are started from lower numbers to higher-numbers and reverse on shutdown. Multiple entities with the same start-order can be started in parallel and the order is unspecified. This value must be 0 or higher.Reconfigure privilege: VApp.ApplicationConfig
    startDelay (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Delay in seconds before continuing with the next entity in the order of entities to be started.Reconfigure privilege: VApp.ApplicationConfig
    waitingForGuest (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Determines if the virtual machine should start after receiving a heartbeat, from the guest. When a virtual machine is next in the start order, the system either waits a specified period of time for a virtual machine to power on or it waits until it receives a successful heartbeat from a powered on virtual machine. By default, this is set to false.This property has no effect for vApps.Reconfigure privilege: VApp.ApplicationConfig
    startAction (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       How to start the entity. Valid settings are none or powerOn. If set to none, then the entity does not participate in auto-start.Reconfigure privilege: VApp.ApplicationConfig
    stopDelay (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Delay in seconds before continuing with the next entity in the order sequence. This is only used if the stopAction is guestShutdown.Reconfigure privilege: VApp.ApplicationConfig
    stopAction (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Defines the stop action for the entity. Can be set to none, powerOff, guestShutdown, or suspend. If set to none, then the entity does not participate in auto-stop.Reconfigure privilege: VApp.ApplicationConfig
    destroyWithParent (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Whether the entity should be removed, when this vApp is removed. This is only set for linked children.Reconfigure privilege: VApp.ApplicationConfig
