print(" Niveau Terminée ")
base_score = 1000
coins_collected_str = input("Nombre de pièces collectées : ")
coins_collected = int(coins_collected_str)
no_damage_str = input("Avez-vous terminé sans subir de dégâts ? (oui/non) : ").lower()
no_damage_bonus = no_damage_str == "oui"
coin_bonus = coins_collected * 50
damage_multiplier = 2 if no_damage_bonus else 1
final_score = (base_score + coin_bonus) * damage_multiplier
print("\n Détails de score")
print(f"Score de base : {base_score}")
print(f"Bonus (pièces) : +{coin_bonus}")
print(f"Multiplicateur (sans dégâts) : x{damage_multiplier}")
print(f"SCORE FINAL : {final_score}")
