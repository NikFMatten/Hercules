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

# Attacking
def user_attack_menu(user_attacks):
    #Purpose: allows user to choose which attack
    count = 1
    print("Your attacks:")
    for items in user_attacks:
        print(f'\t{count} for {items}')
        count += 1
    
    users_choice = int(input("\nWhich attack would you like to perform? "))
    print('\n')
    
    if users_choice == 1:
        return user_attacks[0]
    elif users_choice == 2:
        return user_attacks[1]
    elif users_choice == 3:
        return user_attacks[2]
    else: 
        print("Invalid selection, something happens, need to fix") 
        # If invalid selection, still continues to perform_attacks() but with "None" as attack. Dmg still delivered

# Chooses random attack for foe
def random_foe_attack(enemy_attacks):
    return random.choice(enemy_attacks)

# Chooses random strength for attack
def random_attack_strength(attack_strength):
    return random.choice(attack_strength)

def perform_attacks():
    users_attack = user_attack_menu(hercules['list_of_attacks'])
    foes_attack = random_foe_attack(nesus['list_of_attacks'])
    users_random_attack_strength = random_attack_strength(hercules['attack power'])
    foes_random_attack_strength = random_attack_strength(nesus['attack power'])

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