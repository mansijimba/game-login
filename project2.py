
from customtkinter import*
from PIL import Image,ImageTk
import tkinter.messagebox as m
import sqlite3
import pygame
import sys
import time
import random
import threading

#connecting with database 
conn=sqlite3.connect('SIGN.db')
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(username TEXT NOT NULL,password TEXT NOT NULL)""")


def login():
    if Userentry.get() == '' or passwordentry.get() == '':
        m.showerror('Error', 'ALL DATA ARE REQUIRED')
    else:
        cursor.execute('SELECT password FROM users WHERE username=?', [Userentry.get()])
        stored_password = cursor.fetchone()
        if stored_password is None:
            m.showerror('Error', 'Invalid username')
            Userentry.delete(0, END)
        elif stored_password[0] != passwordentry.get():
            m.showerror('Error', 'Incorrect password')
            passwordentry.delete(0, END)
        else:
            m.showinfo('Success', 'Logged in successfully')

            Userentry.delete(0, END)
            passwordentry.delete(0, END)
            window.focus()

            window.destroy()

            launch_game_window()
        

def register():
    if Userentry.get() == '' or passwordentry.get() == '':
        m.showerror('Error', 'ALL DATA ARE REQUIRED')
    else:
        cursor.execute('SELECT username FROM users WHERE username=?', [Userentry.get()])
        existing_username = cursor.fetchone()
        if existing_username is not None:
            m.showerror('Error', 'Username already exists')
            Userentry.delete(0, END)
        else:
            cursor.execute('INSERT INTO users(username, password) VALUES(?, ?)',
                           [Userentry.get(), passwordentry.get()])
            conn.commit()
            m.showinfo('Success', 'Registration is successful')
            right_move()
            Userentry.delete(0, END)
            passwordentry.delete(0, END)
            window.focus()


def left_move():
    topframe.place(x=40,y=30)
    headingLabel.configure(text='Sign up')
    innerbutton.configure(text='Sign up')
    
def right_move():
    topframe.place(x=255, y=30)
    headingLabel.configure(text='Log in')
    innerbutton.configure(text='Log in', command=login)


#create an application window
window=CTk()
window.title("Registration and Login page")
window.geometry("550x500")
window.resizable(0,0)

#creating main frame for the window
mainframe=CTkFrame(window,fg_color='yellow green',width=500,height=450)
mainframe.grid(row=0,column=0,padx=20,pady=28)
 
#create log in button
Login_but=CTkButton(mainframe,text='Login',fg_color='yellow green',font=('arial',20,'bold'),
                    border_color='forest green',border_width=2,hover_color='forest green',command=right_move)
Login_but.place(x=330,y=377)

#create sign up button
Sign_but=CTkButton(mainframe,text='Sign up',fg_color='yellow green',font=("arial",20,"bold"),
                   border_color="forest green",border_width=2,hover_color="forest green",command=left_move)
Sign_but.place(x=30,y=377)

#create frame
topframe=CTkFrame(window,fg_color='white',width=290,height=480)
topframe.place(x=40,y=30)

#setting image as logo
logo=CTkImage(light_image=Image.open('log-in.png'),size=(80,80))
logoLabel=CTkLabel(topframe,image=logo,text=' ')
logoLabel.grid(row=0,column=0,pady=(30,0))

#creating textbox labels and entry boxes
headingLabel=CTkLabel(topframe,text='Sign up',font=('arial',36,'bold'),text_color="forest green")
headingLabel.grid(row=1,column=0,pady=(30,0))
Userentry=CTkEntry(topframe,font=('arial',20,'bold'),width=180,height=30,placeholder_text='username')
Userentry.grid(row=2,column=0,padx=20,pady=(20,30))
passwordentry=CTkEntry(topframe,font=('arial',20,'bold'),width=180,height=30,placeholder_text='password',show='*')
passwordentry.grid(row=3,column=0,padx=30,pady=(0,20))

#Creating innerbutton for sign up
innerbutton=CTkButton(topframe,text='Sign up',fg_color='forest green',font=('arial',25,'bold'),
                      hover_color="yellow green",cursor='hand2',command=register)
innerbutton.grid(row=4,column=0,pady=(30))


def launch_game_window():
    root=CTk()
    root.geometry("710x480")
    root.resizable(0,0)
    root.config(bg="lavenderblush2")

    def game_destroy():
        game_thread= threading.Thread(target=game) #Create the thread for the game
        game_thread.start()
        root.destroy() 

    img0 = Image.open("text.png")
    img1 = Image.open("start_btn.png")
    img2 = Image.open("exit_btn.png")

    resized_img0 = img0.resize((250, 120), Image.ANTIALIAS)
    resized_img1 = img1.resize((130, 90), Image.ANTIALIAS)
    resized_img2 = img2.resize((130, 90), Image.ANTIALIAS)

    img0_obj= ImageTk.PhotoImage(resized_img0)
    button_header = CTkLabel(root, image=img0_obj, text=" ")
    button_header.place(x = 270, y = 10)


    img1_obj = ImageTk.PhotoImage(resized_img1)
    img2_obj = ImageTk.PhotoImage(resized_img2)

    button1 = CTkButton(root, image=img1_obj, command=game_destroy, text=" ")
    button1.place(x=105, y=210)
    button2 = CTkButton(root, image=img2_obj, text=" ",command=root.destroy)
    button2.place(x=490, y=210)

    root.mainloop()

def launch_game():
    game()


def game():
    #Difficulty settings
    #Easy      ->  5
    #Medium    ->  8
    #Hard      ->  15
    #Harder    ->  20
    #Impossible->  50
    difficulty = 10

    # Window size
    frame_size_x = 840
    frame_size_y = 550

    # Checks for errors encountered
    check_errors = pygame.init()
    # pygame.init() example output -> (6, 0)
    # second number in tuple gives number of errors
    if check_errors[1] > 0:
        print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
        sys.exit(-1)
    else:
        print('[+] Game successfully initialised')



    # Initialise game window
    pygame.display.set_caption('Hungry Snake')
    game_window = pygame.display.set_mode((frame_size_x, frame_size_y))


    # Colors (R, G, B)
    black = pygame.Color(238,238,224)
    white = pygame.Color(218,165,32)
    red = pygame.Color(139,26,26)
    darkseagreen = pygame.Color(105,139,105)
    blue = pygame.Color(0, 0, 255)


    # FPS (frames per second) controller
    fps_controller = pygame.time.Clock()


    # Game variables
    snake_pos = [100, 50]
    snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

    food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
    food_spawn = True

    direction = 'RIGHT'
    change_to = direction

    score = 0


    # Game Over
    def game_over():
        my_font = pygame.font.SysFont('times new roman', 90)
        game_over_surface = my_font.render('YOU DIED', True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
        game_window.fill(black)
        game_window.blit(game_over_surface, game_over_rect)
        show_score(0, red, 'times', 20)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()


    # Score
    def show_score(choice, color, font, size):
        global score_rect
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(score), True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (frame_size_x/10, 15)
        else:
            score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
        game_window.blit(score_surface, score_rect)
        # pygame.display.flip()


    # Main logic
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Whenever a key is pressed down
            elif event.type == pygame.KEYDOWN:
                # W -> Up; S -> Down; A -> Left; D -> Right
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'
                # Esc -> Create event to quit the game
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        # Making sure the snake cannot move in the opposite direction instantaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        # Snake body growing mechanism
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        # Spawning food on the screen
        if not food_spawn:
            food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
        food_spawn = True
        # GFX
        game_window.fill(black)
        for pos in snake_body:
            # Snake body
            # .draw.rect(play_surface, color, xy-coordinate)
            # xy-coordinate -> .Rect(x, y, size_x, size_y)
            pygame.draw.rect(game_window, darkseagreen, pygame.Rect(pos[0], pos[1], 10, 10))\

        # Snake food
        pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        # Game Over conditions
        # Getting out of bounds
        if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
            game_over()
        if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
            game_over()
        # Touching the snake body
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over()

        show_score(1, white, 'consolas', 20)
        # Refresh game screen
        pygame.display.update()
        # Refresh rate
        fps_controller.tick(difficulty)

window.mainloop()


# def launch_game_window():
#     root=CTk()
#     root.geometry("710x480")
#     root.resizable(0,0)
#     root.config(bg="lavenderblush2")

#     def game_destroy():
#         game_thread= threading.Thread(target=game) #Create the thread for the game
#         game_thread.start()
#     root.destroy() 

#     img0 = Image.open("text.png")
#     img1 = Image.open("start_btn.png")
#     img2 = Image.open("exit_btn.png")

#     resized_img0 = img0.resize((250, 120), Image.ANTIALIAS)
#     resized_img1 = img1.resize((130, 90), Image.ANTIALIAS)
#     resized_img2 = img2.resize((130, 90), Image.ANTIALIAS)

#     img0_obj= ImageTk.PhotoImage(resized_img0)
#     button_header = CTkLabel(root, image=img0_obj, text=" ")
#     button_header.place(x = 270, y = 10)


#     img1_obj = ImageTk.PhotoImage(resized_img1)
#     img2_obj = ImageTk.PhotoImage(resized_img2)

#     button1 = CTkButton(root, image=img1_obj, command=game_destroy, text=" ")
#     button1.place(x=105, y=210)
#     button2 = CTkButton(root, image=img2_obj, text=" ",command=root.destroy)
#     button2.place(x=490, y=210)

#     root.mainloop()

# def launch_game():
#     game()
