from api.models import Pokemon

# Pokemon object with all characteristics
def create_test_pokemon():
  return Pokemon.objects.create(
    attack = 100,
    classification = "Some Classification",
    defense = 25,
    height_m = 1.0,
    hp = 50,
    japanese_name = "Japanese Name",
    name = "Test Pokemon",
    pokedex_number = 1,
    sp_attack = 14,
    sp_defense = 16,
    speed = 55,
    type1 = "grass",
    type2 = "poison",
    weight_kg = 13,
    generation = 2,
    is_legendary = False,
  )
