import pokebase as pb
import json

pokedex = []
for i in range(1, 10):
    new_pokemon = pb.pokemon(i)
    new_pokemon_species = pb.pokemon_species(i)
    pokemon_fte = new_pokemon_species.flavor_text_entries
    for j in pokemon_fte:
        if j.language.name =="en" and j.version.name == "alpha-sapphire" or j.language.name == "en" and j.version.name == "ultra-sun":
            new_pokemon_description = j.flavor_text
    new_pokemon_name =new_pokemon.name
    new_pokemon_number = new_pokemon.id
    new_pokemon_type = new_pokemon.types
    new_pokemon_image = new_pokemon.sprites.front_default
    pokedex.append({"name": new_pokemon_name,
                "number": new_pokemon_number,
                "types": new_pokemon_type,
                "image": new_pokemon_image,
                "description": new_pokemon_description })
# for i in range (1,10):
#     new_pokemon = pb.pokemon_species(i)
#     new_pokemon_description = new_pokemon.flavor
#     print(new_pokemon_description)
# for j in range (1, 10):

#     new_pokemon = pb.pokemon_species(j)
#     pokeman = new_pokemon.flavor_text_entries
#     for i in pokeman:
#             if i.language.name == "en" and i.version.name =="alpha-sapphire" or i.language.name =="en" and i.version.name =="ultra-sun":
#                 pokedex["description"] = i.flavor_text


print(pokedex)
# print(pokedex[0])


# print(pokedex)
# print(dir(pokedex[0]))
# print(pokedex[0].name)
# print(pokedex[0].sprites.front_default)
# print(pokedex[0].types)
# print(pokedex[0].id)poke = pb.pokemon('3')
# name = poke.name
# types = []
# type1 = poke.types[0].type
# types.append(type1)
# try:
#    type2= poke.types[1].type
# except IndexError:
#    type2= 0

# # if type2 == 0:
# #     print(f'{name} is a {type1} type')
# # else:
# #     print(f'{name} is a {type1} and {type2} type')

# if type2 == 0:
#    pass
# else:
#    types.append(type2)
# print(types)
# poketype1 = types[0]
# poketype2 = types[1]

