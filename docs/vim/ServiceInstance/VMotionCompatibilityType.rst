vim.ServiceInstance.VMotionCompatibilityType
============================================
  Types of a host's compatibility with a designated virtual machine that is a candidate for VMotion. Used with queryVMotionCompatibility both as inputs (to designate which compatibility types to test for) and as outputs (to specify which compatibility types apply for each host).
  :contained by: `vim.ServiceInstance <vim/ServiceInstance.rst>`_

  :type: `vim.ServiceInstance.VMotionCompatibilityType <vim/ServiceInstance/VMotionCompatibilityType.rst>`_

  :name: software

values:
--------

cpu
   The host's CPU features are compatible with the the virtual machine's requirements.

software
   The software platform on the host supports VMotion and is compatible with the virtual machine.
