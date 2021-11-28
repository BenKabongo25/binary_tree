# -*- coding: utf-8 -*-

import sys
import io
from main import *

SHOW_FLAG = False
COUNTER_FLAG = False

arbre = None
A = Point(7, 6); arbre = creerArbre(A, None, None, 0) # cs = 0
B = Point(2, 10); arbre = inserer(arbre, B) # cs = 1
C = Point(11, 3); arbre = inserer(arbre, C) # cs = 1
D = Point(10, 9); arbre = inserer(arbre, D) # cs = 0
E = Point(4, 4); arbre = inserer(arbre, E) # cs = 0
F = Point(5, 8); arbre = inserer(arbre, F) # cs = 1
G = Point(6, 1); arbre = inserer(arbre, G) # cs = 0
H = Point(8, 7); arbre = inserer(arbre, H) # cs = 1
I = Point(1, 5); arbre = inserer(arbre, I) # cs = 1
J = Point(9, 2); arbre = inserer(arbre, J) # cs = 0
K = Point(8, 4); arbre = inserer(arbre, K) # cs = 0
L = Point(9, 5); arbre = inserer(arbre, L) # cs = 1
M = Point(5, 9); arbre = inserer(arbre, M) # cs = 0
N = Point(6, 3); arbre = inserer(arbre, N) # cs = 1
O = Point(7, 8); arbre = inserer(arbre, O) # cs = 1
P = Point(2, 3); arbre = inserer(arbre, P) # cs = 0

def testPoint():
    A = Point(3, 5)
    assert A == Point(3, 5)
    A.x = 2
    A.y = 3
    assert A == Point(2, 3)
    A[0] = 3
    A[1] = 2
    assert A == Point(3, 2)
    assert A[0] == 3 and A[1] == 2

def testDist():
    assert dist(Point(0,0), Point(1,1)) == math.sqrt(2)

def testZone():
    a = Point(0,0); b = Point(2,2); zone = Zone(a,b)
    assert zone.ig == a and zone.sd == b
    assert zone == Zone(Point(0,0), Point(2,2))
    assert not zone == Zone(Point(0,0), Point(1,1))

def testEstUnPointDeLaZone():
    a = Point(0,0); b = Point(2,2); zone = Zone(a,b)
    assert estUnPointDeLaZone(Point(1,1), zone)
    assert not estUnPointDeLaZone(Point(-1,-1), zone)

def testABRZ():
    assert arbre.valeur == A
    assert arbre.cs == 0
    assert arbre.gauche.valeur == B
    assert arbre.droit.valeur == C

def testCreerArbre():
    a = creerArbre(A, None, None, 0)
    assert a.valeur == A
    assert a.gauche == None
    assert a.droit == None
    assert a.cs == 0
    b = creerArbre(B, None, None, 1)
    c = creerArbre(C, None, None, 1)
    a = creerArbre(A, b, c, 0)
    assert a.gauche == b
    assert a.droit == c

def testInserer():
    assert arbre.valeur == A
    assert arbre.cs == 0
    assert arbre.gauche.valeur == B and arbre.gauche.cs == 1
    assert arbre.droit.valeur == C and arbre.gauche.cs == 1

def testRecherche():
    assert recherche(None, P) == None
    assert recherche(arbre, P).valeur == P
    assert recherche(arbre, Point(0,0)) == None

def testMinX():
    assert minX(arbre).valeur == I

def testMinXY():
    assert minXY(arbre, 0).valeur == I
    assert minXY(arbre, 1).valeur == G

def testDansDroiteV():
    sys.stdout = io.StringIO()
    dansDroiteV(arbre, 9)
    assert str(J) in sys.stdout.getvalue()
    assert str(L) in sys.stdout.getvalue()
    sys.stdout.seek(2)
    dansDroiteV(arbre, 8)
    assert str(H) in sys.stdout.getvalue()
    assert str(K) in sys.stdout.getvalue()
    assert str(B) not in sys.stdout.getvalue()
    sys.stdout.close()
    sys.stdout = sys.__stdout__

def testDansDroite():
    sys.stdout = io.StringIO()
    dansDroite(arbre, 9, 0)
    assert str(J) in sys.stdout.getvalue()
    assert str(L) in sys.stdout.getvalue()
    sys.stdout.seek(2)
    dansDroite(arbre, 3, 1)
    assert str(C) in sys.stdout.getvalue()
    assert str(N) in sys.stdout.getvalue()
    assert str(P) in sys.stdout.getvalue()
    assert str(K) not in sys.stdout.getvalue()
    sys.stdout.close()
    sys.stdout = sys.__stdout__

def testIntersection():
    sys.stdout = io.StringIO()
    intersection(arbre, Point(-math.inf,-math.inf), Point(math.inf,math.inf))
    assert str(A) in sys.stdout.getvalue()
    assert str(P) in sys.stdout.getvalue()
    sys.stdout.seek(2)
    intersection(arbre, E, D)
    assert str(A) in sys.stdout.getvalue()
    assert str(F) in sys.stdout.getvalue()
    assert str(O) in sys.stdout.getvalue()
    assert str(B) not in sys.stdout.getvalue()
    assert str(I) not in sys.stdout.getvalue()
    assert str(P) not in sys.stdout.getvalue()
    sys.stdout.close()
    sys.stdout = sys.__stdout__

def testPlusProche():
    def plusproche2(p):
        plusproche = None
        distance = math.inf
        for pt in [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P]:
            if dist(pt, p) < distance:
                plusproche = pt
                distance = dist(pt, p)
        return plusproche
    assert plusproche(arbre, Point(0, 0)).valeur == plusproche2(Point(0, 0))
    assert plusproche(arbre, Point(1, 1)).valeur == plusproche2(Point(1, 1))
    assert plusproche(arbre, Point(2, 3)).valeur == plusproche2(Point(2, 3))
    assert plusproche(arbre, Point(5, 0)).valeur == plusproche2(Point(5, 0))
    assert plusproche(arbre, Point(0, 9)).valeur == plusproche2(Point(0, 9))

print("Résultat des tests")
testPoint()
testDist()
testZone()
testEstUnPointDeLaZone()
testABRZ()
testCreerArbre()
testInserer()
testRecherche()
testMinX()
testMinXY()
testDansDroiteV()
testDansDroite()
testIntersection()
testPlusProche()
print("Tous les tests sont ok")
