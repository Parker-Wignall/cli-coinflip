import random
import time
def main():
    answer = input("Heads or Tails?")
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