import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from rich.table import Table
from rich.console import Console

class Network:
    def __init__(self, network_range, timeout=1):
        self.network = network_range
        self.timeout = timeout

    def _scan_host_socket(self, ip, port=1000):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(self.timeout)
                s.connect((ip, port))
                return ip, True
        except (socket.timeout, socket.error):
            return ip, False

    def host_scan(self, port):
        try:
            network = ipaddress.ip_network(self.network, strict=False)
            hosts_up = []
            with ThreadPoolExecutor(max_workers=100) as executor:
                futures = {executor.submit(self._scan_host_socket, str(host), port): host for host in tqdm(network.hosts(), desc="Escaneando hosts")}

                for future in tqdm(futures, desc="Obteniendo resultados"):
                    ip, is_up = future.result()
                    if is_up:
                        hosts_up.append(ip)

            return hosts_up
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    @staticmethod
    def pretty_print(data, data_types="hosts"):
        console = Console()
        table = Table(show_header=True, header_style="bold magenta")
        if data_types == "hosts":
            table.add_column("Hosts up", style="bold green")
            for host in data:
                table.add_row(host, end_section=True)
        console.print(table)