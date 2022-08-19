import random

nesus = {
    'health' : 1,
    'attack power' : [5,10,15],
    'list_of_attacks' : ['punch', 'charge', 'kick']
}

hercules = {
        'health' : 100,
        'attack power' : [5,10,15],
        'list_of_attacks' : ['punch', 'headbutt', 'sword slash']
    }

# Attacking
def user_attack_menu(user_attacks):
    #Purpose: allows user to choose which attack
    count = 1
    print("Your attacks:")
    for items in user_attacks:
        print(f'\t{count} for {items}')
        count += 1
    
    users_choice = int(input("Which attack would you like to perform? "))
    if users_choice == 1:
        return user_attacks[0]
    elif users_choice == 2:
        return user_attacks[1]
    elif users_choice == 3:
        return user_attacks[2]

# Chooses random attack for foe
def random_foe_attack(enemy_attacks):
    return random.choice(enemy_attacks)

# Chooses random strength for attack
def random_attack_strength(attack_strength):
    return random.choice(attack_strength)

# Health
# Attacking string: attack with for damage
def user_attacking_string(which_attack_from_user, which_foe, damage):
    print(f'You {which_attack_from_user}ed {which_foe} for {damage} damage!')

def foe_attacking_string(which_foe, which_attack_from_foe, damage):
    print(f'{which_foe} {which_attack_from_foe}ed you for {damage} damage!')

# Keeping track of users health
def keeping_track_of_users_health(users_health, foes_damage):
    hercules['health'] = users_health - foes_damage
    if hercules['health'] <= 0:
        print("You died")
    else:
        print("Your health: ", hercules['health'])

# Keeping track of foe's health  
def keeping_track_of_foes_health(foes_health, users_damage):
    nesus['health'] = foes_health - users_damage
    if nesus['health'] <= 0:
        print("Nesus died")
    else:
        print("Nesus' Health: ", nesus['health'])

# Purpose: Runs program
def main():
    users_attack = user_attack_menu(hercules['list_of_attacks'])
    foes_attack = random_foe_attack(nesus['list_of_attacks'])
    users_random_attack_strength = random_attack_strength(hercules['attack power'])
    foes_random_attack_strength = random_attack_strength(nesus['attack power'])

    user_attacking_string(users_attack, "Nesus", users_random_attack_strength)
    keeping_track_of_foes_health(nesus['health'], users_random_attack_strength)

    if nesus['health'] > 0:
        foe_attacking_string("Nesus", foes_attack, foes_random_attack_strength)
        keeping_track_of_users_health(hercules['health'], foes_random_attack_strength)

main()