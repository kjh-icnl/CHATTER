import time, sys

def delete_last_line():
    "Use this function to delete the last line in the STDOUT"

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')

def main():
	print("LINE 1")
	time.sleep(2)
	delete_last_line()
	time.sleep(2)	
	print("LINE 2")
	print("CHANGED")

if __name__ == '__main__':
	main()

