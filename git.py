import time
from getpass import getuser
import os


class Path:
    def __init__(self, caminho):
        self.caminho: str = caminho

    def gitList(self):
        """
        first function
        :return:
        """
        itens = os.system(f'ls {self.caminho}')
        return str(itens)


class Git:
    """
    do commands for to starts git
    """
    def __init__(self, nomePasta, commit, url):
        self.nomePasta = nomePasta
        self.commit = commit
        self.url = url
        self.caminho = f'/home/{getuser()}/{self.nomePasta}/'

    def gitInitAdd(self):
        """
            this is an important class, because it creates a git repository
        """
        caminho = f'/home/{getuser()}/{self.nomePasta}'
        # commands
        os.system(f'cd {self.caminho}')
        time.sleep(1)
        os.system(f'git init {self.caminho} && cd {self.caminho} && git add .')

    def gitCommit(self):
        """
        commit git
        :return:
        """
        time.sleep(1)
        os.system(f'cd {self.caminho} && git commit -m {self.commit}')

    def gitPush(self):
        self.gitInitAdd()
        self.gitCommit()
        os.system(f'cd {self.caminho} && git remote add origin {self.url}')
        time.sleep(1)
        os.system(f'cd {self.caminho} && git branch -M main')
        time.sleep(1)
        os.system(f'cd {self.caminho} && git push -u origin main')


if __name__ == '__main__':
   pass