
vim.LatencySensitivity
======================
  Specification of the latency-sensitivity information.The latency-sensitivity is used to request from the kernel a constraint on the scheduling delay of the virtual CPUs or other resources. This allows latency-sensitive applications(e.g. VOIP, audio/video streaming, etc.) to run in a virtual machine which is configured to use specific scheduling latencies and to be scheduled with low latency.The kernel does not provide any guarantee that it will meet the latency-sensitivity requirement of a virtual machine CPU or other resources but it will always accept the latency-sensitivity value provided.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    level (`vim.LatencySensitivity.SensitivityLevel <vim/LatencySensitivity/SensitivityLevel.rst>`_):

       The nominal latency-sensitive level of the application.
    sensitivity (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The custom absolute latency-sensitivity value of the application. This value will be used only when the latency-sensitivity `level <vim/LatencySensitivity.rst#level>`_ property is is set tocustom. It is ignored in all other cases.The unit of this value is micro-seconds and the application is more latency sensitive when this value is smaller. For example, if the absolute latency-sensitivity is 2000us, the kernel will try to schedule the virtual machine in a way so that its scheduling latency is not more than 2ms.
