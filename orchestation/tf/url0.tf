 resource "aws_instance" "url0" {
 ami= "ami-04b9e92b5572fa0d1"
key_name = "terrakey" 
vpc_security_group_ids= [ "sg-03bf4ad9a70591b13" ] 
instance_type = "t2.micro" 
provisioner "remote-exec" { 
inline = [ 
 "apt install apache2" 
 ]
}
}