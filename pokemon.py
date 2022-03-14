#The line below will open a file containing a sample subset of the
#information about every pokemon through Generation 7:

pokedex = open("pokemon.txt", 'r')

#Each line of the file has 13 values, separated by commas.
#They are: 
#
#
# - Number: The numbered ID of the Pokemon, an integer
# - Name: The name of the Pokemon, a string
# - Type1: The Pokemon's primary type, a string
# - Type2: The Pokemon's secondary type, a string (this
#   may be blank)
# - HP: The Pokemon's HP statistic, an integer in the range
#   1 to 255
# - Attack: The Pokemon's Attack statistic, an integer in
#   the range 1 to 255
# - Defense: The Pokemon's Defense statistic, an integer in
#   the range 1 to 255
# - SpecialAtk: The Pokemon's Special Attack statistic, an
#   integer in the range 1 to 255
# - SpecialDef: The Pokemon's Special Defense statistic, an
#   integer in the range 1 to 255
# - Speed: The Pokemon's Speed statistic, an integer in the
#   range 1 to 255
# - Generation: What generation the Pokemon debuted in, an
#   integer in the range 1 to 7
# - Legendary: Whether the Pokemon is considered "legendary"
#   or not, either TRUE or FALSE
# - Mega: Whether the Pokemon is "Mega" or not, either TRUE
#   or FALSE
#
#I the assignment we were given some questions to answer.
#I wrote a class called Pokemon to easen the task, and a bunch
#of functions or "regular code" to find answers to the questions.

#------------------------------------------------------------------------

#Starting off by making a class called Pokemon with a
#calculate_total_power method in it

class Pokemon:
    def __init__(self, ID_num, name, type1, type2, HP, attack, defense, special_atk, \
                 special_def, speed, generation, legendary, mega):
        self.ID_num = ID_num
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.HP = int(HP)
        self.attack = int(attack)
        self.defense = int(defense)
        self.special_atk = int(special_atk)
        self.special_def = int(special_def)
        self.speed = int(speed)
        self.generation = generation
        self.legendary = legendary
        self.mega = mega
        #self.total.power = calculate_total_power()
        
    def calculate_total_power(self):
        total_power = self.HP + self.attack + self.defense + self.special_atk + \
        self.special_def + self.speed
        return total_power

#-------------------------------------------------------------------------        
#am iterating through the pokedex-file and appending the info from
#each line to an individual instance of the Pokemon-class
#then I'm making a list of all the instances, so that I more easily can access
#information about the pokemons.

pokemon_instances = []

for index, line in enumerate(pokedex):
    if index > 0:
        line = line.strip("\n")
        line = line.split(",")

        (ID_num, name, type1, type2, HP, attack, defense, special_atk, special_def, \
         speed, generation, legendary, mega) = line

        object_name = "pokemon" + str(index)
        #print(object_name)

        object_name = Pokemon(ID_num, name, type1, type2, HP, attack, defense, \
                         special_atk, special_def, speed, generation, legendary, mega)

        pokemon_instances.append(object_name)

pokedex.close()

#---------------------------------------------------------------------------

#The code underneath is for finding out which type (either type1 or type2)
#is most regular. 
type_dict = {}

for pokemon in pokemon_instances:
    if pokemon.type1 not in type_dict:
        type_dict[pokemon.type1] = 1
    else:
        type_dict[pokemon.type1] += 1
        
for pokemon in pokemon_instances:
    if pokemon.type2 not in type_dict:
        type_dict[pokemon.type2] = 1
    else:
        type_dict[pokemon.type2] += 1

#looping over the different types to find the most regular one
max = 0
most_regular = ""
for pok_type, amount in type_dict.items():
    if not pok_type == "" and amount > max:
        max = amount
        most_regular = pok_type

#printing the result
print("The most regular type is {}. The amount is {}.".format(most_regular, max))

#---------------------------------------------------------------------------

#function to find highest HP of all pokemon instances
def find_highest_HP(pokemon_instances):
    
    highest_HP = 0
    name_highest_HP = None

    for pokemon in pokemon_instances:
        if pokemon.HP > highest_HP:
            highest_HP = pokemon.HP
            name_highest_HP = pokemon.name
         
    result = "The Pokemon with the highest HP is " \
    + name_highest_HP + " (" + str(highest_HP) + ")."

    return result
        
print(find_highest_HP(pokemon_instances))

#---------------------------------------------------------------------------

#function to find highest defense stats of all pokemon instances
#(sum of defense and special defense)
def highest_defense_statistics(pokemon_instances):
    
    highest_def_stat = 0
    name_highest_def_stat = None

    for pokemon in pokemon_instances:
        defense = pokemon.defense + pokemon.special_def
        
        if (pokemon.mega == True) or (pokemon.legendary == True):
            continue
        elif defense > highest_def_stat:
            highest_def_stat = defense
            name_highest_def_stat = pokemon.name
            
    result = "The pokemon with the highest defense stats is " \
    + name_highest_def_stat +  " (" + str(highest_def_stat) + ")."

    return result
        
print(highest_defense_statistics(pokemon_instances))

#---------------------------------------------------------------------------

#function to calculate...:
def strongest_non_legend_mega_pokemon(pokemon_instances):
    
    strongest_nonlegmega_pokemon = None
    highest_points = 0

    for pokemon in pokemon_instances:
        
        if pokemon.legendary == "FALSE" and pokemon.mega == "FALSE":
            total_points = pokemon.calculate_total_power()
            if total_points > highest_points:
                highest_points = total_points
                strongest_nonlegmega_pokemon = pokemon.name

    result = "The strongest non legend mega pokemon is " + \
             strongest_nonlegmega_pokemon + " (" + str(highest_points) + ")."
         
    return result
        
print(strongest_non_legend_mega_pokemon(pokemon_instances))

#---------------------------------------------------------------------------

#function to calculate highest average speed among the types (1 and 2 included)
def highest_average_speed_among_types(pokemon_instances):
    
    type_dict = {}

    for pokemon in pokemon_instances:
        average = 0
        
        if pokemon.type1 not in type_dict:
            type_dict[pokemon.type1] = [pokemon.speed]
            type_dict[pokemon.type1].append(1)
        else:
            type_dict[pokemon.type1][0] += pokemon.speed
            type_dict[pokemon.type1][1] += 1

        if pokemon.type2 not in type_dict:
            type_dict[pokemon.type2] = [pokemon.speed]
            type_dict[pokemon.type2].append(1)
        else:
            type_dict[pokemon.type2][0] += pokemon.speed
            type_dict[pokemon.type2][1] += 1
    
    highest_average = 0
    type_highest_average = None
    
    for key, value in type_dict.items():
        (speed, num) = value
        average = speed / num
        if average > highest_average:
            highest_average = average
            type_highest_average = key

    result = "The type with the highest average speed among all types is " \
             + type_highest_average + " (" + str(highest_average) + ")."
    
    return result
        
print(highest_average_speed_among_types(pokemon_instances))

#---------------------------------------------------------------------------

#Among all 7 Pokemon generations, which generation had the highest
#average sum of all six stats (HP, Attack, Defense, Special Attack,
#Special Defense, and Speed)?
def calculate_strongest_generation(pokemon_instances):
    
    generation_dict = {}


    for pokemon in pokemon_instances:
        total_points = pokemon.calculate_total_power()
        if pokemon.generation not in generation_dict:
            generation_dict[pokemon.generation] = [total_points, 1]            
        else:
            generation_dict[pokemon.generation][0] += total_points
            generation_dict[pokemon.generation][1] += 1
     
    highest_average = 0
    
    for key, value in generation_dict.items():
        (sum_total_points, generation_quantity) = value
        average = sum_total_points / generation_quantity
        if average > highest_average:
            highest_average = average
            strongest_generation = key

    highest_average = round(highest_average, 2)

    result = "The strongest generation is " + strongest_generation + \
             ", with the highest average sum of all six stats of " + \
             str(highest_average) + "."
         
    return result
        
print(calculate_strongest_generation(pokemon_instances))

#---------------------------------------------------------------------------

#Rounded to the nearest integer, how much higher is the average sum of all
#six stats among Mega Pokemon then their non-Mega versions?
#Note that Mega Pokemon share the same Number (the first column)
#as their non-Mega versions, which will allow you to find all Pokemon that
#have a Mega version.
def difference_mega_nonmega_average_sum_six_stats(pokemon_instances):
    
    mega_dict = {}
    non_mega_dict = {}

    #filling up the mega dictionary with all the mega pokemons
    for pokemon in pokemon_instances:
        if pokemon.mega == "TRUE":
            total_points = pokemon.calculate_total_power()
            if pokemon.ID_num not in mega_dict:
                mega_dict[pokemon.ID_num] = [total_points, 1]           
            else:                
                mega_dict[pokemon.ID_num][0] += total_points
                mega_dict[pokemon.ID_num][1] += 1

    #filling up the non-mega dictionary with all the non-mega pokemons 
    for pokemon in pokemon_instances:
        if (pokemon.ID_num in mega_dict) and (pokemon.mega == "FALSE"):
            total_points = pokemon.calculate_total_power()
            if pokemon.ID_num not in non_mega_dict:
                non_mega_dict[pokemon.ID_num] = [total_points, 1]           
            else:                
                non_mega_dict[pokemon.ID_num][0] += total_points
                #don't think it's important to count, is only one of each,
                #can use length of dict instead
                non_mega_dict[pokemon.ID_num][1] += 1
  
    mega_average = 0
    non_mega_average = 0

    #variables used to sum up amounts in the mega_dict
    sum_total_mega_points = 0
    sum_mega_quantity = 0

    #iterating through the mega_dict to sum up points and quantity
    for key, value in mega_dict.items():
        (total_points, mega_quantity) = value
        sum_total_mega_points += total_points
        sum_mega_quantity += mega_quantity
           
    mega_average = sum_total_mega_points / sum_mega_quantity
    
    
    #variables used to sum up amounts in the non_mega_dict    
    sum_total_non_mega_points = 0
    sum_non_mega_quantity = 0

    #iterating through the non_mega_dict to sum up points and quantity
    for key, value in non_mega_dict.items(): 
        (total_points, generation_quantity) = value
        sum_total_non_mega_points += total_points
        sum_non_mega_quantity += mega_quantity
        
    non_mega_average = sum_total_non_mega_points / sum_non_mega_quantity
    
    #Now that I have the averages for both mega and non-mega versions,
    #I can calculate the difference between them
    difference = round(mega_average - non_mega_average)

    result = "The difference between the average sum of all six stats among \
Mega Pokemon and their non-Mega versions is " + str(difference) + "."
    
    return result
        
print(difference_mega_nonmega_average_sum_six_stats(pokemon_instances))

