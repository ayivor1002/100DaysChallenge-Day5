import random

#declaration de la liste des lettres
lettres=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#declaration de la liste des nombres
nombres=['0','1','2','3','4','5','6','7','8','9']

#declaration de la liste des symboles
symboles=['!','#','$','%','&','(',')','*','+','-','/','{','}','_']

#mot de bienvenue
print("Bienvenue sur le generateur de mots de passe\n")

#recuperation de l'entree de l'utilisateur 
nbr_lettres=int(input("Combien de lettres voulez vous dans votre mot de passe?: "))

#recuperation de l'entree de l'utilisateur 
nbr_symboles=int(input("Combien de symboles voulez vous dans votre mot de passe?: "))

#recuperation de l'entree de l'utilisateur 
nbr_nombres=int(input("Combien de nombres voulez vous dans votre mot de passe?: "))

#declaration du tableau qui contiendra les lettres choisies au hasard
tab_l=[]

#boucle parcourant la liste des lettres
for i in range(0, nbr_lettres):
  #choix au hasard d'une lettre
  c=random.choice(lettres)
  #ajout de la lettre choisie a la liste tab_l
  tab_l.append(c)
#print(tab_l)


#declaration du tableau qui contiendra les nombres choisies au hasard
tab_n=[]
for i in range(0, nbr_nombres):
  #choix au hasard d'un nombre
  c1=random.choice(nombres)
  #ajout du nombre choisie a la liste tab_n
  tab_n.append(c1)
#print(tab_n)


#declaration du tableau qui contiendra les symboles choisies au hasard
tab_s=[]
for i in range(0, nbr_symboles):
  #choix au hasard d'un symbole
  c2=random.choice(symboles)
  #ajout du symbole choisi a la liste tab_s
  tab_s.append(c2)
#print(tab_s)

#creation d'un nouveau tableau contenant les informations des trois tableaux precedants
ps_tab=tab_l+tab_n+tab_s

#print(ps_tab)
#modification de l'ordre des elements de la nouvelle liste
random.shuffle(ps_tab)

#print(ps_tab)

#declaration de la chaine de caractere qui contiendra la forme finale du mot de passe
password=""
for item in ps_tab:
  #ajout de chaque lettre de la liste a la chaine de caractere
  password+=item

#affichage du mot de passe
print("votre mot de passe: "+password)