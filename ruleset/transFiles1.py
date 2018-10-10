import sys

def main(argv):
	with open('gpx_100rules', 'r') as f:
		for line in f.readlines():
			arr = line.split()
			print(arr[0])
			print(arr[1])
			print(arr[2] + ' : ' + arr[4])
			print(arr[5] + ' : ' + arr[7])
			with open('wroteFile', 'a+') as w:
				w.write
	f.closed

if __name__ == '__main__':
	main(sys.argv)
