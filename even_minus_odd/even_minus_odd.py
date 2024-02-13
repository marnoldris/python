#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:53:26 2023

@author: matthew
"""

import dice as d
import sys

#%% Initial variables
# Initialize some variables
num_tokens = 21
scores = {
    'player 1': 0,
    'player 2': 0,
    }
dice_list = [d.Dice(6) for i in range(6)]
yes_values = ['y', '', 'yes']
current_player = 'player 1'

#%% Functions
def score() -> int:
    evens = 0
    odds = 0
    for dice in dice_list:
        # Check for even values
        if dice.get_value() % 2 == 0:
            evens += dice.get_value()
        else:
            odds += dice.get_value()
    # Find the difference
    roll_score = evens - odds
    return roll_score

def game_over_check() -> None:
    if num_tokens <= 0:
        if scores['player 1'] > scores['player 2']:
            winner = 'player 1'
        else:
            winner = 'player 2'
        print(f'Game over! {winner.title()} wins!')
        sys.exit()
    else:
        print(f'There are {num_tokens} tokens remaining.')

#%% Main gameplay loop
while True:
    #%%% Ask to play
    print(f'{current_player.title()}, would you like to play? (Y/n)')
    play = input('> ').lower()
    if play in yes_values:
        #%%% Roll the dice
        print(f'Rolling the dice for {current_player.title()}...')
        for dice in dice_list:
            print(f'You rolled a {dice.roll()}')
        #%%% Score the roll
        player_roll = score()
        print(f'You rolled a score of {player_roll}')
        #%%% Adjust player scores
        if player_roll >= 0:
            # if there are enough tokens to pay for it
            if player_roll <= num_tokens:
                scores[current_player] += player_roll
                num_tokens -= player_roll
            else:
                scores[current_player] += num_tokens
                num_tokens = 0
        else:
            # player_roll is already negative so we add it
            net_value = scores[current_player] + player_roll
            if net_value >= 0:
                scores[current_player] += player_roll
                num_tokens -= player_roll
            else:
                # We know that the player's score is insufficient
                # so we take all of their tokens and set
                # their score to 0.
                num_tokens += scores[current_player]
                scores[current_player] = 0
        print(f'{current_player.title()}\'s score is {scores[current_player]}')
    else:
        print('Okay, quitting...')
        sys.exit()
    game_over_check()
    #%%% Switch players
    if current_player == 'player 1':
        current_player = 'player 2'
    else:
        current_player = 'player 1'
