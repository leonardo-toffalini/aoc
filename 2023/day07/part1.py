with open('day7/input.txt', 'r') as f:
  players = f.readlines()

letter_map = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}

def classify_hand(hand):
  counts = [hand.count(card) for card in hand]
  if 5 in counts:
    return 6
  elif 4 in counts:
    return 5
  elif 3 in counts:
    if 2 in counts:
      return 4
    return 3
  elif counts.count(2) == 4:
    return 2
  elif 2 in counts:
    return 1
  else:
    return 0

def hand_strength(hand):
  return (classify_hand(hand), [letter_map.get(card, card) for card in hand])

plays = []
for player in players:
  hand, bid = player.split()
  plays.append((hand, int(bid)))

plays.sort(key = lambda play: hand_strength(play[0]))

total = 0

for rank, (_, bid) in enumerate(plays):
  # print(f'rank: {rank + 1}, bid: {bid}')
  total += (rank + 1) * bid

print(total)

