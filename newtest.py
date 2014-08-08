import sys
import json
import re

def main():
    user_input = raw_input("Enter poem:").split(' ')
    poem_len = len(user_input)
    print poem_len

if __name__ == '__main__':
    main()
