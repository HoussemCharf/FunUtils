import httplib2
import os
import sys
import json
from bs4 import BeautifulSoup as bs
import urllib2
import re
import base64
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow


CLIENT_SECRETS_FILE = "client_id.json"
CLIENT_SECRET_PASS='''aHR0cDovL3d3dy55b3V0dWJlaW5tcDMuY29tL3dpZGdldC9idXR0b24vP3ZpZGVvPWh0dHBzOi8vd3d3LnlvdXR1YmUuY29tL3dhdGNoP3Y9'''
SERVICE_TOKEN = '''aHR0cDovL3d3dy55b3V0dWJlaW5tcDMuY29t'''
YOUTUBE_READ_WRITE_SSL_SCOPE = "https://www.googleapis.com/auth/youtube.force-ssl"
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.
MISSING_CLIENT_SECRETS_MESSAGE = "WARNING: Please configure OAuth 2.0" 

# Authorize the request and store authorization credentials.
def get_authenticated_service(args):
  flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=YOUTUBE_READ_WRITE_SSL_SCOPE,
    message=MISSING_CLIENT_SECRETS_MESSAGE)

  storage = Storage("youtube-api-snippets-oauth2.json")
  credentials = storage.get()

  if credentials is None or credentials.invalid:
    credentials = run_flow(flow, storage, args)

  # Trusted testers can download this discovery document from the developers page
  # and it should be in the same directory with the code.
  return build(API_SERVICE_NAME, API_VERSION,
      http=credentials.authorize(httplib2.Http()))


args = argparser.parse_args()
service = get_authenticated_service(args)

def print_results(results):
  List_of_ids_name = []
  for x in results["items"]:
  #category id = 10 means music source gist
  # https://gist.github.com/dgp/1b24bf2961521bd75d6c
    if x["snippet"]["categoryId"] == "10" :
      List_of_ids_name.append([x["snippet"]["title"],x["id"]])
  #DEBUGGING PURPOSES
  #print results["items"][0]["snippet"]["categoryId"]
  #print results["items"][0]["snippet"]["title"]
  #print results["items"][0]["id"]
  print "List Downloaded:"
  for alpha in List_of_ids_name:
    print alpha[0]+"\r"
  return List_of_ids_name


# Build a resource based on a list of properties given as key-value pairs.
# Leave properties with empty values out of the inserted resource.
def build_resource(properties):
  resource = {}
  for p in properties:
    # Given a key like "snippet.title", split into "snippet" and "title", where
    # "snippet" will be an object and "title" will be a property in that object.
    prop_array = p.split('.')
    ref = resource
    for pa in range(0, len(prop_array)):
      is_array = False
      key = prop_array[pa]
      # Convert a name like "snippet.tags[]" to snippet.tags, but handle
      # the value as an array.
      if key[-2:] == '[]':
        key = key[0:len(key)-2:]
        is_array = True
      if pa == (len(prop_array) - 1):
        # Leave properties without values out of inserted resource.
        if properties[p]:
          if is_array:
            ref[key] = properties[p].split(',')
          else:
            ref[key] = properties[p]
      elif key not in ref:
        ref[key] = {}
        ref = ref[key]
      else:
        ref = ref[key]
  return resource

# Remove keyword arguments that are not set
def remove_empty_kwargs(**kwargs):
  good_kwargs = {}
  if kwargs is not None:
    for key, value in kwargs.iteritems():
      if value:
        good_kwargs[key] = value
  return good_kwargs




#download the song file and saves it in the current folder
def download_mp3(link,song_name):
  f = urllib2.urlopen(link)
  data = f.read()
  with open(song_name+".mp3", "wb") as code:
    code.write(data)
# get the direct link of the file
def get_the_mp3 (id):
  html_page = urllib2.urlopen(base64.b64decode(CLIENT_SECRET_PASS)+id)
  soup = bs(html_page, "html.parser")
  link = soup.find(id="downloadButton")
  result = str(base64.b64decode(SERVICE_TOKEN)+link.get('href'))
  return result
#get ids of videos 

def videos_list_my_rated_videos(service, **kwargs):
  kwargs = remove_empty_kwargs(**kwargs) 
  results = service.videos().list(
    **kwargs
  ).execute()

  ToBeDownloaded=print_results(results)
  for element in ToBeDownloaded:
    download_mp3(get_the_mp3(element[1]),element[0])
# Start of the main function
videos_list_my_rated_videos(service,
    part='snippet,contentDetails,statistics',
    myRating='like')