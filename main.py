import story_line
import random

nesus = {
    'health' : 200,
    'attack power' : 10,
    'list_of_attacks' : ['punch', 'charge', 'kick']
}
cyclops = {
    'health' : 300,
    'attack power' : 10,
    'list_of_attacks' : ['stomp', 'club swing']
}
hydra = {
    'health' : 400,
    'attack power' : 10,
    'list_of_attacks' : ['bite']
}

hercules = {
        'health' : 1000,
        'attack power' : 15,
        'list_of_attacks' : ['punch', 'headbutt', 'sword slash']
    }

def user_attack_menu():
    #Purpose: allows user to choose which attack
    list_of_attacks = hercules.get("list_of_attacks")
    print(list_of_attacks)
    users_attack = int(input("Which attack would you like to perform? "))
    if users_attack == 1:
        print(list_of_attacks[0])
    elif users_attack == 2:
        print(list_of_attacks[1])
    elif users_attack == 3:
        print(list_of_attacks[2])


def foes_random_attack(name_of_foe):
    #Purpose: randomly picks which attack to use against user
    list_of_attacks = name_of_foe.get("list_of_attacks")
    foe_random_attack = random.choice(list_of_attacks)
    return foe_random_attack

def users_health():
    #Purpose: keep track of users's health. adds or subtracts.
    users_health = hercules.get("health")
    if users_health == 0:
        return
    pass

def foes_health():
    #Purpose: keep track of foe's health. adds or subtracts
    pass

def attack():
    #Purpose: user attack to lower foes health. foes attack to lower users health. Terminate attack once user or foe reaches zero health
    pass

def run_game():
    #Purpose: call other functions in a logical order that will determine game flow
    story_line.start_of_game_story()
    story_line.first_foe_story()
    story_line.second_foe_story()
    story_line.third_foe_story()
    story_line.end_of_game_story()

#run_game()
#user_attack_menu()

print(foes_random_attack(nesus))
print(foes_random_attack(nesus))
print(foes_random_attack(nesus))