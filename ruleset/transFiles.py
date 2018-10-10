import sys

def main(argv):
	count=1
	with open('Test8rules', 'r') as f:
		for line in f.readlines():
			arr = line.split()
			arr0=arr[0].strip('@')
			temp1=''
			if 	arr[2]=='0' and arr[4]=='32767':
				temp1 = ",tp_src=0/32768"
			if arr[2]==arr[4]:
				temp1=",tp_src={0}".format(arr[2])
			if arr[2]=='0' and arr[4]=='65535':
				temp1=''
			if 	arr[2]=='32768' and arr[4]=='65535':
				temp1 = ",tp_src=32768/32768"

			temp2=''

			if arr[5] == '0' and arr[7] == '32767':
				temp2 = ",tp_dst=0/32768"
			if arr[5] == arr[7]:
				temp2 = ",tp_dst={0}".format(arr[5])
			if arr[5] == '0' and arr[7] == '65535':
				temp2 = ''
			if arr[5] == '32768' and arr[7] == '65535':
				temp2 = ",tp_dst=32768/32768"

			s="priority={0},dl_type=0x0800,nw_proto=17,nw_src={1},nw_dst={2}{3}{4},actions=output:2".format(count,arr0,arr[1],temp1,temp2)
			count+=1;
			print(s)
			with open('rulesFile', 'a') as w:
				w.write(s+"\n")
	f.closed

if __name__ == '__main__':
	main(sys.argv)
