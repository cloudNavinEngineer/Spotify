import sys
import json
import re

def main():
    user_input = raw_input("Enter poem:").split(' ')
    poem_len = len(user_input)
    print poem_len

if __name__ == '__main__':
    main()

pseudo code
-------------------------------
# all functions
# Function to find center of the list or string
ptr= findcenter()

# Function to search the track
tracksearch()

#function to resize right
resize_right()

#function to resize left
resize_left()

------------------------------

Title_left =list.join(0 - center)
Title_right= list.join(center - end)

tracksearch(Title_left)
tracksearch(Title_right)

if found
done:

else
{
resize_right(Title_left)
resize_left(Title_right)

	if both found done:

	# now take the left part and find the track for that 1st
	# this way we are splitting the string into 3 but not into equal parts 
	# the left is divided into 2 parts  and the 3rd part is right part
		else
		    split=findcenter(Title_right):
			tracksearch(0-split)
			if found done:
				else
				{
					resize_right()
					resize_left()
				}
}
