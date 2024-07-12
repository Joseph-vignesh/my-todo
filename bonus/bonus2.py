contents = ['Hello', 'everyone']
files = ['doc.txt','presentation.txt']

for content, filename in zip(contents, files):
    file = open(f"../basic/{files} ", 'w')
    file.write(content)