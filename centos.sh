yum -y update
yum -y install httpd
systemctl start httpd.service
systemctl enable httpd.service