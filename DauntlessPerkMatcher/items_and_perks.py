'''
Created on Jul 18, 2019

@author: eltigre
'''

import sys


class attributes(object):
    '''
    classdocs
    '''

    def __init__(self):

        self.perks = {
            'Assassins Vigour': 'Defence',
            'Bloodless': 'Defence',
            'Fireproof': 'Defence',
            'Fortress': 'Defence',
            'Guardian': 'Defence',
            'Iceborne': 'Defence',
            'Insulated': 'Defence',
            'Nine Lives': 'Defence',
            'Shellshock Resist': 'Defence',
            'Sturdy': 'Defence',
            'Tough': 'Defence',
            'Warmth': 'Defence',
            'Agility': 'Mobility',
            'Conditioning': 'Mobility',
            'Endurance': 'Mobility',
            'Endurance': 'Mobility',
            'Evasion': 'Mobility',
            'Fleet Footed': 'Mobility',
            'Nimble': 'Mobility',
            'Swift': 'Mobility',
            'Aetherhunter': 'Power',
            'Deconstruction': 'Power',
            'Knockout King': 'Power',
            'Overpower': 'Power',
            'Pacifier': 'Power',
            'Rage': 'Power',
            'Ragehunter': 'Power',
            'Sharpened': 'Power',
            'Acidic': 'Technique',
            'Adrenaline': 'Technique',
            'Barbed': 'Technique',
            'Bladestorm': 'Technique',
            'Cunning': 'Technique',
            'Evasive Fury': 'Technique',
            'Merciless': 'Technique',
            'Molten': 'Technique',
            'Predator': 'Technique',
            'Savagery': 'Technique',
            'Weighted Strikes': 'Technique',
            'Wild Frenzy': 'Technique',
            'Aetherborne': 'Utility',
            'Aetheric Attunement': 'Utility',
            'Aetheric Frenzy': 'Utility',
            'Conduit': 'Utility',
            'Energized': 'Utility',
            'Lucent': 'Utility',
            'Medic': 'Utility',
            'Stunning Vigour': 'Utility',
            'Vampiric': 'Utility'
        }


class items(object):

    def __init__(self):

        self.weapons = [
            {
                'name': 'Gnasher',
                'armorPiece': 'sword',
                'perk': 'Ragehunter',
                'slot': 'Utility',
                'slot2': 'Defense'
            },
            {
                'name': 'Shrike',
                'armorPiece': 'sword',
                'perk': 'Conditioning',
                'slot': 'Mobility',
                'slot2': 'Mobility'
            },
            {
                'name': 'Quillshot',
                'armorPiece': 'sword',
                'perk': 'Acidic',
                'slot': 'Technique',
                'slot2': 'Defense'
            },
            {
                'name': 'Skarn',
                'armorPiece': 'sword',
                'perk': 'Knockout King',
                'slot': 'Power',
                'slot2': 'Defense'
            },
            {
                'name': 'Charrogg',
                'armorPiece': 'sword',
                'perk': 'Aetherhunter',
                'slot': 'Power',
                'slot2': 'Defense'
            },
            {
                'name': 'Embermane',
                'armorPiece': 'sword',
                'perk': 'Evasive Fury',
                'slot': 'Technique',
                'slot2': 'Mobility'
            },
            {
                'name': 'Skraev',
                'armorPiece': 'sword',
                'perk': 'Nimble',
                'slot': 'Technique',
                'slot2': 'Mobility'
            },
            {
                'name': 'Drask',
                'armorPiece': 'sword',
                'perk': 'Aetheric Attunement',
                'slot': 'Power',
                'slot2': 'Utility'
            },
            {
                'name': 'Nayzaga',
                'armorPiece': 'sword',
                'perk': 'Barbed',
                'slot': 'Utility',
                'slot2': 'Mobility'
            },
            {
                'name': 'Pangar',
                'armorPiece': 'sword',
                'perk': 'Knockout King',
                'slot': 'Power',
                'slot2': 'Defense'
            },
            {
                'name': 'Hellion',
                'armorPiece': 'sword',
                'perk': 'Overpower',
                'slot': 'Power',
                'slot2': 'Power'
            },
            {
                'name': 'Stormclaw',
                'armorPiece': 'sword',
                'perk': 'Energized',
                'slot': 'Technique',
                'slot2': 'Mobility'
            },
            {
                'name': 'Kharabak',
                'armorPiece': 'sword',
                'perk': 'Bladestorm',
                'slot': 'Technique',
                'slot2': 'Mobility'
            },
            {
                'name': 'Rezakiri',
                'armorPiece': 'sword',
                'perk': 'Cunning',
                'slot': 'Technique',
                'slot2': 'Utility'
            },
            {
                'name': 'Shrowd',
                'armorPiece': 'sword',
                'perk': 'Cunning',
                'slot': 'Power',
                'slot2': 'Utility'
            },
            {
                'name': 'Koshai',
                'armorPiece': 'sword',
                'perk': 'Sharpened',
                'slot': 'Power',
                'slot2': 'Utility'
            },
            {
                'name': 'Riftstalker',
                'armorPiece': 'sword',
                'perk': 'Wild Frenzy',
                'slot': 'Technique',
                'slot2': 'Utility'
            },
            {
                'name': 'Valomyr',
                'armorPiece': 'sword',
                'perk': 'Aetherhunter',
                'slot': 'Power',
                'slot2': 'Utility'
            },
            {
                'name': 'Boreus',
                'armorPiece': 'sword',
                'perk': 'Conditioning',
                'slot': 'Power',
                'slot2': 'Defense'
            },
            {
                'name': 'The Hunger',
                'armorPiece': 'sword',
                'perk': '',
                'slot': 'Power',
                'slot2': 'Utility'
            }
        ]

        self.helmets = [
            {
                'name': 'Gnasher',
                'armorPiece': 'helmet',
                'perk': 'Bloodless',
                'slot': 'Defence'
            },
            {
                'name': 'Shrike',
                'armorPiece': 'helmet',
                'perk': 'Evasion',
                'slot': 'Technique'
            },
            {
                'name': 'Quillshot',
                'armorPiece': 'helmet',
                'perk': 'Savagery',
                'slot': 'Defence'
            },
            {
                'name': 'Skarn',
                'armorPiece': 'helmet',
                'perk': 'Tough',
                'slot': 'Defence'
            },
            {
                'name': 'Charrogg',
                'armorPiece': 'helmet',
                'perk': 'Fireproof',
                'slot': 'Defence'
            },
            {
                'name': 'Embermane',
                'armorPiece': 'helmet',
                'perk': 'Evasive Fury',
                'slot': 'Mobility'
            },
            {
                'name': 'Skraev',
                'armorPiece': 'helmet',
                'perk': 'Fleet Footed',
                'slot': 'Mobility'
            },
            {
                'name': 'Drask',
                'armorPiece': 'helmet',
                'perk': 'Aetheric Attunement',
                'slot': 'Power'
            },
            {
                'name': 'Nayzaga',
                'armorPiece': 'helmet',
                'perk': 'Medic',
                'slot': 'Utility'
            },
            {
                'name': 'Pangar',
                'armorPiece': 'helmet',
                'perk': 'Knockout King',
                'slot': 'Power'
            },
            {
                'name': 'Hellion',
                'armorPiece': 'helmet',
                'perk': 'Ragehunter',
                'slot': 'Technique'
            },
            {
                'name': 'Stormclaw',
                'armorPiece': 'helmet',
                'perk': 'Energized',
                'slot': 'Technique'
            },
            {
                'name': 'Kharabak',
                'armorPiece': 'helmet',
                'perk': 'Shellshock Resist',
                'slot': 'Mobility'
            },
            {
                'name': 'Rezakiri',
                'armorPiece': 'helmet',
                'perk': 'Conduit',
                'slot': 'Technique'
            },
            {
                'name': 'Shrowd',
                'armorPiece': 'helmet',
                'perk': 'Rage',
                'slot': 'Power'
            },
            {
                'name': 'Koshai',
                'armorPiece': 'helmet',
                'perk': 'Agility',
                'slot': 'Technique'
            },
            {
                'name': 'Riftstalker',
                'armorPiece': 'helmet',
                'perk': 'Aetheric Attunement',
                'slot': 'Utility'
            },
            {
                'name': 'Valomyr',
                'armorPiece': 'helmet',
                'perk': 'Lucent',
                'slot': 'Power'
            },
            {
                'name': 'Boreus',
                'armorPiece': 'helmet',
                'perk': 'Conditioning',
                'slot': 'Utility'
            },
            {
                'name': 'Prismatic Grace',
                'armorPiece': 'helmet',
                'perk': '',
                'slot': 'Technique'
            },
            {
                'name': 'Tragic Echo',
                'armorPiece': 'helmet',
                'perk': '',
                'slot': 'Power'
            },
            {
                'name': 'The Skullforge',
                'armorPiece': 'helmet',
                'perk': '',
                'slot': 'Defence'
            }
        ]
        self.chests = [
            {
                'name': 'Gnasher',
                'armorPiece': 'chest',
                'perk': 'Tough',
                'slot': 'Defence'
            },
            {
                'name': 'Shrike',
                'armorPiece': 'chest',
                'perk': 'Evasion',
                'slot': 'Mobility'
            },
            {
                'name': 'Quillshot',
                'armorPiece': 'chest',
                'perk': 'Savagery',
                'slot': 'Technique'
            },
            {
                'name': 'Skarn',
                'armorPiece': 'chest',
                'perk': 'Guardian',
                'slot': 'Defence'
            },
            {
                'name': 'Charrogg',
                'armorPiece': 'chest',
                'perk': 'Aetherhunter',
                'slot': 'Utility'
            },
            {
                'name': 'Embermane',
                'armorPiece': 'chest',
                'perk': 'Evasive Fury',
                'slot': 'Mobility'
            },
            {
                'name': 'Skraev',
                'armorPiece': 'chest',
                'perk': 'Adrenaline',
                'slot': 'Mobility'
            },
            {
                'name': 'Drask',
                'armorPiece': 'chest',
                'perk': 'Aetheric Attunement',
                'slot': 'Power'
            },
            {
                'name': 'Nayzaga',
                'armorPiece': 'chest',
                'perk': 'Medic',
                'slot': 'Defence'
            },
            {
                'name': 'Pangar',
                'armorPiece': 'chest',
                'perk': 'Fortress',
                'slot': 'Power'
            },
            {
                'name': 'Hellion',
                'armorPiece': 'chest',
                'perk': 'Molten',
                'slot': 'Technique'
            },
            {
                'name': 'Stormclaw',
                'armorPiece': 'chest',
                'perk': 'Energized',
                'slot': 'Mobility'
            },
            {
                'name': 'Kharabak',
                'armorPiece': 'chest',
                'perk': 'Bladestorm',
                'slot': 'Technique'
            },
            {
                'name': 'Rezakiri',
                'armorPiece': 'chest',
                'perk': 'Cunning',
                'slot': 'Utility'
            },
            {
                'name': 'Shrowd',
                'armorPiece': 'chest',
                'perk': 'Rage',
                'slot': 'Power'
            },
            {
                'name': 'Koshai',
                'armorPiece': 'chest',
                'perk': 'Predator',
                'slot': 'Utility'
            },
            {
                'name': 'Riftstalker',
                'armorPiece': 'chest',
                'perk': 'Conduit',
                'slot': 'Utility'
            },
            {
                'name': 'Valomyr',
                'armorPiece': 'chest',
                'perk': 'Nine Lives',
                'slot': 'Power'
            },
            {
                'name': 'Boreus',
                'armorPiece': 'chest',
                'perk': 'Rage',
                'slot': 'Defence'
            }


        ]
        self.gloves = [
            {
                'name': 'Gnasher',
                'armorPiece': 'gloves',
                'perk': 'Ragehunter',
                'slot': 'Power'
            },
            {
                'name': 'Shrike',
                'armorPiece': 'gloves',
                'perk': 'Weighted Strikes',
                'slot': 'Mobility'
            },
            {
                'name': 'Quillshot',
                'armorPiece': 'gloves',
                'perk': 'Barbed',
                'slot': 'Technique'
            },
            {
                'name': 'Skarn',
                'armorPiece': 'gloves',
                'perk': 'Fortress',
                'slot': 'Defence'
            },
            {
                'name': 'Charrogg',
                'armorPiece': 'gloves',
                'perk': 'Rage',
                'slot': 'Utility'
            },
            {
                'name': 'Embermane',
                'armorPiece': 'gloves',
                'perk': 'Fireproof',
                'slot': 'Technique'
            },
            {
                'name': 'Skraev',
                'armorPiece': 'gloves',
                'perk': 'Warmth',
                'slot': 'Mobility'
            },
            {
                'name': 'Drask',
                'armorPiece': 'gloves',
                'perk': 'Sharpened',
                'slot': 'Utility'
            },
            {
                'name': 'Nayzaga',
                'armorPiece': 'gloves',
                'perk': 'Aetheric Attunement',
                'slot': 'Utility'
            },
            {
                'name': 'Pangar',
                'armorPiece': 'gloves',
                'perk': 'Knockout King',
                'slot': 'Defence'
            },
            {
                'name': 'Hellion',
                'armorPiece': 'gloves',
                'perk': 'Molten',
                'slot': 'Power'
            },
            {
                'name': 'Stormclaw',
                'armorPiece': 'gloves',
                'perk': 'Insulated',
                'slot': 'Mobility'
            },
            {
                'name': 'Kharabak',
                'armorPiece': 'gloves',
                'perk': 'Conditioning',
                'slot': 'Mobility'
            },
            {
                'name': 'Rezakiri',
                'armorPiece': 'gloves',
                'perk': 'Conduit',
                'slot': 'Technique'
            },
            {
                'name': 'Shrowd',
                'armorPiece': 'gloves',
                'perk': 'Medic',
                'slot': 'Utility'
            },
            {
                'name': 'Koshai',
                'armorPiece': 'gloves',
                'perk': 'Evasive Fury',
                'slot': 'Power'
            },
            {
                'name': 'Riftstalker',
                'armorPiece': 'gloves',
                'perk': 'Evasion',
                'slot': 'Mobility'
            },
            {
                'name': 'Valomyr',
                'armorPiece': 'gloves',
                'perk': 'Lucent',
                'slot': 'Defence'
            },
            {
                'name': 'Boreus',
                'armorPiece': 'gloves',
                'perk': 'Rage',
                'slot': 'Power'
            }
        ]
        self.legs = [
            {
                'name': 'Gnasher',
                'armorPiece': 'legs',
                'perk': 'Tough',
                'slot': 'Power'
            },
            {
                'name': 'Shrike',
                'armorPiece': 'legs',
                'perk': 'Bloodless',
                'slot': 'Mobility'
            },
            {
                'name': 'Quillshot',
                'armorPiece': 'legs',
                'perk': 'Shellshock Resist',
                'slot': 'Technique'
            },
            {
                'name': 'Skarn',
                'armorPiece': 'legs',
                'perk': 'Guardian',
                'slot': 'Defence'
            },
            {
                'name': 'Charrogg',
                'armorPiece': 'legs',
                'perk': 'Rage',
                'slot': 'Power'
            },
            {
                'name': 'Embermane',
                'armorPiece': 'legs',
                'perk': 'Evasion',
                'slot': 'Defence'
            },
            {
                'name': 'Skraev',
                'armorPiece': 'legs',
                'perk': 'Adrenaline',
                'slot': 'Utility'
            },
            {
                'name': 'Drask',
                'armorPiece': 'legs',
                'perk': 'Fleet Footed',
                'slot': 'Utility'
            },
            {
                'name': 'Nayzaga',
                'armorPiece': 'legs',
                'perk': 'Insulated',
                'slot': 'Defence'
            },
            {
                'name': 'Pangar',
                'armorPiece': 'legs',
                'perk': 'Warmth',
                'slot': 'Defence'
            },
            {
                'name': 'Hellion',
                'armorPiece': 'legs',
                'perk': 'Fortress',
                'slot': 'Power'
            },
            {
                'name': 'Stormclaw',
                'armorPiece': 'legs',
                'perk': 'Aetheric Frenzy',
                'slot': 'Mobility'
            },
            {
                'name': 'Kharabak',
                'armorPiece': 'legs',
                'perk': 'Conditioning',
                'slot': 'Power'
            },
            {
                'name': 'Rezakiri',
                'armorPiece': 'legs',
                'perk': 'Agility',
                'slot': 'Mobility'
            },
            {
                'name': 'Shrowd',
                'armorPiece': 'legs',
                'perk': 'Nine Lives',
                'slot': 'Utility'
            },
            {
                'name': 'Koshai',
                'armorPiece': 'legs',
                'perk': 'Predator',
                'slot': 'Utility'
            },
            {
                'name': 'Riftstalker',
                'armorPiece': 'legs',
                'perk': 'Conduit',
                'slot': 'Mobility'
            },
            {
                'name': 'Valomyr',
                'armorPiece': 'legs',
                'perk': 'Aetherhunter',
                'slot': 'Utility'
            },
            {
                'name': 'Boreus',
                'armorPiece': 'legs',
                'perk': 'Iceborne',
                'slot': 'Technique'
            }
        ]
        self.lanterns = [
            {
                'name': 'Lantern',
                'armorPiece': 'lantern',
                'perk': '',
                'slot': 'Utility'
            }
        ]


class itemSets(object):

    def getSetPerks(self, weapon, helmet, chest, gloves, legs, lantern):
        setPerks = []
        setPerks.append(weapon['perk'])
        setPerks.append(helmet['perk'])
        setPerks.append(chest['perk'])
        setPerks.append(gloves['perk'])
        setPerks.append(legs['perk'])
        setPerks.append(lantern['perk'])

        return setPerks

    def getSetSlots(self, weapon, helmet, chest, gloves, legs, lantern):
        setSlots = []
        setSlots.append(weapon['slot'])
        setSlots.append(weapon['slot2'])
        setSlots.append(helmet['slot'])
        setSlots.append(chest['slot'])
        setSlots.append(gloves['slot'])
        setSlots.append(legs['slot'])
        setSlots.append(lantern['slot'])

        return setSlots

    def __init__(self, weapons, helmets, chests, gloves, legs, lantern):
        self.weapon = weapons
        self.helmet = helmets
        self.chest = chests
        self.gloves = gloves
        self.legs = legs
        self.lantern = lantern

        self.setPerks = self.getSetPerks(
            weapons, helmets, chests, gloves, legs, lantern)
        self.setSlots = self.getSetSlots(
            weapons, helmets, chests, gloves, legs, lantern)

    def printItems(self):
        print(self.weapon['name'], self.weapon['armorPiece'], end='\t')
        print(self.helmet['name'], self.helmet['armorPiece'], end='\t')
        print(self.chest['name'], self.chest['armorPiece'], end='\t')
        print(self.gloves['name'], self.gloves['armorPiece'], end='\t')
        print(self.legs['name'], self.legs['armorPiece'], end='\t')
        print(self.lantern['name'], self.lantern['armorPiece'])

    def perkDiff(self, reqPerks):
        for item in self.setPerks:
            if item in reqPerks:
                reqPerks.remove(item)
        return reqPerks

    def slotDiff(self, reqSlots):
        for item in self.setSlots:
            if item in reqSlots:
                reqSlots.remove(item)
        return reqSlots
