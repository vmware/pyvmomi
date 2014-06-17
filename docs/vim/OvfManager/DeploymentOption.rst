.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.OvfManager.DeploymentOption
===============================
  A deployment option as defined in the OVF specfication.This corresponds to the Configuration element of the DeploymentOptionSection in the specification.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    key (`str`_):

       The key of the deployment option, corresponding to the ovf:id attribute in the OVF descriptor
    label (`str`_):

       A localized label for the deployment option
    description (`str`_):

       A localizable description for the deployment option.
