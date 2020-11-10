"""
MadLibs
Author: Jesse Mitchell
Period/Core: Core 6


"""


#Print commands and user inputs for the first paragrah or chunck of wrtiing. 
print("Let's Play Silly Sentences! \n")
name_input = input("Enter a male name: ")
second_name_input = input("Enter another diffrent name: ")
city_input = input("Enter the name of a city: ")
size_adjective = input("Enter a size adjective: ")
type_of_pet = input("Enter an animal: ")
user_age = input("Enter an age (Writen as a number): ")
food_input = input("Enter a food noun(In plural tense): ")



#Print commands and input for the second section of writing 

mysterious_creature_state = input("Enter an adjective: ")
user_color_input = input("Enter a color: ")
first_noun_input = input("Enter a noun: ")
article_of_clothing = input("Enter an article of clothing (Written in pural form): ")
movement_adverb = input("Enter a movment adverb (Make sure to capitalize this specific word): ")
ground_verb = input("Enter a verb: ")

# Third set of commands for user input
user_input_action_verb = input("Enter a verb: ")
cell_holding_matieral = input("Enter a building material: " )
creature_swarm_number = input("Enter a number: ")
pet_interjection = input("Enter an interjection: ")
feeling_verb = input("Enter a feeling word(Such as words like kind, fear, or calm): ")
creature_adjective = input("Enter an adjective: ")
body_part = input("Enter a body part of any animal: ")
color_input = input("Enter a color: ")

#Fourth Set of user inputs
user_verb_input = input("Enter a verb (In past tense): ")
piece_of_furniture = input("Enter a piece of furniture: ")
wakingup_adverb = input("Enter an adverb: ")
adverb_input = input("Enter an verb (In past tense): ")

#First commands of writing the actual Mad Lib story using the input above 
print ("\n\t{} lived and worked on a {} farm in {} where he lived with his pet {}, named {}. "  .format(name_input, size_adjective, city_input, type_of_pet, second_name_input), end="") 
print(name_input + " inherited the farm from his father when he was only " + str(user_age) + " years old and he took over the responsibility of farming " + food_input + ". ")

#Second section of commands of writing the actual Mad Lib story using the input above

print ("\t One day when {} and {} were out in the field they noticed an a/an {} {} {}. {} was so stunned by the sight of this never seen before creature that it knocked his {} off. {} the mysterious creature disappeared before his eyes, and then the ground he stood on began to {}. "  .format(name_input, second_name_input, mysterious_creature_state, user_color_input, first_noun_input, name_input, article_of_clothing, movement_adverb, ground_verb ))

#Third section of the final story

print(f"\t {name_input} and {second_name_input} began to {user_input_action_verb} into the ground and they fell into a dark moist {cell_holding_matieral} jail cell. A swarm of around {creature_swarm_number} of the mysterious creatures began to circle around the farmer and his pet let out a large, \"{pet_interjection}!\" as both clammered close together in {feeling_verb}. Then one of the creatures crawled into the two’s cage and held out a {creature_adjective} {body_part} holding a pair of {article_of_clothing} similar to those of {name_input}\'s. These {article_of_clothing} however were {color_input} colored, and from somewhere the farmer nor his farm hand could see the creature said in an haior-raising voice,\"I much prefer them in {color_input}.\"")

#Fourth and last section of the final mad lib story

print("\t" + name_input + " in a sweat " + user_input_action_verb +  " out of his " + piece_of_furniture + " " + wakingup_adverb + " awaking form his sleep and realizing it was all a dream. He felt " + adverb_input + " to see " + second_name_input + " by his side and no creatures in sight." + "\n\n\t\t The End!!!")