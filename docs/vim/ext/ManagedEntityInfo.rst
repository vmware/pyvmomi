.. _str: https://docs.python.org/2/library/stdtypes.html

.. _type: ../../vim/ext/ManagedByInfo.rst#type

.. _iconUrl: ../../vim/ext/ManagedEntityInfo.rst#iconUrl

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.ext.ManagedEntityInfo
=========================
  This data object contains information about entities managed by this extension. The data can be used by clients to show extra information about managed virtual machines or vApps, such as a custom icon and a description of the entity.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    type (`str`_):

       Managed entity type, as defined by the extension. This matches the `type`_ field in the configuration about a virtual machine or vApp.
    smallIconUrl (`str`_, optional):

       The URL to a 16x16 pixel icon in PNG format for entities of this type managed by this extension. The design of the icon should allow for the possibility of it being badged with the power state of the entity by the vSphere client. If you do not provide this icon, the icon at `iconUrl`_ , if found, is scaled down to 16x16 pixels.
    iconUrl (`str`_, optional):

       The URL to an icon in PNG format that is no larger than 256x256 pixels. This icon will be scaled to 16x16, 32x32, 64x64, and 128x128 if needed. The icon is shown for all entities of this type managed by this extension.
    description (`str`_, optional):

       Description of this managed entity type. This is typically displayed by clients, and should provide users with information about the function of entities of this type.
