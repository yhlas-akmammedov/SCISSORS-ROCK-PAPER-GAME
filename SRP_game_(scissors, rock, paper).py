import random
import time
import getpass
import socket
import msvcrt

# --- ULTIMATE NEON PALETTE ---
RED, GREEN, YELLOW, BLUE = "\033[31m", "\033[32m", "\033[33m", "\033[34m"
MAGENTA, CYAN, WHITE, RESET = "\033[35m", "\033[36m", "\033[37m", "\033[0m"
BOLD, UNDERLINE = "\033[1m", "\033[4m"
BG_RED, BG_GREEN, BG_BLUE, BG_MAGENTA = "\033[41m", "\033[42m", "\033[44m", "\033[45m"

def typewriter(text, speed=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()

def show_tactics():
    print(f"\n{BG_MAGENTA}{BOLD}{WHITE} 🧠 LOSS ANALYSIS & MOTIVATION 🧠 {RESET}")
    typewriter(f"{YELLOW}Don't be discouraged, my dude! Every loss is just a lesson.{RESET}")
    print(f"\n{CYAN}--- PRO TACTICS TO WIN NEXT TIME ---{RESET}")
    print(f"1. {BOLD}The Winner's Bias:{RESET} People often repeat the move that just won. Counter it!")
    print(f"2. {BOLD}The Double Bluff:{RESET} If someone plays Rock twice, they rarely play it a third time.")
    print(f"3. {BOLD}The Loser's Switch:{RESET} A loser usually switches to the move that just beat them.")
    typewriter(f"\n{GREEN}Keep your head up. Go back and crush them!{RESET}")

def show_manual():
    print(f"\n{BG_MAGENTA}{BOLD}{WHITE}    📜 GLOBAL MANUAL 📜    {RESET}")
    print(f"{CYAN}• {BOLD}r{RESET} = Rock 🪨  | {CYAN}• {BOLD}s{RESET} = Scissors ✂️  | {CYAN}• {BOLD}p{RESET} = Paper 📄")
    print(f"{YELLOW}Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.{RESET}")
    print(f"{GREEN}Online: Use Mode [3] to Host. Your friend must connect to your IP.{RESET}")
    print(f"{WHITE}--- Press any key to return to your spot ---{RESET}")
    msvcrt.getch()
    print(f"{GREEN}Back in action!{RESET}\n")

def smart_input(prompt):
    while True:
        user_val = input(f"{BOLD}{WHITE}{prompt}{RESET} {CYAN}>>{RESET} ").strip().lower()
        if user_val == 'i':
            show_manual()
            continue
        return user_val

def warm_up_quiz():
    history_quiz = {
        "Which country invented this game?": "china",
        "In which century did it become popular? (5/17/20)": "17",
        "What was its ancient name? (Shoushiling/Zuefa)": "shoushiling"
    }
    print(f"\n{BG_BLUE}{BOLD}{WHITE}    📜 QUICK QUIZ TIME 📜    {RESET}")
    score = 0
    for q, a in history_quiz.items():
        ans = smart_input(f"{CYAN}{q}{RESET}")
        if ans == a:
            print(f"{GREEN}Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}Wrong! It was {a}.{RESET}")
    print(f"{YELLOW}Quiz finished! Score: {score}/3{RESET}\n")

# --- 1. GREETING ---
print(f"{BG_BLUE}{BOLD}{WHITE}    🚀 ROCK-PAPER-SCISSORS EVOLUTION 🚀    {RESET}")
typewriter(f"{BOLD}{BLUE}Hi my dude! We are gonna play some Rock, Paper, Scissors!{RESET}")
print(f"{YELLOW}PRO TIP: Press 'i' at any prompt if you need instructions!{RESET}")

# --- 2. NICKNAME CREATION ---
user1_raw = smart_input(f"\n{BOLD}Create your Nick{RESET}")
user1_nick = f"{BOLD}{BLUE}{user1_raw}{RESET}"
typewriter(f"Welcome to the system, {user1_nick}!", speed=0.05)

# --- 3. OPTIONAL QUIZ ---
wants_quiz = smart_input(f"\nDo you want a history quiz? ({GREEN}y{RESET}/{RED}n{RESET})")
if wants_quiz == 'y':
    warm_up_quiz()

rob_info = {"name": f"{BOLD}{MAGENTA}V-I-C-T-O-R{RESET}"}
abbr_opt = {"r": f"{WHITE}ROCK 🪨{RESET}", "s": f"{WHITE}SCISSORS ✂️{RESET}", "p": f"{WHITE}PAPER 📄{RESET}"}

# --- 4. SELECTING MODES ---
while True:
    print("\n" + CYAN + "★ "*15 + RESET)
    print(f"{BG_RED}{BOLD}{WHITE}    MAIN MENU    {RESET}")
    print(f"{GREEN} [1] {RESET} vs COMPUTER ({rob_info['name']})")
    print(f"{GREEN} [2] {RESET} vs HUMAN (Local PvP)")
    print(f"{GREEN} [3] {RESET} vs ONLINE (Host Game)")
    print(f"{RED} [0] {RESET} EXIT")
    
    mode = smart_input(f"\n{BOLD}COMMAND > {RESET}")

    if mode == "0":
        typewriter(f"{BG_RED} TERMINATING... BYE DUDE! {RESET}", speed=0.05)
        break
    if mode not in ["1", "2", "3"]:
        continue

    user1_score, user2_score, conn = 0, 0, None

    if mode == "1":
        user2_nick, is_pc, is_online = rob_info["name"], True, False
    elif mode == "2":
        u2_raw = smart_input("Player 2 Nick")
        user2_nick = f"{BOLD}{RED}{u2_raw}{RESET}"
        is_pc, is_online = False, False
    elif mode == "3":
        is_pc, is_online = False, True
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('0.0.0.0', 5555))
        server.listen(1)
        server.settimeout(0.1)
        
        my_ip = socket.gethostbyname(socket.gethostname())
        typewriter(f"\n{BG_BLUE}{BOLD} GENERATING CONNECTION LINK... {RESET}")
        print(f"Your IP Address: {YELLOW}{BOLD}{my_ip}{RESET}")
        print(f"{WHITE}Waiting for a friend to join...{RESET}")

        connected = False
        while not connected:
            try:
                conn, addr = server.accept()
                connected = True
            except socket.timeout:
                if msvcrt.kbhit() and msvcrt.getch().decode().lower() == 'b':
                    break
        if not connected:
            continue
        
        conn.send(user1_raw.encode())
        user2_raw_name = conn.recv(1024).decode()
        user2_nick = f"{BOLD}{RED}{user2_raw_name}{RESET}"

    # --- 5. PLAYING ---
    typewriter(f"\n{BOLD}{YELLOW}BATTLE START: {user1_nick} vs {user2_nick}{RESET}", speed=0.04)
    for round_num in range(1, 4):
        status_msg = f"\n{BOLD}{WHITE}{BG_BLUE}    ROUND #{round_num}    {RESET}\nScore: {user1_raw} {user1_score} | {user2_score} {user2_raw_name if is_online else 'P2'}"
        print(status_msg)
        
        if is_online:
            conn.send(f"DISPLAY|{status_msg}".encode())
            time.sleep(0.1)
            conn.send("GO".encode())

        u1_input = smart_input(f"{user1_nick} move (r/s/p)")
        
        if is_pc:
            u2_input = random.choice(['r', 's', 'p'])
        elif is_online:
            typewriter(f"{WHITE}Waiting for {user2_nick}...{RESET}")
            u2_input = conn.recv(1024).decode().lower()
        else:
            u2_input = getpass.getpass(f"{BOLD}{user2_nick}'s move (hidden): {RESET}").lower()

        res_text = f"{user1_nick}: {abbr_opt[u1_input]} {MAGENTA}VS{RESET} {user2_nick}: {abbr_opt[u2_input]}"
        typewriter(res_text)
        
        if u1_input == u2_input:
            point_msg = f"{YELLOW}--- TIE! ---{RESET}"
        elif (u1_input == 'r' and u2_input == 's') or (u1_input == 's' and u2_input == 'p') or (u1_input == 'p' and u2_input == 'r'):
            point_msg = f"{BG_GREEN}{BOLD} POINT FOR {user1_raw.upper()}! {RESET}"
            user1_score += 1
        else:
            point_msg = f"{BG_RED}{BOLD} POINT FOR {user2_nick}! {RESET}"
            user2_score += 1
        
        print(point_msg)
        if is_online:
            conn.send(f"DISPLAY|{res_text}\n{point_msg}".encode())

        if user1_score == 2 or user2_score == 2:
            break

    # --- 6. END GAME & MOTIVATION ---
    final_score = f"\n{BOLD}{CYAN}FINAL SCORE: {user1_nick} {user1_score} : {user2_score} {user2_nick}{RESET}"
    print(final_score)
    if is_online: conn.send(f"DISPLAY|{final_score}".encode())
    
    if user1_score == user2_score:
        typewriter(f"{YELLOW}The match ended in a draw!{RESET}")
    elif user1_score < user2_score:
        show_tactics()
    else:
        typewriter(f"\n{BG_GREEN}{BOLD}{WHITE} 🏆 VICTORY! YOU ARE THE BEST! 🏆 {RESET}", speed=0.05)
        if is_online and conn:
            conn.send("SHOW_TACTICS_TRIGGER".encode())

    if is_online and conn:
        conn.send("GAME_OVER".encode())
        conn.close()
    input(f"\n{CYAN}Press Enter to return to Menu...{RESET}")