import random

# Simple dice adventure: roll dice, fight monsters, collect gold.

monsters = ["Goblin", "Skeleton", "Slime", "Bat"]
player_hp = 20
gold = 0
round_number = 1

print("=== Dice Adventure ===")

# while loop: keep playing until HP runs out or we win enough gold
while player_hp > 0 and gold < 30:
    monster = random.choice(monsters)
    monster_hp = random.randint(5, 12)
    print(f"\nRound {round_number}: A wild {monster} appears with {monster_hp} HP!")

    # inner while loop: fight until someone drops
    while monster_hp > 0 and player_hp > 0:
        player_roll = random.randint(1, 6)
        monster_roll = random.randint(1, 6)

        # branching
        if player_roll > monster_roll:
            monster_hp -= player_roll
            print(f"  You rolled {player_roll} and hit the {monster}! (its HP: {max(monster_hp, 0)})")
        elif player_roll < monster_roll:
            player_hp -= monster_roll
            print(f"  The {monster} rolled {monster_roll} and hit you! (your HP: {max(player_hp, 0)})")
        else:
            print(f"  Both rolled {player_roll}. Clash! No damage.")

    if player_hp > 0:
        loot = random.randint(5, 15)
        gold += loot
        print(f"You defeated the {monster} and found {loot} gold! Total: {gold}")
    round_number += 1

# Result
if player_hp <= 0:
    print("\nYou were defeated. Game over.")
else:
    print(f"\nYou win with {player_hp} HP and {gold} gold!")

# for loop: show a little scoreboard
print("\n--- Scoreboard ---")
for stat, value in [("Rounds", round_number - 1), ("HP", max(player_hp, 0)), ("Gold", gold)]:
    print(f"{stat:<8}: {value}")

# for loop with range: random lucky numbers
print("\nYour lucky numbers:")
for i in range(1, 4):
    print(f"  #{i}: {random.randint(1, 100)}")
