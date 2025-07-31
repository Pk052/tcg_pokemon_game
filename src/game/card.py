class Card:
    def __init__(self, name, card_type, hp=None, attacks=None, weakness=None, resistance=None):
        self.name = name
        self.card_type = card_type  # 'pokemon', 'trainer', 'energy'
        self.hp = hp
        self.attacks = attacks or []
        self.weakness = weakness
        self.resistance = resistance
        self.image_path = f"assets/cards/{name.lower().replace(' ', '_')}.png"

class PokemonCard(Card):
    def __init__(self, name, hp, pokemon_type, attacks, evolution_stage=0, evolves_from=None):
        super().__init__(name, 'pokemon', hp, attacks)
        self.pokemon_type = pokemon_type
        self.evolution_stage = evolution_stage
        self.evolves_from = evolves_from

class TrainerCard(Card):
    def __init__(self, name, effect):
        super().__init__(name, 'trainer')
        self.effect = effect

class EnergyCard(Card):
    def __init__(self, name, energy_type):
        super().__init__(name, 'energy')
        self.energy_type = energy_type

