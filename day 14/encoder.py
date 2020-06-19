
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
longalpha=len(alphabet)

def calculfreq (L):
    #renvoie une liste de listes contenant le caractère suivi de sa fréquence d'apparition
    M=[]
    for k in range (longalpha):
        M.append([alphabet[k],0])
    n=len(L)
    for k in range(0,longalpha):
        for i in range (0,n):
            if L[i]== alphabet[k]:
                M[k][1]+=1
    return M


def insere(x,liste):
    #x est une liste de deux élements: le caractère et sa fréquence d'apparition
    if liste==[]:
        return [x]
    elif (x[1])<=(liste[0][1]):
        return [x] + liste
    else:
        return[liste[0]] + insere(x,liste[1:len(liste)])

def fusion(liste1,liste2):
    if liste1==[]:
        return liste2
    elif liste2==[]:
        return liste1
    else:
        return fusion(liste1[1:len(liste1)],insere(liste1[0],liste2))

def tri_fusion(liste):
    #renvoie la liste classée par ordre croissant de fréquence d'apparition des éléments
    n=len(liste)
    if n==0 or n==1:
        return liste
    else:
        return fusion(tri_fusion(liste[0:n//2]),tri_fusion(liste[n//2:n]))


#on va créer l'arbre binaire



def nombreetapes(n):
    #n est le nombre de caractères
    p=n
    i=0
    while p!=1:
        if p%2==0:
            p=p/2
        else:
            p=(p+1)/2
        i+=1
    return i

#création de classe d'arbre

class Arbre():
    def __init__ (self,donnee,gauche=None,droit=None):
        self.donnee = donnee
        self.gauche = gauche
        self.droit = droit
    def __repr__ (self):
        return("Arbre de noeud {} de fils gauche {} et de fils droit {}".format(self.donnee,self.gauche,self.droit))



class Feuille(Arbre):
    def __init__ (self,donnee):
        self.gauche = None
        self.droit = None
        self.donnee = donnee


def arbrehuff(liste):
    #la liste correspond au dictionnaire classé par ordre croissant de fréquences
    l=liste
    m=[]
    h=[]

    for k in range(0,len(l)):
        if l[k][1]!=0:
            m.append (l[k][0])
            h.append (l[k][1])
    #m est la liste des caractères dans l'ordre de trifusion
    #h est la liste des fréquences associées
    i=0
    #transformer h en liste d'arbres
    h1=[]
    for i in range (0,len(h)):
        h1.append(Arbre(h[i]))
    h=h1
    g=[]
    nbdetapes= nombreetapes(len(h))
    while i<nbdetapes:
        if len(h)%2==0:
            for j in range (0,len(h)-1):
                k=(h[j].donnee)+(h[j+1].donnee)
                g.append(Arbre(k,h[j],h[j+1]))
        else:
            for i in range(0,len(h)-2):
                k=(h[j].donnee)+(h[j+1].donnee)
                g.append(Arbre(k,h[j],h[j+1]))
            g.append(Arbre(h[len(h)-1]))
        h=g
        g=[]
        i+=1
    return h

freq = {"A":5,"B":1,"C":1,"D":1}
h=arbrehuff(freq)
print(h)
