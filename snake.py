import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

HIGH_SCORE_FILE = 'highscore.txt'

def read_high_score():
    try:
        with open(HIGH_SCORE_FILE, 'r') as f:
            return int(f.read().strip())
    except:
        return 0

def write_high_score(score):
    with open(HIGH_SCORE_FILE, 'w') as f:
        f.write(str(score))

# Initialize the screen
curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

key = KEY_RIGHT
score = 0
lives = 3
level = 1
multiplier = 1
high_score = read_high_score()

snake = [[4, 10], [4, 9], [4, 8]]
food = [10, 20]
obstacles = []  # Define the obstacles list here

def place_food():
    food = None
    while food is None:
        nf = [randint(1, 18), randint(1, 58)]
        food = nf if nf not in snake and nf not in obstacles else None
    return food

def generate_obstacle(obstacles):
    obstacle = None
    while obstacle is None:
        new_obstacle = [randint(1, 18), randint(1, 58)]
        if new_obstacle not in snake and new_obstacle != food and new_obstacle not in obstacles:
            obstacle = new_obstacle
    return obstacle

# Initial obstacles
obstacles = [generate_obstacle(obstacles) for _ in range(3)]
for obs in obstacles:
    win.addch(obs[0], obs[1], 'X')

win.addch(food[0], food[1], '#')

while key != 27:  # While Esc key is not pressed
    win.border(0)
    win.addstr(0, 2, 'Score : ' + str(score) + ' ')
    win.addstr(0, 20, 'Lives : ' + str(lives) + ' ')
    win.addstr(0, 30, 'Level : ' + str(level) + ' ')
    win.addstr(0, 40, 'Multiplier : ' + str(multiplier) + ' ')
    win.addstr(0, 50, 'High Score : ' + str(high_score) + ' ')
    win.timeout(150 - (len(snake) // 5 + len(snake) // 10) % 120)

    prev_key = key
    event = win.getch()
    key = key if event == -1 else event

    if key == ord(' '):  # Pause the game
        key = -1
        while key != ord(' '):
            key = win.getch()
        key = prev_key
        continue

    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:
        key = prev_key

    new_head = [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1),
                snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)]

    if new_head[0] == 0: new_head[0] = 18
    if new_head[1] == 0: new_head[1] = 58
    if new_head[0] == 19: new_head[0] = 1
    if new_head[1] == 59: new_head[1] = 1

    if new_head in snake[1:] or new_head in obstacles:  # Check for collisions
        break  # Terminate the game immediately

    snake.insert(0, new_head)

    if snake[0] == food:  # Check if snake eats the food
        score += 10 * multiplier
        if score > high_score:
            high_score = score
        if score % 100 == 0:
            level += 1
            multiplier += 1

        food = place_food()
        win.addch(food[0], food[1], '#')
        
        # Generate a new obstacle
        new_obstacle = generate_obstacle(obstacles)
        obstacles.append(new_obstacle)
        win.addch(new_obstacle[0], new_obstacle[1], 'X')
    else:
        tail = snake.pop()
        win.addch(tail[0], tail[1], ' ')

    win.addch(snake[0][0], snake[0][1], '*')

curses.endwin()
if score > high_score:
    write_high_score(high_score)
print("\nGame Over!")
print("Score:", score)
print("High Score:", high_score)
print("Level:", level)
print("Multiplier:", multiplier)
