import boto3
from pprint import pprint
from drivers.TipoInstancia import TipoInstancia
import pickle

class awsDriver():
    def discover_types(self,use_cache=False):
        tipos = []
        if use_cache:
            with open("drivers/aws_cache.pkl","rb") as pkl:
                tipos = pickle.load(pkl)
            
        else:
            #sin cache
            ec2 = boto3.client('ec2')
            tipos = ec2.describe_instance_types()
            with open("drivers/aws_cache.pkl","wb+") as pkl:
                pickle.dump(tipos,pkl)
            



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