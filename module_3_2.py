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


inv = Invoice('Google', 500)
print(str(inv))