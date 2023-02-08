# my_text = open("doc.txt")
# content = my_text.read()
# print(content)
# my_text.close()

# Otra forma sin tener que cerrar el archivo:
with open("./doc.txt", mode="w") as my_txt:
    my_txt.write("Hi")
# El mode puede ser r: read, w: write y sobreescribe o a: append que añade
with open("doc.txt", mode="r") as my_txt:
    print(my_txt.read())
with open("new_doc.txt", mode="w") as my_txt:
    my_txt.write("Hi2")

#path:
# ./ significa en la carpeta actual
# ../ en la capeta superior