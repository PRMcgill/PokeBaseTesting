import pokebase as pb
import json

pokedex = []
for i in range(1, 808):
        
        new_pokemon = pb.pokemon(i)
        new_pokemon_species = pb.pokemon_species(i)
        pokemon_fte = new_pokemon_species.flavor_text_entries
        for fte in pokemon_fte:
                if fte.language.name =="en" and fte.version.name == "alpha-sapphire" or fte.language.name == "en" and fte.version.name == "ultra-sun":
                        new_pokemon_description = fte.flavor_text
        new_pokemon_name =new_pokemon.name
        new_pokemon_number = new_pokemon.id
        types = []
        type1 = new_pokemon.types[0].type
        types.append(type1)
        try:
                type2 = new_pokemon.types[1].type
        except IndexError:
                type2 = ''
        if type2 == '':
                type2 = None
                types.append(type2)
        else:
                types.append(type2)
        new_pokemon_type1 = types[0]
        if len(types) ==2:
                new_pokemon_type2 = types[1]
        else:
                pass
        new_pokemon_image = new_pokemon.sprites.front_default
        new_pokedex_entry = {"name": new_pokemon_name,
                "number": new_pokemon_number,
                "type1": new_pokemon_type1,
                "type2": new_pokemon_type2,
                "image": new_pokemon_image,
                "description": new_pokemon_description}
        pokedex.append(new_pokedex_entry)
        
   
print(pokedex)




