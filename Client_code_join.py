import socket
import time
import sys

# --- NEON STYLE ---
RED, GREEN, YELLOW, BLUE = "\033[31m", "\033[32m", "\033[33m", "\033[34m"
MAGENTA, CYAN, WHITE, RESET = "\033[35m", "\033[36m", "\033[37m", "\033[0m"
BOLD, BG_BLUE, BG_MAGENTA = "\033[1m", "\033[44m", "\033[45m"

def typewriter(text, speed=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()

def show_tactics():
    print(f"\n{BG_MAGENTA}{BOLD}{WHITE} 🧠 LOSS ANALYSIS & MOTIVATION 🧠 {RESET}")
    typewriter(f"{YELLOW}Don't be discouraged, my dude! Every loss is just a lesson.{RESET}")
    print(f"\n{CYAN}--- PRO TACTICS FOR NEXT TIME ---{RESET}")
    print(f"1. {BOLD}The Winner's Bias:{RESET} People often repeat the move that just won.")
    print(f"2. {BOLD}The Double Bluff:{RESET} If someone plays Rock twice, they rarely do it a third time.")
    print(f"3. {BOLD}The Loser's Switch:{RESET} A loser usually switches to the move that beat them.")
    typewriter(f"\n{GREEN}Keep your head up. Go back and crush them!{RESET}")

# --- CONNECTION ---
print(f"{BG_BLUE}{BOLD}{WHITE} 🚀 ROCK-PAPER-SCISSORS: CLIENT MODE 🚀 {RESET}")
host_ip = input(f"{YELLOW}Enter Host IP: {RESET}").strip()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print(f"{CYAN}Connecting...{RESET}")
    client.connect((host_ip, 5555))
    
    # Регистрация ника
    host_nick = client.recv(1024).decode()
    my_nick = input(f"{BOLD}Your Nick: {RESET}")
    client.send(my_nick.encode())
    
    print(f"{GREEN}⚡ LINK ESTABLISHED! Opponent: {host_nick}{RESET}")

    while True:
        # Слушаем сервер (тебя)
        data = client.recv(2048).decode()
        
        if not data:
            break

        # Если сервер прислал инфу о раунде или счете
        if data.startswith("DISPLAY|"):
            content = data.replace("DISPLAY|", "")
            print(content)

        # Если сервер ждет наш ход
        elif data == "GO":
            move = ""
            while move not in ['r', 's', 'p']:
                move = input(f"{BOLD}{CYAN}Your move (r/s/p): {RESET}").lower()
            client.send(move.encode())
            print(f"{WHITE}Waiting for opponent...{RESET}")

        # Если мы проиграли и сервер прислал тактики
        elif "SHOW_TACTICS_TRIGGER" in data:
            show_tactics()
            break
        
        # Если игра закончилась
        elif "GAME_OVER" in data:
            print(f"\n{YELLOW}Match finished by host.{RESET}")
            break

except Exception as e:
    print(f"\n{RED}Error: {e}{RESET}")
finally:
    client.close()
    input(f"\n{CYAN}Press Enter to exit...{RESET}")