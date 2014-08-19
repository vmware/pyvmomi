
vim.profile.cluster.ClusterProfile
==================================
  


:extends: vim.profile.Profile_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


Attributes
----------


Methods
-------


UpdateClusterProfile(config):
   Update the ClusterProfile with the specified config.


  Privilege:
               Profile.Edit



  Args:
    config (`vim.profile.cluster.ClusterProfile.ConfigSpec <vim/profile/cluster/ClusterProfile/ConfigSpec.rst>`_):
       Specification which describes the changes.




  Returns:
    None
         

  Raises:

    `vim.fault.DuplicateName <vim/fault/DuplicateName.rst>`_: 
       If the profile with the new name already exists.


