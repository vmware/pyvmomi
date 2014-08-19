
vim.ServiceInstance.HostVMotionCompatibility
============================================
  The object type for the array returned by queryVMotionCompatibility; specifies the VMotion compatibility types for a host.
:extends: vmodl.DynamicData_

Attributes:
    host (`vim.HostSystem <vim/HostSystem.rst>`_):

       The prospective host for the virtual machine.
    compatibility ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Ways in which the host is compatible with the designated virtual machine that is a candidate for VMotion. This array will be a subset of the set of VMotionCompatibilityType strings that were input to queryVMotionCompatibility.
