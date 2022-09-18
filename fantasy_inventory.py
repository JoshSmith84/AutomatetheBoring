# Automate the boring Stuff chapter 5 practice Project -
# Fantasy Game Inventory - answer.
# Author: Josh Smith


def displayInventory(inventory: dict) -> None:
    """Take input Dictionary and output inventory like a game.
    Input Dictionary should contain keys with all integers as values.
     However, the function is coded to return an error if that is not the case,
     and remove the incorrect item.
     :param: Dictionary or items and item amounts to display
     """
    print("Inventory:")
    item_total = 0
    for k, v in list(inventory.items()):
        # FILL THIS PART IN
        if isinstance(v, int):
            print(f'{v} {k}')
            item_total += v
        else:
            print(f'Error. Unable to display {k} amount. '
                  f'It is not a valid integer.'
                  f' Removing {k} from inventory.')
            inventory.pop(k)
    print(f'Total number of items: {item_total}.\n')


def add_inventory(a: dict, b: list) -> dict:
    """Take existing dictionary of items and use a list to add items.
    If items already exist in inventory, increase the count.

    :param: dictionary as it is before addition of loot
    :param: List of items to add
    :return: Updated inventory
    """
    for item in b:
        a.setdefault(item, 0)
        a[item] = a[item] + 1
    return a


# code to test functions
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12,
         'spam': 'four'}

displayInventory(stuff)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
add_inventory(stuff, dragonLoot)

displayInventory(stuff)

# Functions tested and working with some extra credit improvements
