.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.ManagedEntity: ../../vim/ManagedEntity.rst

.. _vim.profile.Profile: ../../vim/profile/Profile.rst

.. _vmodl.fault.InvalidArgument: ../../vmodl/fault/InvalidArgument.rst

.. _vim.profile.ComplianceResult: ../../vim/profile/ComplianceResult.rst

.. _vim.profile.ExpressionMetadata: ../../vim/profile/ExpressionMetadata.rst


vim.profile.ComplianceManager
=============================
  Interface handling the Compliance aspects of entities.


:since: `vSphere API 4.0`_


Attributes
----------


Methods
-------


CheckCompliance(profile, entity):
   Check compliance of an entity against a Profile.


  Privilege:
               System.View



  Args:
    profile (`vim.profile.Profile`_, optional):
       If specified, check compliance against the specified profiles. If not specified, use the profiles associated with the entities. If both Profiles and Entities are specified, Check the compliance of each Entity against each of the profile specified.For more information, look at the KMap below.P represents if Profile is specified.E represents if Entity is specified.P ^P --------------------------------------------------- | Check compliance | Profiles associated | E| of each entity | with the specified | | against each of the | entity will be used | | profiles specified. | for checking | | | compliance. | | | | | | | --------------------------------------------------- | All entities | InvalidArgument | | associated with the | Exception is thrown. | | profile are checked. | | ^E| | | | | | | | | | | | ---------------------------------------------------


    entity (`vim.ManagedEntity`_, optional):
       If specified, the compliance check is done against this entity.




  Returns:
     `vim.Task`_:
         

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       If neither profile nor entity is specified.


QueryComplianceStatus(profile, entity):
   Query the compliance status based on Profile and Entity filter.


  Privilege:
               System.View



  Args:
    profile (`vim.profile.Profile`_, optional):
       If specified, compliance result for the specified profiles will be returned. This acts like a filtering criteria for the ComplianceResults based on specified profiles.


    entity (`vim.ManagedEntity`_, optional):
       If specified, compliance results for these entities will be returned. This acts like a filtering criteria for the ComplianceResults based on entities.




  Returns:
    `vim.profile.ComplianceResult`_:
         ComplianceResult. ComplianceResult information may not be available for all the entities. If the ComplianceResult is not available already, a new ComplianceCheck will not be triggered.

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       If neither profile nor entity is specified.


ClearComplianceStatus(profile, entity):
   Clear the saved ComplianceResult based on profile and entity filtering criteria.


  Privilege:
               Profile.Clear



  Args:
    profile (`vim.profile.Profile`_, optional):
       If specified, clear the ComplianceResult related to the Profile.


    entity (`vim.ManagedEntity`_, optional):
       If specified, clear the ComplianceResult related to the entity. If profile and entity are not specified, all the ComplianceResults will be cleared.




  Returns:
    None
         


QueryExpressionMetadata(expressionName, profile):
   Query the metadata for the expressions.


  Privilege:
               System.View



  Args:
    expressionName (`str`_, optional):
       Names of the Expressions for which metadata is requested. If expressionNames are not specified, metadata for all known expressions is returned


    profile (`vim.profile.Profile`_, optional, since `vSphere API 5.0`_ ):
       Base profile whose context needs to be used during the operation




  Returns:
    `vim.profile.ExpressionMetadata`_:
         

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       If expressionName is invalid.


