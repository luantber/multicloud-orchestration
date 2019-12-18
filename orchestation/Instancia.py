import os
class InstanciaAWS():
    def __init__(self,tipo,id):
        self.tipo = tipo
        self.id = id
        self.public_ip = None

    def create_tf(self):
        cadena = ''' resource "aws_instance" '''
        cadena += '''"''' + self.id + '''" '''
        cadena += '{'
        cadena += '''\n ami= "ami-0d5d9d301c853a04a"\n'''
        cadena += '''key_name = "terrakey" \n'''
        cadena += '''vpc_security_group_ids= [ "sg-03bf4ad9a70591b13" ] \n''' #UBUNTU
        cadena += '''instance_type = "''' + self.tipo.name + '''" \n'''  #tipo Tipo instancia FIX
        cadena += '''provisioner "remote-exec" { \n'''

        cadena += '''connection {
        type     = "ssh"
        user     = "ubuntu"
        private_key = "${file("terrakey.pem")}"
        host     = "${aws_instance.''' + self.id + '''.public_ip}"
    }\n'''


        cadena += '''inline = [ \n "sudo apt -y install apache2" \n ]\n'''
        cadena += '''}\n'''
        cadena += '}\n'
        

        cadena += '''output "'''+ self.id + '''_ip"{
	                value = "${aws_instance.''' + self.id + '''.public_ip}"
                }'''

        #  key_name = "terrakey"
        #  vpc_security_group_ids= [ "sg-08981f593c413b9c3" ]

        print(cadena)
        with open( os.path.join ("orchestation/tf/",self.id+".tf"),"w+" ) as f:
            f.write(cadena)


