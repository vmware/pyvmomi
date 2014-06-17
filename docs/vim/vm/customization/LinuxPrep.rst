.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _Valid timeZone values: ../../../timezone.rst

.. _vim.vm.customization.NameGenerator: ../../../vim/vm/customization/NameGenerator.rst

.. _vim.vm.customization.IdentitySettings: ../../../vim/vm/customization/IdentitySettings.rst


vim.vm.customization.LinuxPrep
==============================
  This is the Linux counterpart to the Windows Sysprep object. LinuxPrep contains machine-wide settings that identify a Linux machine in the same way that the Sysprep type identifies a Windows machine.
:extends: vim.vm.customization.IdentitySettings_

Attributes:
    hostName (`vim.vm.customization.NameGenerator`_):

       The network host name of the (Linux) virtual machine.
    domain (`str`_):

       The fully qualified domain name.
    timeZone (`str`_, optional):

       The case-sensitive timezone, such as Europe/Sofia. ``_  `Valid timeZone values`_ are based on the tz (timezone) database used by Linux and other Unix systems. The values are strings (xsd:string) in the form "Area/Location," in which Area is a continent or ocean name, and Location is the city, island, or other regional designation.
    hwClockUTC (`bool`_, optional):

       Specifies whether the hardware clock is in UTC or local time.
        * True when the hardware clock is in UTC.
        * False when the hardware clock is in local time.
