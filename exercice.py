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
	while value != 0:
		if value >= 20:
			twenties = value % 20
			print(twenties)
			pass
		elif value >= 10:
			reste = value - twenties*20
			tens = int(reste / 10)
			print(tens)

			pass
		elif value >= 5:
			reste =value -(twenties*20 + tens*10)

			pass
		elif value >= 1:
			ones = fives / 1
			pass
	return (twenties, tens, fives, ones);

# def format_base(value, base, digit_letters):
# 	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
# 	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
# 	result = ""
# 	abs_value = abs(value)
# 	while abs_value != 0:
# 		pass
# 	if value < 0:
# 		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
# 		pass
# 	return result


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
	# print(format_base(-42, 16, "0123456789ABCDEF"))
