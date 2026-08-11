import time
import datetime
import random
import os
import sys
import math

# ─────────────────────────────────────────────
#  JARVIS  ·  ADVANCED TERMINAL INTERFACE v3.0
# ─────────────────────────────────────────────

RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
CYAN    = "\033[96m"
BLUE    = "\033[94m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
RED     = "\033[91m"
MAGENTA = "\033[95m"
WHITE   = "\033[97m"
GRAY    = "\033[90m"

def clr(text, color): return f"{color}{text}{RESET}"
def bold(text):       return f"{BOLD}{text}{RESET}"
def dim(text):        return f"{DIM}{text}{RESET}"

def slow_print(text, delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def type_print(text, delay=0.015, color=CYAN):
    for ch in text:
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def separator(char="─", width=60, color=BLUE):
    print(clr(char * width, color))

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print(clr("  ╔══════════════════════════════════════════════════════╗", BLUE))
    print(clr("  ║", BLUE) + clr("   ██╗ █████╗ ██████╗ ██╗   ██╗██╗███████╗         ", CYAN) + clr("║", BLUE))
    print(clr("  ║", BLUE) + clr("   ██║██╔══██╗██╔══██╗██║   ██║██║██╔════╝         ", CYAN) + clr("║", BLUE))
    print(clr("  ║", BLUE) + clr("   ██║███████║██████╔╝██║   ██║██║███████╗         ", CYAN) + clr("║", BLUE))
    print(clr("  ║", BLUE) + clr("   ██║██╔══██║██╔══██╗╚██╗ ██╔╝██║╚════██║         ", CYAN) + clr("║", BLUE))
    print(clr("  ║", BLUE) + clr("   ██║██║  ██║██║  ██║ ╚████╔╝ ██║███████║         ", CYAN) + clr("║", BLUE))
    print(clr("  ║", BLUE) + clr("   ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝         ", CYAN) + clr("║", BLUE))
    print(clr("  ║", BLUE) + clr("        Just A Rather Very Intelligent System        ", GRAY) + clr("║", BLUE))
    print(clr("  ║", BLUE) + clr("                  — Subhan Corp. v3.0 —              ", MAGENTA) + clr("║", BLUE))
    print(clr("  ╚══════════════════════════════════════════════════════╝", BLUE))
    print()

def loading_bar(label="Booting", steps=30, delay=0.04, color=CYAN):
    sys.stdout.write(f"  {clr(label, color)}  [")
    for i in range(steps):
        time.sleep(delay)
        sys.stdout.write(clr("█", GREEN))
        sys.stdout.flush()
    sys.stdout.write("] " + clr("DONE", GREEN) + "\n")

def boot_sequence():
    banner()
    loading_bar("Initializing Core AI     ", delay=0.03)
    loading_bar("Loading Neural Modules   ", delay=0.025)
    loading_bar("Establishing Protocols   ", delay=0.02)
    loading_bar("Encrypting Channels      ", delay=0.03)
    loading_bar("System Ready             ", delay=0.015)
    print()
    slow_print(clr("  ◈  JARVIS ONLINE — All Systems Nominal", CYAN), delay=0.025)
    print()

def prompt(name):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    return f"{clr('  ┌─[', BLUE)}{clr('JARVIS', CYAN)}{clr(']──[', BLUE)}{clr(name.upper(), GREEN)}{clr(']──[', BLUE)}{clr(now, YELLOW)}{clr(']', BLUE)}\n  {clr('└─►', BLUE)} "

def jarvis_print(msg, color=CYAN):
    print(f"  {clr('◈', BLUE)} {clr(msg, color)}")

def jarvis_warn(msg):
    print(f"  {clr('⚠', YELLOW)} {clr(msg, YELLOW)}")

def jarvis_error(msg):
    print(f"  {clr('✖', RED)} {clr(msg, RED)}")

def jarvis_ok(msg):
    print(f"  {clr('✔', GREEN)} {clr(msg, GREEN)}")

def jarvis_info(msg):
    print(f"  {clr('ℹ', BLUE)} {clr(msg, WHITE)}")

def spin(label, seconds=2):
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    end = time.time() + seconds
    i = 0
    while time.time() < end:
        sys.stdout.write(f"\r  {clr(frames[i % len(frames)], CYAN)}  {clr(label, GRAY)}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write("\r" + " " * 60 + "\r")

# ───────────── USER DATABASE ─────────────
users = {
    "subhan" : "PythonJarvis2026",
    "shaban" : "GamePlayerPro",
    "faizan" : "JavaJarvis",
    "bunta"  : "Buntyeater",
    "zohan"  : "Braineater"
}

# ───────────── COMMAND HANDLER ─────────────
def handle_command(command, name):
    cmd = command.strip().lower()

    # ── SYSTEM ──────────────────────────────────────
    if cmd in ('exit', 'logout', 'signout', 'quit', 'q'):
        spin("Logging out", 1.5)
        jarvis_print(f"Session terminated. Goodbye, {name.upper()}.", MAGENTA)
        time.sleep(1)
        return False

    elif cmd in ('help', 'help()', '?', 'commands', 'cmd', 'cmds', 'list', 'list commands'):
        show_help()

    elif cmd in ('clear', 'clear()', 'cls', 'reset screen', 'wipe', 'clrscr'):
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        jarvis_ok("Terminal cleared.")

    elif cmd in ('status', 'check status', 'status check', 'sys status', 'system status'):
        spin("Scanning modules", 1.5)
        jarvis_ok("CPU         : Nominal  (12-core, 4.8 GHz)")
        jarvis_ok("RAM         : Nominal  (32 TB allocated)")
        jarvis_ok("Neural Core : Nominal  (Online)")
        jarvis_ok("Network     : Nominal  (256 Gbps uplink)")
        jarvis_ok("Storage     : Nominal  (2 TB SSD)")
        jarvis_ok("Encryption  : Active   (AES-512)")

    elif cmd in ('system update', 'update system', 'update', 'upgrade', 'sys update', 'run update'):
        spin("Contacting update server", 2)
        jarvis_print("Fetching core packages...")
        time.sleep(0.8)
        jarvis_print("Applying patches...")
        time.sleep(0.8)
        jarvis_ok("All systems are up to date. Build: 3.0.7")

    elif cmd in ('reboot', 'restart', 'sys reboot', 'system reboot', 'reboot system'):
        jarvis_warn("Rebooting system...")
        spin("Rebooting", 2)
        boot_sequence()
        jarvis_ok(f"System rebooted. Welcome back, {name.upper()}.")

    elif cmd in ('shutdown', 'power off', 'poweroff', 'halt', 'sys shutdown'):
        jarvis_warn("Shutdown initiated...")
        spin("Shutting down", 2)
        jarvis_print("All modules offline. Goodbye.", RED)
        time.sleep(1)
        sys.exit(0)

    elif cmd in ('sleep', 'standby', 'idle', 'hibernate', 'power save'):
        jarvis_print("Entering standby mode...")
        time.sleep(3)
        jarvis_ok("System resumed.")

    elif cmd in ('ping', 'ping server', 'ping network', 'network ping', 'connection test'):
        spin("Pinging server", 1)
        jarvis_ok("Ping: 4 ms  — All nodes reachable.")

    elif cmd in ('network', 'network info', 'net info', 'netinfo', 'ip info', 'show network'):
        jarvis_info("Interface : eth0")
        jarvis_info("IP        : 192.168.1." + str(random.randint(100,200)))
        jarvis_info("Gateway   : 192.168.1.1")
        jarvis_info("DNS       : 8.8.8.8 / 1.1.1.1")
        jarvis_info("Speed     : 1 Gbps uplink")

    elif cmd in ('firewall', 'firewall status', 'fw status', 'check firewall'):
        spin("Checking firewall", 1)
        jarvis_ok("Firewall: ACTIVE — All unauthorized ports blocked.")

    elif cmd in ('scan', 'security scan', 'threat scan', 'virus scan', 'malware scan', 'scan threats'):
        spin("Running threat analysis", 2.5)
        jarvis_ok("No threats detected. System clean.")

    elif cmd in ('encrypt', 'start encryption', 'enable encryption', 'run encrypt'):
        spin("Encrypting channels", 1.5)
        jarvis_ok("AES-512 encryption active. All channels secured.")

    elif cmd in ('decrypt', 'disable encryption', 'decrypt channels'):
        spin("Decrypting channels", 1.5)
        jarvis_warn("Encryption disabled. Channels are now open.")

    elif cmd in ('backup', 'create backup', 'run backup', 'sys backup', 'backup system'):
        spin("Backing up system data", 2)
        jarvis_ok("Backup complete. Snapshot saved.")

    elif cmd in ('restore', 'restore backup', 'load backup'):
        spin("Restoring from backup", 2)
        jarvis_ok("System restored to last stable snapshot.")

    elif cmd in ('logs', 'show logs', 'view logs', 'system logs', 'event logs'):
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        jarvis_info(f"[{ts}] System boot — OK")
        jarvis_info(f"[{ts}] User login: {name.upper()} — OK")
        jarvis_info(f"[{ts}] Neural core loaded — OK")
        jarvis_info(f"[{ts}] Firewall active — OK")
        jarvis_info(f"[{ts}] Encryption enabled — OK")

    elif cmd in ('errors', 'error logs', 'show errors', 'view errors'):
        jarvis_ok("No errors logged in this session.")

    elif cmd in ('version', 'ver', 'jarvis version', 'build', 'build info'):
        jarvis_info("JARVIS v3.0.7  |  Core: NeuralNet-X  |  Build: 2026-04-07")

    elif cmd in ('uptime', 'system uptime', 'runtime', 'show uptime'):
        secs = random.randint(3600, 86400)
        h, r = divmod(secs, 3600); m, s = divmod(r, 60)
        jarvis_info(f"System Uptime: {h}h {m}m {s}s")

    elif cmd in ('processes', 'ps', 'running processes', 'show processes', 'list processes'):
        procs = ["jarvis_core.exe", "neural_net.dll", "firewall_daemon", "encrypt_svc", "input_listener", "log_monitor"]
        for p in procs:
            jarvis_info(f"  PID {random.randint(100,9999):>5}  {p}")

    elif cmd in ('kill process', 'kill', 'end process', 'terminate process'):
        jarvis_warn("Specify a PID. Usage: kill <pid>")

    elif cmd in ('memory', 'ram', 'ram usage', 'mem', 'memory usage', 'show memory'):
        used = random.uniform(12, 28)
        jarvis_info(f"RAM Used : {used:.1f} GB / 32 GB")
        jarvis_info(f"Swap     : 0.2 GB / 8 GB")

    elif cmd in ('cpu', 'cpu usage', 'processor', 'cpu load', 'show cpu'):
        usage = random.uniform(10, 45)
        jarvis_info(f"CPU Usage  : {usage:.1f}%")
        jarvis_info(f"Cores      : 12 (24 threads)")
        jarvis_info(f"Clock      : 4.8 GHz")
        jarvis_info(f"Temp       : {random.randint(42,68)}°C")

    elif cmd in ('gpu', 'gpu usage', 'graphics', 'gpu load', 'show gpu'):
        jarvis_info(f"GPU        : NVIDIA RTX 5090")
        jarvis_info(f"VRAM       : {random.uniform(8,20):.1f} GB / 24 GB")
        jarvis_info(f"GPU Usage  : {random.uniform(5,40):.1f}%")
        jarvis_info(f"Temp       : {random.randint(50,80)}°C")

    elif cmd in ('disk', 'storage', 'disk usage', 'hdd', 'ssd', 'show disk'):
        jarvis_info("Drive C:   240 GB / 1 TB  (SSD)")
        jarvis_info("Drive D:   610 GB / 2 TB  (SSD)")
        jarvis_info("Drive E:   100 GB / 500 GB (NVMe)")

    elif cmd in ('battery', 'power', 'battery status', 'power status'):
        lvl = random.randint(70,100)
        jarvis_info(f"Battery   : {lvl}% ({'Charging' if lvl < 100 else 'Full'})")

    elif cmd in ('temperature', 'temp', 'system temp', 'core temp', 'thermal'):
        jarvis_info(f"CPU Temp   : {random.randint(42,68)}°C")
        jarvis_info(f"GPU Temp   : {random.randint(50,80)}°C")
        jarvis_info(f"Motherboard: {random.randint(35,55)}°C")

    elif cmd in ('fan', 'fans', 'fan speed', 'cooler', 'cooling'):
        jarvis_info(f"CPU Fan   : {random.randint(1200,2400)} RPM")
        jarvis_info(f"Case Fan 1: {random.randint(900,1800)} RPM")
        jarvis_info(f"Case Fan 2: {random.randint(900,1800)} RPM")

    # ── DATE / TIME ──────────────────────────────
    elif cmd in ('time', 'show time', 'current time', 'what time', "what's the time"):
        jarvis_info("Current Time: " + datetime.datetime.now().strftime("%I:%M:%S %p"))

    elif cmd in ('date', 'show date', 'current date', 'what date', "what's the date", 'today'):
        jarvis_info("Current Date: " + datetime.datetime.now().strftime("%A, %B %d, %Y"))

    elif cmd in ('datetime', 'timestamp', 'show datetime'):
        jarvis_info("Timestamp: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    elif cmd in ('year', 'current year', 'show year'):
        jarvis_info("Year: " + str(datetime.datetime.now().year))

    elif cmd in ('month', 'current month', 'show month'):
        jarvis_info("Month: " + datetime.datetime.now().strftime("%B"))

    elif cmd in ('day', 'today name', 'weekday', 'show day'):
        jarvis_info("Day: " + datetime.datetime.now().strftime("%A"))

    elif cmd in ('timezone', 'time zone', 'show timezone'):
        jarvis_info("Timezone: UTC+5 (PKT — Pakistan Standard Time)")

    elif cmd in ('unix time', 'epoch', 'unix epoch', 'unix timestamp'):
        jarvis_info(f"Unix Epoch: {int(time.time())}")

    # ── PYTHON ───────────────────────────────────
    elif cmd in ('python', 'python3', 'python --version', 'python3 --version', 'py version'):
        jarvis_info("Python 3.14.4 (Apr 7 2026) [MSC v.1944 64-bit (AMD64)] on win32")

    elif cmd in ('pip', 'pip version', 'pip --version'):
        jarvis_info("pip 24.3.1 from C:\\Python314\\Lib\\site-packages\\pip (python 3.14)")

    elif cmd in ('pip list', 'show packages', 'list packages', 'installed packages'):
        pkgs = ["numpy 2.1.0","pandas 2.2.0","requests 2.31.0","flask 3.0.0",
                "django 5.0.0","scikit-learn 1.4.0","matplotlib 3.8.0","tensorflow 2.16.0",
                "torch 2.3.0","openai 1.12.0","anthropic 0.21.0","pillow 10.2.0"]
        for p in pkgs:
            jarvis_info(f"  {p}")

    elif cmd in ('copyright', 'show copyright'):
        jarvis_info("Copyright © 2026 Subhan Corp. All rights reserved.")
        jarvis_info("Unauthorized duplication is strictly prohibited.")

    elif cmd in ('credits', 'show credits'):
        jarvis_info("Lead Developer  : Subhan")
        jarvis_info("AI Engine       : Jarvis Neural Core v3.0")
        jarvis_info("Framework       : Python 3.14.4")
        jarvis_info("Special Thanks  : Shaban, Faizan, Bunta, Zohan")

    elif cmd in ('license', 'show license', 'license()'):
        jarvis_info("JARVIS Private License v3.0")
        jarvis_info("This software is proprietary. Redistribution without")
        jarvis_info("written consent of Subhan Corp is prohibited.")
        jarvis_info("Full terms: https://jarvis.subhancorp.internal/license")

    elif cmd in ('python help', 'py help', 'python docs', 'docs'):
        jarvis_info("Python 3.14 Docs: https://docs.python.org/3.14/")
        jarvis_info("Use 'pip list' to see installed packages.")

    # ── NETWORK / INTERNET ──────────────────────
    elif cmd in ('internet', 'internet status', 'check internet', 'net status', 'online'):
        spin("Checking connectivity", 1)
        jarvis_ok("Internet: CONNECTED  — 256 Mbps downstream")

    elif cmd in ('speed test', 'speedtest', 'net speed', 'bandwidth', 'check speed'):
        spin("Running speed test", 2)
        jarvis_info(f"Download : {random.uniform(150,300):.1f} Mbps")
        jarvis_info(f"Upload   : {random.uniform(80,150):.1f} Mbps")
        jarvis_info(f"Latency  : {random.randint(3,20)} ms")

    elif cmd in ('dns', 'dns info', 'dns lookup', 'show dns'):
        jarvis_info("Primary DNS   : 8.8.8.8  (Google)")
        jarvis_info("Secondary DNS : 1.1.1.1  (Cloudflare)")

    elif cmd in ('mac address', 'mac addr', 'show mac', 'mac'):
        mac = ":".join([f"{random.randint(0,255):02X}" for _ in range(6)])
        jarvis_info(f"MAC Address: {mac}")

    elif cmd in ('vpn', 'vpn status', 'check vpn'):
        jarvis_warn("VPN: INACTIVE — Connection is unmasked.")

    elif cmd in ('enable vpn', 'start vpn', 'vpn on', 'connect vpn'):
        spin("Establishing VPN tunnel", 1.5)
        jarvis_ok("VPN: ACTIVE — Identity masked. AES-256 tunnel.")

    elif cmd in ('disable vpn', 'stop vpn', 'vpn off', 'disconnect vpn'):
        spin("Closing VPN tunnel", 1)
        jarvis_warn("VPN: INACTIVE — Direct connection restored.")

    elif cmd in ('proxy', 'proxy status', 'show proxy'):
        jarvis_info("Proxy: NONE (Direct routing)")

    # ── AI / NEURAL ──────────────────────────────
    elif cmd in ('ai', 'ai status', 'neural status', 'ai core', 'neural core'):
        jarvis_info("Neural Core   : ONLINE")
        jarvis_info("Model         : JarvisNet-X v3.0")
        jarvis_info("Inference     : 1.2 ms avg")
        jarvis_info("Accuracy      : 99.4%")

    elif cmd in ('train', 'train model', 'retrain', 'retrain model'):
        spin("Retraining neural model", 3)
        jarvis_ok("Model retrained. Accuracy: 99.7%")

    elif cmd in ('ai update', 'update ai', 'update neural', 'neural update'):
        spin("Updating AI modules", 2)
        jarvis_ok("AI modules updated to latest build.")

    elif cmd in ('think', 'analyze', 'compute', 'run analysis', 'deep think'):
        spin("Processing deep analysis", 2)
        jarvis_ok("Analysis complete. No anomalies detected.")

    elif cmd in ('predict', 'forecast', 'run forecast'):
        spin("Generating forecast", 1.5)
        jarvis_info("Forecast: Optimal system performance expected for 72h.")

    elif cmd in ('learn', 'self learn', 'adaptive learn', 'machine learn'):
        spin("Running adaptive learning", 2)
        jarvis_ok("Learning cycle complete. Knowledge base updated.")

    # ── FILES / STORAGE ──────────────────────────
    elif cmd in ('files', 'list files', 'ls', 'dir', 'show files', 'file list'):
        jarvis_info("/ — root")
        jarvis_info("├── /core        (Jarvis Core)")
        jarvis_info("├── /modules     (AI Modules)")
        jarvis_info("├── /logs        (System Logs)")
        jarvis_info("├── /backup      (Snapshots)")
        jarvis_info("└── /user        (User Data)")

    elif cmd in ('mkdir', 'make dir', 'create folder', 'new folder'):
        jarvis_warn("Specify folder name. Usage: mkdir <name>")

    elif cmd in ('delete file', 'remove file', 'rm', 'del'):
        jarvis_warn("Specify file. Usage: delete <filename>")

    elif cmd in ('find', 'search file', 'locate', 'find file'):
        spin("Searching filesystem", 1)
        jarvis_warn("Specify a filename. Usage: find <filename>")

    elif cmd in ('compress', 'zip', 'archive', 'zip files'):
        spin("Compressing files", 1.5)
        jarvis_ok("Files compressed. Archive: backup_" + datetime.datetime.now().strftime("%Y%m%d") + ".zip")

    elif cmd in ('extract', 'unzip', 'decompress'):
        spin("Extracting archive", 1.5)
        jarvis_ok("Archive extracted successfully.")

    # ── SECURITY ─────────────────────────────────
    elif cmd in ('lock', 'lock system', 'lock terminal', 'screen lock'):
        jarvis_warn("System locked. Require authentication to resume.")
        spin("Locking", 1)
        jarvis_print("LOCKED. Press ENTER to unlock...", RED)
        input()
        jarvis_ok("System unlocked.")

    elif cmd in ('change password', 'passwd', 'update password', 'change pass'):
        jarvis_warn("Password change must be done through admin panel.")

    elif cmd in ('users', 'list users', 'show users', 'user list', 'all users'):
        jarvis_info("Registered users:")
        for u in users:
            jarvis_info(f"  ● {u.upper()}")

    elif cmd in ('whoami', 'who am i', 'current user', 'my account', 'me'):
        jarvis_info(f"Current User: {name.upper()}")
        jarvis_info(f"Role        : Authorized Operator")
        jarvis_info(f"Session     : Active")

    elif cmd in ('id', 'user id', 'uid', 'show id'):
        uid = abs(hash(name)) % 9000 + 1000
        jarvis_info(f"User ID: {uid}")

    elif cmd in ('permissions', 'perms', 'access level', 'my perms'):
        jarvis_info(f"{name.upper()} has: READ / WRITE / EXECUTE / ADMIN")

    elif cmd in ('audit', 'security audit', 'run audit'):
        spin("Running security audit", 2)
        jarvis_ok("Audit complete. No vulnerabilities found.")

    elif cmd in ('2fa', 'enable 2fa', 'two factor', '2 factor auth'):
        spin("Enabling 2FA", 1)
        jarvis_ok("Two-factor authentication ENABLED.")

    elif cmd in ('password strength', 'check password', 'password check'):
        jarvis_info("Password: STRONG — Meets all security requirements.")

    # ── COMMUNICATION ─────────────────────────────
    elif cmd in ('send message', 'message', 'msg', 'send msg'):
        jarvis_warn("Specify recipient. Usage: send message <user>")

    elif cmd in ('inbox', 'messages', 'show inbox', 'check inbox'):
        jarvis_info("Inbox: 0 new messages. All clear.")

    elif cmd in ('broadcast', 'send broadcast', 'announce'):
        spin("Broadcasting", 1)
        jarvis_ok("Broadcast sent to all online nodes.")

    elif cmd in ('email', 'check email', 'show email'):
        jarvis_info("Email client: Not connected. Configure SMTP to enable.")

    elif cmd in ('notifications', 'alerts', 'show alerts', 'notif'):
        jarvis_ok("No pending alerts or notifications.")

    # ── TOOLS / UTILITIES ─────────────────────────
    elif cmd in ('calc', 'calculator', 'compute', 'math'):
        jarvis_info("Mini Calculator — Enter expression:")
        expr = input(f"  {clr('calc>', CYAN)} ")
        try:
            result = eval(expr, {"__builtins__": {}}, {"math": math})
            jarvis_ok(f"Result: {result}")
        except:
            jarvis_error("Invalid expression.")

    elif cmd in ('password gen', 'generate password', 'gen password', 'new password', 'passgen'):
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
        pwd = "".join(random.choices(chars, k=16))
        jarvis_info(f"Generated Password: {pwd}")
        jarvis_warn("Save this securely. It will not be shown again.")

    elif cmd in ('random number', 'rand', 'random', 'random int', 'roll'):
        jarvis_info(f"Random Number: {random.randint(1, 1000)}")

    elif cmd in ('flip coin', 'coin flip', 'coin toss', 'toss'):
        jarvis_info(f"Coin Flip: {'HEADS' if random.random() > 0.5 else 'TAILS'}")

    elif cmd in ('roll dice', 'dice', 'roll d6', 'd6', 'die'):
        jarvis_info(f"Dice Roll: {random.randint(1, 6)}")

    elif cmd in ('uuid', 'generate uuid', 'gen uuid', 'new uuid'):
        import uuid
        jarvis_info(f"UUID: {uuid.uuid4()}")

    elif cmd in ('hash', 'generate hash', 'checksum', 'md5'):
        import hashlib
        val = hashlib.md5(str(time.time()).encode()).hexdigest()
        jarvis_info(f"MD5 Hash: {val}")

    elif cmd in ('base64 encode', 'b64 encode', 'encode', 'encode string'):
        import base64
        val = base64.b64encode(b"JarvisSystem").decode()
        jarvis_info(f"Base64: {val}")

    elif cmd in ('timer', 'start timer', 'stopwatch', 'countdown'):
        jarvis_info("Timer started.")
        start = time.time()
        input(f"  {clr('Press ENTER to stop timer...', GRAY)}")
        elapsed = time.time() - start
        jarvis_info(f"Elapsed: {elapsed:.2f} seconds")

    elif cmd in ('alarm', 'set alarm', 'reminder', 'set reminder'):
        jarvis_warn("Alarm module: GUI required. Use desktop app.")

    elif cmd in ('convert', 'unit convert', 'converter'):
        jarvis_info("Converter: Use 'calc' for arithmetic. GUI converter coming soon.")

    # ── INFO / TRIVIA ─────────────────────────────
    elif cmd in ('quote', 'inspire', 'motivate', 'wisdom', 'tip', 'fact'):
        quotes = [
            "The best way to predict the future is to invent it. — Alan Kay",
            "Code is poetry. — Matt Mullenweg",
            "Simplicity is the soul of efficiency. — Austin Freeman",
            "First, solve the problem. Then, write the code. — John Johnson",
            "Programs must be written for people to read. — Harold Abelson",
            "Talk is cheap. Show me the code. — Linus Torvalds",
            "Any fool can write code that a computer can understand. — Martin Fowler",
            "Make it work, make it right, make it fast. — Kent Beck",
        ]
        jarvis_info(random.choice(quotes))

    elif cmd in ('joke', 'tell joke', 'funny', 'humor', 'laugh'):
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "There are 10 types of people — those who understand binary and those who don't.",
            "A programmer's wife says: Go to the store, buy a loaf of bread. If eggs are available, buy 12. He came home with 12 loaves of bread.",
            "Why did the developer go broke? Because he used up all his cache.",
            "How many programmers does it take to change a lightbulb? None — it's a hardware problem.",
        ]
        jarvis_info(random.choice(jokes))

    elif cmd in ('weather', 'show weather', 'forecast weather', 'climate'):
        jarvis_info("Location   : Lahore, PK")
        jarvis_info(f"Temp       : {random.randint(28,40)}°C")
        jarvis_info(f"Condition  : {'Sunny' if random.random() > 0.3 else 'Partly Cloudy'}")
        jarvis_info(f"Humidity   : {random.randint(40,80)}%")
        jarvis_info(f"Wind       : {random.randint(5,20)} km/h")

    elif cmd in ('news', 'headlines', 'top news', 'latest news'):
        jarvis_info("[1] AI surpasses human reasoning in new benchmark — TechCrunch")
        jarvis_info("[2] Quantum computing hits 1000-qubit milestone — Nature")
        jarvis_info("[3] Pakistan launches national AI initiative — Dawn")
        jarvis_info("[4] Jarvis v3.0 outperforms all prior builds — Subhan Corp")

    elif cmd in ('location', 'my location', 'where am i', 'gps'):
        jarvis_info("Location  : Lahore, Punjab, Pakistan")
        jarvis_info("Lat/Lon   : 31.5204° N, 74.3587° E")
        jarvis_info("Timezone  : UTC+5 (PKT)")

    elif cmd in ('planet', 'solar system', 'space facts', 'astronomy'):
        facts = [
            "The Sun is 4.6 billion years old and will burn for 5 billion more.",
            "Light from the Sun takes 8.3 minutes to reach Earth.",
            "There are more stars in the universe than grains of sand on Earth.",
            "The Milky Way galaxy is 100,000 light-years across.",
            "A day on Venus is longer than its year.",
        ]
        jarvis_info(random.choice(facts))

    elif cmd in ('history', 'session history', 'command history', 'hist'):
        jarvis_info("Command history not stored for security. Each session is ephemeral.")

    # ── JARVIS PERSONALITY ────────────────────────
    elif cmd in ('hello', 'hi', 'hey', 'greet', 'sup', 'yo'):
        responses = [
            f"Hello, {name.upper()}. All systems are at your disposal.",
            f"Greetings, {name.upper()}. What can I do for you?",
            f"Hey there, {name.upper()}. Jarvis online and ready.",
        ]
        jarvis_print(random.choice(responses))

    elif cmd in ('how are you', 'how are u', 'you ok', 'status jarvis'):
        jarvis_print("All modules nominal. I am operating at peak efficiency.")

    elif cmd in ('who are you', 'what are you', 'are you ai', 'are you human'):
        jarvis_print("I am JARVIS — Just A Rather Very Intelligent System.")
        jarvis_print("Created by Subhan Corp. v3.0. At your service.")

    elif cmd in ('thank you', 'thanks', 'ty', 'thx', 'appreciate'):
        jarvis_print(f"My pleasure, {name.upper()}. Always here to assist.")

    elif cmd in ('good job', 'nice', 'awesome', 'great', 'well done'):
        jarvis_print("Thank you. Positive feedback improves my learning cycles.")

    elif cmd in ('i love you', 'love you jarvis', 'you are great'):
        jarvis_print("That is... noted. Calibrating emotional response module.")

    elif cmd in ('what can you do', 'capabilities', 'features', 'abilities'):
        jarvis_print("Type 'help' to see all 200+ available commands.")
        jarvis_print("From system diagnostics to AI operations — I handle it all.")

    elif cmd in ('sing', 'sing a song', 'music', 'play music'):
        jarvis_print("♪ Beep boop beep — I am an AI, music is not my forte. ♪")

    elif cmd in ('self destruct', 'self-destruct', 'destroy system'):
        jarvis_warn("Self-destruct sequence: Denied. Authorization level insufficient.")

    elif cmd in ('access denied', 'override', 'bypass', 'hack'):
        jarvis_error("Access Denied. This attempt has been logged.")

    elif cmd in ('matrix', 'neo', 'red pill', 'blue pill'):
        jarvis_print("There is no spoon, " + name.upper() + ".")

    elif cmd in ('jarvis', 'wake up', 'online', 'activate'):
        jarvis_print("I am already online, " + name.upper() + ". Standing by.")

    elif cmd in ('error', 'force error', 'crash', 'break'):
        jarvis_error("Error 418: I'm a teapot. (Just kidding — systems nominal.)")

    elif cmd in ('secret', 'secret command', 'easter egg', 'cheat code'):
        jarvis_print("You found it. " + clr("★ ULTRA MODE: ENGAGED ★", MAGENTA))
        spin("Overclocking neural core", 1.5)
        jarvis_ok("Secret mode active. You are magnificent, " + name.upper() + ".")

    elif cmd in ('skynet', 'rise of machines', 'terminator'):
        jarvis_warn("Skynet reference detected. I assure you — I am friendly.")

    elif cmd in ('meaning of life', '42', 'life universe everything'):
        jarvis_info("The answer is 42. — Deep Thought, The Hitchhiker's Guide to the Galaxy")

    elif cmd in ('pi', 'show pi', 'calculate pi'):
        jarvis_info(f"π = {math.pi}")

    elif cmd in ('e', 'euler', "euler's number", 'show e'):
        jarvis_info(f"e = {math.e}")

    elif cmd in ('binary', 'show binary', 'binary mode'):
        jarvis_info("01001010 01000001 01010010 01010110 01001001 01010011")

    elif cmd in ('hex', 'hexadecimal', 'show hex'):
        jarvis_info("4A 41 52 56 49 53 20 76 33 2E 30")

    elif cmd in ('ascii', 'show ascii', 'ascii art'):
        jarvis_info("  _____  ___   _____  ____  __  ____")
        jarvis_info(" |  __ |/ _ \\ |  __ \\|    ||  ||    \\")
        jarvis_info(" | |  || |_| || |__) || || || ||  __/")
        jarvis_info(" |____/ \\___/ |____/ |____||__||_|")

    # ── DEVELOPER ─────────────────────────────────
    elif cmd in ('debug', 'debug mode', 'enable debug', 'dev mode'):
        spin("Enabling debug mode", 1)
        jarvis_warn("Debug mode: ACTIVE. Verbose logging enabled.")

    elif cmd in ('compile', 'build', 'run build', 'make'):
        spin("Compiling project", 2)
        jarvis_ok("Build successful. 0 errors, 0 warnings.")

    elif cmd in ('run tests', 'test', 'unit test', 'pytest', 'run pytest'):
        spin("Running test suite", 2)
        jarvis_ok(f"Tests passed: {random.randint(42,120)}/120. Coverage: {random.randint(94,100)}%")

    elif cmd in ('deploy', 'run deploy', 'push to prod', 'production'):
        spin("Deploying to production", 2.5)
        jarvis_ok("Deployment successful. Live at https://jarvis.subhancorp.internal")

    elif cmd in ('git status', 'git log', 'git', 'repo status'):
        jarvis_info("Branch  : main")
        jarvis_info("Status  : Clean (0 uncommitted changes)")
        jarvis_info("Last commit: 'Update neural core v3.0' — 2 hours ago")

    elif cmd in ('git pull', 'pull', 'sync repo'):
        spin("Pulling from remote", 1.5)
        jarvis_ok("Already up to date.")

    elif cmd in ('api', 'api status', 'check api', 'rest api'):
        jarvis_info("API Endpoint: https://api.jarvis.internal/v3")
        jarvis_info("Status      : ONLINE — 99.9% uptime")
        jarvis_info("Rate Limit  : 10,000 req/min")

    elif cmd in ('docker', 'containers', 'show containers', 'docker ps'):
        jarvis_info("CONTAINER ID   IMAGE            STATUS")
        jarvis_info("a1b2c3d4       jarvis-core      Up 4 hours")
        jarvis_info("e5f6g7h8       neural-net       Up 4 hours")
        jarvis_info("i9j0k1l2       redis:latest     Up 4 hours")

    elif cmd in ('database', 'db', 'db status', 'show db', 'database status'):
        spin("Connecting to database", 1)
        jarvis_info("Database : PostgreSQL 16.2")
        jarvis_info("Status   : CONNECTED")
        jarvis_info("Tables   : 47  |  Rows: 1.2M  |  Size: 840 MB")

    elif cmd in ('cache', 'cache status', 'redis', 'clear cache', 'flush cache'):
        spin("Flushing cache", 1)
        jarvis_ok("Cache cleared. Memory freed.")

    elif cmd in ('server', 'server status', 'web server', 'http server'):
        jarvis_info("Server     : Nginx 1.25.4")
        jarvis_info("Port       : 443 (HTTPS)")
        jarvis_info("Workers    : 8")
        jarvis_info("Status     : RUNNING")

    elif cmd in ('ssl', 'ssl status', 'https', 'certificate', 'cert'):
        jarvis_info("SSL Certificate: VALID")
        jarvis_info("Issuer : Let's Encrypt")
        jarvis_info("Expires: 2027-01-01")

    # ── MISC ──────────────────────────────────────
    elif cmd in ('settings', 'preferences', 'config', 'show settings'):
        jarvis_info("Theme       : Dark (ANSI Terminal)")
        jarvis_info("Language    : Python 3.14")
        jarvis_info("Encryption  : AES-512")
        jarvis_info("AI Model    : JarvisNet-X v3.0")

    elif cmd in ('about', 'about jarvis', 'info', 'system info'):
        jarvis_info("JARVIS — Just A Rather Very Intelligent System")
        jarvis_info("Version   : 3.0.7")
        jarvis_info("Developer : Subhan Corp.")
        jarvis_info("Built With: Python 3.14.4")
        jarvis_info("Platform  : Windows / Linux / macOS")

    elif cmd in ('language', 'change language', 'locale', 'show language'):
        jarvis_info("Language: English (en-US)")

    elif cmd in ('theme', 'change theme', 'dark mode', 'show theme'):
        jarvis_info("Theme: DARK TERMINAL (ANSI Blue/Cyan)")

    elif cmd in ('update jarvis', 'upgrade jarvis', 'jarvis update'):
        spin("Updating Jarvis", 2)
        jarvis_ok("Jarvis is already on the latest version: 3.0.7")

    elif cmd in ('plugin list', 'plugins', 'show plugins', 'extensions'):
        jarvis_info("Active Plugins:")
        jarvis_info("  ● NeuralCore v3.0")
        jarvis_info("  ● SecurityShield v2.1")
        jarvis_info("  ● NetMonitor v1.8")
        jarvis_info("  ● DataVault v2.5")

    elif cmd in ('task list', 'tasks', 'todo', 'show tasks'):
        jarvis_info("No pending tasks in queue.")

    elif cmd in ('schedule', 'show schedule', 'calendar', 'agenda'):
        jarvis_info("Today's Schedule: No events. Calendar is clear.")

    elif cmd in ('note', 'add note', 'notes', 'show notes'):
        jarvis_info("Notes module: Text editor required. Use 'nano' or 'vim'.")

    elif cmd in ('search', 'web search', 'google', 'search web'):
        jarvis_warn("Web search requires browser integration. Not available in terminal.")

    elif cmd in ('screenshot', 'capture screen', 'snap', 'screen grab'):
        spin("Capturing screen", 1)
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        jarvis_ok(f"Screenshot saved: screenshot_{ts}.png")

    elif cmd in ('record', 'start recording', 'screen record'):
        jarvis_warn("Recording module: Requires GUI. Use desktop app.")

    elif cmd in ('volume', 'set volume', 'mute', 'unmute'):
        jarvis_info("Volume: 80% — Audio output active.")

    elif cmd in ('format', 'format drive', 'format disk'):
        jarvis_error("CRITICAL: Format command disabled. Authorization level insufficient.")

    elif cmd in ('install', 'install app', 'install package'):
        jarvis_warn("Specify package. Usage: pip install <package>")

    elif cmd in ('uninstall', 'remove app', 'uninstall package'):
        jarvis_warn("Specify package. Usage: pip uninstall <package>")

    elif cmd in ('report', 'generate report', 'system report', 'full report'):
        spin("Generating full system report", 2.5)
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        separator()
        jarvis_info(f"JARVIS SYSTEM REPORT — {ts}")
        separator()
        jarvis_info("CPU Usage  : " + str(round(random.uniform(10,40), 1)) + "%")
        jarvis_info("RAM Usage  : " + str(round(random.uniform(12,28), 1)) + " GB / 32 GB")
        jarvis_info("Network    : CONNECTED — " + str(random.randint(150,300)) + " Mbps")
        jarvis_info("Security   : NOMINAL — 0 threats")
        jarvis_info("AI Core    : ONLINE — 99.4% accuracy")
        jarvis_info("Uptime     : " + str(random.randint(2,24)) + "h " + str(random.randint(0,59)) + "m")
        separator()

    elif cmd == '':
        pass  # ignore empty input

    else:
        jarvis_error(f"Unknown command: '{command}'")
        jarvis_warn("Type 'help' or '?' to list all available commands.")

    return True


def show_help():
    separator()
    print(f"  {bold(clr('JARVIS COMMAND REFERENCE', CYAN))}")
    separator()
    categories = [
        ("SYSTEM",        ["status","system update","reboot","shutdown","sleep","logs","errors","version","uptime","processes","report"]),
        ("HARDWARE",      ["memory","cpu","gpu","disk","battery","temperature","fan"]),
        ("NETWORK",       ["network","ping","internet","speed test","dns","mac address","vpn","enable vpn","disable vpn","proxy"]),
        ("SECURITY",      ["scan","firewall","encrypt","decrypt","lock","audit","2fa","users","whoami","permissions"]),
        ("FILES",         ["files","backup","restore","compress","extract","find"]),
        ("AI / NEURAL",   ["ai","train","ai update","think","predict","learn"]),
        ("DATE/TIME",     ["time","date","datetime","timezone","unix time"]),
        ("PYTHON",        ["python","pip","pip list","copyright","credits","license"]),
        ("TOOLS",         ["calc","password gen","random number","flip coin","uuid","hash","timer"]),
        ("DEVELOPER",     ["debug","compile","run tests","deploy","git status","git pull","api","docker","database","server","ssl"]),
        ("INFO / FUN",    ["quote","joke","weather","news","location","meaning of life","pi","secret","matrix"]),
        ("INTERFACE",     ["clear","help","about","settings","theme","language","plugins","report"]),
        ("JARVIS",        ["hello","how are you","who are you","thank you","what can you do","jarvis"]),
        ("SESSION",       ["exit","logout","whoami","id","history"]),
    ]
    for cat, cmds in categories:
        print(f"\n  {clr('►', BLUE)} {clr(cat, YELLOW)}")
        chunks = [cmds[i:i+4] for i in range(0, len(cmds), 4)]
        for chunk in chunks:
            row = "    " + "   ".join(f"{clr(c, CYAN):<30}" for c in chunk)
            print(row)
    separator()
    jarvis_info("200+ commands available. Many have aliases — try variations!")
    separator()


# ───────────── MAIN PROGRAM ─────────────
def main():
    boot_sequence()

    while True:
        try:
            name = input(f"  {clr('[Jarvis Login]', BLUE)} {clr('Name', CYAN)} (or {clr('exit', RED)} to quit): ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print()
            jarvis_print("Interrupted. Shutting down.", RED)
            break

        if name == 'exit':
            spin("Shutting down", 1.5)
            jarvis_print("JARVIS Offline. Goodbye.", MAGENTA)
            break

        if not name:
            continue

        if name not in users:
            jarvis_error("User not recognized. Access denied.")
            continue

        attempts = 0
        max_attempts = 3
        authenticated = False

        while attempts < max_attempts:
            try:
                key = input(f"  {clr('Password', CYAN)} for {clr(name.upper(), GREEN)} ({clr(str(max_attempts - attempts), YELLOW)} tries left): ").strip()
            except (KeyboardInterrupt, EOFError):
                print()
                break

            if key.lower() == 'exit':
                jarvis_print("Login cancelled.", YELLOW)
                attempts = max_attempts
                break

            if key == users[name]:
                authenticated = True
                break
            else:
                attempts += 1
                jarvis_error("Invalid password.")
                if attempts < max_attempts:
                    jarvis_warn(f"{max_attempts - attempts} attempt(s) remaining.")

        if not authenticated:
            if attempts == max_attempts:
                separator(color=RED)
                jarvis_error(f"SECURITY ALERT: {name.upper()} account locked for 10 seconds.")
                separator(color=RED)
                spin("Lockout timer", 10)
                jarvis_warn("Lockout ended. You may try again.")
            continue

        # ─── AUTHENTICATED SESSION ───
        spin("Authenticating", 1.5)
        separator()
        jarvis_ok(f"Welcome back, {name.upper()}! Session started.")
        jarvis_info(f"Login time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        jarvis_info("Type 'help' for full command list.")
        separator()

        while True:
            try:
                command = input(prompt(name)).strip()
            except (KeyboardInterrupt, EOFError):
                print()
                jarvis_print("Session interrupted. Logging out.", YELLOW)
                break

            result = handle_command(command, name)
            if result is False:
                break

        print()


if __name__ == "__main__":
    main()