import os
import os.path as path
import shutil

RED   = "\033[1;31m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
YELLOW = "\u001b[33m"

root = input('Caminho absoluto da pasta do batch backup, ex.: D:\\Downloads\\Jogos\\Wii U\\backups jogos\\2022-01-29T100416_new \n');
root.replace('\\', '\\\\');
root.replace('/', '\\');

slotNumberToCreateFolder = input('Número do slot para criação da pasta, 0 a 255 \n')
dirlist = [item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item))]
numberOfMovedFolders = 0
numberOfAlreadyExistsSlotFolders = 0
numberOfCreatedSlotFolders = 0

for dirName in dirlist:
    dirPath = root + '/' + dirName;
    subdirectoriesList = [item for item in os.listdir(dirPath) if os.path.isdir(os.path.join(dirPath, item))]
    folderToCreate = root + '/' + dirName + '/' + slotNumberToCreateFolder;

    if(path.isdir(folderToCreate)):
        print(RESET + 'A pasta para o slot ' + slotNumberToCreateFolder + ' para o jogo ' + dirName + RESET + RED + ' já existe meu querido.')
        numberOfAlreadyExistsSlotFolders += 1
    else:
        os.mkdir(folderToCreate)
        numberOfCreatedSlotFolders += 1

    for subDirectoryName in subdirectoriesList:
        subDirectoryPath = dirPath + '/' +subDirectoryName;

        if(subDirectoryName != 'common' and len(subDirectoryName) > 3):
            if(shutil.move(subDirectoryPath, folderToCreate)):
                numberOfMovedFolders += 1

print(GREEN + 'Execução concluída, ' + str(numberOfMovedFolders) + ' pastas foram movidas para seus devidos lugares')
print(YELLOW + str(numberOfAlreadyExistsSlotFolders) + ' pastas de slot já existiam e não foram criadas')
print(GREEN + str(numberOfCreatedSlotFolders) + ' novas pastas de slot foram criadas')
