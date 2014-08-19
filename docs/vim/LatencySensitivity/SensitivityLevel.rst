vim.LatencySensitivity.SensitivityLevel
=======================================
  Enumeration of the nominal latency-sensitive values which can be used to specify the latency-sensitivity level of the application.In terms of latency-sensitivity the values relate: high>medium>normal>low.
  :contained by: `vim.LatencySensitivity <vim/LatencySensitivity.rst>`_

  :type: `vim.LatencySensitivity.SensitivityLevel <vim/LatencySensitivity/SensitivityLevel.rst>`_

  :name: custom

values:
--------

high
   The relative latency-sensitivity high value.

custom
   deprecated as of vSphere API Ver 5.5. Value will be ignored and treated as "normal" latency sensitivity. The custom absolute latency-sensitivity specified in `sensitivity <vim/LatencySensitivity.rst#sensitivity>`_ property is used to define the latency-sensitivity.When this value is set to `level <vim/LatencySensitivity.rst#level>`_ the `sensitivity <vim/LatencySensitivity.rst#sensitivity>`_ property should be set also.

medium
   The relative latency-sensitivity medium value.

low
   The relative latency-sensitivity low value.

normal
   The relative latency-sensitivity normal value.This is the default latency-sensitivity value.
