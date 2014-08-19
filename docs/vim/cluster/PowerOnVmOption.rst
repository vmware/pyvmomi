vim.cluster.PowerOnVmOption
===========================
  Defines the options for a Datacenter::powerOnVm() invocation.

  :type: `vim.cluster.PowerOnVmOption <vim/cluster/PowerOnVmOption.rst>`_

  :name: ReserveResources

values:
--------

OverrideAutomationLevel
   Override the DRS automation level. Value type: `DrsBehavior <vim/cluster/DrsConfigInfo/DrsBehavior.rst>`_ Default value: current behavior

ReserveResources
   Reserve resources for the powering-on VMs throughout the power-on session. When this option is set to true, the server will return at most one recommended host per manual VM, and the VM's reservations are held on the recommended host until the VM is actually powered on (either by applying the recommendation or by a power-on request on the VM), or until the recommendation is cancelled, or until the recommendation expires. The expiration time is currently set to 10 minutes. This option does not have an effect on automatic VMs since their recommendations are executed immediately. This option is effective on DRS clusters only. Value type: boolean Default value: false
