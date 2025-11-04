print("vérificateur de mot de passe")
password = input("Entrez votre mot de passe : ")
password_length = len(password)
has_digit = any(ch.isdigit() for ch in password)
is_long_enough = password_length >= 8
is_strong = is_long_enough and has_digit
print("\n--- RAPPORT DE FORCE DU MOT DE PASSE ---")
print(f"Longueur ≥ 8 caractères : { if is_long_enough else}")
print(f"Contient un chiffre : { if has_digit else")
print("Conclusion :", "Votre mot de passe est considéré comme fort !" if is_strong else "Votre mot de passe peut être amélioré.")

