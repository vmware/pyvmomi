
vim.vm.customization.Specification
==================================
  The Specification data object type contains information required to customize a virtual machine when deploying it or migrating it to a new host.
:extends: vmodl.DynamicData_

Attributes:
    options (`vim.vm.customization.Options <vim/vm/customization/Options.rst>`_, optional):

       Optional operations (either LinuxOptions or WinOptions).
    identity (`vim.vm.customization.IdentitySettings <vim/vm/customization/IdentitySettings.rst>`_):

       Network identity and settings, similar to Microsoft's Sysprep tool. This is a Sysprep, LinuxPrep, or SysprepText object.
    globalIPSettings (`vim.vm.customization.GlobalIPSettings <vim/vm/customization/GlobalIPSettings.rst>`_):

       Global IP settings constitute the IP settings that are not specific to a particular virtual network adapter.
    nicSettingMap ([`vim.vm.customization.AdapterMapping <vim/vm/customization/AdapterMapping.rst>`_], optional):

       IP settings that are specific to a particular virtual network adapter. The AdapterMapping object maps a network adapter's MAC address to its Adapter settings object. May be empty if there are no network adapters, else should match number of network adapters in the VM.
    encryptionKey ([`int <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Byte array containing the public key used to encrypt any passwords stored in the specification. Both the client and the server can use this to determine if stored passwords can be decrypted by the server or if the passwords need to be re-entered and re-encrypted before the specification can be used.
