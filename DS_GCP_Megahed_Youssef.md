# Ds GCP - Opti Cloud - Megahed Youssef

## Question de cours (5 points)

### Création d'un Service Account :  
1. Aller sur la console GCP → IAM & Admin → Service Accounts.  
2. Cliquer sur **Créer un Service Account**, donner un nom et définir les permissions nécessaires.  
3. Générer une clé (éviter sauf si nécessaire) et télécharger le fichier JSON sécurisé.  
4. Bonnes pratiques : attribuer le moins de permissions possible (principe du moindre privilège), ne pas exposer les clés, utiliser Workload Identity Federation si possible.  

### Création d'un Bucket :  
1. Aller sur la console GCP → Cloud Storage → Créer un Bucket.  
2. Définir le **nom**, la **région** (ex : multi-régional pour plus de disponibilité, régional pour réduire les coûts).  
3. Choisir une **classe de stockage** (Standard, Nearline, Coldline, Archive).  
4. Définir les **règles de conservation** et les droits IAM.  
5. Impact : une bonne région améliore la latence, une mauvaise gestion des droits peut exposer les données.  

### Gestion des droits (IAM) :  
IAM permet de gérer **qui peut faire quoi** sur une ressource GCP.  
Exemple : Pour restreindre l’accès à un bucket critique :  
- Accorder uniquement le rôle **Storage Object Viewer** aux utilisateurs qui doivent lire les fichiers.  
- Accorder **Storage Admin** uniquement aux administrateurs.  
- Utiliser des groupes IAM plutôt que des permissions individuelles.  

### Configuration de la facturation :  
1. Aller sur la console GCP → Facturation → Associer un compte de facturation à un projet.  
2. Définir un **budget et des alertes** pour surveiller les coûts.  
3. Activer **les rapports et exports de facturation** pour suivre la consommation.  
4. Précautions : Toujours limiter les ressources inutiles, surveiller les machines virtuelles et les buckets de stockage actifs.  

### Règles de vie :  
**On range son poste et on dit "Au revoir !"**