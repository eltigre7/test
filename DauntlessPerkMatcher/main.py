import itertools

from items_and_perks import attributes, items, itemSets

gear = items()
perks = attributes()

sets = itertools.product(gear.weapons, gear.helmets,
                         gear.chests, gear.gloves, gear.legs, gear.lanterns)

requirements = [
    'Iceborne', 'Iceborne',
    'Rage', 'Rage',
    'Wild Frenzy', 'Wild Frenzy',
    'Aetheric Attunement', 'Aetheric Attunement',
    'Energized', 'Energized',
    'Overpower', 'Overpower'
]

matches = []


def diff(list1, list2):

    for item in list2:
        if item in list1:
            list1.remove(item)
    return list1


for combination in sets:
    reqList = requirements.copy()

    try:

        tempSet = itemSets(combination[0], combination[1], combination[2],
                           combination[3], combination[4], combination[5])
        perkDiff = tempSet.perkDiff(reqList)
        slotDiff = [perks.perks[item] for item in perkDiff]
        slotDiff = tempSet.slotDiff(slotDiff)
        if not slotDiff:
            matches.append(tempSet)

    except:
        print('error')

print(len(matches))
for item in matches:
    item.printItems()
