#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	power = voltage**2/resistance
	return (f"The power dissipated is {power}W")

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	v1[0]
	v1[1]

	if (v1[0]*v2[0]) + (v1[0]*v2[1]) == 0:
		return (f"Les vecteurs {v1} et {v2} sont orthogonaux")
	else:
		return(f"Les vecteurs {v1} et {v2} ne sont pas orthogonaux")


	pass

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	somme = longueur_de_liste = 0
	for v in values:
		if v >= 0:
			somme += v
			longueur_de_liste += 1



	return somme / longueur_de_liste
	pass # La variable v contient une valeur de la liste.
#
def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	twenties = 0
	tens = 0
	fives = 0
	twos = 0
	while value != 0:
		if value >= 20:
			twenties = value // 20
			value = value % 20


		elif value >= 10:
			tens = value // 10
			value = twenties % 10


		elif value >= 5:
			fives = value // 5
			value = value % 5


		elif value >= 1:
			twos = value // 1
			value = 0

	return (twenties, tens, fives, twos);

def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		digit_value = abs_value % base #42%16=10
		result += digit_letters[digit_value]  #on va chercher la lettre à la position 10(A)
		abs_value //= base #42//16=2
	if value < 0:
		result += "-" #On rajoute un signe négatif si value < 0
	return result[::-1] # [start:stop:step] on inverse le step pour que A2 = 2A


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
	print(format_base(-42, 16, "0123456789ABCDEF"))
