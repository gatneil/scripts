sleep 30s
wget https://github.com/gatneil/scripts/raw/master/TechReadyDemo/vmss_node.tar.gz
tar -xvf vmss_node.tar.gz
cd vmss_node
sh initialize.sh root $1
