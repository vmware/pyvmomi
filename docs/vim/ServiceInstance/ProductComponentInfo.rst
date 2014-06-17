.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.ServiceInstance.ProductComponentInfo
========================================
  ProductComponentInfo data object type describes installed components. Product component is defined as a software module that is released and versioned independently but has dependency relationship with other products. If one product, for usability or any other reason, bundles other products, ProductComponentInfo type may be used to describe installed components. For example, ESX product may bundle VI Client in its releases.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    id (`str`_):

       Opaque identifier that is unique for this product component
    name (`str`_):

       Canonical name of product component
    version (`str`_):

       Version of product component
    release (`int`_):

       Release property is a number which increments with each new release of product. Product release may not rev version but release number is always incremented.
