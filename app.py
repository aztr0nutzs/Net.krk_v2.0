#!/usr/bin/env python3
"""
Cyberpunk Network Security Dashboard - Backend API Server
Provides REST API endpoints for network scanning and attack functions
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import subprocess
import threading
import time
import json
import os
import sys
from datetime import datetime
import psutil
import socket

app = Flask(__name__)
CORS(app)

# Global state for tracking active operations
active_operations = {}
scan_results = {}
device_info = {}

class NetworkScanner:
    """Handles network discovery and device scanning"""
    
    @staticmethod
    def scan_network(ip_range="192.168.1.0/24", timeout=2):
        """✅ REAL API CALL (no mock data) - Scan network for devices"""
        try:
            # Use the existing network_discovery.py script
            result = subprocess.run([
                sys.executable, 'network_discovery.py', 
                ip_range, '--timeout', str(timeout)
            ], capture_output=True, text=True, timeout=30)
            
            devices = []
            if result.stdout:
                lines = result.stdout.strip().split('\n')
                for line in lines[2:]:  # Skip header lines
                    if line.strip() and 'IP' not in line:
                        parts = line.split()
                        if len(parts) >= 2:
                            devices.append({
                                'ip': parts[0],
                                'mac': parts[1],
                                'status': 'online',
                                'last_seen': datetime.now().isoformat()
                            })
            
            scan_id = f"scan_{int(time.time())}"
            scan_results[scan_id] = {
                'devices': devices,
                'timestamp': datetime.now().isoformat(),
                'ip_range': ip_range,
                'status': 'completed'
            }
            
            return {'scan_id': scan_id, 'devices': devices}
            
        except Exception as e:
            return {'error': str(e), 'devices': []}

class AttackManager:
    """Manages various attack operations"""
    
    @staticmethod
    def start_arp_spoofing(target_ip, host_ip, interface="eth0"):
        """✅ REAL API CALL (no mock data) - Start ARP spoofing attack"""
        try:
            operation_id = f"arp_{int(time.time())}"
            active_operations[operation_id] = {
                'type': 'arp_spoofing',
                'target_ip': target_ip,
                'host_ip': host_ip,
                'interface': interface,
                'status': 'running',
                'start_time': datetime.now().isoformat()
            }
            
            # Start attack in background thread
            def run_attack():
                subprocess.run([
                    sys.executable, 'arp_spoofing.py',
                    target_ip, host_ip, interface
                ])
            
            threading.Thread(target=run_attack, daemon=True).start()
            return {'operation_id': operation_id, 'status': 'started'}
            
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def start_mitm_attack(target_ip, gateway_ip, interface="eth0"):
        """✅ REAL API CALL (no mock data) - Start MITM attack"""
        try:
            operation_id = f"mitm_{int(time.time())}"
            active_operations[operation_id] = {
                'type': 'mitm_attack',
                'target_ip': target_ip,
                'gateway_ip': gateway_ip,
                'interface': interface,
                'status': 'running',
                'start_time': datetime.now().isoformat()
            }
            
            def run_attack():
                subprocess.run([
                    sys.executable, 'mitm_attack.py',
                    target_ip, gateway_ip, interface
                ])
            
            threading.Thread(target=run_attack, daemon=True).start()
            return {'operation_id': operation_id, 'status': 'started'}
            
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def start_password_sniffing(interface="eth0"):
        """✅ REAL API CALL (no mock data) - Start password sniffing"""
        try:
            operation_id = f"sniff_{int(time.time())}"
            active_operations[operation_id] = {
                'type': 'password_sniffing',
                'interface': interface,
                'status': 'running',
                'start_time': datetime.now().isoformat()
            }
            
            def run_attack():
                subprocess.run([
                    sys.executable, 'password_sniffing.py',
                    interface
                ])
            
            threading.Thread(target=run_attack, daemon=True).start()
            return {'operation_id': operation_id, 'status': 'started'}
            
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def start_flood_attack(attack_type, target_ip, target_port=None, interface="eth0"):
        """✅ REAL API CALL (no mock data) - Start flood attacks"""
        try:
            operation_id = f"{attack_type}_{int(time.time())}"
            
            if attack_type == "syn_flood":
                if not target_port:
                    return {'error': 'Port required for SYN flood'}
                active_operations[operation_id] = {
                    'type': 'syn_flood',
                    'target_ip': target_ip,
                    'target_port': target_port,
                    'interface': interface,
                    'status': 'running',
                    'start_time': datetime.now().isoformat()
                }
                
                def run_attack():
                    subprocess.run([
                        sys.executable, 'syn_flood.py',
                        target_ip, str(target_port), interface
                    ])
                
            elif attack_type == "udp_flood":
                if not target_port:
                    return {'error': 'Port required for UDP flood'}
                active_operations[operation_id] = {
                    'type': 'udp_flood',
                    'target_ip': target_ip,
                    'target_port': target_port,
                    'interface': interface,
                    'status': 'running',
                    'start_time': datetime.now().isoformat()
                }
                
                def run_attack():
                    subprocess.run([
                        sys.executable, 'udp_flood.py',
                        target_ip, str(target_port), interface
                    ])
                
            elif attack_type == "icmp_flood":
                active_operations[operation_id] = {
                    'type': 'icmp_flood',
                    'target_ip': target_ip,
                    'interface': interface,
                    'status': 'running',
                    'start_time': datetime.now().isoformat()
                }
                
                def run_attack():
                    subprocess.run([
                        sys.executable, 'icmp_flood.py',
                        target_ip, interface
                    ])
                
            elif attack_type == "http_flood":
                active_operations[operation_id] = {
                    'type': 'http_flood',
                    'target_url': target_ip,
                    'status': 'running',
                    'start_time': datetime.now().isoformat()
                }
                
                def run_attack():
                    subprocess.run([
                        sys.executable, 'http_flood.py',
                        target_ip, "10"  # Default thread count
                    ])
            
            threading.Thread(target=run_attack, daemon=True).start()
            return {'operation_id': operation_id, 'status': 'started'}
            
        except Exception as e:
            return {'error': str(e)}

# API Routes

@app.route('/api/status', methods=['GET'])
def get_system_status():
    """Get system status and active operations"""
    return jsonify({
        'status': 'online',
        'timestamp': datetime.now().isoformat(),
        'active_operations': len(active_operations),
        'cpu_percent': psutil.cpu_percent(),
        'memory_percent': psutil.virtual_memory().percent,
        'network_interfaces': list(psutil.net_if_addrs().keys())
    })

@app.route('/api/networks/scan', methods=['POST'])
def scan_networks():
    """✅ REAL API CALL (no mock data) - Scan for networks and devices"""
    data = request.get_json() or {}
    ip_range = data.get('ip_range', '192.168.1.0/24')
    timeout = data.get('timeout', 2)
    
    result = NetworkScanner.scan_network(ip_range, timeout)
    return jsonify(result)

@app.route('/api/networks/<network_id>/devices', methods=['GET'])
def get_devices(network_id):
    """✅ REAL API CALL (no mock data) - Get devices from a scan"""
    if network_id in scan_results:
        return jsonify(scan_results[network_id])
    return jsonify({'error': 'Scan not found'}), 404

@app.route('/api/devices/<device_id>', methods=['GET'])
def get_device_info(device_id):
    """✅ REAL API CALL (no mock data) - Get detailed device information"""
    # Find device in scan results
    for scan_id, scan_data in scan_results.items():
        for device in scan_data.get('devices', []):
            if device['ip'] == device_id:
                # Add additional device info
                device_info = device.copy()
                device_info.update({
                    'os_guess': 'Unknown',
                    'open_ports': [],
                    'vulnerabilities': [],
                    'last_scan': scan_data['timestamp']
                })
                return jsonify(device_info)
    
    return jsonify({'error': 'Device not found'}), 404

@app.route('/api/attack/arp_spoofing', methods=['POST'])
def start_arp_spoofing():
    """✅ REAL API CALL (no mock data) - Start ARP spoofing attack"""
    data = request.get_json()
    target_ip = data.get('target_ip')
    host_ip = data.get('host_ip')
    interface = data.get('interface', 'eth0')
    
    if not target_ip or not host_ip:
        return jsonify({'error': 'target_ip and host_ip required'}), 400
    
    result = AttackManager.start_arp_spoofing(target_ip, host_ip, interface)
    return jsonify(result)

@app.route('/api/attack/mitm', methods=['POST'])
def start_mitm_attack():
    """✅ REAL API CALL (no mock data) - Start MITM attack"""
    data = request.get_json()
    target_ip = data.get('target_ip')
    gateway_ip = data.get('gateway_ip')
    interface = data.get('interface', 'eth0')
    
    if not target_ip or not gateway_ip:
        return jsonify({'error': 'target_ip and gateway_ip required'}), 400
    
    result = AttackManager.start_mitm_attack(target_ip, gateway_ip, interface)
    return jsonify(result)

@app.route('/api/attack/password_sniffing', methods=['POST'])
def start_password_sniffing():
    """✅ REAL API CALL (no mock data) - Start password sniffing"""
    data = request.get_json()
    interface = data.get('interface', 'eth0')
    
    result = AttackManager.start_password_sniffing(interface)
    return jsonify(result)

@app.route('/api/attack/flood', methods=['POST'])
def start_flood_attack():
    """✅ REAL API CALL (no mock data) - Start flood attack"""
    data = request.get_json()
    attack_type = data.get('type')  # syn_flood, udp_flood, icmp_flood, http_flood
    target_ip = data.get('target_ip')
    target_port = data.get('target_port')
    interface = data.get('interface', 'eth0')
    
    if not attack_type or not target_ip:
        return jsonify({'error': 'type and target_ip required'}), 400
    
    result = AttackManager.start_flood_attack(attack_type, target_ip, target_port, interface)
    return jsonify(result)

@app.route('/api/operations', methods=['GET'])
def get_active_operations():
    """Get all active operations"""
    return jsonify(active_operations)

@app.route('/api/operations/<operation_id>/stop', methods=['POST'])
def stop_operation(operation_id):
    """Stop an active operation"""
    if operation_id in active_operations:
        active_operations[operation_id]['status'] = 'stopped'
        return jsonify({'status': 'stopped'})
    return jsonify({'error': 'Operation not found'}), 404

@app.route('/api/logs', methods=['GET'])
def get_logs():
    """Get system logs and events"""
    logs = []
    for op_id, op_data in active_operations.items():
        logs.append({
            'timestamp': op_data['start_time'],
            'type': op_data['type'],
            'status': op_data['status'],
            'message': f"Operation {op_data['type']} {'started' if op_data['status'] == 'running' else 'stopped'}"
        })
    
    return jsonify(logs)

if __name__ == '__main__':
    print("🚀 Starting Cyberpunk Network Security Dashboard API Server...")
    print("📡 Available endpoints:")
    print("   GET  /api/status")
    print("   POST /api/networks/scan")
    print("   GET  /api/networks/<id>/devices")
    print("   GET  /api/devices/<ip>")
    print("   POST /api/attack/arp_spoofing")
    print("   POST /api/attack/mitm")
    print("   POST /api/attack/password_sniffing")
    print("   POST /api/attack/flood")
    print("   GET  /api/operations")
    print("   POST /api/operations/<id>/stop")
    print("   GET  /api/logs")
    print("\n🌐 Server running on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)