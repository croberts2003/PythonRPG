from inventory import player_inventory, TYPE, DESCRIPTION, MELEE, RANGE, MAGIC, SPEED, SELL, BUY

def merchant():
    items = player_inventory()
    i = 1
    for item in items:
        item = items[item]
        print(str(i) + '. ' + str(item[DESCRIPTION]))
        i = i + 1

merchant()
