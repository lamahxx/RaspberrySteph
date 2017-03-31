######## PROGRAMME A COMPLETER / MODIFIER #########

######## FADING NON INCLU #########################

######## LIST FONCTIONS #################################
#                                                       #
#   Couleurs : Bleu, Rouge, Vert                        #
#   Fermeture Auto apres X: 1 min, 5 min, 10 min        #
#                                                       #
####### FIN LIST FONCTIONS ##############################

import os   #Chercher & importer les libs si existe
import sys  ######################################
import termios #Lib de fonctions d ENTREE/SORTIE
import tty ######################################
#import pigpio #Lib de fonctions des PINS
import time
from thread import start_new_thread # Module/Fonction pour threading

######### DEFINITION DES PINS ############
######### A CHANGER EN FONCTION ##########
######### DES PINS UTILISES ##############

ROUGE = 17
VERT = 22
BLEU = 24

r = 0.0 #############################
v = 0.0 # TOUT EST ETEINT AU DEMARRAGE
b = 0.0 ##############################

abort = False
state = True

#pi = pigpio.pi() # On raccourci le nom de la commande

####    FONCTIONS   ####
# Ici on defini avant les fonctions qu on va utiliser dans le programme
# Le programme est interprete de haut en bas
# 'def' c'est pour definir la fonction


def getCh(): # Stockage d entree clavier dans la variable 'ch'
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
    finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch

def checkKey(): # Verification de l'entree clavier stockee dans 'ch'
        global state
        global abort
        #global brightChanged

        while True: # On veut tout le temps verifier l entree clavier
                c = getCh()

                if c == 'a' and state :
                   ## print ("JE SUIS ROUGE MAINTENANT")
                  pi.set_PWM_dutycycle(17, 255)
                    time.sleep(0.01) # Pour eviter le spam j imagine
                   # brightChanged = False

                if c == 'z' and state:
                
                   # print("JE SUIS VERT MAINTENANT")
                   pi.set_PWM_dutycycle(22, 255)
                    #brightChanged = True
                    time.sleep(0.01)
                    #brightChanged = False

                if c == 'e' and state:
                    pi.set_PWM_dutycycle(24, 255)
                    # brightChanged = True
                    time.sleep(0.01)
                    # brightChanged = False

                if c == 'p':
                    state = False
                    print ("Pause...")
                    time.sleep(0.1)

                if c == 'r':
                    state = True
                    print("Reprise du programme")
                    time.sleep(0.1)

                if c == 'c':
                    abort = True
                    break

start_new_thread(checkKey, ())

print (" A POUR ROUGE // Z POUR VERT // E POUR BLEU //")
print (" P = Pause // R = Reprendre")
print (" C = Terminer le processus")

while abort == False:
    if state == True:
         print("RASPBERRY LED")
         time.sleep(5)

print("Aborting")
pi.set_PWM_dutycycle(17, 0)
pi.set_PWM_dutycycle(22, 0)
pi.set_PWM_dutycycle(24, 0)

