# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: Ryane Mehdi Djari
#  Prénom Nom: Sunny Liu
import explorer
import randomizer

count=0

def get_team_name():
    return "VROUM VROUM HASBULLA" # à compléter (comme vous voulez)

def step(robotId, sensors):
	global count
	#les robots 1 et 8 changent de comportement chaque 100 iterations
	#les robots 2 et 7 changent de comportement apres 50 puis 150 puis 50 et ainsi de suite
	#les robots 3 à 6 executent uniquement le randomizer
	if robotId%8 == 1 or robotId%8 == 6 and (count % 100) < 50: #chaque 50 iterations
		return suivre.step(robotId,sensors)
	if robotId%8 >= 2 and robotId%8 <= 5 :
		return explorer.step(robotId,sensors)
	if(robotId%8 == 0):
		count += 1	
	if count % 200 < 100:#chaque 100 
		return explorer.step(robotId,sensors)
	else:
		return suivre.step(robotId,sensors)

