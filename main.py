"""
MadLibs
Author: Jesse Mitchell
Period/Core: Core 6


"""
#Print commands and user inputs for the first paragrah or chunck of wrtiing. 
print("Let's Play Silly Sentences! \n")
name_input = input("Enter a name: ")
second_name_input = input("Enter another diffrent name: ")
city_input = input("Enter the name of a city: ")
size_adjective = input("Enter a size adjective: ")
type_of_pet = input("Enter a animal: ")
user_age = input("Enter an age (writen as a number): ")
food_input = input("Enter: a food noun: ")



#Print commands and input for the second section of writing 

mysterious_creature_state = input("Enter an adjective: ")
user_color_input = input("Enter a color: ")
first_noun_input = input("Enter a noun: ")
farmer_verb = input("Enter a past tense verb: ")
article_of_clothing = input("Enter an article of clotrhing: ")
movement_adverb = input("Enter a movment adverb: ")
ground_verb = ("Enter a verb: ")



#First commands of writing the actual Mad Lib story using the input above 
print ("\t{} lived and worked on a {} farm in {} where he lived with his pet {}, named {}. "  .format(name_input, size_adjective, city_input, type_of_pet, second_name_input), end="") 
print(name_input + " inherited the farm from father when he was only " + str(user_age) + " years old and he took over the responsibility of farming " + food_input ". ")

#Second section of commands of writing the actual Mad Lib story using the input above

print ("\tOne day when {} and {} were out in the field they noticed an a/an {} {} {}. {} was so {} by the sight of this never seen before creature that it knocked his {} off. {} the mysterious creature disappeared before his eyes, and then the ground he stood on began to {}. "  .format(name_input, second_name_input, mysterious_creature_state, user_color_input, first_noun_input, name_input, farmer_verb, article_of_clothing, movement_adverb, ground )
