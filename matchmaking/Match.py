import json
from drivers.awsDriver import awsDriver


# print(data)
def match(file_req,use_cache=False):
    with open(file_req) as json_file:
        data = json.load(json_file)
        # print(data)
        lista = awsDriver().discover_types(use_cache=use_cache)
        # lista = GCpDriver().discover_types(use_cache=use_cache)

        resultado_final = []
        resultado_query = []
        if 'all' in data.keys():
            for x in lista:
                if x.ram == data['all']['ram'] and x.cpu == data['all']['cpu']:
                    resultado_query.append(x)
            print(resultado_query)
            instancia_tipo = resultado_query[0]
            resultado_final = [instancia_tipo]*data['nodos']
                
        # for r in resultado:
        #     r.describe()
        return resultado_final
