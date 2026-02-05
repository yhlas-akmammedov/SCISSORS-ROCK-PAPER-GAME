✨ Features
3 Game Modes: * 🤖 vs PC (V-I-C-T-O-R): Practice against a randomized bot.

   👥 Local PvP: Play with a friend on the same keyboard (hidden inputs).

   🌐 Online/LAN: Host a game on your network and battle friends via IP.

   Neon Terminal UI: Full ANSI color support for a high-energy "cyber" feel.

   Smart Sync: Real-time round updates, score tracking, and "GO" signals to prevent network lag.

   Loss Analysis: Integrated pro-tactics and psychological motivation for the defeated player.

   History Quiz: Built-in warm-up quiz about the origins of the game.

🛠 Installation & Requirements
Python 3.x installed.

No external libraries needed! Uses built-in socket, time, and msvcrt.

Ensure your firewall allows Python to communicate on Port 5555.!!!!!!

🎮 How to Play
  1. Hosting a Match (The Server)
     Run SRP_game_(scissors, rock, paper).py

     Select Mode [3].
    
     The terminal will display your Local IP Address (e.g., 192.168.x.x).

Wait for your friend to connect.

2. Joining a Match (The Client)
Run client.py on another computer (or another terminal).

  Enter the Host's IP Address when prompted.

  Battle!

🧩 Commands
r : Rock 🪨

p : Paper 📄

s : Scissors ✂️

i : Open Global Manual (works mid-game!)

📡 Network Architecture
The game uses a Synchronized Handshake logic:

  Host sends Round Data.

  Host sends GO trigger to Client.

  Client unlocks input and sends move.

  Host calculates winner and broadcasts DISPLAY packet to both screens.

🛡 Disclaimer
This game is designed for local networks. For playing over the internet, port forwarding or a VPN like Hamachi/ZeroTier is required.!!!!!!! 
                                                                                                                           
                                                                                                                            Created by yhlas_akmammedov 60%(Gemini AI 30%)