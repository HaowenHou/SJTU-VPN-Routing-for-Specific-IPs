# SJTU VPN Routing for Specific IPs

## Introduction

This script is to direct network traffic for specific IPs through Windows VPN, while leaving other traffic unaffected. This is useful for connection to a server through a VPN without disrupting the normal internet activities.

After setting up, you only need to one-key connect the VPN in Windows, and then run this script.

Note that this approach is available for not only SJTU VPN, but for all the VPNs that can be configured in Windows.

## Setup Instructions

1. Set up a VPN in Windows

    Set up an IKEv2 VPN connection named `sjtu` by following the [official guide](https://net.sjtu.edu.cn/info/1200/3286.htm).

2. Change default routing behavior

    Below uses Windows 11 as an example, but other versions of Windows are similar.

    - Open Windows 11 Settings > `Network & internet` > `VPN`

    - Expand the VPN `sjtu` > `Advanced options` > Click `Edit` in `More VPN properties`

    - `Networking` > Highlight `IPv4` > `Properties`
    
    - `Advanced...` > Uncheck `Use default gateway on remote network`

    <div style="text-align: center;">
        <img src="pics\change_windows_default_routing.png" width="350"/>
    </div>

3. Routing specific IPs

    In the script, assign the IPs you want to route under the VPN to the `ips` list.

## References

[How can I make the Windows VPN route selective traffic (by destination network)?](https://superuser.com/questions/12022/how-can-i-make-the-windows-vpn-route-selective-traffic-by-destination-network)

[How to prevent Windows 7 using VPN gateway by default?](https://superuser.com/questions/861454/how-to-prevent-windows-7-using-vpn-gateway-by-default/862409#862409)

## Note

This approach may be further simplified through interface name following [this](https://documentation.meraki.com/MX/Client_VPN/Configuring_Split_Tunnel_Client_VPN#Configuring_Split_Tunnel_for_Windows).