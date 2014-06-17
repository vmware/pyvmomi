.. _str: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.LocalizationManager.MessageCatalog
======================================
  Description of an available message catalog
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    moduleName (`str`_):

       The module or extension that publishes this catalog. The moduleName will be empty for the core catalogs for the VirtualCenter server itself.
    catalogName (`str`_):

       The name of the catalog.
    locale (`str`_):

       The locale for the catalog.
    catalogUri (`str`_):

       The URI (relative to the connection URL for the VirtualCenter server itself) from which the catalog can be downloaded. The caller will need to augment this with a scheme and authority (host and port) to make a complete URL.
    lastModified (`datetime`_, optional):

       The last-modified time of the catalog file, if available
    md5sum (`str`_, optional):

       The checksum of the catalog file, if available
    version (`str`_, optional):

       The version of the catalog file, if available The format is dot-separated version string, e.g. "1.2.3".
