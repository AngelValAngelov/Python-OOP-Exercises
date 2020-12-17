from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon.name not in [p.name for p in self.pokemon]:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for p in self.pokemon:
            if p.name == pokemon_name:
                self.pokemon.remove(p)
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemon)}\n"
        res = '\n'.join([f"- {x.pokemon_details()}" for x in self.pokemon])
        return result + res + "\n" + ""


