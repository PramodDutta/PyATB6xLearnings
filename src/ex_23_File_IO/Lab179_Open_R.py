try:
    with open('testdata.txt', 'r') as file:
        content = file.read()
    # content = file.readlines() # list manner
        print(content)
except FileNotFoundError as fnfe:
    print(fnfe)
