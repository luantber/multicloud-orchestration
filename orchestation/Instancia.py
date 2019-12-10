import os
class Instancia():
    def __init__(self,tipo,id):
        self.tipo = tipo
        self.id = id

    def create_tf(self):
        cadena = ''' resource "aws_instance" '''
        cadena += '''"''' + self.id + '''" '''
        cadena += '{'
        cadena += '''\n ami= "ami-04b9e92b5572fa0d1"\n'''
        cadena += '''instance_type = "t2.micro" \n'''
        cadena += '''provisioner "local-exec" { \n'''
        cadena += '''command = "sudo apt install apache2"\n'''
        cadena += '''}\n'''
        cadena += '}'
        

        print(cadena)
        with open( os.path.join ("orchestation/tf/",self.id+".tf"),"w+" ) as f:
            f.write(cadena)


