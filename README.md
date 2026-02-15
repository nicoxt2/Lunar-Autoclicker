# Lunar Autoclicker

> A powerful, lightweight autoclicker with a modern UI. Click faster, automate repetitive tasks, and take control.

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)
![Platform](https://img.shields.io/badge/platform-Windows-blue.svg)

---

## 🚀 Features

- **Multiple Click Types**: Left, right, and middle mouse button support
- **Adjustable Speed**: Control clicks per second (1-200 CPS) with precision
- **Custom Hotkeys**: Assign any keyboard key to start/stop clicking
- **Global Shortcuts**: Hotkeys work even when the app is in the background
- **Modern UI**: Dark theme with neon accents for a sleek experience
- **Real-time Status**: Live feedback on clicking status
- **Lightweight**: Small file size, minimal resource usage
- **Standalone EXE**: No Python installation required

---

## 📋 System Requirements

### To Run the EXE:
- **Windows** (7, 8, 10, 11)
- **RAM**: 50MB minimum
- **Processor**: Any modern processor
- **No Python installation required**

### To Run from Source (.py):
- **Python 3.7+**
- **pynput** library
- **tkinter** (usually included with Python)

---

## 💻 Installation

### Option 1: Use the EXE (Recommended)
1. Download `AutoClicker Pro.exe` from the releases
2. Double-click to run
3. No installation needed!

### Option 2: Run from Source
```bash
# Clone or download the repository
cd autoclicker

# Install required dependencies
pip install pynput

# Run the application
python autoclicker.py
```

### Option 3: Build Your Own EXE
```bash
# Install PyInstaller
pip install pyinstaller pynput

# Navigate to the directory with autoclicker.py
cd your/path/to/autoclicker

# Build the EXE
pyinstaller --onefile --windowed --name="AutoClicker Pro" autoclicker.py

# Find your EXE in the 'dist' folder
```

---

## 🎮 How to Use

### Basic Setup
1. **Launch** the AutoClicker Pro application
2. **Select Click Type**: Choose between Left, Right, or Middle click
3. **Adjust Speed**: Use the slider to set clicks per second (1-50 CPS)
4. **Configure Hotkeys**: 
   - Click the "START Key" button and press the key you want to start clicking
   - Click the "STOP Key" button and press the key you want to stop clicking
5. **Start Clicking**: Press the START button or your configured hotkey

### Controls
| Action | Default | Customizable |
|--------|---------|--------------|
| Start Clicking | F6 | Yes ✓ |
| Stop Clicking | F7 | Yes ✓ |
| Click Type | Left | Yes ✓ |
| Speed (CPS) | 10 | Yes ✓ (1-200) |

### Status Indicators
- 🟢 **RUNNING** - AutoClicker is actively clicking
- ⚫ **STOPPED** - AutoClicker is idle

---

## ⚙️ Configuration

### Click Types
- **Left Click** (🖱): Standard left mouse button click
- **Right Click** (🖱): Right mouse button click (context menu)
- **Middle Click** (🖱): Middle mouse button click

### Speed Settings
- **Min**: 1 CPS (1 click per second)
- **Max**: 200 CPS (200 clicks per second)
- **Recommended**: 10-20 CPS for most tasks

### Hotkey Examples
- **F6** - Function key
- **a** - Letter key
- **space** - Space bar
- **enter** - Return key
- **1** - Number key

---

## 🎯 Use Cases

### Gaming
- Auto-farming in MMORPGs
- Rapid clicking in clicker games
- Faster inventory management
- AFK activities (with appropriate games)

### Productivity
- Automating repetitive clicking tasks
- Mass form filling
- Testing user interfaces
- Data entry acceleration

### General Tasks
- Batch processing
- Rapid response testing
- Accessibility automation
- Workflow optimization

---

## ⚠️ Safety & Ethical Usage

### ✅ Safe Uses
- Personal productivity and accessibility
- Testing and development
- Single-player gaming
- Legitimate automation tasks

### ❌ Not Recommended For
- Online multiplayer games (may violate ToS)
- Unauthorized access to systems
- Spam or malicious activities
- Any use that violates terms of service

**Always respect the terms of service of applications you use.**

---

## 🐛 Troubleshooting

### Issue: "EXE doesn't start"
**Solution**: 
- Make sure Windows Defender or antivirus isn't blocking it
- Try running as Administrator
- Check that you downloaded the latest version

### Issue: "Clicks don't register"
**Solution**:
- Ensure the target window is in focus
- Check that the CPS value isn't too high (try 10-20)
- Some applications require administrator privileges (right-click → Run as Administrator)

### Issue: "Hotkeys not working"
**Solution**:
- Make sure you assigned a valid hotkey (click the buttons and press a key)
- Some keys may be reserved by your system
- Try different keys like F6, F7, F8, etc.

### Issue: "Module not found: pynput"
**Solution**:
```bash
pip install pynput --upgrade
```

### Issue: "ModuleNotFoundError: No module named 'tkinter'"
**Solution**:
- **Windows**: Tkinter usually comes with Python, reinstall Python and check "TCL/TK and IDLE" box
- **Linux**: `sudo apt-get install python3-tk`
- **Mac**: `brew install python-tk`

---

## 🔧 Advanced: Building from Source

### Build for Windows EXE
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=icon.ico autoclicker.py
```

### Build with Custom Icon
1. Prepare a `.ico` file (use online converters)
2. Place it in the same directory as the script
3. Run:
```bash
pyinstaller --onefile --windowed --icon=myicon.ico autoclicker.py
```

### Minimize File Size
```bash
pyinstaller --onefile --windowed --noupx autoclicker.py
```

---

## 📊 Performance

| Metric | Value |
|--------|-------|
| Startup Time | < 1 second |
| Memory Usage | ~30-50 MB |
| EXE File Size | ~30 MB |
| Max CPS | 200 (configurable) |
| Supported Windows | 7, 8, 10, 11 |

---

## 🎨 UI Features

- **Dark Theme**: Easy on the eyes, modern aesthetic
- **Neon Accents**: Pink (#ff006e) and cyan (#00d9ff) highlights
- **Responsive**: Smooth button interactions and status updates
- **Intuitive Layout**: Clear sections for configuration

---

## 🔐 Security & Privacy

- **No Internet Connection**: Works completely offline
- **No Data Collection**: All operations are local
- **No Logging**: Your clicks and hotkeys are never recorded
- **Source Code Available**: Full transparency on what the app does

---

## 📝 Limitations

- **Windows Only**: Currently supports Windows 7 and later
- **Single Window**: One instance at a time
- **Max Speed**: Limited to 200 CPS for stability
- **No Recording**: Cannot record and replay sequences (yet)

---

## 🤝 Contributing

Found a bug? Have a feature request?
1. Check existing issues
2. Create a detailed bug report with:
   - Your Windows version
   - Steps to reproduce
   - Expected vs. actual behavior
   - Screenshots if applicable

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

**MIT License**: Free to use, modify, and distribute

---

## 🙏 Acknowledgments

- Built with **Python** and **Tkinter**
- Mouse/Keyboard control via **pynput**
- Distributed with **PyInstaller**

---

## 📞 Support

Having issues? Try these resources:

1. **Check the Troubleshooting section** above
2. **Read the INSTRUCCIONES_EXE.txt** file
3. **Verify your Windows version** is supported
4. **Try running as Administrator**

---

## 🚀 Future Roadmap

- [ ] Macro recording and playback
- [ ] Multi-click sequences
- [ ] Custom click patterns
- [ ] Statistics and analytics
- [ ] Dark/Light theme toggle
- [ ] Mac and Linux support
- [ ] Cloud configuration sync

---

## 📦 Version History

### v1.0.0 (Current)
- ✅ Initial release
- ✅ Basic clicking functionality
- ✅ Custom hotkey support
- ✅ Modern UI design
- ✅ Standalone EXE distribution

---

## ⭐ Quick Tips

1. **Start slow**: Begin with 10-15 CPS and increase gradually
2. **Test first**: Always test with a text editor before using in games
3. **Use F-keys**: F6 and F7 are less likely to conflict with other apps
4. **Admin rights**: Run as Administrator for better compatibility
5. **Safe defaults**: The default settings (F6/F7, 10 CPS, Left Click) are safe

---

## 🎓 FAQ

**Q: Is this legal?**  
A: Yes, using autoclickers is legal. However, using them against the Terms of Service of applications (like online games) may result in account bans.

**Q: Can I use this in online games?**  
A: Most online games prohibit autoclickers. Use at your own risk.

**Q: How fast can it click?**  
A: Up to 50 CPS, though system limitations may prevent registering every click.

**Q: Does it work in all programs?**  
A: Works in most programs, but some have click detection that may prevent it from working.

**Q: Can I run multiple instances?**  
A: Yes, you can open the EXE multiple times for different hotkeys/speeds.

**Q: Is my data safe?**  
A: Completely safe. The app doesn't collect or transmit any data.

---

## 💡 Ideas for Users

- **Productivity**: Automate repetitive web form filling
- **Gaming**: AFK mining/farming in single-player games
- **Testing**: Automated UI testing for developers
- **Accessibility**: Assist users with limited mobility
- **Learning**: Great project for Python beginners to understand threading and UI

---

**Made with ❤️ for automation enthusiasts**

---

*Last Updated: 2026*  
*AutoClicker Pro v1.0.0*
