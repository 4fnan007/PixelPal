import requests
import time
import os
import signal

def save_chat():
    choice = input("\nDo you want to save the chat in the current directory? (y/n): ")
    if choice.lower() == "y":
        # Save the chat
        with open("chat_log.txt", "w") as file:
            file.write(chat_log)
        print("Chat saved successfully.")
    elif choice.lower() == "n":
        print("Chat not saved.")
    else:
        print("Invalid choice. Chat not saved.")

    exit(0)

def signal_handler(signal, frame):
    save_chat()

signal.signal(signal.SIGINT, signal_handler)


print("                                                                     ")
print("         ███████████████████████████████████████████████████         ")
print("         █▄─▄▄─█▄─▄█▄─▀─▄█▄─▄▄─█▄─▄███████▄─▄▄─██▀▄─██▄─▄███         ")
print("         ██─▄▄▄██─███▀─▀███─▄█▀██─██▀██████─▄▄▄██─▀─███─██▀█         ")
print("         ▀▄▄▄▀▀▀▄▄▄▀▄▄█▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▀▀▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀         ")
print(" 𝙷𝚊𝚟𝚎 𝚢𝚘𝚞 𝚜𝚎𝚎𝚗 𝚢𝚘𝚞𝚛 𝚏𝚊𝚟𝚘𝚛𝚒𝚝𝚎 𝚌𝚑𝚊𝚛𝚊𝚌𝚝𝚎𝚛𝚜 𝚌𝚑𝚊𝚝𝚝𝚒𝚗𝚐 𝚝𝚘𝚐𝚎𝚝𝚑𝚎𝚛 𝚙𝚕𝚊𝚗𝚗𝚒𝚗𝚐 𝚜𝚘𝚖𝚎𝚝𝚑𝚒𝚗𝚐 \n")                   
print("                                                          Developed By Afnan")
print("                                                 https://github.com/4fnan007")   
time.sleep(1)
print("\nThis magnificent AutoGPT program act as a virtual characters within two separate ChatGPT instances,\nEngaging in autonomous conversation while embodying the persona of a beloved character from a specified movie or series.")
input("Provide the name of your fictional character and the TV show or movie in which they appeared for each instance for autochat. \n \nIf you understand what am saying just press Enter...\n")
print("____________________________________(ᴘɪxᴇʟ ᴘᴀʟ)____________________________________")
show_name1 = input("\nEnter the name of the TV show or Movie that your character is appeared: ")
character_name1 = input("Enter the name of character played in that TV show or movie: ")
print(f"\n(0_0) => Okay cool broo!! So your first character instance is {character_name1} from {show_name1}.\n\n")
show_name2 = input("Enter the name of the TV show or Movie that your character is appeared for next GPT instance: ")
character_name2 = input("Enter the name of character played in that TV show or movie: ")
input(f"\n(0-0) => Alright than your second character instance is {character_name2} from {show_name2}.\nPress Enter to confirm...\n")
metaprompt = (' ')
time.sleep(1)
os.system('clear')
print("____________________________________(ᴘɪxᴇʟ ᴘᴀʟ)____________________________________")
print("\nGreat! Let's start the conversation between your two characters.\n")
print(f"Who need to ask chat prompt or question first")
value = input(f"Enter '1' if you want {character_name1} to ask the first question, or enter '2' if you want {character_name2} to ask the first question: ")
if value == "1":
    question = input(f"What do you want to ask {character_name2} from {character_name1}: ")
    if os.path.exists('source/char_prompt.txt'):
        with open('source/char_prompt.txt', 'r') as file:
            words = file.read().split()
    else:
        with open('char_prompt.txt', 'r') as file:
            words = file.read().split()
    char_prompt1 = ' '.join(words).format(character_name=character_name2, show_name=show_name2, question=question, opposite_character=character_name1, opposite_show=show_name1)
    chat1 = requests.get("http://localhost:5001/chat?q=%s" % char_prompt1)
    opposite_char_req = (f"i am act as a {character_name2} from {show_name2} and i will response and answer like that {character_name2} using the tone, manner and vocabulary, and i the virtual character {character_name2} asking first question. if you understand please say 'YES, i understood'.")
    opposite_char_instance = ' '.join(words).format(character_name=character_name1, show_name=show_name1, question=opposite_char_req, opposite_character=character_name2, opposite_show=show_name2)
    chat2 = requests.get("http://localhost:5002/chat?q=%s" % opposite_char_instance)
    os.system('clear')    
    if os.path.exists('source/banner.py'):
        os.system('python source/banner.py')
    else:
        os.system('python banner.py')
    print(f"\nTOPIC: {question} \n \n")
    chat_log = (f"\nTOPIC: {question} \n")
    print(f"{character_name2}: ", chat1.text)
    print("                                                                                        ")   
    chat_log += f"\n{character_name2}: {chat1.text}\n"
    while True:
        chat2 = requests.get("http://localhost:5002/chat?q=%s" % (chat1.text.replace("ChatGPT", "")))
        print(f"{character_name1}: ", chat2.text)
        chat_log += f"\n{character_name1}: {chat2.text}\n"
        print("                                                                                                        ")
        chat1 = requests.get("http://localhost:5001/chat?q=%s" % (chat2.text.replace("ChatGPT", "")))
        print(f"{character_name2}: ", chat1.text)
        chat_log += f"\n{character_name2}: {chat1.text}\n"
        print("________________________________________________________________________________________________________")
        print("                                                                                                        ")
        try:
            if keyboard.is_pressed('ctrl+c'):  # Check if Ctrl+C is pressed
                print("\nCtrl+C pressed. Do you want to save the chat?")
                save_chat = input("Enter 'y' to save the chat or 'n' to close the program: ")
                if save_chat.lower() == 'y':
                    save_file = "chat_log.txt"
                    with open(save_file, "w") as file:
                        file.write(chat_log)
                    print("Chat saved successfully.")
                    print("All chats saved:")
                    with open(save_file, "r") as file:
                        print(file.read())
                    break
                elif save_chat.lower() == 'n':
                    break
                else:
                    print("Invalid input. Closing the program.")
                    break
        except:
            pass

elif value == "2":
    question = input(f"What do you want to ask {character_name1} from {character_name2}: ")
    if os.path.exists('source/char_prompt.txt'):
        with open('source/char_prompt.txt', 'r') as file:
            words = file.read().split()
    else:
        with open('char_prompt.txt', 'r') as file:
            words = file.read().split()
    char_prompt2 = ' '.join(words).format(character_name=character_name1, show_name=show_name1, question=question, opposite_character=character_name2, opposite_show=show_name2)
    chat2 = requests.get("http://localhost:5002/chat?q=%s" % char_prompt2)
    opposite_char_req = (f"i always act as a {character_name1} from {show_name1} and i will response and answer like that {character_name1} using the tone, manner and vocabulary, and i the virtual character {character_name1} asking first question. if you understand please say 'YES, i understood'.")
    opposite_char_instance = ' '.join(words).format(character_name=character_name2, show_name=show_name2, question=opposite_char_req, opposite_character=character_name1, opposite_show=show_name1)
    chat1 = requests.get("http://localhost:5001/chat?q=%s" % (opposite_char_instance))
    os.system('clear')    
    if os.path.exists('source/banner.py'):
        os.system('python source/banner.py')
    else:
        os.system('python banner.py')   
    print(f"\nTOPIC: {question} \n \n")
    chat_log = (f"\nTOPIC: {question} \n")
    print(f"{character_name1}: ", chat2.text)
    print("                                                                                        ")   
    chat_log += f"{character_name2}: {chat1.text}\n"
    while True:
        chat1 = requests.get("http://localhost:5001/chat?q=%s" % (chat2.text.replace("ChatGPT", "")))
        print(f"{character_name2}: ", chat1.text)
        chat_log += f"{character_name2}: {chat1.text}\n"
        print("                                                                                                        ")
        chat2 = requests.get("http://localhost:5002/chat?q=%s" % (chat1.text.replace("ChatGPT", "")))
        print(f"{character_name1}: ", chat2.text)
        chat_log += f"{character_name1}: {chat2.text}\n"
        print("________________________________________________________________________________________________________")
        print("                                                                                                        ")
        try:
            if keyboard.is_pressed('ctrl+c'):  # Check if Ctrl+C is pressed
                print("\nCtrl+C pressed. Do you want to save the chat?")
                save_chat = input("Enter 'y' to save the chat or 'n' to close the program: ")
                if save_chat.lower() == 'y':
                    save_file = "chat_log.txt"
                    with open(save_file, "w") as file:
                        file.write(chat_log)
                    print("Chat saved successfully.")
                    print("All chats saved:")
                    with open(save_file, "r") as file:
                        print(file.read())
                    break
                elif save_chat.lower() == 'n':
                    break
                else:
                    print("Invalid input. Closing the program.")
                    break
        except:
            pass    
else:
    print("Wrong option!!! Enter option 1 or 2 only. Try again... ")
    time.sleep(1)
    os.system('clear')
    exit(0)
