.. _vim.Task: ../../../vim/Task.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.profile.Profile: ../../../vim/profile/Profile.rst

.. _vim.fault.DuplicateName: ../../../vim/fault/DuplicateName.rst

.. _vim.profile.cluster.ClusterProfile.ConfigSpec: ../../../vim/profile/cluster/ClusterProfile/ConfigSpec.rst


vim.profile.cluster.ClusterProfile
==================================
  


:extends: vim.profile.Profile_
:since: `vSphere API 4.0`_


Attributes
----------


Methods
-------


UpdateClusterProfile(config):
   Update the ClusterProfile with the specified config.


  Privilege:
               Profile.Edit



  Args:
    config (`vim.profile.cluster.ClusterProfile.ConfigSpec`_):
       Specification which describes the changes.




  Returns:
    None
         

  Raises:

    `vim.fault.DuplicateName`_: 
       If the profile with the new name already exists.


