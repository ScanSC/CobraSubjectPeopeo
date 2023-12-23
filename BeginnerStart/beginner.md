# Peopeo - Beginner

## Les bases de pygame

Nous allons travailler dans le dossier "Peopeo" de "BeginnerStart".  

Commencez par ouvrir le fichier [main.py](Peopeo/main.py).

### Les imports

Les deux premières lignes sont des imports de <span style="color:#f1c35f">pygame</span> et <span style="color:#f1c35f">sys</span>.  
<span style="color:#f1c35f">Pygame</span> est notre librairie (code déjà fait) qui nous permettra de créer le jeu  
<span style="color:#f1c35f">Sys</span> est la librairie système que l'on utilisera notamment pour appeler la fonction <span style="color:#f1c35f">exit</span> permettant d'interrompre le programme.

La ligne suivante est également un import, mais celui-ci appelle du code présent dans le fichier [gameProperties.py](Peopeo/gameProperties.py) que vous avez peut être remarqué avant d'ouvrir [main.py](Peopeo/main.py).  
Nous importons donc une variable <span style="color:#f1c35f">settings</span> provenant de [gameProperties.py](Peopeo/gameProperties.py).

Si vous allez dans [gameProperties.py](Peopeo/gameProperties.py), vous trouverez une **class** ainsi que notre variable <span style="color:#f1c35f">settings</span> définie par cette **class**. Cette variable contient donc un **objet** <span style="color:#f1c35f">Settings</span> possédant diverses propriétés de notre jeu. Grâce à cette variable, nous pourrons utiliser les valeurs qu'elle contient sans les ré-écrire à chaque fois, et donc si on veut les modifier c'est aussi très rapide.

### La class Game

Revenons dans [main.py](Peopeo/main.py).  
On a une **class** <span style="color:#f1c35f">Game</span> qui est la **class** principale de notre jeu. La première méthode de cette **class** est son **constructeur**. Cette méthode est celle qui initialise notre **objet** <span style="color:#f1c35f">Game</span> à sa création.  
L'**attribut** <span style="color:#f1c35f">window</span> contient la fenêtre pygame de notre jeu.

Ensuite nous avons la **méthode** <span style="color:#f1c35f">run</span> qui contient la boucle principale du jeu. Cette boucle réalisera trois grandes actions :  
Détecter les **events** (touche pressée, click de souris...) et réaliser des actions en conséquence.  
Actualiser les éléments du jeu (position du joueur, animations...)  
Afficher les éléments du jeu.

Pour l'instant, il y a trois choses dans cette boucle :  
* `self.window.fill((0,0,0))` -> recouvre la fenêtre avec la couleur donnée en paramètre, ici du noir.
* `for event in pygame.event.get():` -> cette boucle gère les **events**. Si l'**event** est **QUIT** alors elle arrête proprement le programme.
* `pygame.display.flip()` -> affiche à l'écran les éléments qui ont été dessinés (**draw**).

Pour finir, les dernières lignes initialisent <span style="color:#f1c35f">pygame</span>, créent un **objet** <span style="color:#f1c35f">Game</span> puis appellent la **méthode** <span style="color:#f1c35f">run</span>.

## Lancer le jeu

Pour lancer le jeu exécutez simplement la commande `python <path-vers-main.py>`.  
Par exemple : `python Peopeo/main.py`.

Pour l'instant vous devriez juste avoir une fenêtre noire qui s'ouvre. Pour la fermer vous pouvez cliquer sur la croix en haut à droite. Celà va appeler l'**event QUIT** et donc arrêter le programme comme expliqué plus haut.

## Créer le joueur

Dans le fichier [player.py](Peopeo/player.py), vous avez le début de notre futur joueur. C'est une **class** <span style="color:#f1c35f">Player</span> avec des **prototypes** (Ligne définissant les propriété de base de la fonction ou méthode) de **méthodes** vides.

1 -  `def __init__(self)` -> C'est le **constructeur** de notre joueur.  
> Ajoutez lui un **attribut** <span style="color:#f1c35f">pos_x</span> (le joueur ne se déplacant que horizontalement, nous n'avons pas besoin de stocker sa position verticale).

2 - `def update(self)` -> C'est la **méthode** qui sera appelée quand on voudra actualiser les propriétés de notre joueur.  
> Nous voulons que le joueur suive la souris horizontalement. Faites en sorte que la **méthode** <span style="color:#f1c35f">update</span> modifie la propriété "pos_x" pour qu'elle prenne la valeur de la position horizontale de la souris.
Pour récupérer la position de la souris, utilisez `pygame.mouse.get_pos()`

3 - `def draw(self, window)` -> Cette **méthode** dessine les éléments visuels de notre joueur sur la fenêtre. Pour rester sur quelque chose de simple, nous allons utiliser des formes: un cercle et un rectangle. L'objectif est d'obtenir ceci :  
![](../DocAssets/player.png)

> Utilisez `pygame.draw.circle()` et `pygame.draw.rectangle()` pour obtenir un résultat similaire.  
Pour la position de ces formes, pensez à utiliser l'**attribut** <span style="color:#f1c35f">pos_x</span> ainsi que `settings.windowHeight` pour correctement placer verticalement le joueur en fonction de la taille de la fenêtre. Attention, quand la valeur de la position verticale augmente, l'élément déscend.  


>Pour tester votre joueur, il faut l'utiliser dans [main.py](Peopeo/main.py). Vous pouvez rajouter un **attribut** <span style="color:#f1c35f">player</span> à la **class** <span style="color:#f1c35f">Game</span> puis dans la **méthode** <span style="color:#f1c35f">run</span>, vous appelez les **méthodes** <span style="color:#f1c35f">update</span> puis <span style="color:#f1c35f">draw</span> de votre **objet** <span style="color:#f1c35f">player</span>.  
Noubliez pas d'importer [player.py](Peopeo/player.py) !

Maintenant que votre joueur s'affiche et bouge correctement, nous allons lui faire tirer des projectiles.

## La clock

Pour l'instant il y a un problème invisible avec notre jeu : la boucle de jeu tourne à la vitesse à laquelle l'ordinateur l'exécute, ce qui veut dire que la vitesse du jeu dépend de la puissance de la machine.  
Pour régler ce problème, nous allons utiliser la clock de <span style="color:#f1c35f">pygame</span>

> Ajoutez à la **class** <span style="color:#f1c35f">Game</span> un **attribut** <span style="color:#f1c35f">clock</span> initialisant la clock avec `pygame.time.clock()`.

> Ajoutez la ligne suivante dans la boucle du jeu : `self.clock.tick(settings.refreshRate)`  
La **méthode** <span style="color:#f1c35f">tick</span> de la clock fait en sorte que la boucle dans la quelle elle se trouve tourne à une vitesse dépendant de la valeur donnée en paramètre. Ainsi, quelque soit la puissance de la machine le jeu tournera à la même vitesse (à moins que votre ordinateur ne soit pas assez puissant pour faire tourner le jeu, ce qui n'arrivera pas dans notre projet).

## Le tir

### Le projectile

>Cette fois vous allez créer le fichier vous même ("projectile.py").  
N'oubliez pas d'importer <span style="color:#f1c35f">pygame</span> !

Vous allez définir une **class** <span style="color:#f1c35f">Projectile</span> avec un **constructeur**, et les méthodes <span style="color:#f1c35f">update</span> et <span style="color:#f1c35f">draw</span>.  

Le **constructeur** :
> Dans notre cas, le projectile doit pouvoir apparaître à n'importe quelle position horizontale, le constructeur va donc prendre cette valeur en paramètre : `def __init__(self, x)`.
Pour ce qui est de la position verticale, elle sera toujours la même au début.

La **méthode** <span style="color:#f1c35f">update</span> :
> Le projectile doit se déplacer verticalement vers le haut

La **méthode** <span style="color:#f1c35f">draw</span> :
> Le projectile peut simplement être représenté par un cercle ou un rectangle.

Maintenant il faut utiliser cette **class** <span style="color:#f1c35f">Projectile</span> dans notre code. Pour celà je vous propose d'ajouter un **attribut** <span style="color:#f1c35f">projectiles</span> à notre **class** <span style="color:#f1c35f">Player</span> qui contiendra une **liste** d'**objets** <span style="color:#f1c35f">Projectile</span>.

### Tirer le projectile

La **méthode** <span style="color:#f1c35f">shoot</span> :
> Rajoutez une **méthode** <span style="color:#f1c35f">shoot</span> à la **class** <span style="color:#f1c35f">Player</span>. Cette **méthode** doit ajouter un nouvel **objet** <span style="color:#f1c35f">Projectile</span> à notre **attribut** <span style="color:#f1c35f">projectiles</span>.

L'action de tir :
> De retour dans [main.py](Peopeo/main.py), dans la boucle gérant les **events**, rajoutez la détection du clic de la souris. Lorsque un clic est détecté, appellez la **méthode** <span style="color:#f1c35f">shoot</span> du joueur.

> N'oubliez pas d'appeler les **méthodes** <span style="color:#f1c35f">update</span> et <span style="color:#f1c35f">draw</span> pour chaque projectile. Vous pouvez faire ça dans la boucle principale du jeu ou dans les **méthodes** du même nom de votre player.

Une fois tout celà fait, vous devriez avoir un joueur pouvant tirer des projectiles.

## Les ennemis


### La class Enemy

Les ennemis apparaîtront en haut de l'écran et se déplaceront vers le bas à des vitesses différentes.

> Créez un fichier "enemy.py" contenant une class <span style="color:#f1c35f">Enemy</span> avec un **constructeur** et les **méthodes** <span style="color:#f1c35f">update</span> et <span style="color:#f1c35f">draw</span>.

Pour la vitesse différente pour chaque ennemi, utilisez la fonction `randint()` de la librairie <span style="color:#f1c35f">random</span> ou bien ajoutez un paramètre "speed" au **constructeur** et on utilisera randint plus tard.

> De la même manière dont vous avez ajouté une liste de projectiles au joueur, ajoutez une liste d'ennemis à <span style="color:#f1c35f">Game</span> puis appelez <span style="color:#f1c35f">update</span> et <span style="color:#f1c35f">draw</span> dans la boucle du jeu pour chaque ennemi de la liste.

### Faire apparaître les ennemis

Il faut faire apparaître les ennemis à des positions horizontales aléatoires, à une fréquence irrégulière (dépendant de la difficulté) et avec des vitesses différentes (si vous ne l'avez pas déjà géré à l'intérieur de la **class** <span style="color:#f1c35f">Enemy</span>). On va donc utiliser `randint`.

> Ajoutez une **méthode** <span style="color:#f1c35f">spawnEnemy</span> à la **class** <span style="color:#f1c35f">Game</span> puis appelez là dans la boucle du jeu.  
Je vous recommande d'ajouter un **attribut** <span style="color:#f1c35f">enemySpawn</span> initialisé à 0 afin de pouvoir retenir le moment où le dernier ennemi a été créé.  
Regardez ce que vous pouvez faire avec `pygame.time`

Essayez de trouver une logique de vous même pour créer ce code, mais si vous n'y arrivez pas, vous pouvez utiliser le code ci-dessous.

```python
def spawnEnemy(self):
    if pygame.time.get_ticks() - self.enemySpawn > 700:
        self.enemySpawn = pygame.time.get_ticks()
        if random() <= settings.difficulty:
            # faire apparaître un ennemi
```

Maintenant vous avez un joueur qui tir et des ennemis qui apparaîssent et avancent vers le bas. Mais il manque les interactions, ce qui donne tout l'intérêt du jeu.

### Les collisions

Nous allons faire en sorte que quand un projectile touche un ennemi, les deux sont supprimés, et que si un ennemi touche le joueur, on perd (on ferme le jeu). Si un ennemi sort de l'écran, il faut penser à le supprimer.

Dans [tools.py](Peopeo/tools.py) vous trouverez une **fonction** <span style="color:#f1c35f">collision</span>. Cette fonction renvoie **True** ou **False** si il y a collision ou non entre les deux rectangles donnés en paramètre.

> Dans la **class** <span style="color:#f1c35f">Game</span> créez une **méthode** <span style="color:#f1c35f">checkCollisions</span> qui devra réaliser les actions citées plus haut.

Pour vous aider voici la logique recommandée :

```
Pour chaque ennemi
    Pour chaque projectile
        Si enemi en dehors de l'écran
            Détruire enemi
        Si collision entre enemi et projectile
            Détruire enemi et projectile
        Si collision entre enemi et joueur
            Fermer le jeu (comme dans les events)
```

> Appelez la **méthode** <span style="color:#f1c35f">checkCollisions</span> dans la boucle du jeu.

Si tout fonctionne, vous avez maitenant un jeu jouable !

## Et maintenant ?

Si il vous reste assez de temps, vous pouvez essayer d'améliorer votre jeu en ajoutant des point de vie, des enemis différents, ou bien en changeant les règles du jeu. Libre à vous de faire ce qui vous fait plaisir.