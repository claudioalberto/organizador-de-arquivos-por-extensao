# -*- coding: utf-8 -*-

import sys
from os import listdir, makedirs, remove
from os.path import isfile, dirname, realpath, splitext, exists, join
import shutil
import core

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
readed_folders = core.verify_path_is_folder(current_path)
get_extensions = core.get_extension_from_file(list_files, list_extensions)
created_folders = core.create_directories_with_name_of_extension(list_extensions)
copied_folders = core.copy_files_to_folder(list_files, current_path, current_path)
deleted_files_old = core.delete_files_old(list_files, current_path)
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
