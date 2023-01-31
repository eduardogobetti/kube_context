from glob import glob
import os
from pathlib import Path
import shutil
from rich.pretty import pprint
from rich.prompt import Confirm

def k_get_context():
    return [os.path.basename(file) for file in glob(f'{Path.home()}/.kube/context/*.yml')]

def k_set_context(option):
    shutil.copyfile(f'{Path.home()}/.kube/context/{option}', f'{Path.home()}/.kube/config')

if __name__ == '__main__':
    options = k_get_context()
    selected = Confirm.choices("Selecione o contexto kubernetes:", options)
    option = selected[0] if selected else None
    k_set_context(option)
