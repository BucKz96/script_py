
# coding: utf-8

# # Python : Manipulation des données avec Pandas

# Pandas est une librairie Python spécialisée dans l’analyse des données qui a beaucoup de succès. Dans ce projet pratique, nous nous intéresserons surtout aux fonctionnalités de manipulations de données qu’elle propose. Un objet de type "DataFrame" (tableau de données), permet de réaliser de nombreuses opérations de pré-traitements, de filtrage, de nettoyage, de construction de nouvelles variables à partir des existentes, etc.,... préalables à la modélisation statistique.
# 
# La librairie est très largement documentée. Il faut prendre le temps de consulter le Help et de s'exercer simplement ! Deux liens du Help sont incontournables, celui relative aux DataFrame (http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html#pandas.DataFrame), celui relative aux Series que nous travaillerons également dessus (vecteur de données : http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html#pandas.Series).

# # Librairie Pandas - Options et version
# 
# Il faut charger la librairie et, éventuellement, la configurer selon vos attentes. Pensez à vérifier votre version, elle doit être (non seulement la même sur tous les postes mais aussi la plus récente).

# In[57]:


# 1è étape : il faut charger Pandas
# R :
import pandas as pd

# Vérifiez sa version ? 
# R :
print(pd.__version__) 

# Quelle est la dernière version et MAJ la votre en ligne de commande (au cas où Pandas n'est pas la + récente) ? 
# R :
#conda update pandas
#conda install pkg
#¢onda remove pkg

#pip install pkg
#pip install --upgrade pkg
#pip install --downgrade pkg
#pip remove pkg

# Rappelez les commandes qui permettent d'installer, MAJ, utiliser 1version moins récente et désinstaller 1lib ?   
# R :
#

# Modifiez le nb de lignes à afficher dans les print à 10. L'idée est d'éviter que le projet se résume 
# à de multiples affichages de longs tableaux ! 
# R :
pd.options.display.max_rows = 10

# Modifiez le nb de colonnes à afficher dans les print à 10. L'idée est d'éviter que la console soit rapidement encombrée 
# par un grand nombre de col ! 
# R :
pd.options.display.max_columns = 10

# Malgré le fait que ns avons fixé 1petit nb de col à afficher (à 10), les résultats peuvent être tronqués ds la console !
# En d'autres termes, l'idée est d'améliorer l'affichage ds la console en évitant un retour à la ligne (Spyder, Pyzo, nootebook,..).
# Activez l'option nécessaire à ce besoin ? 
# R : 
pd.set_option('expand_frame_repr', False)

Après avoir réussi ces dernieres manip, créez 1script (startup.py) avec ces diff commandes et indiquez son path à Pyzo.
L'idée est qu'à chaque lancement de Python, vos différents imports et options soient activées automatiquement !
# # Chargement, structure DataFrame et description des données
1DataFrame correspond à 1tableau (lignes x cols) que je noterai à partir de maintenant "df".
Concernant notre fichier "sante.txt" :
La 1è ligne correspond aux noms des vars. A partir de la 2è ligne, ns disposons des valeurs pr chaque enregistrement (individu). 
Le caractère tabulation "\t" fait office de séparateur de cols.
Ns allons vérifier tt ça ds 1 1er tps en lignes de commandes Linux et ds un 2sd temps sur Python.En ligne de commande Linux : 

1) Créez 1répertoire "data" (où vs stockerez d'1façon permanente ts les objets que ns travaillerons dessus).
2) Télécharez à partir du google-drive-datartisan le fichier "sante.txt" (secteur de la sante).
# R : 

Dans le terminal linux (et non ds 1éditeur de texte), déterminez : 
3) la taille du fichier, le nombre de lignes et affichez les 5 1è (lignes). 
# L'idée est d'avoir un aperçu du fichier ET surtout de déterminer : 
# Le fait s'il tiens en mémoire (données massives ou non),
# Le type de séparateur (tabulation, virgule, pipe,...),
# La présence ou non des noms des vars. 
# Le tout pour préparer la commande Python de création de df (à partir de ce fichier) ! 
# R : 

# awk 'END {print NR}' sante.txt ==> Nombre de lignes dans un file
# In[ ]:


# Refaites ces diff manip strictement à l'aide de commandes Python : création de rép "data", téléchargement du fichier,... ?
# R : indice import os, open()

# Revenez sur le script "startup.py" et y mettre les commandes qui vs permettent de : 
# Créer le rép "data" (s'il n'existe pas) ?
# Se positinner dessus automatiquement (à chaque démarrage).
# R :


# In[43]:


# Chargez le fichier en tant qu'objet DataFrame (nom = df_sante) 
# R : 
import pandas as pd
import os
os.chdir('/home/buckz/Data')

df_sante = pd.read_csv('sante.txt')

df_sante = pd.DataFrame()

# Vérifiez que le type obtenu est bien un 'pandas.core.frame.DataFrame'
# R : 
type(df_sante)

Le type DataFrame est bien reconnu. Voyons maintenant sa structure.
Faire un print(df) où vs vérifiez à l'oeil nu, dans la console, ligne par ligne la structure du df n'a pas de sens (contexte Big Data) !
Croyez moi, ça ne va pas vs faire avancer (inversement, au bon entendeur !). 
Ns préferons alors déterminer la dimension du df, afficher un bout des 1ères et dernières lignes (et comparer avec les résultats déjà obtenu avec le fichier ".txt").  
# In[48]:


# Déterminez les dimensions : nb de lignes et nb de colonnes ? 
# R : 

print(pd.read_table(df_sante, index=5, columns=6)
# Vérifier que ce sont les bonnes dimensions avec le fichier ".txt"
# Rq : la ligne d'en-tête n'est pas comptabilisée dans le nombre de lignes ! 


# In[2]:


# Affichez les premières lignes du jeu de données ? 
# R : 


# In[ ]:


# Affichez les dernières lignes du jeu de données ? 
# R : 

Nous passons beaucoup de notre temps à charger des df et à afficher le head (tail) pour vérifier que tt est OK ! 
Il vaut mieux en faire de ça 1fonc 1fois pr tte que vs appelez au besoin ? 
# In[ ]:


# Ecrivez cette fonc où vs géréz les exceptions (contexte script en production) ? 
# R : 


# ### Les colonnes ?

# In[3]:


# Lister les colonnes (les noms des vars) ? 
# R : 


# In[4]:


# Supposons que ce dernier affichage ne vous conviens pas (à l'horizontal, surtout si vs avez 5000 cols) ?! 
# Mettez en place 1boucle "for" qui vous permez d'afficher le résultat (à la verticale) et de le contrôler (nb de col à afficher) ?
# R : 


# In[5]:


# Quelle est le type de chaque colonne : int64, object,... ? 
# R : 

Il y'a combien type ? Que veut dire le type "object" ? 
Question à revenir dessus plus tard (après avoir travaillé sur les Series), combien de type (en ligne de commande) ?   
# R : 
# In[6]:


# Au lieu de taper ces 2 dernières commandes, 
# il existe une commande qui vous permet de retrouver ces 2 derniers résultats (à la fois) ?
# Laquelle ?
# R : 

Pandas a tendance d'abuser de la mémoire lors de chargement des df.
Aussi, il est vivement recommandé de bien affecter les bons types à chaque variable ne serait-ce que pour éviter de faire des opérations douteuses, par exemple arithmétiques sur des vars de type "object".
Ds notre cas, vérifiez que notre fichier ne comporte pas de nombres avec des chiffres après la virgule ?
Malgré cela, Pandas a stocké les cols concernées en int64 au lieu de int8 (gaspillage) !
# In[ ]:


# Par souci d'optimisation, mettez les cols qui sont en int64 en int8 ?
# R : 


# In[ ]:


Q à traiter plus tard : Comment faire la même manip (sans relire le fichier) ? 

Supposons que ns avons à travailler sur un fichier avec des nombres avec des chiffres après la virgule (ou point pr spécifier un décimal (US Vs. EU)
Trouvez l'option ds pd.read_table() qui permet de le spécifier ? 
# R : 
# ### Description des données

# In[8]:


# Trouvez une commande pr présenter les statistiques descriptives de tt le df (min, max, moy,...) ?  
# R : 

Explication : 
Certains indicateurs statistiques ne sont valables que pour : 
# les variables numériques (ex. moyenne, min, etc. pour age, tauxmax,...),
# et inversemment pour les non-numériques (ex. top, freq, etc. pour sexe, typedouleur, ...),
# d'où les NaN dans certaines situations.
Est-ce que ce résultat vs convient ?! 
# Pr plus de clarté, ns souhaitons afficher les stats pr les vars num dans un 1er tps (1è commande ?)
# Et ds un 2sd tps les vars de type objects (2è commande ?)
# Comment faire ? 
# In[33]:


# Stats desc pr les vars num ? 
# R : 


# In[ ]:


# Stats desc pr les vars non-num ? 
# R : 


# ## Manipulation des variables

# ### Accès aux variables
# 
# Il est possible d'accéder explicitement aux variables. Dans un premier temps, nous utilisons directement les noms des champs (les noms des variables, en en-tête de colonne).

# In[9]:


# Accès à une colonne de votre choix ? 
# R : 


# In[10]:


# Autre manière d'accéder à une colonne avec le ".  ? 
# R : 


# In[12]:


# Accéder à un ensemble de colonnes ? 
# R : 


# In[13]:


# Une colonne est un vecteur (Series en terminologie Pandas)
# Affichage des premières valeurs
# R : 


# In[14]:


# Affichage des dernières valeurs
# R : 


# In[15]:


# Statistique descriptive d'une col. Pour plus de détails, voir :
# http://pandas.pydata.org/pandas-docs/stable/basics.html#summarizing-data-describe
# R : 


# In[17]:


# Calculer explicitement la moyenne, par ex col "age"
# R : 


# In[16]:


# Comptage des valeurs, par ex col "typedouleur"
# R : 


# In[18]:


# Un type Series est un vecteur, il est possible d'utiliser des indices
# Première valeur ? 
# R : 


# In[19]:


# 3 premières valeurs ? 
# R : 


# In[21]:


# Triez les valeurs d'une variable de manière croissante ? 
# R : 


# In[23]:


# le tri peut être généralisé aux DataFrame
# par exemple : triez le df selon l'âge puis afficher les 1è lignes
# R : 


# ## Accès indicé aux données d'un DataFrame
# On peut accéder aux valeurs du DataFrame via des indices ou plages d'indice. La structure se comporte alors comme une matrice. La cellule en haut et à gauche est de coordonnées (0,0).
# 
# Il y a différentes manières de le faire, l'utilisation de .iloc[,] constitue une des solutions les plus simples. N'oublions pas que Shape permet d'obtenir les dimensions (lignes et colonnes) du DataFrame.

# In[24]:


# Accèdez à la valeur située en (0,0) ?
# R : 


# In[25]:


# Accédez à la valeur située en dernière ligne, première colonne ? 
# indice : utilisez l'indiçage négatif
# R : 


# In[26]:


# Accédez la valeur située en dernière ligne, première colonne ? 
# indice : shape[0] renvoie le nombre de lignes (1è dimension) qu'il faut réduire de -1 parce que le 1è indice est égal à 0. 
# sinon on déborde
# R : 


# In[27]:


# Accédez aux 5 premières valeurs de toutes les colonnes ? 
# lignes => 0:5 (0 à 5 [non inclus])
# colonnes = : (toutes les colonnes)


# In[28]:


# Accéder aux 5 dernières lignes du df ? avec l'indiçage négatif, on le peut facilement 


# In[29]:


# Accédez aux 5 premières lignes et deux premières colonnes ? 


# In[30]:


# Accédez aux 5 1è lignes et colonnes 0, 1 et 4 ? 
# indice : on a une liste d'indices en colonne


# In[31]:


# faites la même chose autrement ?
# indice : remarquez le rôle de 2 dans 0:5:2


# ## Restrictions avec les conditions - Les requêtes
# 
# Nous pouvons isoler les sous-ensembles d'observations répondant à des critères définis sur les champs. Nous utiliserons préférentiellement la méthode .loc[,] dans ce cadre.

# In[34]:


# Listez les individus présentant une douleur de type A


# In[34]:


# Nous constatons que l'on indexe avec un vecteur de booléens si on va dans le détail. En effet,
print(df['typedouleur'] == "A")


# Seules les observations correspondant à True sont repris par .loc[,]. Nous pouvons les comptabiliser :

# In[35]:


# Comptez le nombre d'individus qui présente une douleur de type "A" ? 


# In[36]:


# pour un ensemble de valeurs de la même variable,
# nous utilisons isin()
print(df.loc[df['typedouleur'].isin(['A','B']),:])


# Des opérateurs logiques permettent de combiner les conditions. Nous utilisons respectivement : & pour ET, | pour OU, et ~ pour la négation.

# In[36]:


# Listez les individus présentant une douleur de type A et angine == oui ? 


# In[37]:


# Liste les personnes de moins de 45 ans, de sexe masculin, présentant une maladie cardiaque ? 


# In[39]:


# On peut n'afficher qu'une partie des colonnes
# On définit la projection dans une liste
colonnes = ['age','sexe','coeur','tauxmax']
# que l'on utilise en paramètre dans .loc[]
# pour la même restruction que précédemment
print(df.loc[(df['age'] < 45) & (df['sexe'] == "masculin") & (df['coeur'] == "presence"),colonnes])


# ## Calculs récapitulatifs - Croisement des variables
# 
# A la manière des tableaux croisés dynamiques (TCD) d'Excel, nous pouvons procéder à des croisements et opérer des calculs récapitulatifs, qui vont du comptage simple aux calculs statistiques mettent en jeu d'autres variables.

# In[38]:


# Fréquences selon sexe et coeur (tri croisé) ? 
# voir : http://pandas.pydata.org/pandas-docs/stable/generated/pandas.crosstab.html


# In[39]:


# Le même tri croisé mais avec un pourcentage en ligne ?
# indice : ns pouvons demander un post-traitement après la commande précedente !  


# In[40]:


# Calculez la moyenne d'âge selon le sexe et la maladie ? 
# indice : ns utilisons la fonction mean() de la classe Series de la librairie Pandas


# In[43]:


# une autre manière de faire avec la commande pivot_table() pour exactement le même résultat
print(df.pivot_table(index=['sexe'],columns=['coeur'],values=['age'],aggfunc=pandas.Series.mean))


# L'utilisation de groupby() permet d'accéder aux sous-DataFrame associés à chaque item de la variable de regroupement. Il est dès lors possible d'appliquer explicitement d'autres traitements sur ces sous-ensembles de données.

# In[46]:


# Scission des données selon le sexe
g = df.groupby('sexe')

# Calculer la dimension du sous-DataFrame associé aux hommes
print(g.get_group('masculin').shape)


# In[41]:


# Calculez la moyenne de l'âge chez les hommes.


# In[48]:


# On peut appliquer différentes fonctions
# agg() permet de revenir sur quelque chose qui ressemble au crosstab()
print(g[['age','depression']].agg([pandas.Series.mean, pandas.Series.std]))


# In[49]:


# Nous pouvons itérer sur les groupes
for groupe in g:
    # groupe est un tuple
    print(groupe[0]) #étiquette du groupe
    # accès à la variable 'age' du groupe concerné
    print(pandas.Series.mean(groupe[1]['age']))


# ## Construction de variables calculées
# 
# Les calculs sont vectorisés pour les vecteurs de type Series de Pandas. Ce qui évite de passer par des boucles fastidieuses pour manipuler les valeurs des vecteurs.

# In[42]:


# Création d'une variable tauxnet (qui n'a aucune signification médicale)
# Utilisation de la libraire numpy (log = logarithme népérien)


# In[43]:


# Ns cherchons à la concaténer au DataFrame


# La construction d'une variable ex-nihilo est également possible. Par ex., nous souhaitons créer une indicatrice pour la variable sexe, 1 pour masculin, 0 pour féminin.

# In[52]:


# Création d'une Série de 0 de la même longueur
# que notre DataFrame(nombre de lignes)
# nous utilisons la méthode de numpy pour cela
code = pandas.Series(numpy.zeros(df.shape[0]))
print(code.shape)


# In[53]:


#les "sexe = masculin" sont codés 1
#de fait, "sexe = feminin" est codé zéro puisque le 
#vecteur a préalablement été créé avec des valeurs 0
code[df['sexe']=='masculin'] = 1
print(code.value_counts())


# In[54]:


#une autre solution plus simple, mais il faut connaître eq()
codebis = df['sexe'].eq('masculin').astype('int')
print(codebis.value_counts())


# ## Graphiques
# 
# Passer par matplotlib permet de réaliser des graphiques performants (http://matplotlib.org/). Mais il faut connaître les procédures de la librairie, ce qui nécessite un apprentissage supplémentaire qui n'est pas toujours évident.
# 
# Heureusement, Pandas propose des commandes simples qui encapsulent l'appel à ces procédures et nous simplifie grandement la vie. Il faut importer matplotlib pour que l'ensemble fonctionne correctement.

# In[55]:


#indiquer que l'on veut voir apparaître les graphiques dans le notebook
#/!\ très important, sinon on ne verrait rien 
get_ipython().magic('matplotlib inline')

#importation de la librairie
import matplotlib.pyplot as plt


# In[44]:


# Tracer 1histogramme de l'âge ? 


# In[45]:


# Tracer 1density plot ? 


# In[46]:


# Tracer l'histogramme de l'âge selon le sexe ? 


# In[47]:


# Comparaison des distributions avec un boxplot ? 


# In[48]:


# Tracer 1scatterplot : age vs. tauxmax ? 


# In[49]:


# Tracer 1scatterplot (age vs. tauxmax) en distinguant les points ? 
# (niveau de gris) selon les valeurs de dépression


# In[51]:


# Tracer 1 scatterplot (age vs. tauxmax) en distinguant les points selon les valeurs de coeur ? 
# indice : nécessite un recodage de coeur - ici en 0/1
# afficher le graphique en spécifiant la couleur (blue = 0, green = 1)


# In[52]:


# Tracer 1diagramme à secteurs - comptage de sexe ? 


# In[53]:


# TRacez le scatterplot des variables pris deux à deux
# Cela n'a d'intérêt que pour les variables quantitatives bien évidemment

