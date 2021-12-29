from tkinter import Tk, simpledialog, messagebox #importing these two widgets from the tkinter module 

#function hto read information stored in text file 
def read_from_file():
    with open("capital_data.txt") as file: #opens text file 
        for line in file:
            line = line.rstrip("\n") #removes neline character 
            country, city = line.split("/") #country variable stores info before '/' in text file and city stores info after '/' in each line 
            the_world[country] = city #country is the key in the dictionary and city is the value 

#function to insert new info program doesn't already know into text file for future reference 
def write_to_file(country_name, city_name): #function will add new country and capital city to text file 
    with open ("capital_data.txt", "a") as file: #'a' means to "append" or add new info to the end of the file 
        file.write("\n" + country_name + "/" + city_name) #creates new line, writes country, puts in country, slash, then city

print ("Ask the Expert - Capital Cities of the World")#print the text into the shell 
root = Tk() #creates an empty Tkinter window
root.withdraw() #hides the Tkinter window 
the_world = {} #creates an empty dictionary that will stores names of countries and capitals -> similar to list except every item has a key and a value

#Main program
read_from_file() #calls the read from file function 

while True: #infinite loop -> program will run until user closes it 
    query_country = simpledialog.askstring ("Country", "Type the name of a country") #simpledialog.askstring is function in Tkinter module that creates the box
                                                                                     #variable stores users response, 'country' is title of box

    if query_country in the_world: #if user's requested country is in the text file, run following procedure
        result = the_world[query_country] #uses query_country as key to find value in the dictionary 
        messagebox.showinfo("Answer", "The capital city of " + query_country + " is " + result + "!") #displays answer in a message box 
    else: #if requested country is not in text box, program learns it from user 
        new_city = simpledialog.askstring("Teach me ", " I don\'t know!" + "What is the capital city of " + query_country + "?") #displays the request to learn
        the_world[query_country] = new_city #adds new_city to the dictionary with query_country as key 
        write_to_file(query_country, new_city)#calls the write to file function 

root.mainloop #event loop that keeps the GUI running 
