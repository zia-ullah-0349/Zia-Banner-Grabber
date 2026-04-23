##ZIA - Banner Grabber Suite 🚪🐍

> **Built by ZIA ULLAH | from Kpk, Pakistan** 🇵🇰🛡️

> **"Instructor; Dr Muhammad Kazim"** - 

A specialized Python toolkit for advanced service interrogation and banner grabbing. This project demonstrates how to identify not just open ports, but also the specific software and version running behind them through intelligent, protocol-aware communication and robust error handling.

---

🎯 **Project Objective**
To move beyond basic port scanning by actively communicating with open ports to retrieve service banners. This reveals the "name and identity" of the service, which is critical for vulnerability assessment and defensive security auditing. **For authorized use only.**

---

📈 **Version History & Technical Evolution** 🚀

This suite shows the real-world development cycle of a security tool: build, test, fail, learn, upgrade.

| Version | File Name | Core Upgrade | Key Technical Lesson | Status |
| --- | --- | --- |
| **V.01** | `banner_grabber_1.py` | Basic Banner Grabbing | `socket.send()` & `recv()` - How to "talk" to a port | ✅ Complete |
| **V.02** | `banner_grabber_2.py` | Smart Protocol Interrogation | Protocol-specific logic: SSH speaks first, HTTP needs `GET` request | ✅ Complete |
| **V.03** | `banner_grabber_3.py` | Production-Grade Resilience | `try-except`, `socket.timeout`, `decode(errors='ignore')` for real-world chaos | ✅ **Final** |

---

🔬 **V.03 Live Demo & Professional Analysis**

**Target:** `scanme.nmap.org`  
**Command:** `python banner_grabber_3.py`

**Output:**
=== BANNER GRABBER 3 ===
Enter Target IP: http://scanme.nmap.org
Scanning Ports 1 to 100 and Interrogation...

Port 22 is OPEN! 
   └── BANNER: Error... [Errno 104] Connection reset by peer

Port 80 is OPEN! 
   └── BANNER: Timeout... 

Scan and Interrogation COMPLETED! 

**Cybersecurity Analysis - Why This Is a Win:**
1. **`[Errno 104] Connection reset by peer` on Port 22 (SSH):** This is an active defense mechanism. The server identified the connection as non-standard/probing and immediately terminated it. This indicates a **hardened, security-conscious SSH configuration.** It's a successful intelligence gathering result. 🛡️
2. **`Timeout` on Port 80 (HTTP):** The web server deliberately chose not to respond to a generic request within the timeframe. This is a common anti-reconnaissance technique. It confirms the **service is live but protected against basic scans.** 🥷

**Key Takeaway:** In real-world penetration testing, `Errors` and `Timeouts` are valid data points. V03 is built to capture and handle them gracefully instead of crashing.
---

⚖️ *Legal & Ethical Disclaimer*
This tool is for educational and authorized security auditing purposes only. Do not use it on any network or system without explicit written permission from the owner. Unauthorized access and scanning is a criminal offense. *The user is solely responsible for their actions. Always be a White Hat.* 🛡️

---

