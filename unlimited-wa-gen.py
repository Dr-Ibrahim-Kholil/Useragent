#Mozilla/5.0 (Linux; Android 13; 2201116PG Build/TKQ1.221114.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.53 Mobile Safari/537
import os
import random

def amul():
    os.system('clear')
    from datetime import datetime

    def print_current_date():
        print('\033[91m#############################################')
        print('\033[92m============================================')
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\033[92m𝔻𝕒𝕥𝕖 𝕒𝕟𝕕 𝕋𝕚𝕞𝕖:",'\033[93m'+current_date)


    # Call the function
    print_current_date()
    
    print('\033[92m============================================')
    print('\033[94m            😈Ibrahim404-Cyber😈')    
    print('\033[92m============User Agent Generator============')
    print('\033[92m============================================')
    print('\033[91m#############################################')
    print('\033[92m')
    for xd in range(int(input("ENTER AMOUNTS : "))):
        print("")
        a = 'Mozilla/5.0 (Linux; Android 13;'
        b = random.choice(['6', '7', '8', '9', '10', '11', '12', '13'])
        c = '2201116PG Build/TKQ1.221114.001; wv'
        d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e = random.randrange(1, 9999)
        f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
        h = random.randrange(80, 103)
        i = '0'
        j = random.randrange(5670, 67900)
        k = random.randrange(40, 150)
        l = 'Mobile Safari/537.'
        make = f'{a} {b}; {c} {d}{e}{f} {g} Version/{h}.0 Chrome/{j}.{k}.{i} {l}'
        print(make)

# Your existing code...

# Call the function
amul()

# Wait for user input to continue
input("\033[91mProses Successful...")
