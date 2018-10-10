import markdown
f = open('FourSum.md', 'r')
htmlmarkdown=markdown.markdown(f.read())
htmlmarkdown = htmlmarkdown.split('\n') 


i = 0
for line in htmlmarkdown:
    print(i,line)
    i += 1


title = htmlmarkdown[2]