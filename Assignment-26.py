# Python implementation to
# read last N lines of a file

# Function to read
# last N lines of the file
def LastNlines(fname, N):
	# opening file using with() method
	# so that file get closed
	# after completing work
	with open(fname) as file:
		
		# loop to read iterate
		# last n lines and print it
		for line in (file.readlines() [-N:]):
			print(line, end ='')

# Driver Code:
if __name__ == '__main__':
	fname = 'example.txt'
	N = 5
	try:
		LastNlines(fname, N)
	except:
		print('File not found')
