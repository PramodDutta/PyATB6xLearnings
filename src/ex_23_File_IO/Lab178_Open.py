# t = open('testdata.txt', 'r')
# t = open('testdata.txt', 'w')
# t = open('testdata.txt', 'r+')
# t = open('testdata.txt', 'w+')
# t = open('testdata.txt', 'b')
# t.close()

# Automatically close
with open('testdata.txt', 'r') as f:
    data = f.read()

print(data)