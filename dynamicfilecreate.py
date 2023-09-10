contents = ['Ram', 'Shyam', 'Kumar']

files = ['first.txt','second.txt','third.txt']

for content, file in zip(contents,files):
    file = open(f"file\{file}", 'w')
    file.write(content)
