import random
import time
def main():
    print(" _  _             _                _____     _ _          ")
    print("| || |___ __ _ __| |___  ___ _ _  |_   _|_ _(_) |___      ")
    print("| __ / -_) _` / _` (_-< / _ \ '_|   | |/ _` | | (_-<      ")
    print("|_||_\___\__,_\__,_/__/ \___/_|    _|_|\__,_|_|_/__/  _ _ ")
    print("| _ \__ _ _ _| |_____ _ _  \ \    / (_)__ _ _ _  __ _| | |")
    print("|  _/ _` | '_| / / -_) '_|  \ \/\/ /| / _` | ' \/ _` | | |")
    print("|_| \__,_|_| |_\_\___|_|     \_/\_/ |_\__, |_||_\__,_|_|_|")
    print("                                      |___/               ")
    
    
    print("Heads or Tails?")
    answer = input("--> ")
    
    verdict = random.randint(0, 2)
    
    if(answer.lower() != "heads" and answer.lower() != "tails"):
        print("Invalid Entry")
        print(answer)
        return
    
    if(verdict == 0):
        verdict = "Heads"
    
    else:
        verdict = "Tails"
    
    print("flipping...")
    
    time.sleep(1.5)
    
    if(answer.lower() == verdict.lower()):
        print(f"Good job the answer was {verdict}")
    else:
        print(f"Verdict is {verdict} Better luck next time")
main()