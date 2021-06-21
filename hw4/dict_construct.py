from pathlib import *
import sys

images = '.jpg .png .jpeg .svg'.split()
movies = '.avi .mp4 .mov .mkv'.split()
docs = '.doc .docx .txt .pdf .xlsx .pptx'.split()
musics = '.mp3 .ogg .wav .amr'.split()
archives = 'zip gz tar'.split()
list_value = [images, movies, docs, musics, archives]
list_keys = ['images', 'movies', 'docs', 'musics', 'archives']
##dict_list_files = {'images': [],
##                   'movies': [],
##                   'docs': [],
##                   'musics': [],
##                   'archives': [],
##                   'unknows': []
##                   }
dict_list_files= {}

for key, value in enumerate(list_keys):
    dict_list_files[value]= list_value[key]
print(dict_list_files)

dict_ext = {}

list_know = []
list_unknow = []
