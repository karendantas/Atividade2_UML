class LibraryItem:
    def __init__(self, Title, Subject, Contributorswtype=None, UPC=None):
        self.Title = Title
        self.UPC = UPC
        self.Subject = Subject
        self.Contributors = Contributorswtype

    # def Locate()


class Book(LibraryItem):
    def __init__(self, ISBN, Authors, Title, Subject, DDS_number):
        super().__init__(Title,Subject)
        self.ISBN = ISBN
        self.Authors = Authors
        self.DDS_number = DDS_number

    def __str__(self):
        return "Title: {}\nAuthors:{}\nSubject:{}".format(self.Title, self.Authors.name, self.Subject)



class CD(LibraryItem):
    def __init__(self, Artist):
        self.Artist = Artist

class DVD(LibraryItem):
    def __init__(self, Director, Actors, Genre):
        self.Director = Director
        self.Actors = Actors
        self.Genre = Genre

class Magazine(LibraryItem):
    def __init__(self, Volume, Issue):
        self.Volume = Volume
        self.Issue = Issue



#Colaboradores
class Contribuitor:
    def __init__(self, name):
        self.name = name

class Author(Contribuitor):
    pass

class Artist(Contribuitor):
    pass

class Actor(Contribuitor):
    pass

class Director(Contribuitor):
    pass

class Editor(Contribuitor):
    pass

class ContribuitorWithType:
    def __init__(self, contribuitor, Type):
        self.contribuitor = contribuitor
        self.type = Type

