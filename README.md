# Module Wiki

Le module Wiki permet de créer et gérer une base de connaissances collaborative pour Django.

## Installation

### Prérequis

- Django 6.0+
- Python 3.12+
- django-tinymce
- django-import-export

### Configuration

1. Ajouter 'wiki' à INSTALLED_APPS dans settings.py :
   ```python
   INSTALLED_APPS = [
       # ... autres apps
       'tinymce',
       'import_export',
       'core',
       'wiki',
   ]
   ```

2. Inclure les URLs dans le fichier principal urls.py :
   ```python
   from django.urls import path, include

   urlpatterns = [
       # ... autres URLs
       path('wiki/', include('wiki.urls')),
   ]
   ```

3. Appliquer les migrations :
   ```bash
   python manage.py migrate wiki
   ```

4. Collecter les fichiers statiques :
   ```bash
   python manage.py collectstatic
   ```

## Modèles

### Cat_Wiki

Catégories pour organiser les articles wiki.

| Champ | Type | Description |
|-------|------|-------------|
| `cw_titre` | CharField | Titre de la catégorie |
| `cw_titre_slgify` | CharField | Slug auto-généré (lecture seule) |

### Wiki

Articles du wiki.

| Champ | Type | Description |
|-------|------|-------------|
| `w_titre` | CharField | Titre de l'article |
| `w_titre_slugify` | CharField | Slug auto-généré (lecture seule) |
| `w_grp` | ForeignKey(Groupe) | Regroupement (optionnel) |
| `w_cat` | ManyToManyField(Cat_Wiki) | Catégories |
| `w_description` | TextField | Résumé (TinyMCE) |
| `w_contenu` | TextField | Contenu principal (TinyMCE) |
| `w_right` | TextField | Contenu à droite (TinyMCE) |
| `w_publier` | Boolean | Publié / non publié |
| `w_reading` | Integer | Nombre de lectures |
| `w_publdate` | DateTime | Date de publication |

## URLs

- `/wiki/` — Index du wiki
- `/wiki/categories/` — Liste des catégories
- `/wiki/tags/` — Liste des tags
- `/wiki/article/<slug>/` — Article spécifique

## Intégration au Core

Pour intégrer le wiki au système de pages du core :

1. Créer une page de type 'lien' avec l'adresse `/wiki/` dans le menu
2. Utiliser les groupes pour organiser les articles wiki
3. Les articles peuvent être liés aux pages existantes via les groupes

## Administration

L'admin Django permet de gérer les catégories et articles. Les champs de texte utilisent TinyMCE pour l'édition riche.

### Actions disponibles

- **Passer en Public** : Rend les articles sélectionnés publics
- **Passer en Privé** : Rend les articles sélectionnés privés

### Filtres

- Par statut de publication
- Par groupe
- Par catégories
- Par date de publication

### Recherche

Recherche dans le titre et le contenu des articles.

## Templates

Les templates se trouvent dans `wiki/templates/wiki/`. Ils utilisent le système de templates de base du core.

## Développement

### Tests

```bash
python manage.py test wiki
```

### Structure des fichiers

```
wiki/
├── __init__.py
├── admin.py          # Configuration admin Django
├── apps.py           # Configuration de l'app
├── forms.py          # Formulaires avec TinyMCE
├── models.py         # Modèles de données
├── tests.py          # Tests unitaires
├── urls.py           # Configuration des URLs
├── views.py          # Vues et logique métier
├── migrations/       # Migrations de base de données
└── templates/        # Templates HTML
```</content>
<parameter name="filePath">/Volumes/Container/dev/wiki/README.md