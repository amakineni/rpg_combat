from rpg_combat.character import Character

def test_character_starts_alive():
    Character = Character()
    assert character.health == 1000
    assert character.level == 1
    assert character.alive