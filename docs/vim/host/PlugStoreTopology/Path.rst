
vim.host.PlugStoreTopology.Path
===============================
  This data object type is an association class that describes a Path and its associated Device. A Path may be claimed by at most one Device.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The identifier for the Path.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of path. Use this property to correlate this path object to other path objects.The state of the Path can be retrieved from the data object (@link vim.host.MultipathStateInfo.Path} on the `HostMultipathStateInfo <vim/host/MultipathStateInfo.rst>`_ data object.Use this name to configure LogicalUnit multipathing policy using `EnableMultipathPath <vim/host/StorageSystem.rst#enableMultipathPath>`_ and `DisableMultipathPath <vim/host/StorageSystem.rst#disableMultipathPath>`_ .
    channelNumber (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The channel number for a path if applicable.
    targetNumber (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The target number for a path if applicable. The target number is not guaranteed to be consistent across reboots or rescans of the adapter.
    lunNumber (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The LUN number for a path if applicable.
    adapter (`vim.host.PlugStoreTopology.Adapter <vim/host/PlugStoreTopology/Adapter.rst>`_, optional):

       The adapter that provided the Path.
    target (`vim.host.PlugStoreTopology.Target <vim/host/PlugStoreTopology/Target.rst>`_, optional):

       The target of the Path if any.
    device (`vim.host.PlugStoreTopology.Device <vim/host/PlugStoreTopology/Device.rst>`_, optional):

       The device that claimed the Path if any.
