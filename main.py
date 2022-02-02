import os
import os.path as path
import shutil

RED = "\033[1;31m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
YELLOW = "\u001b[33m"


def menu():
    while True:
        print('Choose between the options below')
        print('1 - Just create slot folder and move save game into them')
        menu_option = input('2 - Just rename save game user folder (like from 8000000a to 8000000c) \n')
        if menu_option == '1':
            create_slot_folders_and_move_save_game()
            break
        elif menu_option == '2':
            rename_save_game_user_folders()
            break


def prompt_root_folder():
    root = input(
        'Absolute path to batch backups folder (without slash at the end), ex.: D:\\Downloads\\Jogos\\Wii U\\backups jogos\\2022-01-29T100416_new \n')
    root.replace('\\', '\\\\')
    root.replace('/', '\\')

    return root


def get_directory_list(path_to_directory):
    dir_list = [item for item in os.listdir(path_to_directory) if os.path.isdir(os.path.join(path_to_directory, item))]
    return dir_list


def create_slot_folders_and_move_save_game():
    root = prompt_root_folder()
    slot_number_to_create_folder = input('Slot to create folder, like 0 to 255 \n')
    dir_list = get_directory_list(root)
    number_of_moved_folders = 0
    number_of_already_exists_slot_folders = 0
    number_of_created_slot_folders = 0

    for dir_name in dir_list:
        subdirectory_path = root + '/' + dir_name
        subdirectories_list = [item for item in os.listdir(subdirectory_path) if
                               os.path.isdir(os.path.join(subdirectory_path, item))]
        folder_to_create = root + '/' + dir_name + '/' + slot_number_to_create_folder

        if path.isdir(folder_to_create):
            print(
                RESET + 'The folder for slot ' + slot_number_to_create_folder + ' for game ID ' + dir_name + RESET + RED + ' already exists.')
            number_of_already_exists_slot_folders += 1
        else:
            os.mkdir(folder_to_create)
            number_of_created_slot_folders += 1

        for subdirectory_name in subdirectories_list:
            subdirectory_path = subdirectory_path + '/' + subdirectory_name;

            if subdirectory_name != 'common' and len(subdirectory_name) > 3:
                if shutil.move(subdirectory_path, folder_to_create):
                    number_of_moved_folders += 1

    print(GREEN + 'Process finished, ' + str(number_of_moved_folders) + ' folders have been moved')
    print(YELLOW + str(number_of_already_exists_slot_folders) + ' slot folders already exists and were not created')
    print(GREEN + str(number_of_created_slot_folders) + ' new slot folders have been created')

    return 0


def rename_save_game_user_folders():
    root = prompt_root_folder()
    dir_list = get_directory_list(root)
    original_user_folder_name = input('Source user folder name: Example: 8000000a \n')
    new_user_folder_name = input('New user folder name: Example: 8000000c \n')
    number_of_renamed_folders = 0

    for dir_name in dir_list:
        sub_directory_path = root + '/' + dir_name
        subdirectories_list = [item for item in os.listdir(sub_directory_path) if
                               os.path.isdir(os.path.join(sub_directory_path, item))]

        for subdirectory_name in subdirectories_list:
            if (subdirectory_name == original_user_folder_name):
                os.rename(sub_directory_path + '/' + original_user_folder_name, sub_directory_path + '/' + new_user_folder_name)
                number_of_renamed_folders += 1

    print(GREEN + 'Process finished, ' + str(number_of_renamed_folders) + ' folders have been renamed')
    return 0


menu()
