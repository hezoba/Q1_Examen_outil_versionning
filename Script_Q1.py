#Importer le librairie necessaire

import requests
import json

# Demande d'entrée à l'utilisateur

GITHUB_TOKEN = input("Entrez votre token GitHub : ")
GITHUB_USERNAME = input("Entrez votre nom d'utilisateur GitHub : ")
REPO_NAME = input("Entrez le nom du dépôt à créer : ")

# Créer un nouveau dépôt
def create_repo():
    url = f'https://api.github.com/user/repos'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }
    data = {
        'name': REPO_NAME,
        'private': False,
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f"Dépôt '{REPO_NAME}' créé avec succès!")
        return response.json()['url']  # URL du dépôt créé
    else:
        print(f"Erreur lors de la création du dépôt: {response.json()}")
        return None

# Ajouter une issue au dépôt
def create_issue(repo_url, title, body):
    url = f'{repo_url}/issues'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }
    data = {
        'title': title,
        'body': body,
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f"Issue '{title}' créée avec succès!")
    else:
        print(f"Erreur lors de la création de l'issue: {response.json()}")

def main():
    repo_url = create_repo()
    if repo_url:
        create_issue(repo_url, 'Titre de l\'issue 1', 'Description de l\'issue 1')
        create_issue(repo_url, 'Titre de l\'issue 2', 'Description de l\'issue 2')

if __name__ == '__main__':
    main()