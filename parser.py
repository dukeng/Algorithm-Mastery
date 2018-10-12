import markdown
f = open('FourSum.md', 'r')
htmlmarkdown=markdown.markdown(f.read())
htmlmarkdown = htmlmarkdown.split('\n') 


i = 0
for line in htmlmarkdown:
    print(i,line)
    i += 1


title = htmlmarkdown[2]
topic = htmlmarkdown[7]
tags = htmlmarkdown[8]
technics = htmlmarkdown[9]

print(title, tags,technics)