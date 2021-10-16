"""Import nessessary library for script work.
Script for backup screenshots from game clients in one folder
"""
import os
from distutils import dir_util


def backup_screenshots(source_folder, games_list, output_folder):
    for games in games_list:
        destination_dir = os.path.join(
            output_folder,
            games_list[games]
        )
        source = os.path.join(source_folder, games_list[games])
        dir_util.copy_tree(source, destination_dir)


if __name__ == "__main__":
    CLIENTPATH = "C:\Games"
    GAMES_SCREENS_FOLDER_LIST = {
        "DIR_1": "DIR_1\Screenshots",
        "DIR_2": "Test2\Screenshots",
    }
    OUTPUT = "C:\Screenshots"
    backup_screenshots(
        CLIENTPATH,
        GAMES_SCREENS_FOLDER_LIST,
        OUTPUT
    )
