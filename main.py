import random

print("Générateur de mot de passe")

def main():
    while True:
        print("Options:")
        print("Entrez '1' pour générer un mot de passe avec des chiffres")
        print("Entrez '2' pour générer un mot de passe avec des lettres")
        print("Entrez '3' pour générer un mot de passe avec des chiffres et des lettres")
        
        user_input = input("> ")

        if user_input not in ('1', '2', '3'):
            print("Option non valide!")
            continue

        if user_input == "1":
            liste = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            longueur_liste = int(input("Combien de chiffres voulez-vous générer ? "))
            chiffres_aleatoires = [random.choice(liste) for _ in range(longueur_liste)]
            print(f"Les chiffres aléatoires générés sont : {''.join(chiffres_aleatoires)}")

        if user_input == "2":
            liste = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '@']
            longueur_liste = int(input("Combien de lettre voulez-vous générer ? "))
            chiffres_aleatoires = [random.choice(liste) for _ in range(longueur_liste)]
            print(f"Votre mot de passe est : {''.join(chiffres_aleatoires)}")

        if user_input == "3":
            liste = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '@',
                    '1', '2', '3', '4', '5', '6', '7', '8', '9']
            longueur_liste = int(input("Combien de lettre voulez-vous générer ? "))
            chiffres_aleatoires = [random.choice(liste) for _ in range(longueur_liste)]
            print(f"Votre mot de passe est : {''.join(chiffres_aleatoires)}")


        print("Voulez-vous avoir un autre mot de passe ? 'yes' ou 'no'")
        user_input = input("> ")

        if user_input == "no":
            break

main()
