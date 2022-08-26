from tkinter import *
import random

root = Tk()
root.title("Lucky Friend Wheel")
root.geometry("600x600")
root.configure(background="red")

enter_word = Entry(root)
enter_word.place(relx=0.5 , rely=0.2 , anchor=CENTER)

friend_list = Label(root)
random_number = Label(root)
random_friend = Label(root)

lucky_friend_list = []

def addfriend():
    friend_name = enter_word.get()
    lucky_friend_list.append(friend_name)
    friend_list["text"] = "Your Friend List Is : " + str(lucky_friend_list)
    
def randomnumber():
    length = len(lucky_friend_list)
    random_num = random.randint(0 , length-1)
    random_number["text"] = str(random_num)
    random_num_name = lucky_friend_list[random_num]
    random_friend["text"] = "Your Lucky Friend : " + str(random_num_name)
    
btn = Button(root, text="Add Names" , command=addfriend , bg="blue" , fg="white")
btn.place(relx=0.5 , rely=0.3 , anchor=CENTER)

friend_list.place(relx=0.5 , rely=0.4 , anchor=CENTER)

btn1 = Button(root, text="Who Is Your Lucky Friend" , command=randomnumber , bg="blue" , fg="white")
btn1.place(relx=0.5 , rely=0.5 , anchor=CENTER)

random_friend.place(relx=0.5 , rely=0.6 , anchor=CENTER)
random_number.place(relx=0.5 , rely=0.7 , anchor=CENTER)

root.mainloop()

