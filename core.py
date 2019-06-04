
from os import listdir, makedirs, remove
import os.path
from os.path import isfile, dirname, realpath, splitext, exists, join
import shutil
import glob


# verifica a pasta onde está sendo executado é realmente uma pasta valida
def verify_path_is_folder(folder_path):
    if not isfile(folder_path):
        return True
    else:
        return False


# Pega as extensoes dos arquivos dessa pasta e armazena em array
def get_list_files_from_directory(path):
    list_of_files = []
    for f in glob.glob(path + "\\*.*"):
        file = [os.path.basename(f), os.path.splitext(f)[1], f]
        list_of_files.append(file)
    return list_of_files


# Cria as pastas com os nomes das extensões
def create_directories_with_name_of_extension(list_of_extensions, path_to_create):
    try:
        for f in list_of_extensions:
            if f != '.ini':
                namefolder = f.replace('.', '')
                pathfolder = path_to_create + '\\' + namefolder
                if not exists(pathfolder):
                    makedirs(pathfolder)
        return True
    except Exception as e:
        print(e)
        return False


# copia os arquivos para as pastas
def copy_files_to_folder(list_of_files_path, folder_destiny):
    try:
        for f in list_of_files_path:
            if f[1] != '.ini':
                namefoldercurrent = splitext(f[1])[0].replace('.', '')
                print(namefoldercurrent)
                shutil.copy(f[2], folder_destiny + '\\' + namefoldercurrent + '\\' + str(f[0]))
                print('{} copiado com sucesso'.format(f[2]))
        return True
    except Exception as e:
        print(e)
        return False


# deleta os arquivos antigos
def delete_files_old(list_of_files):
    try:
        for f in list_of_files:
            remove(f)
        return True
    except Exception as e:
        print(e)
        return False


# pega a pasta de onde está sendo o seu executado o programa
def get_current_path_folder():
    return dirname(realpath(__file__))


# define qual pasta será exectada
def set_folder_to_organize(path=None):
    if path == None:
        return get_current_path_folder()
    else:
        return path
