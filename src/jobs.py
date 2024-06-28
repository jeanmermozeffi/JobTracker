import requests
import os
import re
import time
from datetime import datetime
import unidecode
import uuid
from urllib.parse import urlencode
from urllib.parse import urljoin

from bs4 import BeautifulSoup


def get_soup(url, features='html.parser', params=None):
    """
    Fonction pour récupérer et parser le contenu HTML d'une URL donnée avec BeautifulSoup.

    Args:
    - url (str): L'URL de la page à scraper.

    Returns:
    - BeautifulSoup object: L'objet BeautifulSoup contenant le contenu HTML parsé.
      None si la requête échoue.
    """

    full_link = url

    if params:
        full_params = urlencode(params)
        full_link = urljoin(url, '?' + full_params)

    # Faire une requête HTTP GET
    response = requests.get(full_link)

    # Vérifier si la requête s'est bien passée
    if response.status_code == 200:
        # Analyser le contenu HTML avec BeautifulSoup
        soup = BeautifulSoup(response.content, features)
        return soup
    else:
        print(f"Erreur {response.status_code} lors de la requête HTTP.")
        return None