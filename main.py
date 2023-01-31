import glob
import os
from pathlib import Path
import shutil
from pick import pick
from rich.console import Console


def k_get_context():
    return [os.path.basename(file) for file in glob.glob(f'{Path.home()}/.kube/context/*.yml')]


def k_set_context(_option):
    shutil.copyfile(f'{Path.home()}/.kube/context/{_option}', f'{Path.home()}/.kube/config')


if __name__ == '__main__':
    console = Console()
    opcoes = k_get_context()
    if len(opcoes) > 0:
        title = 'Selecione o contexto kubernetes: '
        option, index = pick(opcoes, title, indicator='=>')
        k_set_context(option)
    else:
        console.print("Não foi encontrado nenhum perfil.", style="bold red")
