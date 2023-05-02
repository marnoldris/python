#!/usr/bin/python

import shutil
import pyperclip

def print_columns(string_list, width=shutil.get_terminal_size().columns):
    max_length = len(max(string_list, key=len)) + 4
    num_columns = width // (max_length)
    for i in range(0, len(string_list), num_columns):
        for s in string_list[i:i+num_columns]:
            print('{:<{}}'.format(s, max_length), end='')
        print()

def copy_columns(string_list, width=shutil.get_terminal_size().columns):
    max_length = len(max(string_list, key=len)) + 4
    num_columns = width // (max_length)
    formatted_strings = []

    for i in range(0, len(string_list), num_columns):
        formatted_row = ['{:<{}}'.format(s, max_length) for s in string_list[i:i+num_columns]]
        formatted_strings.append(''.join(formatted_row))

    output = '\n'.join(formatted_strings)

    print(output, end='\n\n')
    pyperclip.copy(output)
    print(f'{len(string_list)} card names copied to clipboard...')
    

decklist = [
    'Conduit of Worlds',
    'Scaretiller',
    'Unlicensed Hearse',
    'Seedborn Muse',
    'Tribute to the World Tree',
    'Emmara, Soul of the Accord',
    'Enhanced Surveillance',
    'Drumbellower',
    'Armored Scrapgorger',
    'Sevinne\'s Reclamation',
    'Noble Heirarch',
    'Fallowsage',
    'Quest for Renewal',
    'Order of Whiteclay',
    'Thrummingbird',
    'Unctus, Grand Metatect',
    'Swords to Plowshares',
    'Eternal Witness',
    'Vanish into Eternity',
    'White Sun\'s Twilight (mites?)',
    'Mite Overseer',
    'Skrelv\'s Hive',
    'Norn\'s Wellspring',
    'Ossification',
    'Soul Partition',
    'Reckoner Bankbuster',
    'Staff of Domination',
    'Thousand-year Elixir',
    'Halo Fountain',
    'Shorikai, Genesis Engine',
    'Perennial Behemoth',
    'Haywire Mite',
    'Surgespanner',
    'Ramunap Excavator',
    'Emry, Lurker of the Loch',
    'Strongbrook Schoolmaster',
    'Leadership Vacuum',
    'The Reality Chip',
    'Foundry Inspector',
    'Sun Titan',
    'Sai, Master Thopterist',
    'Eladamri\'s Call',
    'Colossal Skyturtle',
    'Metalwork Colossus',
    ]

copy_columns(decklist, 79)
