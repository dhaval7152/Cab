file="ruleset/$1rulesFile"
sudo ovs-ofctl del-flows br0
sudo ovs-ofctl add-flows br0 $file
echo "Ready to record, start sending packets in 10s"
sleep 10

printf "%-10s %s\n" "Index" "Number" | tee "result/$1result.txt"
for i in {1..20}
do
	num="$(sudo ovs-dpctl dump-flows system@ovs-system | grep recirc_id | wc -l)"
	printf "%-10d %s\n" "$i" "$num" | tee -a "result/$1result.txt"
	sleep 0.5 
done
