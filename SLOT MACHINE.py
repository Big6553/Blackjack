import random

def spin_row():
    symbols = ['A', 'B', 'C', 'D']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == 'A':
            return bet * 5
        elif row[0] == 'B':
            return bet * 3
        elif row[0] == 'C':
            return bet * 2
        else:
            return bet * 1
    return 0

def main():
    balance = 100

    print("****************************")
    print("Welcome to the Slot Machine!")
    print("Symbols: A, B, C, D")
    print("****************************")

    while balance > 0:
        print(f"\nCurrent Balance: ${balance}")
        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient balance. Please enter a smaller bet.")
            continue

        if bet <= 0:
            print("Bet must be greater than zero.")
            continue

        balance -= bet

        print("\nSpinning...\n")
        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You win! Payout: ${payout}")
            balance += payout
        else:
            print("No win. Better luck next time!")

        if balance <= 0:
            print("Game over! You're out of money.")
            break

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

    print(f"Final balance: ${balance}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
