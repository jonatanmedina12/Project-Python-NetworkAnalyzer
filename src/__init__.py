
from src.controller.NetworkAnalyzer import Network

def scan_network():
    network = Network("192.168.1.0/24")

    # Escaneamos los puertos comunes 80 (HTTP) y 443 (HTTPS)
    print("Escaneando puerto 80 (HTTP):")
    up_hosts_80 = network.host_scan(20)
    Network.pretty_print(up_hosts_80)

    print("\nEscaneando puerto 443 (HTTPS):")
    up_hosts_443 = network.host_scan(443)
    Network.pretty_print(up_hosts_443)
