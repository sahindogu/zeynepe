import random
import time

def new_year_gift_exchange():
    print("🎄✨ Welcome! The New Year Gift Exchange is Starting! ✨🎄")
    print("-" * 50)
    print("Add your friends to participate. Type 'q' to quit.")

    participants = []
    while True:
        name = input("Add a name: ")
        if name.lower() == 'q':
            break
        elif name.strip() == "":
            print("⚠️ Please enter a valid name!")
        else:
            participants.append(name.strip())
            print(f"🎁 {name} has joined the exchange!")

    if len(participants) < 2:
        print("⚠️ Not enough participants! At least 2 people are required for the exchange.")
        return

    print("\n🎉 The drawing is happening... Please wait a moment!")
    time.sleep(2)
    print("✨ The drawing is finalizing... 🎁")
    time.sleep(1)

    random.shuffle(participants)
    pairs = [(participants[i], participants[(i + 1) % len(participants)]) for i in range(len(participants))]

    print("\n🎄✨ New Year Gift Exchange Matches ✨🎄")
    print("-" * 50)
    for giver, receiver in pairs:
        time.sleep(0.5)
        print(f"🎁 {giver} ➡️ {receiver}")
    
    print("\n🎊 The exchange is complete! Wishing you a Happy New Year! 🎊")
    print("-" * 50)

if __name__ == "__main__":
    new_year_gift_exchange()
