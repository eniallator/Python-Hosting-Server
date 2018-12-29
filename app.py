import os
import sys
from CONFIG import REPO, BRANCH, DYNO_FOLDER
from src.Update import update_project
from src.DynoManager import DynoManager

PROD = 'production' in sys.argv


def main():
    project_path = os.path.dirname(os.path.realpath(__file__))

    if PROD:
        print('Checking for updates...')
        update_project(project_path, REPO, BRANCH)

    dyno_path = os.path.join(project_path, DYNO_FOLDER)
    dyno_manager = DynoManager(dyno_path)
    dyno_manager.add_dyno(name='Enibot', repo='eniallator/Discord-Enibot', branch='master', main='app.py')
    dyno_manager.add_dyno(name='Overwatch', repo='eniallator/Discord-Overwatch-Bot', branch='master', main='app.py')
    print(dyno_manager._dynos)


if __name__ == "__main__":
    main()
