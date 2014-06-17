.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.profile.PolicyOption: ../../vim/profile/PolicyOption.rst


vim.profile.CompositePolicyOption
=================================
  DataObject represents a composite Policy that is created by the user using different PolicyOptions. The options set in the CompositePolicyOption should be derived from the possible options as indicated by the CompositePolicyOptionMetadata.
:extends: vim.profile.PolicyOption_
:since: `vSphere API 4.0`_

Attributes:
    option (`vim.profile.PolicyOption`_, optional):

       List of policy options that are composed and applicable for this composite policy option. The selected PolicyOptions in a CompositePolicyOption will be used in the policy. PolicyOptions need not be specified if they are not desired for the CompositePolicyOption. Order of PolicyOptions in the PolicyOption array is not significant. The host profile policy engine will not respect order of PolicyOptions. It will apply PolicyOptions in a pre-determined order. Clients of the API must produce PolicyOption in the same order as specified in the metadata.
