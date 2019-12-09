import boto3
from pprint import pprint
from drivers.TipoInstancia import TipoInstancia


class awsDriver():
    def discover_types(self):
        ec2 = boto3.client('ec2')
        tipos = ec2.describe_instance_types()
        # print(tipos.keys())
        # pprint(tipos['InstanceTypes'][0])
        lista = []
        for tipo in  tipos['InstanceTypes']:
            free = tipo['FreeTierEligible']
            name = tipo['InstanceType']
            cpu = tipo['VCpuInfo']['DefaultVCpus']
            ram = tipo['MemoryInfo']['SizeInMiB']
            tipoI = TipoInstancia(name=name,cpu=cpu,ram=ram,free=free) 
            lista.append(tipoI)
        return lista


# for x in awsDriver().discover_types():
#     x.describe()