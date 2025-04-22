import random
from django.shortcuts import render, redirect

# Create your views here.
player_position = 0
board_size = 20

def board(request):
	global player_position

	context = {
		'player_position' : player_position,
		'board_squares' : list(range(board_size)),
	}
	return render(request, 'candyland/board.html', context)

def move(request):
	global player_position
	move_spaces = random.randint(1, 3)
	player_position += move_spaces

	if player_position >= board_size:
		return redirect('win')
	else:
		return redirect('board')

def win(request):
	global player_position
	player_position = 0
	return render(request, 'candyland/win.html')