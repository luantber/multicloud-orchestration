from python_terraform import *
from orchestation.Instancia import InstanciaAWS

def create_plan(specification):
    id_s = "url"
    id = 0
    for nodo in specification:
        instancia = InstanciaAWS(nodo,id_s+str(id))
        instancia.create_tf()
        id+=1

def execute_plan(debug=False):
    t = Terraform(working_dir='orchestation/tf/',terraform_bin_path='/home/luisbch/Documentos/cloud/aws/terraform/terraform')
    t.init()
    if debug:
        return_code, stdout, stderr = t.plan()
    else:
        return_code, stdout, stderr = t.apply(skip_plan=True)

    print(return_code)
    print(stdout)
    print(stderr)
