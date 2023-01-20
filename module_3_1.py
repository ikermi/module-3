positions = ['2b', '3b', 'ss', 'dh']
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

scoreboard = zip(positions, players)

print(list(scoreboard))

# sets
tags = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

print(tags)

query_one = 'python' in tags
query_two = 'ruby' in tags

print(query_one)
print(query_two)

tags_one = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

tags_two = {
  'ruby',
  'coding',
  'tutorials',
  'development'
}

# merged tags
merged_tags = tags_one | tags_two
print(merged_tags)

# tags in tags_one but not in tags_two
exclusive_to_tag_one = tags_one - tags_two
print(exclusive_to_tag_one)

# tags in tags_two but not in tags_one
exclusive_to_tag_two =  tags_two - tags_one
print(exclusive_to_tag_two)

# tags found in both tags_one and tags_two
universal_tags = tags_one & tags_two
print(universal_tags)

# loops
players = {
  '2b': 'Altuve',
  '3b': 'Bregman',
  'ss': 'Correa',
  'dh': 'Gattis'
}

for position, player in players.items():
  print('Position', position)
  print('Player', player)

  usernames = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

for username in usernames:
  if username == 'cersei':
    print(f'Sorry, {username}, you are not allowed')
    continue
  else:
    print(f'{username} is allowed')

for username in usernames:
  if username == 'cersei':
    print(f'Sorry, {username}, you are not allowed')
  else:
    print(f'{username} is allowed')


num_list = range(1, 11)
even_numbers = [num for num in num_list if num % 2 == 0]

# ternary operators
role = 'guest'

auth = 'can access' if role == 'admin' else 'cannot access'

nums = [1, 2, 3, 4]

if 3 in nums:
    print('The number was found')
else:
    print('The number was not found')