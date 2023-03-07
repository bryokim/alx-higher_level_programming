def uppercase(str):
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            char = ord(char) - ord('a') + ord('A')
        else:
            char = ord(char)
        print("{:c}".format(char), end="")
    print("")
