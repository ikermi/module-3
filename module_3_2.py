# The standard for classes is the firs letter uppercase
class Invoice:

  def greeting(self): 
    # functions inside classes need always a default argument
    return 'Hi there'


inv_one = Invoice()
print(inv_one.greeting())

class Invoice:
  def __init__(self, client, total):
    self.client = client
    self.total = total

  def formatter(self):
    return f'{self.client} owes: ${self.total}'


google = Invoice('Google', 100)
snapchat = Invoice('SnapChat', 200)

google.client = 'Hello'
print(google.formatter())
print(snapchat.formatter())

class Invoice:

    # In this class we want to protect the variables. thats whi they have an underscore before the name, 
    # so they cant be called simply saying self.client. THis way it needs to be defined to get the value and to change it
    def __init__(self, client, total):
        self._client = client
        self._total = total

    def formatter(self):
        return f'{self._client} owes: ${self._total}'

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, client):
        self._client = client

    @property
    def total(self):
        return self._total

google = Invoice('Google', 100)

print(google.client)

google.client = 'Yahoo'

print(google.client)

# The dunder __str__ method very useful for debugging
class Invoice:
  def __init__(self, client, total):
    self.client = client
    self.total = total

  def __str__(self):
    return f"Invoice from {self.client} for {self.total}"

  # Sort of like string but it is used in bigger classes usually tu write raw data of the class
  def __repr__(self):
    return f"Invoice({self.client}, {self.total})"


inv = Invoice('Google', 500)
print(str(inv))
print(repr(Invoice))

class Lineup:

    def __init__(self, players):
        self.players = players
        self.last_player_index = (len(self.players) - 1)

    def __iter__(self):
        self.n = 0
        return self

    def get_player(self, n):
        return self.players[n]

    def __next__(self):
        if self.n < self.last_player_index:
            player = self.get_player(self.n)
            self.n += 1
            return player
        elif self.n == self.last_player_index:
            player = self.get_player(self.n)
            self.n = 0
            return player


astros = [
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]

astros_lineup = Lineup(astros)
process = iter(astros_lineup)

class InfiniteLineup:
    def __init__(self, players):
        self.players = players

    def lineup(self):
        lineup_max = len(self.players)
        idx = 0

        while True:
            if idx < lineup_max:
                yield self.players[idx] # yields implements all the __next__ thing and returns self.players[idx] when call it
            else:
                idx = 0
                yield self.players[idx]

            idx += 1

    def __repr__(self):
        return f'InfiniteLineup({self.players})'

    def __str__(self):
        return f"InfiniteLineup with the players: {', '.join(self.players)}"


astros = [
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]

full_lineup = InfiniteLineup(astros)
astros_lineup = full_lineup.lineup()

print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))

class Website:
  def __init__(self, title):
    self.title = title
  # This way instance atribute


ws = Website('My Website Title')
print(ws.__dict__)

ws_two = Website('My Second Title')
print(ws_two.__dict__)


class DifferentWebsite:
  title = 'My Class Title'
  # This way class atribute: a class attribute is an attribute that belongs to the class definition, it's hardcoded directly into the class

dw = DifferentWebsite()
print(dw.title)

dw_two = DifferentWebsite()
print(dw_two.title)

class User:
  def __init__(self, email, first_name, last_name):
    self.email = email
    self.first_name = first_name
    self.last_name = last_name

  def greeting(self):
    return f'Hi {self.first_name} {self.last_name}'

class AdminUser(User): # inheritance (to make sure if u want to use it, ask urself if adminuser is a type os user)
  def active_users(self):
    return '500'


tiffany = AdminUser('tiffany@devcamp.com', 'Tiffany', 'Hudgens')

kristine = User('kristine@devcamp.com', 'Kristine', 'Hudgens')

print(tiffany.active_users())
print(tiffany.greeting())
print(kristine.active_users())

class Html:
    def __init__(self, content):
        self.content = content

    def render(self):             
        raise NotImplementedError("Subclass must implement render method")


class Heading(Html):
    def render(self): # overwriting the render function, this way it it was not overriden it would have raises an error when called
        return f'<h1>{self.content}</h1>'


class Div(Html):
    def render(self):
        return f'<div>{self.content}</div>'


tags = [Div('Some content'), Heading('My Amazing Heading'), Div('Another div')]

for tag in tags:
    print(str(tag) + ': ' + tag.render())

class Heading:
    def __init__(self, content):
      self.content = content

    def render(self):
      return f'<h1>{self.content}</h1>'

class Div:
  def __init__(self, content):
    self.content = content

  def render(self):
    return f'<div>{self.content}</div>'

div_one = Div('Some content')
heading = Heading('My Amazing Heading')
div_two = Div('Another div')

def html_render(tag_object): # this is a polymophic function it doesnt know what type of object it is the input but if it has a render function inside it'll call it
  print(tag_object.render())

html_render(div_one)
html_render(div_two)
html_render(heading)

file_builder = open("logger.txt", "w+")

for i in range(1000):
    file_builder.write(f"I'm on line {i + 1}\n")


# file_builder.write("Hey, I'm in a file!")

file_builder.close()

import fnmatch
from fnmatch import fnmatchcase
import os

def list_files():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.txt'):
            print('Text files:', file)

        if fnmatch.fnmatch(file, '*.rb'):
            print('Ruby files:', file)

        if fnmatch.fnmatch(file, '*.yml'):
            print('Yaml files:', file)

        if fnmatch.fnmatch(file, '*.py'):
            print('Python files:', file)


list_files()

players = [
    "Jose Altuve 2B",
    "Carlos Correa SS",
    "Alex Bregman 3B",
    "Scooter Gennett 2B"
]

second_base_players = [player for player in players if fnmatchcase(player, "* 2B")]

print(second_base_players)