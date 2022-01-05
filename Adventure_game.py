import time
import random


def delay_message(message):
    print(message)
    time.sleep(1.5)


def val_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        elif option in prompt:
            return option
        else:
            delay_message(f'Sorry,the option "{option}" is invalid.\n'
                          "\nTry again!")


def intro():
    delay_message("You are born in an era were \n"
                  "magic is still being practiced.")
    delay_message("A powerful wizard has taken hold of your village \n"
                  "and rules your village with an iron fist, \n"
                  "killing innocent citizens.")
    delay_message("This wizard has taken hold of the rightful king\n"
                  "and has locked him up in prison.\n")
    delay_message("The citizens are scared of this ruler so you\n"
                  "go on a quest\n"
                  "to find a weapon strong enough to defeat this wizard.\n")


def main_choice(items):
    delay_message("Would you like to play? Please enter number 1/2:\n")
    choice = val_input("Enter number: 1/2", ['1', '2'])
    if choice == '1':
        fight_intro(items)
    elif choice == '2':
        farm_intro(items)
    else:
        main_choice(items)


def fight_intro(items):
    my_life = 100
    wizard_life = 100
    delay_message("Rumour has it, there is a cave in the village \n"
                  "that posses this weapon.")
    delay_message("This cave has been cursed by the wizard!\n")
    delay_message("After you break the curse, \n"
                  "the wizard appears and heads straight for you!")
    fight_choice(items, wizard_life, my_life)


def fight_choice(items, wizard_life, my_life):
    fight = val_input("What will you do? Please enter number:\n"
                      "1. Fight!\n"
                      "2. Runaway!\n", ['1', '2'])
    if fight == '1':
        fight_seq1(items, wizard_life, my_life)
    elif fight == '2':
        runaway(items)
    else:
        fight_choice(items, wizard_life, my_life)


def fight_seq1(items, wizard_life, my_life):
    wizard_damage = round(random.randint(0, 50), -1)
    my_damage = round(random.randint(0, 50), -1)
    if 'Wizard killer' in items:
        my_damage = my_damage + 25
        wizard_damage = wizard_damage / 5
        delay_message("You wield a weapon to defeat the wizard!")
        fight_seq2(items, wizard_damage, my_damage, my_life, wizard_life)
    elif 'Wizard killer' not in items:
        my_damage = my_damage/10
        delay_message("You are not using the wizard killer in the fight!")
        fight_seq2(items, wizard_damage, my_damage, my_life, wizard_life)


def fight_seq2(items, wizard_damage, my_damage, my_life, wizard_life):
    delay_message(f"You inflict {my_damage} damage!")
    wizard_life -= my_damage
    print(f"The wizard's life is {wizard_life}/100")
    if wizard_life < 0:
        delay_message("You have successfully killed the wizard!!")
        delay_message("Finally, your people are free from his villian!")
        delay_message("Peace has finally returned to your land.")
        delay_message("Want to play again?")
        play_again()
    elif my_life > 0:
        delay_message("The wizard attacks you!")
        delay_message(f"He inflicts {wizard_damage} damage to you!")
        my_life -= wizard_damage
        print(f"Your health is {my_life}/100")
        if my_life <= 0:
            delay_message("You have been killed by the wizard!")
            delay_message("Evil will continue to reign in your village.")
            delay_message("GAME OVER!")
            play_again()
        else:
            fight_choice(items, wizard_life, my_life)


def runaway(items):
    delay_message("You ran as fast as you can!")
    delay_message("You barely escaped with your life!")
    main_choice(items)


def play_again():
    delay_message("Do you want to play again? Please enter number:")
    again = val_input("play again? [y|n]", ['1', '2'])
    if again == 'y':
        game()
    elif again == 'n':
        delay_message("Thats too bad, till next time!")
        exit(0)
    else:
        play_again()


def farm_intro(items):
    delay_message("You go  to the farm in your village,")
    delay_message("The farm has been nicknamed the Sahara")
    delay_message("Because of how dry it has become\n"
                  "due to it being poisoned by the wizard")
    if "bread" in items:
        delay_message("On your way to the farm you meet a woman.")
        delay_message("The woman hesitates at "
                      "first but approaches you anyway.")
        encounter_woman(items)
    else:
        delay_message("You tried to search for the woman again.")
        delay_message("She is nowhere to be seen!")
        main_choice(items)


def encounter_woman(items):
    delay_message("What will you do? Please enter number:")
    choice = val_input("1. Talk to the woman\n"
                       "2. Ignore her\n", ['1', '2'])
    if choice == '1':
        delay_message("'Can you spare me some food?' "
                      "the woman said.")
        delay_message("You only have a piece of bread with you "
                      "and nothing else.")
        food_choice(items)
    elif choice == '2':
        ignore_woman(items)
    else:
        encounter_woman(items)


def food_choice(items):
    delay_message("Will you give the woman your food? Please enter number:")
    give_food = val_input("1. Give food\n"
                          "2. Continue wandering", ['1', '2'])
    if give_food == '1':
        receive_weapon(items)
    elif give_food == '2':
        ignore_woman(items)
    else:
        food_choice(items)


def receive_weapon(items):
    delay_message("You gave your bread to the woman.")
    items.remove("bread")
    delay_message("'Thank you kind stranger!' said the woman.")
    delay_message("'Despite not having enough for yourself, "
                  "you still gave your food to me'")
    delay_message("'Please take this and defeat the wizard "
                  "that has corrupted our land.'")
    delay_message("You have gained the legendary weapon! The Wizard killer!")
    items.append("Wizard killer")
    main_choice(items)


def ignore_woman(items):
    delay_message("You averted your gaze from the woman "
                  "and continued heading to the farm.")
    delay_message("Yet, you feel that there is something about the woman.")
    main_choice(items)


def game():
    items = ["bread"]
    wizard_life = 100
    my_life = 100
    intro()
    main_choice(items)


if __name__ == "__main__":
    game()
