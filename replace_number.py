s = editor.getText()
editor.clearAll()
n = 16
for i in range(n):
    t = s.replace('@(1)',format(i+1,'02')).replace('@(2)',str(i))
    editor.addText(t)
