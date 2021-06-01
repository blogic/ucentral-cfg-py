# uCentral configuration template renderer

This repository contains python tooling and example templates that can be used to render valid configurations that can be passed to the gateway.

A template can use a special syntax as a placeholder for property values

* "$i/Placeholder/Default"  -  placeholder for an integer value
* "$s/Placeholder/Default"  -  placeholder for a string value

We can use dumpValues.py to get a JSON with the placeholders contained within a configuration template.
```
./dumpValues.py vlan.json
{
    "VLAN": 100,
    "SSID": "OpenWifi",
    "WIFI_ENCRYPTION": "psk2",
    "WIFI_KEY": "OpenWifi",
    "SSID_NAT": "OpenWifi-NAT"
}
```

The output can then be stored and passed to the generateConfig.py script
```
./dumpValues.py vlan.json > vlan.values
# edit vlan.values to match your required settings
./generateConfig.py vlan.json  vlan.values
{'uuid': 1, 'radios': [{'band': '6G', 'country': 'CA', 'channel-mode': 'HE', 'channel-width': 80}, {'band': '5G', 'country': 'CA', 'channel-mode': 'HE', 'channel-width': 80}, {'band': '2G', 'country': 'CA', 'channel-mode': 'HE', 'channel-width': 80}], 'interfaces': [{'name': 'WAN', 'role': 'upstream', 'ethernet': [{'select-ports': ['WAN*']}], 'ipv4': {'addressing': 'dynamic'}}, {'name': 'WAN_VLAN', 'role': 'upstream', 'vlan': {'id': 100}, 'ethernet': [{'select-ports': ['WAN*']}], 'ipv4': {'addressing': 'dynamic'}, 'ssids': [{'name': 'OpenWifi', 'wifi-bands': ['5G', '2G'], 'bss-mode': 'ap', 'encryption': {'proto': 'psk2', 'key': 'OpenWifi'}}]}, {'name': 'LAN', 'role': 'downstream', 'vlan': {'id': 100}, 'services': ['ssh'], 'ethernet': [{'select-ports': ['LAN*']}], 'ipv4': {'addressing': 'static', 'subnet': '192.168.1.1/24', 'dhcp': {'lease-first': 10, 'lease-count': 100, 'lease-time': '6h'}}, 'ssids': [{'name': 'OpenWifi-NAT', 'wifi-bands': ['5G', '2G'], 'bss-mode': 'ap', 'encryption': {'proto': 'psk2', 'key': 'OpenWifi'}}]}], 'services': {'ssh': {'port': 22}}}
```

The resulting output has all the placeholders replaces with the values defined in vlan.values
