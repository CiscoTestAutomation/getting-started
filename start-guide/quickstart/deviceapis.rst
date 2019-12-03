.. _perform-operations-on-device:

Perform operations on device
============================
This topic describes how to use |librarybold| Device ``api`` function to perform a multitude of operations on a Device such as adding or removing configuration, verifying configuration states, retrieving current system state or configuration etc.

How to execute Device APIs
--------------------------

The |library| can perform operations on a Device via specific Device ``api`` functions. Similar to parsing a device, you can perform an operation on a Device using the appropriate ``device.api.function_name()`` call.

Let's see how to perform some basic operations on a Device using the Device's ``api`` function.

#. Load the ``testbed``, create your testbed and Device objects, and connect to the Device::

    # Load testbed and connect to the device
    >>> from genie.testbed import load
    >>> testbed = load('mock.yaml')
    >>> device = testbed.devices['csr1000v-1']
    >>> device.connect()

   *Result*: The system connects to the device and displays the connection details. Once you're connected, you can perform operations on the device |br| |br| 

#. Execute a Device ``api`` function (operation) to get all the routes::

    >>> routes = device.api.get_routes()

    [2019-12-03 13:02:28,738] +++ csr1000v-1: executing command 'show ip route' +++
    show ip route
    Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
           D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
           N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
           E1 - OSPF external type 1, E2 - OSPF external type 2
           i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
           ia - IS-IS inter area, * - candidate default, U - per-user static route
           o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
           a - application route
           + - replicated route, % - next hop override, p - overrides from PfR

    Gateway of last resort is 10.255.0.1 to network 0.0.0.0

    S*    0.0.0.0/0 [254/0] via 10.255.0.1
          10.0.0.0/8 is variably subnetted, 10 subnets, 3 masks
    C        10.0.1.0/24 is directly connected, GigabitEthernet2
    L        10.0.1.1/32 is directly connected, GigabitEthernet2
    C        10.0.2.0/24 is directly connected, GigabitEthernet3
    L        10.0.2.1/32 is directly connected, GigabitEthernet3
    C        10.1.1.1/32 is directly connected, Loopback0
    O        10.2.2.2/32 [110/2] via 10.0.2.2, 6d01h, GigabitEthernet3
                         [110/2] via 10.0.1.2, 00:02:40, GigabitEthernet2
    C        10.11.11.11/32 is directly connected, Loopback1
    B        10.22.22.22/32 [200/0] via 10.2.2.2, 6d01h
    C        10.255.0.0/16 is directly connected, GigabitEthernet1
    L        10.255.8.19/32 is directly connected, GigabitEthernet1
    switch#
    >>>
    >>> print(routes)
    ['0.0.0.0/0', '10.0.1.0/24', '10.0.1.1/32', '10.0.2.0/24', '10.0.2.1/32', '10.1.1.1/32', '10.11.11.11/32', '10.2.2.2/32', '10.22.22.22/32', '10.255.0.0/16', '10.255.8.19/32']
    >>>

#. Execute a Device ``api`` function (operation) to shutdown an interface::

    >>> device.api.shut_interface(interface='GigabitEthernet3')

    [2019-12-03 09:48:49,970] +++ Router: config +++
    config term
    Enter configuration commands, one per line.  End with CNTL/Z.
    Router(config)#interface GigabitEthernet3
    Router(config-if)#shutdown
    Router(config-if)#end
    Router#
    >>>

Supported Device APIs
---------------------
For a complete list of operations (APIs) that the |library| can perform on a Device, visit the `APIs <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/apis>`_ page.

To view which APIs are supported for a Device from Python prompt::

    >>> dir(device.api)

    analyze_rate
    analyze_udp_in_mpls_packets
    bits_to_netmask
    change_configuration_using_jinja_templates
    change_hostname
    check_traffic_drop_count
    check_traffic_expected_rate
    check_traffic_transmitted_rate
    clear_bgp_neighbors_soft
    clear_interface_config
    clear_interface_counters
    clear_interface_interfaces
    clear_ip_bgp_vrf_af_soft
    clear_packet_buffer
    compare_archive_config_dicts
    compare_config_dicts
    config_acl_on_interface
    config_extended_acl
    config_interface_carrier_delay
    config_interface_mtu
    ...

If you try to perform an operation that we don't yet support, the |library| returns the following exception:

 .. code-block:: python

    >>> device.api.get_system_uptime()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/Users/ellewoods/pyats37/lib/python3.7/site-packages/genie/conf/base/api.py", line 52, in wrapper_match
        func = self.get_api(name, device)
      File "/Users/ellewoods/pyats37/lib/python3.7/site-packages/genie/conf/base/api.py", line 101, in get_api
        c=api_name)) from None
    AttributeError: Could not find an API called 'get_system_uptime'
    >>>

If you want to request support for a new Device ``api``, please contact us at pyats-support-ext@cisco.com
