from Domain.book import createBook
from UI.UserInterface import showBooks
from functions.Logic import deleteBookbyId


def newMenu(lista):
    # add
    # showall
    # delete
    while True:
        option = input("Va rog intruduceti comanda(add/showall/delete/help/stop): ")
        text = option.split(";")
        for command in text:
            params = command.split(",")
            if params[0] == "add":
                id = params[1]
                titlu = params[2]
                genCarte = params[3]
                pret = params[4]
                tipReducere = params[5]
                book = createBook(id, titlu, genCarte, pret, tipReducere)
                lista.append(book)
            elif params[0] == "showall":
                showBooks(lista)
            elif params[0] == "delete":
                id = params[1]
                lista = deleteBookbyId(lista, id)
            elif params[0] == "help":
                print("Sintaxa add: add,id,titlu,gen carte,pret,tip reducere;")
                print("sintaxa showall: showall;")
                print("Sintaxa delete: delete,id;")
                print("Sintaxa help: help;")
                print("Sintaxa stop: stop;")
            elif command == "stop":
                return