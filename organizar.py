# -*- coding: utf-8 -*-

import os.path
import core


# status
readed_folders = False  # status - indica se todos os arquivos foram lidos.
get_extensions = False  # status - indica se foi capturado as extensões dos arquivos que estão na pasta.
created_folders = False  # status - indica se as pastas organizadoras já foram criadas.
copied_folders = False  # status - indica se os arquivos foram copiados para as respectivas pastas.
deleted_files_old = False  # status - indica se os arquivos antigos.
done = False  # status - indica se todos os processos foram realizados.


# verifica se todos as funções foram executadas com sucesso
def verify_is_done():
    if readed_folders and get_extensions and created_folders and copied_folders and deleted_files_old:
        return True
    else:
        return False


def main():
    # diretorio atual de onde está sendo executado o programa
    current_path = core.set_folder_to_organize('C:\\Users\\cafgd\\Desktop')

    # armazena os dados(nome do Arquivo, extensão do arquivo e o caminho do arquivo)
    # de todos os arquivos encontrados na pasta
    all_files = core.get_list_files_from_directory(current_path)

    # armazena apenas o nome arquivos encontradas
    files_founded = []
    [files_founded.append(fc[0]) for fc in all_files if fc[0] not in files_founded]
    # armazena as extensões encontradas
    extensions_founded = []
    [extensions_founded.append(fc[1]) for fc in all_files if fc[1] not in extensions_founded]
    # armazena apenas o caminho dos extensões encontradas
    files_path_founded = []
    [files_path_founded.append(fc[2]) for fc in all_files if fc[2] not in files_path_founded]

    # print(files_founded)
    # print(extensions_founded)
    # print(files_path_founded)

    core.verify_path_is_folder(current_path)
    print(current_path)
    core.create_directories_with_name_of_extension(extensions_founded, current_path)
    core.copy_files_to_folder(all_files, current_path)
    opt = str(input("Deseja deletar os arquivos antigos? [y/n]"))
    if opt == "y":
        core.delete_files_old(files_path_founded)


if __name__ == '__main__':
    main()
