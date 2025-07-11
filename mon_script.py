import random
import string

def generer_mot_de_passe(longueur):
    characters = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(characters) for _ in range(longueur))
    return mot_de_passe
