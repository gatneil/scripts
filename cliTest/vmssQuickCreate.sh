set -euxv #helpful for debugging

mkdir -p output # create output dir if it doesn't exist
rm -f output/* # remove old output

# run command and contruct fqdn of pip from the output
azure vmss quick-create -l "West US" -g $1rg -n $1 -C 5 -u negat -p P4ssw0rd -Q Canonical:UbuntuServer:14.04.4-LTS:latest > output/quickCreateStdout.txt
grep "PublicIP" output/quickCreateStdout.txt | grep "creating" | head -n 1 > output/GrepOutput.txt
almost_fqdn=$(awk -F "\"" '{print $2}' output/GrepOutput.txt) # parse out the public IP name, which will also be used in the FQDN
rest_of_fqdn="2.westus.cloudapp.azure.com" # !!! only use 2 because quick-create currently makes 2 pips and uses the 2nd one; this should go away once this is fixed
fqdn=$almost_fqdn$rest_of_fqdn

ssh-keygen -R $fqdn # ssh checks that the remote host ssh keys haven't changed; purge this fqdn in case we have used it before

# test that ssh-ing with the password works (!!! not secure because the password is in plain text in the system's log of commands)
sshpass -p P4ssw0rd ssh -o "StrictHostKeyChecking no" -p 50000 negat@$fqdn ls -l > output/vm0.txt
sshpass -p P4ssw0rd ssh -o "StrictHostKeyChecking no" -p 50001 negat@$fqdn ls -l > output/vm1.txt
sshpass -p P4ssw0rd ssh -o "StrictHostKeyChecking no" -p 50002 negat@$fqdn ls -l > output/vm2.txt
sshpass -p P4ssw0rd ssh -o "StrictHostKeyChecking no" -p 50003 negat@$fqdn ls -l > output/vm3.txt
sshpass -p P4ssw0rd ssh -o "StrictHostKeyChecking no" -p 50004 negat@$fqdn ls -l > output/vm4.txt

# if we find "total" in the output, then the ssh worked; thus we count the lines with "total" and expect 1 for each VM
vm0=$(grep "total" output/vm0.txt | wc -l)
vm1=$(grep "total" output/vm1.txt | wc -l)
vm2=$(grep "total" output/vm2.txt | wc -l)
vm3=$(grep "total" output/vm3.txt | wc -l)
vm4=$(grep "total" output/vm4.txt | wc -l)

res=$(($vm0+$vm1+$vm2+$vm3+$vm4-5))
if [ $res -ne 0 ]
then echo "TEST FAILED"
fi
exit $res
