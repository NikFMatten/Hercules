import random

nesus = {
    'health' : 100,
    'attack power' : [5,10,15],
    'list_of_attacks' : ['punched', 'charged', 'kicked']
}

hercules = {
        'health' : 100,
        'attack power' : [5,10,15],
        'list_of_attacks' : ['punched', 'headbutt', 'sword slashed']
    }

# Builds menu (of users attacks) to choose from
def user_attack_menu(user_attacks):
    #Purpose: allows user to choose which attack
    count = 1
    print("Your attacks:")
    for items in user_attacks:
        print(f'\t{count} for {items}')
        count += 1
    
# User selects which attack to perform    
def user_selecting_attack(user_attacks):
    user_attack_menu(user_attacks)    
    invalid_selection = True
    while invalid_selection:
        users_choice = int(input("\nWhich attack would you like to perform? "))
        if users_choice == 1:
            selected_attack = user_attacks[0]
            invalid_selection = False
        elif users_choice == 2:
            selected_attack = user_attacks[1]
            invalid_selection = False
        elif users_choice == 3:
            selected_attack = user_attacks[2]
            invalid_selection = False
        else: 
            print("Invalid selection, please enter 1, 2 or 3") 
            invalid_selection = True
    return selected_attack

# Chooses random attack for foe
def random_foe_attack(enemy_attacks):
    return random.choice(enemy_attacks)

# Chooses random strength for attack
def random_attack_strength(attack_strength):
    return random.choice(attack_strength)

# Performs user and foes attack on each other. Updates health after attack
def perform_attacks():
    # Collects necessary data to perform attack
    users_attack = user_selecting_attack(hercules['list_of_attacks'])
    foes_attack = random_foe_attack(nesus['list_of_attacks'])
    users_random_attack_strength = random_attack_strength(hercules['attack power'])
    foes_random_attack_strength = random_attack_strength(nesus['attack power'])

    # Ensures user and foe hasn't died to perform attack; attacks and updates health after receving damage
    if hercules['health'] <= 0:
        return
    else:
        attacking_string("You", "Nesus", users_attack, users_random_attack_strength)
        keeping_track_of_health("nesus", users_random_attack_strength)

    if nesus['health'] <= 0:
        return
    else:
        attacking_string("Nesus", "you", foes_attack, foes_random_attack_strength)   
        keeping_track_of_health("hercules", foes_random_attack_strength)

# Attacking string: attack with (x) for damage (x)
def attacking_string(attacker, receiver, which_attack, damage):
    print(f'{attacker} {which_attack} {receiver} for {damage} damage!')

# Keeping track of health
def keeping_track_of_health(damage_receiver, damage):
    if damage_receiver != "hercules":
        nesus['health'] -= damage
        if nesus['health'] <= 0:
            print("Nesus died")
    else:
        hercules['health'] -= damage
        if hercules['health'] <= 0:
            print("You died.")

# Runs the program (while health for either is above 0)
def main():
    while hercules['health'] > 0 and nesus['health'] > 0:
        print(f'\nHercules health: {hercules["health"]} \t Nesus Health: {nesus["health"]}\n')
        perform_attacks()


main()



# Current Known issues:
# - perform_attacks() function has a lot: collects data, performs attack, updates health after attack
# - foe is not generic. Currently only works with one foe - Nesus
# - Global variables for characters (Hercules and Nesus)

# Future  Goals:
# + Add more villians
# + Make 'Nesus' calls generic for the addition of villians
# + Remove characters as a global variable
# + Implement a 'missed attack' -- attack missed causing 0 dmg
# + Eventual storyline