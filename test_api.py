#!/usr/bin/env python3
"""
Test script for Cyberpunk Network Security Dashboard API
Verifies that all endpoints are working correctly
"""

import requests
import json
import time
import sys

API_BASE = "http://localhost:5000/api"

def test_endpoint(method, endpoint, data=None, expected_status=200):
    """Test a single API endpoint"""
    url = f"{API_BASE}{endpoint}"
    
    try:
        if method.upper() == "GET":
            response = requests.get(url, timeout=10)
        elif method.upper() == "POST":
            response = requests.post(url, json=data, timeout=10)
        else:
            print(f"❌ Unsupported method: {method}")
            return False
        
        if response.status_code == expected_status:
            print(f"✅ {method} {endpoint} - Status: {response.status_code}")
            try:
                result = response.json()
                if isinstance(result, dict) and 'error' in result:
                    print(f"   ⚠️  API returned error: {result['error']}")
                return True
            except:
                print(f"   📄 Response: {response.text[:100]}...")
                return True
        else:
            print(f"❌ {method} {endpoint} - Expected: {expected_status}, Got: {response.status_code}")
            print(f"   📄 Response: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print(f"❌ {method} {endpoint} - Connection failed (server not running?)")
        return False
    except requests.exceptions.Timeout:
        print(f"❌ {method} {endpoint} - Timeout")
        return False
    except Exception as e:
        print(f"❌ {method} {endpoint} - Error: {e}")
        return False

def main():
    """Run all API tests"""
    print("🧪 Testing Cyberpunk Network Security Dashboard API")
    print("=" * 60)
    
    # Wait for server to be ready
    print("⏳ Waiting for server to be ready...")
    for i in range(10):
        try:
            response = requests.get(f"{API_BASE}/status", timeout=5)
            if response.status_code == 200:
                print("✅ Server is ready!")
                break
        except:
            if i == 9:
                print("❌ Server not responding after 10 attempts")
                print("   Please make sure the Flask server is running:")
                print("   python app.py")
                return
            time.sleep(1)
    
    print()
    print("🔍 Testing API Endpoints...")
    print()
    
    # Test endpoints
    tests = [
        ("GET", "/status"),
        ("POST", "/networks/scan", {"ip_range": "192.168.1.0/24", "timeout": 1}),
        ("GET", "/operations"),
        ("GET", "/logs"),
        ("POST", "/attack/arp_spoofing", {"target_ip": "192.168.1.100", "host_ip": "192.168.1.1", "interface": "eth0"}),
        ("POST", "/attack/mitm", {"target_ip": "192.168.1.100", "gateway_ip": "192.168.1.1", "interface": "eth0"}),
        ("POST", "/attack/password_sniffing", {"interface": "eth0"}),
        ("POST", "/attack/flood", {"type": "syn_flood", "target_ip": "192.168.1.100", "target_port": 80, "interface": "eth0"}),
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if len(test) == 2:
            method, endpoint = test
            data = None
        else:
            method, endpoint, data = test
        
        if test_endpoint(method, endpoint, data):
            passed += 1
        print()
    
    print("=" * 60)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! API is working correctly.")
    else:
        print("⚠️  Some tests failed. Check the output above for details.")
    
    print()
    print("🌐 Dashboard should be accessible at: file:///path/to/index.html")
    print("📡 API documentation available at: http://localhost:5000")

if __name__ == "__main__":
    main()