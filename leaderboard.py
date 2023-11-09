import pprint
from chessdotcom import get_leaderboards, get_player_stats

# pprint shows data, especially API data in a readable format
#printer = pprint.PrettyPrinter()
#printer.pprint(get_leaderboards().json)

def print_category_leaderboard():
  data = get_leaderboards().json
  categories = data.keys()

  #asking the user to input the category to print
  print('Which category leaderboard would you like to see?')
  for category in categories:
    print(category)
  selected_category = input()

  if selected_category in categories:
    # printing the leaderboard
    for index, item in enumerate(data[selected_category]):
      print(f"Rank: {index + 1} | Name: {item['name']} | Rating: {item['score']}")

def get_player_rating():
  #asking the user for a player's name
  print('Which player\'s stats would you like to see?')
  selected_player = input()

  try:
    data = get_player_stats(selected_player).json
  except:
    print('Player not found.')
    return
  else:
    categories = ['chess_blitz', 'chess_rapid', 'chess_bullet']
    for category in categories:
      print(f"Category: {category} | Current Rating: {data[category]['last']['rating']}")

print_category_leaderboard()
get_player_rating()