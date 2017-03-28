status_file_path=/var/lib/waagent/$(ls /var/lib/waagent | grep Microsoft.Azure.Extensions.Docker | grep -v xml)/status/0.status

while [ 1 == 1 ]
do
	if grep -q "success" $status_file_path; then
		break
	else
		sleep 5
		echo "waiting"
	fi
done

echo 'docker finished; do cool stuff here'
