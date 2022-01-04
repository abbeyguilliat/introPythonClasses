class Animal:
    '''Animal Class'''
    def __init__(self,name,group,species,height,length,weight,age):
        self.__name = name
        self.__group = group
        self.__species = species
        self.__height = height
        self.__length = length
        self.__weight = weight
        self.__age = age

    @property
    def name(self):
        print('Getting name')
        return self.__name
    @name.setter
    def name(self,new_name):
        print('Setting name')
        self.__name = new_name

    @property
    def group(self):
        print('Getting group')
        return self.__group
    @group.setter
    def group(self,new_group):
        print('Setting group')
        self.__group = new_group

    @property
    def species(self):
        print('Getting species')
        return self.__species
    @species.setter
    def species(self,new_species):
        print('Setting species')
        self.__species = new_species

    @property
    def height(self):
        print('Getting height')
        return self.__height
    @height.setter
    def height(self,new_height):
        print('Setting height')
        self.__height = new_height

    @property
    def length(self):
        print('Getting length')
        return self.__length
    @length.setter
    def name(self,new_length):
        print('Setting length')
        self.__length = new_length

    @property
    def weight(self):
        print('Getting weight')
        return self.__weight
    @weight.setter
    def weight(self,new_weight):
        print('Setting weight')
        self.__weight = new_weight

    @property
    def age(self):
        print('Getting age')
        return self.__age
    @age.setter
    def age(self,new_age):
        print('Setting age')
        self.__age = new_age

    def move(self):
        print('Moving')
    
    def eat(self,food):
        print('Eating ' + food)

    def sleep(self):
        print('Sleeping')

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

class Vehicle:
    '''Vehicle Class'''
    def __init__(self,license,model,make,color,manufactureDate):
        self.__license = license
        self.__model = model
        self.__make = make
        self.__color = color
        self.__manufactureDate = manufactureDate

    @property
    def license(self):
        print('Getting license')
        return self.__license
    @license.setter
    def license(self,new_license):
        print('Setting license')
        self.__license = new_license

    @property
    def model(self):
        print('Getting model')
        return self.__model
    @model.setter
    def model(self,new_model):
        print('Setting model')
        self.__model = new_model

    @property
    def make(self):
        print('Getting make')
        return self.__make
    @make.setter
    def make(self,new_make):
        print('Setting make')
        self.__make = new_make
        
    @property
    def color(self):
        print('Getting color')
        return self.__color
    @color.setter
    def color(self,new_color):
        print('Setting color')
        self.__color = new_color

    @property
    def manufactureDate(self):
        print('Getting date of manufacture')
        return self.__manufactureDate
    @manufactureDate.setter
    def manufactureDate(self,new_manufactureDate):
        print('Setting date of manufacture')
        self.__manufactureDate = new_manufactureDate

    def start_stop_engine(self):
        print('Prompting engine')
        
    def drive(self):
        print('Driving')
        
    def brake(self):
        print('Braking')