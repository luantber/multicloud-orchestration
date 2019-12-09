from python_terraform import *
from orchestation.Instancia import Instancia

def create_plan(specification):
    id_s = "url"
    id = 0
    for nodo in specification:
        instancia = Instancia(nodo,id_s+str(id))
        instancia.create_tf()
        id+=1


def execute_plan():
    t = Terraform(working_dir='orchestation/tf/',terraform_bin_path='/home/luisbch/Documentos/cloud/aws/terraform/terraform')
    t.init()
    return_code, stdout, stderr = t.plan()

    #print(return_code)
    print(stdout)
    print(stderr)
