import slot_machine_game_module as smf

def main():

    balance, bet, payout =  smf.get_balance(), 0.00, 0.00

    smf.display_layout()#display information
    
    playerinput = input("press any ENTER to spin, (q) to quit: ")# check if the player wants to spin or quit 
    if playerinput.lower() == "q":
        smf.exit_game()

    #main game loop
    counter = 0
    while balance > 0.00:
        counter += 1
        print(f"**current balance: ${smf.read_balance()}")
   
        try:
            bet = float(input("**place your bet amount: $"))
            if bet > smf.read_balance():
                print("**Insufficient balance")
                continue
            elif bet <= 0:
                print("**Bet must be greater than zero")
                continue
            else:
                balance -= bet
                smf.update_balance(balance)
                print(f"**balance: ${balance}")
                print("**spinning...")
                payout = smf.display_spin(smf.get_payout(bet,smf.get_spin()))
                balance += payout
                smf.update_balance(balance)
        except ValueError:
            print("Invalid input")
            
        # check if the player wants to contuine or quit    
        if counter == 5:
            userinput = input("press ENTER to contuine, (q) to quit: ").lower()
            if userinput == "q":
                print(f"**balance: ${smf.read_balance()}")
                smf.exit_game()
            else:
                counter = 0
                continue


if __name__ == '__main__':
    main()