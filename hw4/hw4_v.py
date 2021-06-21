from pathlib import *
import sys

dict_list_files = {'images': [],
                   'movies': [],
                   'docs': [],
                   'musics': [],
                   'archives': [],
                   'unknown': []
                   }

dict_ext = {}

list_known = []
list_unknown = []


def parse_folder(path):
    for el in path.iterdir():
        if el.is_dir():
            parse_folder(path / el.name)
        else:
            if el.suffix in dict_ext.keys():
                list_know.append(el.suffix)
                name_list = dict_ext[el.suffix]
            else:
                list_unknow.append(el.suffix)
                name_list = 'unknown'
            dict_list_files[name_list].append(el.name)


def main():
    dir_name = sys.argv[1]
    path_dir = Path(dir_name)
    images = '.jpg .png .jpeg .svg'.split()
    movies = '.avi .mp4 .mov .mkv'.split()
    docs = '.doc .docx .txt .pdf .xlsx .pptx'.split()
    musics = '.mp3 .ogg .wav .amr'.split()
    archs = 'zip gz tar'.split()
    list_ext = ['images', 'movies', 'docs', 'musics', 'archives']

    for el in list_ext:
        l = eval(el)
        dict_ext.update(dict(zip(l, [el] * len(l))))

    
    parse_folder(path_dir)

    for k, v in dict_list_files.items():
        print(k, v)
    print(list_known)
    print(list_unknown)


if __name__ == '__main__':
    main()
