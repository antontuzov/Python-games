
def adventure_game():
    print("welcome to adventure game")
    print('you find youself in a dark forest. the path is leading left and right')
    print('which path do you choose?')
    
    choose1 = input("left or right: ").lower()
    
    if choose1 == 'left':
        print('you have come to a river. you can swim across or wait for a boat')
        choose2 = input("swim across or wait for a boat: ").lower()
        if choose2 == 'swim across':
            print('you have arrived at the island in a storm. the island is very cold, and the only thing you can see is clouds')
            choose3 = input('you can go left or right: ').lower()
            if choose3 == 'left':
                print('you have been eaten by a bear')
            elif choose3 == 'right':
                print('you have escaped the bear')
        elif choose2 == 'wait for a boat':
            print('you have arrived at the island in a storm. the island is very cold, and the only thing you can see is clouds')
            choose3 = input('you can go left or right: ').lower()
            if choose3 == 'left':
                print('you have been eaten by a bear')
            elif choose3 == 'right':
                print('you have escaped the bear')
    elif choose1 == 'right':
        print('you have found a river. you can cross or wait')
        choose2 = input('cross or wait: ').lower()
        if choose2 == 'cross':
            print('you have arrived at the island in a storm. the island is very cold, and the only thing you can see is clouds')
            choose3 = input('you can go left or right: ').lower()
            if choose3 == 'left':
                print('you have been eaten by a bear')
            elif choose3 == 'right':
                print('you have escaped the bear')
        elif choose2 == 'wait':
            print('you have been eaten by a bear')
            
    print('thank you for playing')  
    
    
    
if __name__ == '__main__':
    adventure_game()
    