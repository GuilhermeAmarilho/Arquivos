import zipfile, os, shutil
# Escolha o diretório onde quer armazenar o arquivo zipado
diretorio_para_zip = 'SubPasta1\SubPasta2'
arquivo_zip = 'Arquivo.zip'
with zipfile.ZipFile(arquivo_zip, 'w') as zipf:
    for pasta_raiz, subdirs, arquivos in os.walk(diretorio_para_zip):
        for arquivo in arquivos:
            caminho_completo = os.path.join(pasta_raiz, arquivo)
            zipf.write(caminho_completo, os.path.relpath(caminho_completo, diretorio_para_zip))
        # rmtree deleta o diretório atual
        shutil.rmtree('\\Pasta')
        # makedirs cria novamente o diretorio, após apaga-lo
        os.makedirs('\\Encarte')