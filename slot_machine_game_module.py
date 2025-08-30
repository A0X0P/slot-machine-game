#module
import time,random,sys

def display_layout():
    print('#------------------------------------#')
    print('#    **--------Welcome--------**     #')
    print('#    ** 🎰 Slot Machine Game  **     #')
    print('#    ** symbols: 💩 🍒 ⭐ 💎  **     #')
    print('#------------------------------------#')


def balance_file():
    return "balance.txt"


def exit_game():
    print("exiting game...")
    time.sleep(1)
    sys.exit()


def get_symbols():
    return ('💩','🍒','⭐','💎')


def get_spin():
    options, picks = get_symbols(), []
    for _ in range(3):
        picks.append(random.choice(options))
    return picks


def get_payout(bet,spin):
    spin1,spin2,spin3 = spin
    cashout = 0
    symbol = get_symbols()

## dict mapping
    payout, half_payout = {}, {}

    # dynamic creating of the dict
    for i in range(len(symbol)):
        payout[symbol[i]] = (i + 5.5)
        half_payout[symbol[i]] = i + 2.5

    if spin1 == spin2 == spin3:
        print("🎉🎉🎉 JACKPOT!!! 🎉🎉🎉")
        cashout += bet*payout[spin1]
    elif len({spin1, spin2,spin3}) == 3:#checking if a set of the three spin options is equal to 3, different
        cashout = 0
    else:
        if spin1 == spin2 or spin1 == spin3:
            cashout += half_payout[spin1]*bet
        elif spin2 == spin3:
            cashout += half_payout[spin2]*bet
    return cashout,spin1,spin2,spin3


def get_balance():
    filename, contents, bal = balance_file(), "","10.00"
    try:
        with open(filename) as f:
            contents = f.read()
            
    except FileNotFoundError:
        with open(filename,"w") as f:
            f.write("10.00")
        return 10.00
    else:
        try:
                if float(contents) <= 0.00:
                    with open(filename,"w") as f:
                        f.write(bal)
                    return 10.00
                elif float(contents) > 0:
                    return float(contents)
        except ValueError:
                    with open(filename,"w") as f:
                        f.write(bal)
                    return 10.00


def update_balance(balance):
    with open(balance_file(),"w") as f:
        f.write(f"{balance:.2f}")


def read_balance():
    try:
        with open(balance_file()) as f:
            return float(f.read())
    except (FileNotFoundError, ValueError):
        with open(balance_file(), "w") as f:
            f.write("10.00")
        return 10.00

def display_spin(spin):
    payout,spin_1,spin_2,spin_3 = spin
    print(spin_1,end=" ")
    time.sleep(0.3)
    print(spin_2,end=" ")
    time.sleep(0.3)
    print(spin_3,end=" ")
    time.sleep(0.3)
    print(f'   ${payout}')
    return payout


