"""
 author: John Richardson
   date: 8/22/2020
revised: 8/22/2020
   desc: A script to create boilerplate python code
"""

import os
import subprocess


def create_dir(path, dir_name):
    if( dir_name == '' ):
        os.mkdir(path)
        print("created dir {0}".format(path))
    else:
        os.mkdir(os.path.join(path, dir_name))
        print("created dir {0}".format(dir_name))
    


def create_virtual_env():
    print("creating venv")
    venv = subprocess.call(['py', '-m', 'venv', 'venv'])
    print('finished venv')


def main():
    dir_list = ['includes', 'logs', 'python']
    print("Please name your project") 
    user_input = input('=>')
    project_dir = "C:\\projects\\"
    path = os.path.join(project_dir, user_input)
    if(user_input != ""):
        create_dir(path, '')
        for d in dir_list:
            create_dir(path, d)
        os.chdir(path)
        create_virtual_env()
        


if __name__ == "__main__":
    main()