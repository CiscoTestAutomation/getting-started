Learn device features
=====================
.. include:: ../definitions/def_feature.rst 

This section describes how to use the ``learn`` function of the |librarybold| ``Ops`` module for stateful network validation of device features, such as protocols, interfaces, line cards, and other hardware.

:question:`Begin editing from here.`

.. _cli_learn:

Genie Learn
===========

`genie learn` is a powerful tool that can be extensively used to accomplish
stateful network validation across multiple devices, with one linux command.

``Genie`` `Ops` is used to represent the operational state of a `feature` using
Python datastructures. `genie learn` works by to "learning" a `feature`
configured on a `device` by executing ``Genie`` `Ops` directly from a linux
terminal. 

For each `feature`, the operational information is collected by executing
multiple show-commands, after which that output is parsed and stored into a
Python datastructure. 

To see what functionality `genie learn` offers, execute the following in your
linux terminal:

.. code-block:: bash

    (genie) bash-4.1$ genie learn --help
    Usage:
      genie learn [commands] [options]

    Example
    -------
      genie learn ospf --testbed-file /path/to/testbed.yaml
      genie learn ospf --testbed-file /path/to/testbed.yaml --output features_snapshots/ --devices nxos-osv-1
      genie learn ospf interface bgp platform --testbed-file /path/to/testbed.yaml --output features_snapshots/

    Description:
      Learn device feature and parse into Python datastructures

          List of available features: https://pubhub.devnetcloud.com/media/pyats-packages/docs/genie/genie_libs/#/models

    Learn Options:
      ops                   List of Feature to learn, comma separated, ospf,bgp
      --testbed-file        TESTBED_FILE
                            specify testbed_file yaml
      --devices             [DEVICES [DEVICES ...]]
                            List of devices, comma separated, if not provided it will learn on all
                            devices (Optional)
      --output OUTPUT       Which directory to store logs, by default it will be current directory
                            (Optional)
      --single-process      Learn one device at the time instead of in parallel (Optional)
      --via [VIA [VIA ...]]
                            List of connection to use per device "nxos-1:ssh"

    General Options:
      -h, --help            Show help
      -v, --verbose         Give more output, additive up to 3 times.
      -q, --quiet           Give less output, additive up to 3 times, corresponding to WARNING, ERROR,
                            and CRITICAL logging levels

The following is a complete list of of `feature`'s available to learn using
`genie learn`: :models:`Genie Models<http>`. It also provides details on the
Python datastructure that will be built with `genie learn` for each feature.

Refer to :ref:`Genie Ops <ops>` for more information on how ``Genie`` `Ops` works.

Single Feature
--------------

The following is an example of how to learn one `feature` (BGP) on the `device`
`uut`:

.. code-block:: bash
    
    (genie) bash-4.1$ genie learn bgp --testbed-file /path/to/testbed.yaml --devices nx-osv-1

    Learning '['bgp']' on devices '['uut']'
    100%|############################################################| 1/1 [00:11<00:00, 11.04s/it]
    +==============================================================================+
    | Genie Learn Summary for device nx-osv-1                                      |
    +==============================================================================+
    |  Connected to nx-osv-1                                                       |
    |  -   Log: ./connection_uut.txt                                               |
    |------------------------------------------------------------------------------|
    |  Learnt feature 'bgp'                                                        |
    |  -  Ops structure:  ./bgp_nxos_nx-osv-1_ops.txt                              |
    |  -  Device Console: ./bgp_nxos_nx-osv-1_console.txt                          |
    |==============================================================================|

.. note::

    Default behaviour:

    1. `genie learn` will save all the `Ops` objects that are built, into files
        within the current directory of execution; unless argument '--output'
        specifying the directory is provided.

    2. `genie learn` will execute on all `device`'s within the `testbed` YAML in
        *parallel*; unless argument '--single-process' is provided. This will cause
        ``Genie`` to execute `Ops` *sequentially* on each `device`.

Similar to the `genie parse` mechanism, `genie learn` generates 3 files:

1. `Unicon` telnet connection log
2. `device` console output (for all show commands executed in `Ops`)
3. `Ops` Python datastructure in JSON.

The following is a snippet of the `Ops` Python datastructure (in JSON format)
created by `genie learn` for `feature` BGP:

.. code-block:: bash

    (genie) bash-4.1$ more ./bgp_nxos_nx-osv-1_ops.txt
    {
      "attributes": null,
      "commands": null,
      "connections": null,
      "context_manager": {},
      "info": {
        "instance": {
          "default": {
            "bgp_id": 100,
            "peer_policy": {
              "PP-1": {
                "send_community": true,
                "soft_reconfiguration": true
              }
            },
            "peer_session": {
              "PS-1": {
                "disable_connected_check": true
              }
            },
            "protocol_state": "running",
            "vrf": {
              "VRF1": {
                "address_family": {
                  "ipv4 unicast": {
                    "label_allocation_mode": "per-vrf",
                    "nexthop_trigger_delay_critical": 3000,
                    "nexthop_trigger_delay_non_critical": 10000,
                    "nexthop_trigger_enable": true
                  },
                  "ipv6 unicast": {
                    "label_allocation_mode": "per-vrf",
                    "nexthop_trigger_delay_critical": 3000,
                    "nexthop_trigger_delay_non_critical": 10000,
                    "nexthop_trigger_enable": true
                  }
                },
                "cluster_id": "0.0.0.0",
                "confederation_identifier": 0,
                "neighbor": {
                  "55.1.1.101": {
                    "address_family": {
                      "ipv4 unicast": {
                        "as_override": true,
                        "bgp_table_version": 2,
                        "session_state": "idle"
                      }
                    },
            ...

A ``Genie`` `Ops` datastructure contains extensive information on the operational
state of the `feature` on the `device`. Using `genie learn` facilitates and
expedites stateful network validation of all `features` configured on all
`device`'s in a network.

Multiple Features
-----------------

`genie learn` also supports learning multiple `features` on a multiple `device`'s
in a `testbed` as shown in the example below:

.. code-block:: bash

    (genie) bash-4.1$ genie learn bgp ospf --testbed-file /path/to/testbed.yaml --output genie_learn

    Learning '['bgp', 'ospf']' on devices '['nx-osv-1', 'csr1000v-1']
    100%|############################################################| 1/1 [00:27<00:00, 27.60s/it]

    +==============================================================================+
    | Genie Learn Summary for device nx-osv-1                                      |
    +==============================================================================+
    |  Connected to nx-osv-1                                                       |
    |  -   Log: genie_learn/connection_nx-osv-1.txt                                |
    |------------------------------------------------------------------------------|
    |  Learnt feature 'bgp'                                                        |
    |  -  Ops structure:  genie_learn/bgp_nxos_nx-osv-1_ops.txt                    |
    |  -  Device Console: genie_learn/bgp_nxos_nx-osv-1_console.txt                |
    |------------------------------------------------------------------------------|
    |  Learnt feature 'ospf'                                                       |
    |  -  Ops structure:  genie_learn/ospf_nxos_nx-osv-1_ops.txt                   |
    |  -  Device Console: genie_learn/ospf_nxos_nx-osv-1_console.txt               |
    |==============================================================================|

    +==============================================================================+
    | Genie Learn Summary for device csr1000v-1                                    |
    +==============================================================================+
    |  Connected to csr1000v-1                                                     |
    |  -   Log: genie_learn/connection_csr1000v-1.txt                              |
    |------------------------------------------------------------------------------|
    |  Could not learn feature 'bgp'                                               |
    |  -  Exception:      genie_learn/bgp_nxos_csr1000v-1_exception.txt            |
    |  -  Ops structure:  genie_learn/bgp_nxos_csr1000v-1_ops.txt                  |
    |  -  Device Console: genie_learn/bgp_nxos_csr1000v-1_console.txt              |
    |------------------------------------------------------------------------------|
    |  Learnt feature 'ospf'                                                       |
    |  -  Ops structure:  genie_learn/ospf_nxos_csr1000v-1_ops.txt                 |
    |  -  Device Console: genie_learn/ospf_nxos_csr1000v-1_console.txt             |
    |==============================================================================|

`genie learn` creates a new directory with the name specified within '--output'
argument. Within this directory, it creates the `Ops` output for each `feature`
on each `device`.

All Features
------------

`genie learn` can also be used to learn *all* the features available within
``Genie`` `Ops`. 

The following is a complete list of of `feature`'s available to learn using
`genie learn`: :models:`Genie Models<http>`. It also provides details on the
Python datastructure that will be built with `genie learn` for each feature.

Here is an example:

.. code-block:: bash

    (genie) bash-4.1$ genie learn all --testbed-file /path/to/testbed.yaml --devices nx-osv-1 --output genie_learn_all

    Learning '['acl', 'bgp', 'dot1x', 'fdb', 'hsrp', 'igmp', 'interface', 'lag', 'lisp', 'lldp', 'mcast', 'mld', 'msdp', 'nd', 'ntp', 'ospf', 'pim', 'platform', 'prefix_list', 'route_policy', 'routing', 'static_routing', 'stp', 'vlan', 'vrf', 'vxlan', 'arp']' on devices '['uut']'
    100%|##########################################################| 27/27 [01:49<00:00,  3.94s/it]

    +=================================================================================+
    | Genie Learn Summary for device nx-osv-1                                         |
    +=================================================================================+
    |  Connected to nx-osv-1                                                          |
    |  -   Log: genie_learn_all/connection_uut.txt                                    |
    |---------------------------------------------------------------------------------|
    |  Could not learn feature 'acl'                                                  |
    |  -  Exception:      genie_learn_all/acl_nxos_nx-osv-1_exception.txt             |
    |  -  Feature not yet developped for this os                                      |
    |---------------------------------------------------------------------------------|
    |  Learnt feature 'bgp'                                                           |
    |  -  Ops structure:  genie_learn_all/bgp_nxos_nx-osv-1_ops.txt                   |
    |  -  Device Console: genie_learn_all/bgp_nxos_nx-osv-1_console.txt               |
    |---------------------------------------------------------------------------------|
    |  Could not learn feature 'dot1x'                                                |
    |  -  Exception:      genie_learn_all/dot1x_nxos_nx-osv-1_exception.txt           |
    |  -  Feature not yet developped for this os                                      |
    |---------------------------------------------------------------------------------|
    |  Could not learn feature 'fdb'                                                  |
    |  -  Exception:      genie_learn_all/fdb_nxos_nx-osv-1_exception.txt             |
    |  -  Feature not yet developped for this os                                      |
    |---------------------------------------------------------------------------------|
    |  Learnt feature 'hsrp'                                                          |
    |  -  Ops structure:  genie_learn_all/hsrp_nxos_nx-osv-1_ops.txt                  |
    |  -  Device Console: genie_learn_all/hsrp_nxos_nx-osv-1_console.txt              |
    |---------------------------------------------------------------------------------|
    |  Learnt feature 'igmp'                                                          |
    |  -  Ops structure:  genie_learn_all/igmp_nxos_nx-osv-1_ops.txt                  |
    |  -  Device Console: genie_learn_all/igmp_nxos_nx-osv-1_console.txt              |
    |---------------------------------------------------------------------------------|
    |  Learnt feature 'interface'                                                     |
    |  -  Ops structure:  genie_learn_all/interface_nxos_nx-osv-1_ops.txt             |
    |  -  Device Console: genie_learn_all/interface_nxos_nx-osv-1_console.txt         |
    |---------------------------------------------------------------------------------|
    |  Could not learn feature 'lag'                                                  |
    |  -  Exception:      genie_learn_all/lag_nxos_nx-osv-1_exception.txt             |
    |  -  Feature not yet developped for this os                                      |
    |---------------------------------------------------------------------------------|
    |  Could not learn feature 'lisp'                                                 |
    |  -  Exception:      genie_learn_all/lisp_nxos_nx-osv-1_exception.txt            |
    |  -  Feature not yet developped for this os                                      |
    |---------------------------------------------------------------------------------|
    |  Could not learn feature 'lldp'                                                 |
    |  -  Exception:      genie_learn_all/lldp_nxos_nx-osv-1_exception.txt            |
    |  -  Feature not yet developped for this os                                      |
    |---------------------------------------------------------------------------------|
    |  Learnt feature 'mcast'                                                         |
    |  -  Ops structure:  genie_learn_all/mcast_nxos_nx-osv-1_ops.txt                 |
    |  -  Device Console: genie_learn_all/mcast_nxos_nx-osv-1_console.txt             |
    |---------------------------------------------------------------------------------|
    |  Learnt feature 'mld'                                                           |
    |  -  Ops structure:  genie_learn_all/mld_nxos_nx-osv-1_ops.txt                   |
    |  -  Device Console: genie_learn_all/mld_nxos_nx-osv-1_console.txt               |
    |---------------------------------------------------------------------------------|
    |  Learnt feature 'msdp'                                                          |
    |  -  Ops structure:  genie_learn_all/msdp_nxos_nx-osv-1_ops.txt                  |
    |  -  Device Console: genie_learn_all/msdp_nxos_nx-osv-1_console.txt              |
    |---------------------------------------------------------------------------------|
    |  Learnt feature 'nd'                                                            |
    |  -  Ops structure:  genie_learn_all/nd_nxos_nx-osv-1_ops.txt                    |
    |  -  Device Console: genie_learn_all/nd_nxos_nx-osv-1_console.txt                |
    |---------------------------------------------------------------------------------|
    |  Learnt feature 'ntp'                                                           |
    |  -  Ops structure:  genie_learn_all/ntp_nxos_nx-osv-1_ops.txt                   |
    |  -  Device Console: genie_learn_all/ntp_nxos_nx-osv-1_console.txt               |
    |---------------------------------------------------------------------------------|
    |  Learnt feature 'ospf'                                                          |
    |  -  Ops structure:  genie_learn_all/ospf_nxos_nx-osv-1_ops.txt                  |
    |  -  Device Console: genie_learn_all/ospf_nxos_nx-osv-1_console.txt              |
    |---------------------------------------------------------------------------------|
    |  Learnt feature 'pim'                                                           |
    |  -  Ops structure:  genie_learn_all/pim_nxos_nx-osv-1_ops.txt                   |
    |  -  Device Console: genie_learn_all/pim_nxos_nx-osv-1_console.txt               |
    |---------------------------------------------------------------------------------|
    |  Learnt feature 'platform'                                                      |
    |  -  Ops structure:  genie_learn_all/platform_nxos_nx-osv-1_ops.txt              |
    |  -  Device Console: genie_learn_all/platform_nxos_nx-osv-1_console.txt          |
    |---------------------------------------------------------------------------------|
    |  Learnt feature 'prefix_list'                                                   |
    |  -  Ops structure:  genie_learn_all/prefix_list_nxos_nx-osv-1_ops.txt           |
    |  -  Device Console: genie_learn_all/prefix_list_nxos_nx-osv-1_console.txt       |
    |---------------------------------------------------------------------------------|
    |  Learnt feature 'route_policy'                                                  |
    |  -  Ops structure:  genie_learn_all/route_policy_nxos_nx-osv-1_ops.txt          |
    |  -  Device Console: genie_learn_all/route_policy_nxos_nx-osv-1_console.txt      |
    |---------------------------------------------------------------------------------|
    |  Learnt feature 'routing'                                                       |
    |  -  Ops structure:  genie_learn_all/routing_nxos_nx-osv-1_ops.txt               |
    |  -  Device Console: genie_learn_all/routing_nxos_nx-osv-1_console.txt           |
    |---------------------------------------------------------------------------------|
    |  Could not learn feature 'static_routing'                                       |
    |  -  Exception:      genie_learn_all/static_routing_nxos_nx-osv-1_exception.txt  |
    |  -  Feature not yet developped for this os                                      |
    |---------------------------------------------------------------------------------|
    |  Could not learn feature 'stp'                                                  |
    |  -  Exception:      genie_learn_all/stp_nxos_nx-osv-1_exception.txt             |
    |  -  Feature not yet developped for this os                                      |
    |---------------------------------------------------------------------------------|
    |  Learnt feature 'vlan'                                                          |
    |  -  Ops structure:  genie_learn_all/vlan_nxos_nx-osv-1_ops.txt                  |
    |  -  Device Console: genie_learn_all/vlan_nxos_nx-osv-1_console.txt              |
    |---------------------------------------------------------------------------------|
    |  Learnt feature 'vrf'                                                           |
    |  -  Ops structure:  genie_learn_all/vrf_nxos_nx-osv-1_ops.txt                   |
    |  -  Device Console: genie_learn_all/vrf_nxos_nx-osv-1_console.txt               |
    |---------------------------------------------------------------------------------|
    |  Could not learn feature 'vxlan'                                                |
    |  -  Exception:      genie_learn_all/vxlan_nxos_nx-osv-1_exception.txt           |
    |  -  Ops structure:  genie_learn_all/vxlan_nxos_nx-osv-1_ops.txt                 |
    |  -  Device Console: genie_learn_all/vxlan_nxos_nx-osv-1_console.txt             |
    |---------------------------------------------------------------------------------|
    |  Learnt feature 'arp'                                                           |
    |  -  Ops structure:  genie_learn_all/arp_nxos_nx-osv-1_ops.txt                   |
    |  -  Device Console: genie_learn_all/arp_nxos_nx-osv-1_console.txt               |
    |=================================================================================|

`genie learn` is well equipped with efficient error handling. In the event that
the ``Genie`` `Ops` has not been developed for a certain `OS` on a certain
`feature`, `genie learn` will print a proper error message displaying this to the
user as seen in the exampe above:

.. code-block:: text

    |------------------------------------------------------------------------------|
    |  Could not learn feature 'lisp'                                              |
    |  -  Exception:      genie_learn_all/lisp_nxos_nx-osv-1_exception.txt         |
    |  -  Feature not yet developped for this os                                   |
    |------------------------------------------------------------------------------|


`genie learn` is a powerful tool that can be extensively used for accomplish
stateful network validation in a few simple steps

Learn a single feature
-----------------------
*(This content can be re-used elsewhere.)*

#. Step one 
#. Step two
#. Step n 

Learn multiple features
-----------------------
*(This content can be re-used elsewhere.)*

#. Step one 
#. Step two
#. Step n

Learn all features
-------------------
*(This content can be re-used elsewhere.)*

#. Step one 
#. Step two
#. Step n

See also...
*a list of relevant links*

* link 1
* link 2
* link 3







