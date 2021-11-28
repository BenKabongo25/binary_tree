# -*- coding: utf-8 -*-

# DM de ALGORITHMIQUE
#
# Réalisé par Ben KABONGO BUZANGU - 21911598
#
# Novembre 2020

import math

#-------------------------- Utiles pour le DM ----------------------------------

#--- Fonctions et classes(structures) de manipulations des objets Point ---
# Afin de faciliter la manipulation de ces objets, nous avons définis des classes
# et des fonctions
# Nous avons préféré définir une classe Point (plutôt que d'utiliser une liste).
# Nous y avons défini des méthodes permettant d'afficher la valeur des coordonnées
# d'un point, de vérifier si deux points sont égaux
# Dans le but d'alléger le code, on veut souvent accéder aux coordonnées d'un
# point p donné en écrivant p.x ou p[0] et p.y ou p[1]
# La méthode __getitem__ de la classe Point, nous permet cet usage de code, nous
# permettant de considérer un objet Point comme une liste
# La suite des fonctions définies par la suite s'appuient donc sur ces quelques
# méthodes

class Point:
    """
    Représente un point dans le repère (o, i, j)
    @param x: l'abcisse du Point
    @param y: l'ordonnée du Point
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return str((self.x, self.y))

    def __eq__(self, o) -> bool:
        """
        teste l'égalité entre ce point et un autre point o
        @param o: second point
        @return bool
        """
        return o != None and self.x == o.x and self.y == o.y

    def __getitem__(self, index: int) -> int:
        """
        @param index: 0 pour x et 1 pour l'ordonnée
        @return int
        @raise IndexError si indice différent de 0 ou 1
        """
        if index == 0: return self.x
        if index == 1: return self.y
        raise IndexError("L'index doit être soit 0 soit 1")

    def __setitem__(self, index, valeur):
        """
        @param index: 0 pour x et 1 pour l'ordonnée
        @param valeur: nouvelle valeur de l'attribut
        @raise IndexError si indice différent de 0 ou 1
        """
        if index == 0: self.x = valeur
        elif index == 1: self.y = valeur
        else: raise IndexError("L'index doit être soit 0 soit 1")

def dist(A: Point, B: Point) -> float:
    """
    Calcule la distance entre deux points
    @param A: premier point
    @param B: second point
    @return float
    """
    return math.sqrt(math.pow(B.y - A.y, 2) + math.pow(B.x - A.x, 2))

#--- Fonctions et classes de manipulation des objets de type Zone ---
# Etant dans un langage orienté objet, il est plus simple pour nous de visualiser
# chaque structure, élément, nécessaire pour ce DM, comme une classe
# La notion de Zone rectangulaire étant souvent abordée, nous avons donc opté de
# de définir une classe (structure) qui y est associée
# Comme pour la classe Point, nous y avons défini les méthodes nécessaires permet
# -tant une représentation en chaine de caractères, de comparer deux zones, et
# pour alléger les écritures on pourra écrire, pour une zone z, soit z.ig ou z[0]
# pour le point inférieur gauche et z.sd ou z[1] pour le point supérieur droit

class Zone:
    """
    Une zone rectangulaire est composée de deux points (IG et SD)
    @param ig: premier point, le point inférieur gauche
    @param sd: second point, le point supérieur droit
    """

    def __init__(self, ig, sd):
        self.ig = ig
        self.sd = sd

    def __str__(self):
        return f"Zone({self.ig},{self.sd})"

    def __eq__(self, o):
        return o != None and self.ig == o.ig and self.sd == o.sd

    def __getitem__(self, index: int) -> int:
        if index == 0: return self.ig
        if index == 1: return self.sd
        raise IndexError("L'index doit être soit 0 soit 1")

    def __setitem__(self, index, valeur):
        if index == 0: self.ig = valeur
        elif index == 1: self.sd = valeur
        else: raise IndexError("L'index doit être soit 0 soit 1")

def estUnPointDeLaZone(point: Point, zone: Zone) -> bool:
    """
    Vérifie si un point donné est un point de la zone
    @param point: Point
    @param zone: Zone
    @return bool
    """
    return ((zone.ig.x < point.x and point.x <= zone.sd.x) and
            (zone.ig.y < point.y and point.y <= zone.sd.y))

#--- Fonctions et classes pour les ABRZ

class ABRZ:
    """
    structure de ABRZ
    @param valeur: point
    @param cs: coordonnée de séparation
        si cs=0, tout noeud de self.gauche a une abcisse <= à l'abcisse de self
                 tout noeud de self.droit a une abcisse > à l'abcisse de self
        si cs=1, tout noeud de self.gauche a une ordonnée <= à l'ordonnée de self
                 tout noeud de self.droit a une ordonnée > à l'ordonnée de self
        Il doit avoir alternance de cs entre deux sous-arbres successifs
    @param gauche: sous-arbre gauche
    @param droit: sous-arbre droit
    """

    def __init__(self, valeur, cs=0, gauche=None, droit=None):
        if cs != 0 and cs != 1:
            raise Exception("La coordonnée de séparation doit être soit 0 soit 1")
        self.valeur = valeur
        self.cs = cs
        self.gauche = gauche
        self.droit = droit

    def __str__(self):
        return f"({self.valeur},{self.cs})"

    def noeudToString(self):
        """ chaine d'affichage de la valeur et du cs du noeud"""
        return str(self)

def hauteur(A: ABRZ) -> int:
    """fonction qui calcule la hauteur d'un arbre binaire A"""
    if A == None: return -1
    return 1 + max(hauteur(A.gauche), hauteur(A.droit))

def dessinArbre(A: ABRZ, decalage=1) -> str:
    """retourner une chaine d'affichage planaire de l'arbre"""
    if A == None:
        return ""

    def affichageProfondeur(A, profondeur):
        if A == None:
            return " "
        ligne = affichageProfondeur(A.gauche, profondeur - 1)
        if (profondeur == 0):
            #ligne += str(A.valeur) + "," + str(A.cs)
            ligne += A.noeudToString()
        else:
            ligne += " "
        return ligne + affichageProfondeur(A.droit, profondeur - 1)

    chaine = ""
    for p in range(hauteur(A) + 1):
        chaine += affichageProfondeur(A, p) + '\n'
    return chaine

def afficherArbre(A):
    """ affichage de l'arbre"""
    print(dessinArbre(A))

#-------------------------- Fonctions décoratrices -----------------------------

# Dans la plupart de questions, les fonctions parcourent des noeuds de l'arbre
# On peut choisir de permettre de les afficher ou pas
# Et comme pour certaines fonctions, on aura besoin d'un compteur
# Nous allons, pour satisfaire ces deux besoins, definir une fonction python
# particulière : un décorateur. Les décorateurs sont des fonctions permettant
# de modifier le comportement de certaines fonctions
# La fonction décoratrice permettra, pour une fonction, d'afficher et/ou de
# compter si on le veut les noeuds parcourus

SHOW_FLAG = False   # Mettre à True si on veut afficher les noeuds parcourus
COUNTER_FLAG = False# Mettre à True si on veut compter le nombre de noeuds parcourus
compteur = 0        # compteur pour le cas où on compte

def decorator(function):
    """
    permet d'afficher tous les noeuds d'un arbre parcourus par une fonction,
    si SHOW_FLAG = True
    et de compter les noeuds, si COUNTER_FLAG = True
    Cette fonction sera passée en paramètre lors de sa définition
        >>> @decorator
        >>> def function(...):
        ...
    """
    global SHOW_FLAG, COUNTER_FLAG

    def decorated(A: ABRZ, *args, **kw):
        global compteur
        if SHOW_FLAG:
            if A != None:
                print(A.valeur, "vu")
        if COUNTER_FLAG:
            if A != None:
                compteur += 1
        return function(A, *args, **kw)

    return decorated

#-------------------------- Fonctions du DM ------------------------------------

#--- QUESTION 1
# Voir pdf

#--- QUESTION 2
#--- Question 2a
def creerArbre(p: Point, g: ABRZ, d: ABRZ, cs: int) -> ABRZ:
    """
    crée un arbre
    @param p: Point de la racine
    @param g: sous-arbre gauche
    @param d: sous-arbre droit
    @param cs: coordonnée de séparation
    @return ABRZ
    """
    return ABRZ(p, cs, g, d)

#--- Question 2b
@decorator
def inserer(A: ABRZ, p: Point) -> ABRZ:
    """
    insère un point dans un arbre s'il n'existe pas déjà
    @param A: l'arbre
    @param p: le point à insérer
    @return ABRZ
    """
    if A == None:
        return ABRZ(p, 0, None, None)
    if A.valeur == p:
        print("Ce point existe déjà")
    else:
        if p[A.cs] <= A.valeur[A.cs]: # insertion à gauche
            if A.gauche == None:
                A.gauche = ABRZ(p, (A.cs+1)%2, None, None)
            else:
                A.gauche = inserer(A.gauche, p)
        else: # insertion à droite
            if A.droit == None:
                A.droit = ABRZ(p, (A.cs+1)%2, None, None)
            else:
                A.droit = inserer(A.droit, p)
    return A

#--- QUESTION 3
#--- Question 3a
@decorator
def recherche(A: ABRZ, p: Point) -> ABRZ:
    """
    insère un point dans un arbre s'il n'existe pas déjà
    @param A: l'arbre
    @param p: le point à insérer
    @return ABRZ
    """
    if A != None and A.valeur != p:
        if p[A.cs] <= A.valeur[A.cs]: # recherche à gauche
            return recherche(A.gauche, p)
        else: # recherche à droite
            return recherche(A.droit, p)
    return A

#--- Question 3b:
# C'est un peu comme une recherche dichotomique
# La complexité est égal à la hauteur de l'arbre + 1

#--- QUESTION 4
#--- Question 4a
@decorator
def minX(A: ABRZ) -> ABRZ:
    """
    retrouve le noeud de l'arbre avec le plus petit abcisse
    @param A: arbre
    @return ABRZ
    """
    if A.gauche == None and A.droit == None:
        return A
    if A.cs == 0:
        if A.gauche == None:
            return A
        else:
            return minX(A.gauche)
    else:
        res = None
        if A.gauche == None:
            res = minX(A.droit)
        elif A.droit == None:
            res = minX(A.gauche)
        else:
            gauche = minX(A.gauche)
            droit = minX(A.droit)
            res = gauche if gauche.valeur[0] < droit.valeur[0] else droit
        return res if res.valeur[0] < A.valeur[0] else A

#--- Question 4b:
# Noeuds visités par le parcours : A, B, E, I, P

#--- Question 4c
@decorator
def minXY(A: ABRZ, cs: int) -> ABRZ:
    """
    retrouve le noeud à l'abcisse  minimale si cs = 0
                        l'ordonnée minimale si cs = 1
    @param A: arbre
    @param cs: coordonnée de comparaison
    @return ABRZ
    """
    if A.gauche == None and A.droit == None:
        return A
    if A.cs == cs:
        if A.gauche == None:
            return A
        else:
            return minXY(A.gauche, cs)
    else:
        res = None
        if A.gauche == None:
            res = minXY(A.droit, cs)
        elif A.droit == None:
            res = minXY(A.gauche, cs)
        else:
            gauche = minXY(A.gauche, cs)
            droit = minXY(A.droit, cs)
            res = gauche if gauche.valeur[cs] < droit.valeur[cs] else droit
        return res if res.valeur[cs] < A.valeur[cs] else A

#--- Question 5a
#--- QUESTION 5
@decorator
def dansDroiteV(A: ABRZ, x: int):
    """
    Affichage des points de l'arbre d'abcisse x
    @param A: arbre
    @param x: abcisse
    """
    if A != None:
        if A.valeur.x == x:
            print(f"La droite verticale x = {x} passe par le point {A.valeur} de l'arbre")
        if A.cs == 0:
            if A.valeur.x >= x:
                dansDroiteV(A.gauche, x)
            else:
                dansDroiteV(A.droit, x)
        else:
            dansDroiteV(A.gauche, x)
            dansDroiteV(A.droit, x)

#--- Question 5b
# Les points visités sont ACJDHKL

#--- Question 5c
@decorator
def dansDroite(A: ABRZ, p: int, cs: int):
    """
    Affichage des points de l'arbre d'abcisse p si cs = 0
                                    d'ordonnée p si cs = 1
    @param A: arbre
    @param p: valeur de l'abcisse ou de l'ordonnée
    @param cs: coordonnée de comparaison
    """
    if A != None:
        if A.valeur[cs] == p:
            orientation = ("verticale x" if cs == 0 else "horizontale y")
            print(f"La droite {orientation} = {p} passe par le point {A.valeur} de l'arbre")
        if A.cs == cs:
            if A.valeur[cs] >= p:
                dansDroite(A.gauche, p, cs)
            else:
                dansDroite(A.droit, p, cs)
        else:
            dansDroite(A.gauche, p, cs)
            dansDroite(A.droit, p, cs)

#--- QUESTION 6
@decorator
def intersection(A: ABRZ, p: Point, q: Point):
    """
    Affichage des points de l'arbre situé dans la zone formée par les points p et q
    @param A: arbre
    @param p: premier point de la zone
    @param q: second point de la zone
    """
    if A != None:
        zone = Zone(p, q)
        if estUnPointDeLaZone(A.valeur, zone):
            print(f"Le point {A.valeur} est un point de la zone {zone}")
            intersection(A.gauche, p, q)
            intersection(A.droit, p, q)
        else:
            if A.valeur[A.cs] <= zone.ig[A.cs]:
                intersection(A.droit, p, q)
            else:
                intersection(A.gauche, p, q)

#--- QUESTION 7
#--- Question 7a
@decorator
def _plusproche(A: ABRZ,currentProche: ABRZ,p: Point, d: int,zoneParent: Zone) -> ABRZ:
    """
    recherche le point le plus proche en fonction des zones associées
    @param A: noeud courant
    @param currentProche: noeud le plus proche actuel
    @param p: point à approcher
    @param d: distance minimale courante
    @param zoneParent: zones du noeud parent auquel appartient le noeud courant
        Par ex: - Pour A.cs = 0, on sait que A découpe le plan en une zone gauche zg
                et une zone droite zd.
                >>> if A.gauche == B:
                ...     _plusproche(B, p, currentProche, currentDistance, zg)
                >>> if A.droit == C:
                ...     _plusproche(C, p, currentProche, currentDistance, zd)
            La même logique est à appliquer si A.cs = 1 et qu'il s'agit de zone basse
            et zone haute.
        # Ce paramètre de plus est nécessaire pour éviter de parcourir à nouveau
        # l'arbre de départ afin de retrouver les zones associées à chaque noeud
        # On a donc juste besoin de la zone parente à laquelle est associée le noeud
        # afin de retrouver les zones qu'il crée
    """
    # print(A.valeur)
    if dist(A.valeur, p) < d:
        currentProche = A
        d = dist(A.valeur, p)
    zone1 = Zone(Point(zoneParent.ig.x, zoneParent.ig.y), Point(zoneParent.sd.x, zoneParent.sd.y))
    zone2 = Zone(Point(zoneParent.ig.x, zoneParent.ig.y), Point(zoneParent.sd.x, zoneParent.sd.y))
    zone1.sd[A.cs] = A.valeur[A.cs] # zone gauche ou zone basse du noeud courant
    zone2.ig[A.cs] = A.valeur[A.cs] # zone droite ou zone haute du noeud courant
    if estUnPointDeLaZone(p, zone1) and A.gauche != None:
        return _plusproche(A.gauche, currentProche, p, d, zone1)
    elif estUnPointDeLaZone(p, zone2) and A.droit != None:
        return _plusproche(A.droit, currentProche, p, d, zone2)
    return currentProche

#@decorator # pas nécessaire de décorer la fonction
def plusproche(A: ABRZ, p: Point) -> ABRZ:
    """
    Retrouve le noeud dont le point est le plus proche de p
    @param A: arbre
    @param p: point
    @return ABRZ le plus proche de p
    """
    return _plusproche(A, A, p, dist(A.valeur, p),
                    Zone(Point(-math.inf,-math.inf), Point(math.inf,math.inf)))

# Question 7b:
# L'ordre de parcours et ABEFGN
# La complexité de la fonction est égale ici à la hauteur de l'arbre + 1

#-------------------------- Fonctions de tests ---------------------------------

def afficheCompteur():
    if COUNTER_FLAG:
        print(f"---> Nombre de noeuds visités : {compteur}\n")

def testRecherche(A, tabPoints):
    global compteur
    for pt in tabPoints:
        compteur = 0; res = recherche(A,pt)
        if res == None:
            print("\nPoint non trouvé")
        else:
            print(f"\nPoint {pt}. Il est racine de :\n")
            afficherArbre(res)
        afficheCompteur()

def testMinX(A):
    global compteur; compteur = 0
    print("\nLe point d'abcise minimal, racine de:\n")
    res = minX(A)
    afficherArbre(res)
    afficheCompteur()

def testDansDroiteV(A, tabX):
    global compteur
    for vx in tabX:
        print("\nLes points de la droite (x=%.2f) sont:"%(vx))
        compteur = 0; dansDroiteV(A, vx)
        afficheCompteur()

def testIntersection(A, tabZones):
    global compteur
    for zone in tabZones:
        print(f"\nLa zone {zone} contient:")
        compteur = 0; intersection(A, zone.ig, zone.sd)
        afficheCompteur()

def testPlusProche(A, tabPoints):
    global compteur
    for pt in tabPoints:
        compteur = 0
        res = plusproche(A, pt)
        print(f"Le point parmi les plus proches de {pt} est :", end="");
        print(res.valeur)
        afficheCompteur()

#-------------------------- Main -----------------------------------------------

def mainAvecArbreExemple():
    A = None; g = None; d = None
    d = creerArbre(Point(3, 5), None, None, 1)
    g = creerArbre(Point(1, 5), None, None, 1)
    A = creerArbre(Point(2, 4), g, d, 0)
    A = creerArbre(Point(1, 3), None, A, 1)
    d = creerArbre(Point(6, 3), None, None, 1)
    d = creerArbre(Point(5, 4), None, d, 0)
    d = creerArbre(Point(6, 2), None, d, 1)
    A = creerArbre(Point(4, 3), A, d, 0)
    d = creerArbre(Point(5, 9), None, None, 1)
    d = creerArbre(Point(3, 10), None, d, 0)
    A = creerArbre(Point(1, 6), A, d, 1)
    g = creerArbre(Point(9, 8), None, None, 1)
    d = creerArbre(Point(11, 9), g, None, 0)
    d = creerArbre(Point(8, 5), None, d, 1)
    A = creerArbre(Point(7, 1), A, d, 0)

    print("\n-----------------------------------------------------------------")
    print("MAIN AVEC EXEMPLE".center(70)); print()
    print("---------------------------".center(70))

    print("Affichage arbre exemple".center(70)); print()
    afficherArbre(A)
    print("---------------------------".center(70))

    print("Test de la recherche de points".center(70)); print()
    tabPoints = [Point(5, 4), Point(9, 8)]
    testRecherche(A, tabPoints)
    print("---------------------------".center(70))

    print("Test de l'abcisse minimale".center(70)); print()
    testMinX(A)
    print("---------------------------".center(70))

    print("Test dans droite verticale".center(70)); print()
    tabX = Point(5, 6)
    testDansDroiteV(A, tabX)
    print("---------------------------".center(70))

    print("Test intersection avec zone".center(70)); print()
    tabZones = [Zone(Point(1, 2), Point(6, 7)), Zone(Point(6, 1), Point(10, 9))]
    testIntersection(A, tabZones)
    print("---------------------------".center(70))

    print("Test du point le plus proche".center(70)); print()
    tabPoints = [Point(3, 4), Point(5, 2), Point(8, 4), Point(11, 9)]
    testPlusProche(A, tabPoints)

def mainListePoints():
    listePoints = [
        Point(7, 6), Point(2, 10), Point(11, 3), Point(10, 9),
        Point(4, 4), Point(5, 8), Point(6, 1), Point(8, 7),
        Point(1, 5), Point(9, 2), Point(8, 4), Point(9, 5),
        Point(5, 9), Point(6, 3), Point(7, 8), Point(2, 3)
        ]

    print("\n-----------------------------------------------------------------")
    print("MAIN AVEC LISTE DE 16 POINTS".center(70)); print()

    print("Création de l'arbre".center(70))
    A = None
    for pt in listePoints:
        A = inserer(A, pt)
        print("\nAffichage de l'arbre :\n")
        afficherArbre(A)
    print("---------------------------".center(70))

    print("Affichage arbre exemple".center(70)); print()
    afficherArbre(A)
    print("---------------------------".center(70))

    print("Test de la recherche de points".center(70)); print()
    tabPoints = [Point(5, 4), Point(9, 8)]
    testRecherche(A, tabPoints)
    print("---------------------------".center(70))

    print("Test de l'abcisse minimale".center(70)); print()
    testMinX(A)
    print("---------------------------".center(70))

    print("Test dans droite verticale".center(70)); print()
    tabX = Point(5, 6)
    testDansDroiteV(A, tabX)
    print("---------------------------".center(70))

    print("Test intersection avec zone".center(70)); print()
    tabZones = [Zone(Point(1, 2), Point(6, 7)), Zone(Point(6, 1), Point(10, 9))]
    testIntersection(A, tabZones)
    print("---------------------------".center(70))

    print("Test du point le plus proche".center(70)); print()
    tabPoints = [Point(3, 4), Point(5, 2), Point(8, 4), Point(11, 9)]
    testPlusProche(A, tabPoints)

def mainLongueListePoints():
    listePoints = [
        Point(22, 37), Point(9, 26), Point(35, 4), Point(15, 9), Point(8, 10),
        Point(27, 8), Point(34, 30), Point(31, 28), Point(5, 27), Point(3, 27),
        Point(13, 13), Point(12, 37), Point(2, 12), Point(17, 32), Point(1, 28),
        Point(2, 21), Point(32, 7), Point(23, 25), Point(37, 31), Point(24, 21),
        Point(2, 12), Point(23, 35), Point(35, 36), Point(25, 17), Point(10, 39),
        Point(24, 7), Point(36, 14), Point(27, 19), Point(12, 1), Point(38, 20),
        Point(37, 9), Point(17, 27), Point(7, 0), Point(3, 26), Point(9, 13),
        Point(12, 1), Point(23, 20), Point(29, 20), Point(32, 35), Point(1, 33),
        Point(5, 9), Point(37, 36), Point(5, 31), Point(10, 0), Point(27, 26),
        Point(20, 37), Point(27, 9), Point(32, 11), Point(8, 14), Point(3, 20),
        Point(1, 32), Point(31, 1), Point(25, 8), Point(6, 22), Point(1, 39),
        Point(7, 21), Point(6, 23), Point(22, 39), Point(20, 7), Point(11, 15),
        Point(8, 10), Point(25, 24), Point(2, 6), Point(31, 25), Point(22, 1),
        Point(21, 2), Point(4, 21), Point(19, 22), Point(31, 5), Point(8, 38),
        Point(9, 13), Point(24, 6), Point(32, 4), Point(37, 26), Point(27, 3),
        Point(31, 22), Point(25, 18), Point(6, 19), Point(14, 30), Point(19, 30),
        Point(18, 21), Point(2, 39), Point(27, 39), Point(22, 27), Point(39, 11),
        Point(2, 3), Point(24, 38), Point(32, 28), Point(4, 5), Point(1, 6),
        Point(2, 26), Point(14, 11), Point(12, 36), Point(23, 9), Point(17, 35),
        Point(22, 30), Point(38, 5), Point(36, 6), Point(17, 15), Point(29, 33)
        ]

    print("\n-----------------------------------------------------------------")
    print("MAIN AVEC LISTE DE 100 POINTS".center(70)); print()

    print("Création de l'arbre".center(70))
    A = None
    for pt in listePoints:
        A = inserer(A, pt)
        #print("\nAffichage de l'arbre :\n")
        #afficherArbre(A)
    print("---------------------------".center(70))

    print("Affichage arbre exemple".center(70)); print()
    afficherArbre(A)
    print("---------------------------".center(70))

    print("Test de la recherche de points".center(70)); print()
    tabPoints = [Point(24, 7), Point(6, 19), Point(0, 5)]
    testRecherche(A, tabPoints)
    print("---------------------------".center(70))

    print("Test de l'abcisse minimale".center(70)); print()
    testMinX(A)
    print("---------------------------".center(70))

    print("Test dans droite verticale".center(70)); print()
    tabX = Point(5, 6)
    testDansDroiteV(A, tabX)
    print("---------------------------".center(70))

    print("Test intersection avec zone".center(70)); print()
    tabZones = [Zone(Point(1, 2), Point(6, 7)), Zone(Point(6, 1), Point(10, 9))]
    testIntersection(A, tabZones)
    print("---------------------------".center(70))

    print("Test du point le plus proche".center(70)); print()
    tabPoints = [Point(3, 4), Point(5, 2), Point(8, 4), Point(11, 9)]
    testPlusProche(A, tabPoints)

#-------------------------- Programme principal --------------------------------

def main(show=False, counter=False):
    """
    @param show: si show=True, active l'affichage des noeuds visités parcourus
        par les fonctions
    @param counter: si counter=True, active le comptage du nombre de noeuds
        visités par les fonctions
    """
    print("\n-----------------------------------------------------------------")
    print("DM d'ALGORITHMIQUE".center(70))
    print("Ben KABONGO BUZANGU & Meryam EL BOUDOUTI".center(70))
    if show:
        print("\nVous avez choisi d'afficher les noeuds visités.\n"
            "On affichera donc, pour chaque fonction, le point du noeud et "
            "la précision 'vu'.")
    if counter:
        print("\n Vous avez choisi de compter les noeuds visités.\n"
            "On affichera donc, pour chaque fonction, le nombre de noeuds parcourus")
    print("\n-----------------------------------------------------------------")

    # S'il y activation de ces deux affichages, avant l'affichage des résultats
    # d'une méthode, les noeuds visités sont affichés avant
    # Le nombre de noeuds est affiché après
    global SHOW_FLAG, COUNTER_FLAG
    SHOW_FLAG = show # afficher ou pas les noeuds parcourus
    COUNTER_FLAG = counter # compter ou pas les noeuds

    mainAvecArbreExemple()
    mainListePoints()
    mainLongueListePoints()

if __name__ == '__main__':
    main(show=True,counter=True)
