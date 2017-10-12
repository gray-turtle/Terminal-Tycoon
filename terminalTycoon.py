#! /usr/bin/python3

import random, os, time, threading

def start_game():
    print('Welcome to Terminal Tycoon!!')
    print()
    start = input('Start new game? [y,n] ')
    if start == 'y':
        main_menu()
    elif start == 'n':
        quit()
    else:
        os.system('clear')
        start_game()

def lose():
    os.system('clear')
    print('You\'ve run out of money! You lose.')
    start_game()

#funds
money_amount = 100
bits_amount = 100
bytes_amount = 100

#number of currently operating workers
miners = 0

def work_miners():
    global miners, bits_amount, money_amount

    while True:
        time.sleep(10)
        bits_amount += 2 * miners

factory_workers = 0

def work_factory_workers():
    global factory_workers, bits_amount, bytes_amount, money_amount

    while True:
        if bits_amount > 8 * factory_workers:
            time.sleep(20)
            bits_amount -= 8 * factory_workers
            bytes_amount += 1 * factory_workers

merchants = 0

def work_merchants():
    global merchants, bytes_amount, money_amount

    while True:
        if bytes_amount > 1 * merchants:
            time.sleep(30)
            bytes_amount -= 1 * merchants
            money_amount += 10 * merchants

def salary():
    global money_amount, miners, factory_workers, merchants

    while True:
        time.sleep(60)
        money_amount -= 10 * (miners + factory_workers + merchants)
        if money_amount < 0:
            lose()

def show_funds():
    print()
    print('Money = ' + str(money_amount))
    print('Bits = ' + str(bits_amount))
    print('Bytes = ' + str(bytes_amount))
    print()
    print('Miners = ' + str(miners))
    print('Factory Workers = ' + str(factory_workers))
    print('Merchants = ' + str(merchants))
    print()

first_salary = 1
first_mine_hire = 1
first_factory_hire = 1
first_market_hire = 1

#set if first time at a menu or not
first_main_menu = 1
first_mine_menu = 1
first_factory_menu = 1
first_market_menu = 1

##################################
#..........MAIN MENU.............#
##################################

def main_menu():
    global first_main_menu, bits_amount, money_amount
    
    print()
    print('#################')
    print('----MAIN MENU----')
    print('#################')

    if first_main_menu == 1:
        print()
        print('-------------------')
        print()
        print('Uh oh! You only have 100 money; if you run out of money the game is over! You\'ll have to mine some bits and sell them if you want to make more and become a terminal tycoon!')
        print('Enter \"help\" into the command line to learn how to play.')
        print()
        print('-------------------')
        first_main_menu = 0
    else:
        pass

    show_funds()
    
    main_command = input('Command: ')
    
    if main_command == 'help':
        print('Enter \"mine\" to go to the mine menu.')
        print('Enter \"factory\" to go to the factory menu.')
        print('Enter \"market\" to go to the market menu.')
        print('Enter \"quit\" to quit the game.')
        print('Enter \"help\" to see this text again.')
        print('Enter \"main\" to return to the main menu at any time. You can only switch between menus from the main menu.')
        main_menu()
    elif main_command == 'quit':
        quit()
    elif main_command == 'mine':
        mine_menu()
    elif main_command == 'factory':
        factory_menu()
    elif main_command == 'market':
        market_menu()
    else:
        print('You can enter "help" if you don\'t know what you\'re doing.')
        main_menu()

##################################
#.............MINE...............#
##################################

def mine_menu():
    global first_mine_menu, first_salary, bits_amount, money_amount, miners, first_mine_hire
    
    print()
    print('############')
    print('----MINE----')
    print('############')

    if first_mine_menu == 1:
        print()
        print('-------------------')
        print()
        print('Welcome to the mine menu! Here you can hire and keep track of your miners; you can also do a little mining yourself.')
        print('Enter \"help\" into the command line to learn how to start mining some bits.')
        print()
        print('-------------------')
        first_mine_menu = 0
    else:
        pass

    show_funds()

    mine_command = input('Command: ')
    
    if mine_command == 'mine':
        mine_number = random.randint(1, 2)
        pickaxe = random.randint(1, 2) 
        if pickaxe == mine_number:
            bit_reward_list = [1] * 40 + [2] * 30 + [3] * 15 + [4] * 10 + [5] * 5
            bit_reward = random.choice(bit_reward_list)
            bits_amount += bit_reward
            print('You mined ' + str(bit_reward) + ' bits!')
            mine_menu()
        else:
            print('No luck, try again.')
            mine_menu()
    elif mine_command == 'hire':
        if money_amount > 10:
            money_amount -= 10
            miners += 1
            if first_mine_hire == 1:
                first_mine_hire = 0
                miners_thread = threading.Thread(target=work_miners)
                miners_thread.start()
            else:
                mine_menu()
            if first_salary == 1:
                salary_thread = threading.Thread(target=salary)
                salary_thread.start()
                first_salary = 0
                mine_menu()
            else:
                mine_menu()
        else:
            print('You don\'t have enough money!')
            mine_menu()
    elif mine_command == 'help':
        print('Enter \"mine\" to try mining for some bits.')
        print('Enter \"hire\" to hire a miner for 10 money; a miner mines 1 bit every 10 seconds and costs 10 money every minute.')
        print('Enter \"main\" to return to the main menu.')
        print('Enter \"help\" to see this text again.')
        mine_menu()
    elif mine_command == 'factory':
        factory_menu()
    elif mine_command == 'market':
        market_menu()
    elif mine_command == 'main':
        main_menu()
    else:
        print('You can enter "help" if you don\'t know what you\'re doing.')
        mine_menu()


##################################
#............FACTORY.............#
##################################

def factory_menu():
    
    global first_factory_menu, factory_workers, bits_amount, bytes_amount, money_amount, first_factory_hire, first_salary
    
    print()
    print('###############')
    print('----FACTORY----')
    print('###############')

    if first_factory_menu == 1:
        print()
        print('-------------------')
        print()
        print('This is the factory menu; here you can synthesise bits into bytes and hire factory workers to do it automatically.')
        print('Enter \"help\" into the command line to learn how to start synthesizing.')
        print()
        print('-------------------')
        first_factory_menu = 0
    else:
        pass
    
    show_funds()

    factory_command = input('Command: ')

    if factory_command == 'main':
        main_menu()
    elif factory_command == 'hire':
        if money_amount > 15:
            money_amount -= 15
            factory_workers += 1
            if first_factory_hire == 1:
                first_factory_hire = 0
                factory_workers_thread = threading.Thread(target=work_factory_workers)
                factory_workers_thread.start()
            else:
                factory_menu()
            if first_salary == 1:
                salary_thread = threading.Thread(target=salary)
                salary_thread.start()
                first_salary = 0
                factory_menu()
            else:
                factory_menu()
        else:
            print('You don\'t have enough money!')
            market_menu()

    elif factory_command == 'synthesize bits':
        if bits_amount > 8:
            bits_amount -= 8
            bytes_amount += 1
            factory_menu()
        else:
            print('You don\'t have enough bits!')
            factory_menu()
    elif factory_command == 'help':
        print('Enter \"synthesize bits\" to synthesize 8 bits into a byte --make sure you have enough!')
        print('Enter \"hire\" to hire a factory worker for 15 money. Factory workers synthesize 1 byte every 20 seconds and cost 10 money per minute!')
        print('Enter \"main\" to return to the main menu.')
        print('Enter \"help\" to see this text again.')
    else:
        print('You can enter "help" if you don\'t know what you\'re doing.')
        factory_menu()


##################################
#............MARKET..............#
##################################

def market_menu():

    global money_amount, bytes_amount, merchants, first_market_menu, first_salary, first_market_hire
    
    print()
    print('##############')
    print('----MARKET----')
    print('##############')

    if first_market_menu == 1:
        print()
        print('-------------------')
        print()
        print('Congratulations! You\'ve made it to the market menu. Here you can finally turn all your effort into cold, hard cash. Be careful though, it costs 10 money to start a sale! You can also hire some merchants to do your trading for you.')
        print('Enter \"help\" into the command line to learn how to sell some bytes.')
        print()
        print('-------------------')
        first_market_menu = 0
    else:
        pass

    show_funds()

    market_command = input('Command: ')

    if market_command == 'main':
        main_menu()
    elif market_command == 'sell':
        money_amount -= 10
        if money_amount < 0:
            lose()
        if bytes_amount > 0:
            purchase = random.randint(1, bytes_amount)
            offer_list = [1] * 15 + [2] * 20 + [3] * 40 + [4] * 50 + [5] * 60 + [6] * 50 + [7] * 45 + [8] * 35 + [9] * 20 + [10] * 20 + [11] * 20 + [12] * 20 + [13] * 15 + [14] * 15 + [15] * 15 + [16] * 15 + [17] * 10 + [18] * 10 + [19] * 10 + [20] * 5
            offer = random.choice(offer_list)
            print('A buyer has offered ' + str(offer * purchase) + ' money for ' + str(purchase) + ' bytes!')
            accept_offer = input('Accept this offer? [y, n] ')
            if accept_offer == 'y':
                bytes_amount -= purchase
                money_amount += offer * purchase
                market_menu()
            else:
                haggle_again_list = [0] * 3 + [1] * 10 + [2] * 8 + [3] * 5 + [4] * 2
                haggle_again = random.choice(haggle_again_list)
                while haggle_again > 0:
                
                    haggle = random.randint(-5, (-5 + offer))
                    bar = random.randint(-2, 2)
                    if haggle < bar:
                        offer += random.choice(offer_list)
                        print('Wait! The buyer has decided they are now willing to offer ' + str(offer * purchase) + ' money for ' + str(purchase) + ' bytes!')
                        accept_haggle = input('Accept this new offer? [y, n] ')
                        if accept_haggle == 'y':
                            bytes_amount -= purchase
                            money_amount += offer * purchase
                            market_menu()
                        else:
                            haggle_again -= 1
                print('Offer declined, better luck next time!')
                market_menu()
        else:
            print('You don\'t have any bytes!')
            market_menu()
    elif market_command == 'hire':
        if money_amount > 20:
            money_amount -= 20
            merchants += 1
            if first_market_hire == 1:
                first_market_hire = 0
                merchants_thread = threading.Thread(target=work_merchants)
                merchants_thread.start()
            else:
                market_menu()
            if first_salary == 1:
                salary_thread = threading.Thread(target=salary)
                salary_thread.start()
                first_salary = 0
                market_menu()
            else:
                market_menu()
        else:
            print('You don\'t have enough money!')
            market_menu()

    elif market_command == 'help':
        print('Enter \"sell\" to begin accepting offers for your bytes. If you don\'t like the offer then you can decline it (they might be willing to raise their offer, especially if they didn\'t offer a lot in the first place), be careful though, entering into a sale with a new buyer costs 10 money!')
        print('Enter \"hire\" to hire a merchant for 20 money. Merchants enter into a new sale every 30 seconds for free, but they cannot haggle and will always sell 1 byte at a time for 10 money. Merchants cost 10 money every minute.')
        print('Enter \"main\" to return to the main menu.')
        print('Enter \"help\" to see this text again.') 
        market_menu()
    else:
        print('You can enter \"help\" if you don\'t know what you\'re doing.')
        market_menu()

##################################
#............LAUNCH..............# 
##################################

start_game()

