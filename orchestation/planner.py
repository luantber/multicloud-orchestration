from python_terraform import *

t = Terraform(working_dir='tf/',terraform_bin_path='/home/luisbch/Documentos/cloud/aws/terraform/terraform')
t.init()
return_code, stdout, stderr = t.plan()

#print(return_code)
print(stdout)
print(stderr)