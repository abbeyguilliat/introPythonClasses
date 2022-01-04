## BASE CLASS
class Book:
    '''Book Class'''
    def __init__(self,isbn,title,author,publisher,pages,publishDate):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__pages = pages
        self.__publishDate = publishDate

    @property
    def isbn(self):
        print('Getting ISBN')
        return self.__isbn
    @isbn.setter
    def isbn(self,new_isbn):
        print('Setting ISBN')
        self.__isbn = new_isbn

    @property
    def title(self):
        print('Getting title')
        return self.__title
    @title.setter
    def title(self,new_title):
        print('Setting title')
        self.__title = new_title

    @property
    def author(self):
        print('Getting author')
        return self.__author
    @author.setter
    def author(self,new_author):
        print('Setting author')
        self.__author = new_author

    @property
    def publisher(self):
        print('Getting publisher')
        return self.__publisher
    @publisher.setter
    def publisher(self,new_publisher):
        print('Setting publisher')
        self.__publisher = new_publisher

    @property
    def pages(self):
        print('Getting page count')
        return self.__pages
    @pages.setter
    def pages(self,new_pages):
        print('Setting page count')
        self.__pages = new_pages

    @property
    def publishDate(self):
        print('Getting date of publication')
        return self.__publishDate
    @publishDate.setter
    def publishDate(self,new_publishDate):
        print('Setting date of publication')
        self.__publishDate = new_publishDate

    def open_cover(self):
        print('Opening book')
        
    def turn_page(self):
        print('Turning page')

    def close_cover(self):
        print('Closing book')

## INHERITING CLASS: TEXTBOOK
class Textbook(Book):
    '''Textbook Class, Inheriting from Book'''
    def __init__(self,isbn,title,author,publisher,pages,publishDate,currentOwner,subject,gradeLevel,cost):
        super().__init__(isbn)
        super().__init__(title)
        super().__init__(author)
        super().__init__(publisher)
        super().__init__(pages)
        super().__init__(publishDate)
        self.__owner = currentOwner
        self.__subject = subject
        self.__level = gradeLevel
        self.__cost = cost
    
    @property
    def owner(self):
        return self.__owner
    @owner.setter
    def owner(self,new_owner):
        self.__owner = new_owner

    @property
    def subject(self):
        return self.__subject
    @subject.setter
    def subject(self,new_subject):
        self.__subject = new_subject

    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self,new_level):
        self.__level = new_level

    @property
    def cost(self):
        return self.__cost
    @cost.setter
    def cost(self,new_cost):
        self.__cost = new_cost

    def readPage(self):
        print('Reading page')

    def highlightText(self):
        print('Highlighting text')

## INHERITING CLASS: ADDRESS BOOK
class AddressBook(Book):
    '''Address Book, Inheriting from Book'''
    def __init__(self,isbn,title,author,publisher,pages,publishDate,owner,percentFilled):
        super().__init__(isbn)
        super().__init__(title)
        super().__init__(author)
        super().__init__(publisher)
        super().__init__(pages)
        super().__init__(publishDate)
        self.__owner = owner
        self.__filled = percentFilled

    @property
    def owner(self):
        return self.__owner
    @owner.setter
    def owner(self,new_owner):
        self.__owner = new_owner

    @property
    def percentFilled(self):
        return self.__filled
    @percentFilled.setter
    def percentFilled(self,new_fill):
        self.__filled = new_fill

    def lookupEntry(self,person):
        print("Searching for " + person + "'s address")

    def addEntry(self,person):
        print("Adding an entry for " + person)