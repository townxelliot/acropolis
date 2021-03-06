import pytest
import requests
import urllib.parse
from pytest_bdd import scenario, given, when, then, parsers, scenarios
from rdflib import Namespace

scenarios('media.feature')

@given("a query <query> and media <media>")
def for_q_media(context, query, media):
  """
  eg.
    http://localhost/?q=Dracula&media=http://purl.org/dc/dcmitype/StillImage
  """
  context['params']['q'] = query
  context['params']['media'] = media
