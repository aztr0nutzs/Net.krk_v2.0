#!/usr/bin/env python3
"""
Cyberpunk Network Security Dashboard Startup Script
Starts the Flask backend server and provides instructions for accessing the dashboard
"""

import subprocess
import sys
import time
import webbrowser
import os
from threading import Timer

def install_requirements():
    """Install required Python packages"""
    print("🔧 Installing required packages...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], 
                      check=True, capture_output=True, text=True)
        print("✅ Packages installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install packages: {e}")
        return False

def start_backend_server():
    """Start the Flask backend server"""
    print("🚀 Starting backend API server...")
    try:
        # Start the Flask app
        subprocess.Popen([sys.executable, 'app.py'])
        print("✅ Backend server started on http://localhost:5000")
        return True
    except Exception as e:
        print(f"❌ Failed to start backend server: {e}")
        return False

def open_dashboard():
    """Open the dashboard in the default web browser"""
    print("🌐 Opening dashboard in browser...")
    try:
        # Get the absolute path to the HTML file
        html_path = os.path.abspath('index.html')
        webbrowser.open(f'file://{html_path}')
        print("✅ Dashboard opened in browser")
    except Exception as e:
        print(f"❌ Failed to open dashboard: {e}")
        print(f"📁 Please manually open: {html_path}")

def main():
    """Main startup function"""
    print("=" * 60)
    print("🎮 CYBERPUNK NETWORK SECURITY DASHBOARD")
    print("=" * 60)
    print()
    
    # Check if we're in the right directory
    if not os.path.exists('app.py'):
        print("❌ Error: app.py not found. Please run this script from the project directory.")
        return
    
    # Install requirements
    if not install_requirements():
        return
    
    # Start backend server
    if not start_backend_server():
        return
    
    # Wait a moment for server to start
    print("⏳ Waiting for server to initialize...")
    time.sleep(3)
    
    # Open dashboard
    open_dashboard()
    
    print()
    print("=" * 60)
    print("🎯 DASHBOARD READY!")
    print("=" * 60)
    print("📡 Backend API: http://localhost:5000")
    print("🌐 Dashboard: Open index.html in your browser")
    print()
    print("🔧 Available API Endpoints:")
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
    print()
    print("⚠️  Note: Some attacks require root privileges")
    print("⚠️  Use responsibly and only on networks you own")
    print()
    print("Press Ctrl+C to stop the server")
    
    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Shutting down...")
        print("✅ Dashboard stopped")

if __name__ == "__main__":
    main()