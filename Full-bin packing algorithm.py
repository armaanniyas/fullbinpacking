items = [8, 7, 14, 9, 6, 9, 5, 15, 6, 7, 8]
bin_height = 20
bins = 0

def highest(list):
  largestNum = 0
  for item in list:
      if item > largestNum:
        largestNum = item
  return largestNum
def packing(target, list):
  smallestDiff = bin_height
  for item in list:
    diff = target - item
    if diff < smallestDiff and diff >= 0:
      smallestDiff = diff
      store = item
  return store
def listCheck():
  count = 0
  possible = False

  for item in items:
    if item <= remainder:
      count = count + 1

  if count > 0:
    possible = True

  return possible

while len(items) > 0:
  tempBin = []
  bins = bins + 1
  
  largest = highest(items)
  tempBin.append(largest)
  items.remove(largest)
  remainder = bin_height - largest
  
  possible = listCheck()
  
  while remainder != 0 and possible:
    partner = packing(remainder, items)
    tempBin.append(partner)
    items.remove(partner)
    remainder = remainder - partner
    possible = listCheck()
  
  print('Bin', bins, ':', tempBin)