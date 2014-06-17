.. _heartbeatDatastore: ../../../vim/cluster/DasConfigInfo.rst#heartbeatDatastore

.. _vim.cluster.DasConfigInfo: ../../../vim/cluster/DasConfigInfo.rst

.. _vim.cluster.DasConfigInfo.HBDatastoreCandidate: ../../../vim/cluster/DasConfigInfo/HBDatastoreCandidate.rst

vim.cluster.DasConfigInfo.HBDatastoreCandidate
==============================================
  The policy to determine the candidates from which vCenter Server can choose heartbeat datastores.
  :contained by: `vim.cluster.DasConfigInfo`_

  :type: `vim.cluster.DasConfigInfo.HBDatastoreCandidate`_

  :name: allFeasibleDsWithUserPreference

values:
--------

allFeasibleDs
   vCenter Server chooses heartbeat datastores from all the feasible ones, i.e., the datastores that are accessible to more than one host in the cluster. The choice will be made without giving preference to those specified by the user (see `heartbeatDatastore`_ ).

allFeasibleDsWithUserPreference
   vCenter Server chooses heartbeat datastores from all the feasible ones while giving preference to those specified by the user (see `heartbeatDatastore`_ ). More specifically, the datastores not included in `heartbeatDatastore`_ will be chosen if and only if the specified ones are not sufficient.

userSelectedDs
   vCenter Server chooses heartbeat datastores from the set specified by the user (see `heartbeatDatastore`_ ). More specifically, datastores not included in the set will not be chosen. Note that if `heartbeatDatastore`_ is empty, datastore heartbeating will be disabled for HA.
