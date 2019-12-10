 resource "aws_instance" "url1" {
 ami= "ami-04b9e92b5572fa0d1"
instance_type = "t2.micro" 
provisioner "local-exec" { 
command = "sudo apt install apache2"
}
}