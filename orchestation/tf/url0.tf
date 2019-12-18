 resource "aws_instance" "url0" {
 ami= "ami-0d5d9d301c853a04a"
key_name = "terrakey" 
vpc_security_group_ids= [ "sg-03bf4ad9a70591b13" ] 
instance_type = "t2.micro" 
provisioner "remote-exec" { 
connection {
        type     = "ssh"
        user     = "ubuntu"
        private_key = "${file("terrakey.pem")}"
        host     = "${aws_instance.url0.public_ip}"
    }
inline = [ 
 "sudo apt -y install apache2" 
 ]
}
}
output "url0_ip"{
	                value = "${aws_instance.url0.public_ip}"
                }