import os
import shutil
from os import path, listdir


# retorna o caminho da pasta que será organizada
def set_path_to_organize(path_folder):
    if path_folder == '.':
        return path.dirname(path.realpath(__file__))
    else:
        return path_folder


# retorna uma lista com os arquivos encontradas em uma pasta
def get_files_from_folder(path_folder):
    list_files = []
    for f in listdir(path_folder):
        if path.isfile(path_folder + '/' +f):
            list_files.append(f)
    return list_files


# retorna uma lista com extensões de uma lista de arquivos
def get_extensions_from_files(list_files):
    list_extensions = []
    for f in list_files:
        current_extension = os.path.splitext(os.path.basename(f))[1].replace('.', '')
        if current_extension not in list_extensions:
            list_extensions.append(current_extension)
    return list_extensions


def create_folders_from_name_list(name_list, path_folder, status=False, verbose_mode=False):
    for n in name_list:
        if n != '.ini':
            folder = path_folder + '\\' + n
            if not os.path.exists(folder):
                os.makedirs(folder)
                status = True
            else:
                if verbose_mode is True:
                    print('A pasta {} já existe.'.format(folder))
    return status


# Copia os arquivos para a pasta destino de acordo com a extensão
def copy_files_to_folders_specific(list_files, list_folders, path_folder_root, writable=False, status=False, verbose_mode=False):
    try:
        for f in list_files:
            ext_temp = os.path.splitext(os.path.basename(f))[1].replace('.', '')
            if ext_temp in list_folders:
                file = path_folder_root + '\\' + ext_temp + '\\' + f
                if os.path.exists(file):
                    if writable is False:
                        opt = input('AVISO:\nEstamos tentando copiar o arquivo "{}" para a pasta destino, porém já existe um arquivo com o mesmo no diretorio, você deseja substituí-lo?[S/N]'.format(f))
                        if opt == 's' or opt == 'S':
                            shutil.copy(path_folder_root + '\\' + f, path_folder_root + '\\' + ext_temp)
                            status = True
                    else:
                        shutil.copy(path_folder_root + '\\' + f, path_folder_root + '\\' + ext_temp)
                        status = True
                else:
                    shutil.copy(path_folder_root + '\\' + f, path_folder_root + '\\' + ext_temp)
                    status = True
        if status is True:
            if verbose_mode is True:
                print("Arquivos copiados com sucesso!")
        return status
    except Exception as err:
        print(err)


# deleta uma lista de arquivos de uma pasta
def delete_files_from_list_of_files(list_of_files, path_folder_root='', delete_forced = False, status=False, verbose_mode=False):
    for f in list_of_files:
        if path_folder_root is not '':
            file = path_folder_root + '\\' + f
        else:
            file = f
        try:
            if delete_forced is True:
                os.remove(file)
                status = True
            else:
                opt = input('Tem certeza que você deseja deletar essa lista de arquivos?[S/N]')
                if opt is 's' or opt is 'S':
                    os.remove(file)
                    delete_forced=True
                    status = True
            if status is True:
                if verbose_mode is True:
                    print('Arquivos deletados com sucesso!')
        except Exception as err:
            print(err)
            status=False
