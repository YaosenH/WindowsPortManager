import psutil
import socket
from known_processes import PROCESS_DATA

def get_port_info():
    """
    Retrieves a list of network connections with process details.
    Returns a list of dictionaries.
    """
    connections = []
    try:
        # Retrieve all network connections (inet for IPv4/IPv6)
        # We focus on TCP/UDP
        for conn in psutil.net_connections(kind='inet'):
            try:
                pid = conn.pid
                if pid is None:
                    continue
                
                process = psutil.Process(pid)
                name = process.name()
                
                # Enrich with known process data
                proc_info = PROCESS_DATA.get(name, {})
                description = proc_info.get("description", "未知进程")
                importance = proc_info.get("importance", "未知")

                # Convert status to string or use empty for UDP
                status = conn.status if conn.status else "N/A"
                
                conn_info = {
                    "pid": pid,
                    "name": name,
                    "local_address": f"{conn.laddr.ip}:{conn.laddr.port}",
                    "remote_address": f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A",
                    "status": status,
                    "protocol": "TCP" if conn.type == socket.SOCK_STREAM else "UDP",
                    "port": conn.laddr.port,
                    "description": description,
                    "importance": importance
                }
                connections.append(conn_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                # Process might have ended or we don't have permission
                continue
    except psutil.AccessDenied:
        # Need admin rights for some info
        pass

    # Sort by port number
    connections.sort(key=lambda x: x['port'])
    return connections

def kill_process(pid):
    """
    Kills a process by PID.
    Returns (success: bool, message: str)
    """
    try:
        process = psutil.Process(pid)
        name = process.name()
        
        # Check importance
        proc_info = PROCESS_DATA.get(name, {})
        importance = proc_info.get("importance", "未知")
        
        if importance == "不可kill":
            return False, f"禁止操作：进程 '{name}' 标记为不可kill，强制结束可能导致系统不稳定。"

        process.kill()
        return True, f"Process {pid} ({name}) killed successfully."
    except psutil.NoSuchProcess:
        return False, f"Process {pid} does not exist."
    except psutil.AccessDenied:
        return False, f"Access denied. Cannot kill process {pid}. Try running as Administrator."
    except Exception as e:
        return False, f"Error killing process: {str(e)}"

def kill_process_by_name(name):
    """
    Kills all processes with the given name using taskkill.
    """
    import subprocess
    
    # Check importance first
    proc_info = PROCESS_DATA.get(name, {})
    importance = proc_info.get("importance", "未知")
    if importance == "不可kill":
        return False, f"禁止操作：进程 '{name}' 标记为不可kill。"

    try:
        # use taskkill /F /T /IM <name>
        # /F = Force, /T = Tree (kill children), /IM = Image Name
        cmd = ["taskkill", "/F", "/T", "/IM", name]
        
        # Run command and capture output
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            return True, f"Successfully killed all instances of {name}."
        else:
            # taskkill returns non-zero if process not found or access denied
            err_msg = result.stderr.strip() or result.stdout.strip()
            return False, f"Failed to kill {name}: {err_msg}"
            
    except Exception as e:
        return False, f"Error executing taskkill: {str(e)}"

def export_to_csv(data, filename):
    """
    Exports the connection data to a CSV file.
    """
    import csv
    try:
        if not data:
            return False, "No data to export."
            
        keys = data[0].keys()
        with open(filename, 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
        return True, f"Data exported to {filename}"
    except Exception as e:
        return False, f"Export failed: {str(e)}"
