import os
class Instancia():
    def __init__(self,tipo,id):
        self.tipo = tipo
        self.id = id

    def create_tf(self):
        cadena = ''' resource "aws_instance" '''
        cadena += '''"''' + self.id + '''" '''
        cadena += '{'
        cadena += '''\n ami= "ami-2757f631"\n'''
        cadena += '''instance_type = "t2.micro"\n'''
        cadena += '}'


# resource "aws_instance" "example" {
#   ami           = "ami-2757f631"
#   instance_type = "t2.micro"
# }

        print(cadena)
        with open( os.path.join ("orchestation/tf/",self.id+".tf"),"w+" ) as f:
            f.write(cadena)


