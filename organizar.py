# -*- coding: utf-8 -*-

import sys
from os import listdir, makedirs, remove
from os.path import isfile, dirname, realpath, splitext, exists, join
import shutil

# status
readed_folders = False #status - indica se todos os arquivos foram lidos.
get_extensions = False #status - indica se foi capturado as extensões dos arquivos que estão na pasta.
created_folders = False #status - indica se as pastas organizadoras já foram criadas.
copied_folders = False #status - indica se os arquivos foram copiados para as respectivas pastas.
deleted_files_old = False #status - indica se os arquivos antigos.
done = False #status - indica se todos os processos foram realizados.


# Pega o diretorio atual de onde está sendo executado o programa
current_path = dirname(realpath(__file__))

#armazena as extensões encontradas na pasta
list_extensions = []

# armazena os nomes dos arquivos armazenado na pasta
list_files = [f for f in listdir(current_path) if isfile(f)]

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

# verifica se todos as funções foram executadas com sucesso
def verify_is_done():
    if readed_folders and get_extensions and created_folders and copied_folders and deleted_files_old:
        return True
    else:
        return False

# Reports
# print('Current Directory: {}'.format(current_path))
# print('Files: {}'.format(list_files))
# print('Extensions: {}'.format(list_extensions))
readed_folders = verify_path_is_folder(current_path)
get_extensions = get_extension_from_file(list_files, list_extensions)
created_folders = create_directories_with_name_of_extension(list_extensions)
copied_folders = copy_files_to_folder(list_files, current_path, current_path)
deleted_files_old = delete_files_old(list_files, current_path)
done =  verify_is_done()


if readed_folders:
    print('Pasta lida com sucesso!')
if get_extensions:
    print('Lista de extensões criadas com sucesso!')
if created_folders:
    print('Pastas organizadoras criadas com sucesso')
if copied_folders:
    print('Arquivos copiados paras as pastas com sucesso')
if deleted_files_old:
    print('Arquvos antigos deletados com sucesso')
if done:
    print('Organização realizado com sucesso')
