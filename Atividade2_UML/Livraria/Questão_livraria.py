from LibraryItem import LibraryItem, Book, CD, DVD, Magazine, Author
import re
class Catalog:
    book_list = []

    def add_ToCatalog(self, object):

        if isinstance(object, LibraryItem):
            self.book_list.append(object)
            print("Adicionado ao catálogo")

    def Search(self, search):
       
      
        for o in self.book_list:
            if search == o.Title or search == o.Authors.name or search == o.Subject:
                encontrado = True
                print(o)
            else:
                encontrado = False

        if encontrado is False:
            print("Não encontrado")
     


author1 = Author("Isac Asimov")
author2 = Author("Miranda")
livro1 = Book(1, author1, "eu Robo", "Ficção Cientifíca", 222 )
livro2 = Book(2, author2, "Beibe", "Conto", 122 )
catalogo = Catalog()


catalogo.add_ToCatalog(livro1)
catalogo.add_ToCatalog(livro2)
catalogo.Search("eu Robo")

