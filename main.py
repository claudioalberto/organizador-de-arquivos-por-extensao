import core
# Versão CLI (Versão Principal)

def organize():
    print('-'*36)
    print('{}Organizador de Arquivos por Extensão{}'.upper().format('\033[3;34m', '\033[m'))
    print('-'*36)
    c_path = core.set_path_to_organize('/home/claudioalberto/Documents/teste')
    c_files = core.get_files_from_folder(c_path,)
    c_exts = core.get_extensions_from_files(c_files)
    core.create_folders_from_name_list(c_exts, c_path)
    core.copy_files_to_folders_specific(c_files, c_exts, c_path)
    core.delete_files_from_list_of_files(c_files, c_path)
    print('-' * 36)
    print('\033[mRelatório Final\033[m')
    print('-'*36)
    print('Pasta Selecionada: {}'.format(c_path))
    print('Numero de Arquivos Encontrado: {}'.format(len(c_files)))
    print('Extenções encontradas: {}'.format(c_exts))


def summary():
    c_path = core.set_path_to_organize('/home/claudioalberto/Documents/teste')
    file = open('{}/summary-organizacao-de-arquivos.txt'.format(c_path), 'w+')
    file.write('Relatório - Organizando arquivos por Extensão\n'.upper())
    file.write('-'*45)
    file.write('\nPasta organizada:\n')
    file.write('Número de Arquivos encontrado:\n')
    file.write('Extensões encontrada:\n')
    file.write('- txt\n')
    file.write('- doc\n')
    file.write('Pastas Criadas:\n')
    file.write('- txt\n')
    file.write('- doc\n')
    file.write('-'*45)
    file.write('\nLogs\n')
    file.write('*Copiando arquivos\n')
    file.write('**Arquivo-text.txt\n')
    file.write('*Deletando arquivos antigos\n')
    file.write('**Arquivo-text.txt\n')
    file.close()



if __name__ == '__main__':
   # organize()
    summary()