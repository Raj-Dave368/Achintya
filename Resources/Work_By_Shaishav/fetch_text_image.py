import easyocr

reader=easyocr.Reader(['en'])

results = reader.readtext('sample.png')

# print(results)

text = ''

for result in results:
    text +=result[1]+ ' ' 

print(text)