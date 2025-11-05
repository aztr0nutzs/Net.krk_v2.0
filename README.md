# 🎮 Cyberpunk Network Security Dashboard

A futuristic, dark-themed network security dashboard with real API integration and 3D network visualization. This dashboard provides a cyberpunk-styled interface for network scanning, device discovery, and security testing tools.

## ✨ Features

### 🎨 Cyberpunk UI Design
- **Dark Theme**: Black/near-black background with neon accents
- **Neon Colors**: Cyan, magenta, violet, and green glow effects
- **Futuristic Typography**: Orbitron and Rajdhani fonts
- **Smooth Animations**: Hover effects, glitch animations, and transitions
- **3D Network Map**: Interactive Three.js visualization

### 🔧 Real API Integration
- **No Mock Data**: All functions connect to actual backend endpoints
- **Network Discovery**: Real network scanning using existing Python tools
- **Attack Modules**: Integration with all security testing tools
- **Live Status Updates**: Real-time system monitoring
- **Operation Tracking**: Active operation management

### 🛠️ Available Tools
- **Network Scanning**: ARP-based device discovery
- **ARP Spoofing**: Man-in-the-middle attacks
- **Password Sniffing**: Network traffic monitoring
- **Flood Attacks**: SYN, UDP, ICMP, and HTTP floods
- **DNS Spoofing**: Domain redirection attacks
- **SSL Stripping**: HTTPS downgrade attacks

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip (Python package manager)
- Modern web browser with WebGL support

### Installation

1. **Clone or download the project files**

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the dashboard:**
   ```bash
   python start_dashboard.py
   ```

   Or manually:
   ```bash
   # Start backend server
   python app.py
   
   # Open index.html in your browser
   ```

### Testing the API

Run the test script to verify all endpoints:
```bash
python test_api.py
```

## 📁 Project Structure

```
cyberpunk-dashboard/
├── app.py                 # Flask backend API server
├── index.html            # Main dashboard HTML
├── styles.css            # Cyberpunk CSS styling
├── dashboard.js          # Frontend JavaScript with 3D visualization
├── requirements.txt      # Python dependencies
├── start_dashboard.py    # Startup script
├── test_api.py          # API testing script
├── README.md            # This file
└── [attack_modules].py  # Existing Python security tools
```

## 🔌 API Endpoints

### System Status
- `GET /api/status` - Get system status and active operations
- `GET /api/logs` - Get system logs and events

### Network Operations
- `POST /api/networks/scan` - Scan network for devices
- `GET /api/networks/<id>/devices` - Get devices from a scan
- `GET /api/devices/<ip>` - Get detailed device information

### Attack Operations
- `POST /api/attack/arp_spoofing` - Start ARP spoofing attack
- `POST /api/attack/mitm` - Start MITM attack
- `POST /api/attack/password_sniffing` - Start password sniffing
- `POST /api/attack/flood` - Start flood attacks (SYN, UDP, ICMP, HTTP)

### Operation Management
- `GET /api/operations` - Get all active operations
- `POST /api/operations/<id>/stop` - Stop an active operation

## 🎯 Usage Guide

### 1. Network Discovery
1. Enter an IP range (e.g., `192.168.1.0/24`)
2. Click "SCAN NETWORK"
3. Watch devices appear in the 3D network map
4. Click on devices to view details

### 2. Attack Execution
1. Select a device from the network map
2. Choose an attack type from the right panel
3. Configure attack parameters in the modal
4. Confirm and execute the attack
5. Monitor progress in the operations list

### 3. 3D Network Visualization
- **Rotate**: Click and drag to rotate the view
- **Zoom**: Scroll to zoom in/out
- **Pan**: Right-click and drag to pan
- **Reset**: Click "RESET VIEW" to return to default
- **Wireframe**: Toggle wireframe mode
- **Labels**: Toggle device labels

## ⚠️ Important Notes

### Security & Legal
- **Authorized Use Only**: Only use on networks you own or have explicit permission to test
- **Root Privileges**: Some attacks require root/sudo privileges
- **Responsible Disclosure**: Report vulnerabilities through proper channels
- **Legal Compliance**: Ensure compliance with local laws and regulations

### Technical Requirements
- **Network Interface**: Attacks require appropriate network interfaces
- **Permissions**: Some operations need elevated privileges
- **Firewall**: Ensure firewall allows necessary connections
- **Dependencies**: All Python packages must be installed

## 🐛 Troubleshooting

### Common Issues

**"Connection failed" errors:**
- Ensure the Flask server is running (`python app.py`)
- Check that port 5000 is not blocked
- Verify the API base URL in `dashboard.js`

**3D visualization not working:**
- Ensure your browser supports WebGL
- Check browser console for Three.js errors
- Try a different browser (Chrome/Firefox recommended)

**Attacks not executing:**
- Check if you have the required permissions
- Verify network interface names (eth0, wlan0, etc.)
- Check the backend logs for error messages

**Scan results not appearing:**
- Ensure the target network is reachable
- Check if ARP scanning is allowed on your network
- Verify the IP range format (e.g., 192.168.1.0/24)

### Debug Mode

Enable debug mode in `app.py`:
```python
app.run(host='0.0.0.0', port=5000, debug=True)
```

Check browser console for JavaScript errors and network requests.

## 🔧 Customization

### Adding New Attack Types
1. Add the attack function to `app.py`
2. Create a new endpoint in the Flask app
3. Add the attack button to `index.html`
4. Implement the attack form in `dashboard.js`
5. Add the attack execution logic

### Modifying the UI
- Edit `styles.css` for visual changes
- Modify `index.html` for layout changes
- Update `dashboard.js` for functionality changes

### API Extensions
- Add new endpoints in `app.py`
- Update the frontend to call new endpoints
- Add corresponding UI elements

## 📄 License

This project is for educational and authorized security testing purposes only. Users are responsible for complying with applicable laws and regulations.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For issues and questions:
1. Check the troubleshooting section
2. Review the API test results
3. Check browser and server logs
4. Ensure all dependencies are installed

---

**⚠️ Disclaimer**: This tool is designed for authorized security testing only. Unauthorized use on networks you don't own is illegal and unethical. Use responsibly!