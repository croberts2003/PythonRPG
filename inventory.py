TYPE = ''
DESCRIPTION = ''
MELEE = 0
RANGE = 0
MAGIC = 0
SPEED = 0
SELL = 0
BUY = 0

def player_inventory():
    items = {
        'club': {
            TYPE: 'melee',
            DESCRIPTION: 'Club: A rough-hewn log, perfect for bashing heavily armored monsters.',
            MELEE: 2,
            RANGE: 0.5,
            MAGIC: 0.25,
            SPEED: 1,
            SELL: 10,
            BUY: 15
        },
        'sabre': {
            TYPE: 'melee',
            DESCRIPTION: 'Sabre: A thin bladed sword capable of fast striking smaller, quicker monsters.',
            MELEE: 1,
            RANGE: 0.75,
            MAGIC: 0.1,
            SPEED: 2,
            SELL: 10,
            BUY: 15
        },
        'knives': {
            TYPE: 'melee',
            DESCRIPTION: 'Knives: An assortment of small blades fit for slashing and throwing.',
            MELEE: 0.5,
            RANGE: 2,
            MAGIC: 0.5,
            SPEED: 2.5,
            SELL: 10,
            BUY: 15
        }
    }

    return items
