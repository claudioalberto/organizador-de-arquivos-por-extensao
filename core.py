
import sys
from os import listdir, makedirs, remove
from os.path import isfile, dirname, realpath, splitext, exists, join
import shutil

#verifica a pasta onde está sendo executado é realmente uma pasta valida
def verify_path_is_folder(folder_path):
    if not isfile(folder_path):
        return True
    else:
        return False

# Pega as extensoes dos arquivos dessa pasta e armazena em array
def get_extension_from_file(list_of_files, output_array):
    try:
        for f in list_of_files:
            output_array.append(splitext(f)[1])
        return True
    except Exception as e:
        print(e)
        return False

# Cria as pastas com os nomes das extensões
def create_directories_with_name_of_extension(list_of_extensions):
    try:
        for f in list_of_extensions:
            namefolder = str(f).replace('.', '')
            if not exists(namefolder):
                makedirs(namefolder)
        return True
    except Exception as e:
        print(e)
        return False

# copia os arquivos para as pastas
def copy_files_to_folder(list_of_files, folder_origin, folder_destiny):
    try:
        for f in list_of_files:
            namefoldercurrent = splitext(f)[1].replace('.','')
            shutil.copy(folder_origin + '\\' + f, folder_destiny + '\\' + namefoldercurrent + '\\' + f)
        return True
    except Exception as e:
        print(e)
        return False

#deleta os arquivos antigos
def delete_files_old(list_of_files, folder_path):
    try:
        for f in list_of_files:
            remove(folder_path + '\\' + f)
        return True
    except Exception as e:
        print(e)
        return False
