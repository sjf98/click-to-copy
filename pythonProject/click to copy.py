# tkinter is a python gui library
import tkinter as tk
# pyperclip allows you to work with your clipboard
import pyperclip as pc

# array of all the messages
messages = [
        "Hey! Try making sure there are no hidden spaces at the start/end of your email when you’re trying to sign in, and try changing the first letter to upper/lower case. This can sometimes cause an issue with signing in and is something we'll be addressing soon. Hope this helps!",
        "Hey! Thank you for your interest in Hey! You can sign up to our platform here, www.ooohey.com/. Once you've signed up and connected your Instagram we'll get in touch when we've found a campaign that suits you!",
        "Hey!! All you need is an Instagram account ✅ and to be signed up and connected on our site.\nBrands will be matched to you and you'll be able to accept or decline jobs accordingly based on what you're happy to post :) \nHere’s an explainer video: \nhttps://www.instagram.com/tv/CXbfHWkgz3u/?utm_source=ig_web_copy_link",
        "Hey there! Brands pay for the content you post when you're signed up, so the money comes from those that want to promote their products and services on social media through your posts!",
        "Hey! The pay per post depends on the engagement you have, the relevance of your account to the promotional material and on the brand that have sent you the promotional content to post - so it varies from post to post.",
        "All you have to do now is wait! \nMore and more brand campaigns are coming over the next few weeks where signups will be selected to post and get paid. \nYou'll get an email over the coming weeks about being selected for a brand campaign and you'll be able to start posting and earning!"

    ]

# function to copy a message to a clipboard
def copy(num):
    pc.copy(messages[num])
    print(messages[num])


if __name__ == '__main__':
    # initialize tkinter gui as root
    root = tk.Tk()
    # set the root dimensions as 750x500
    root.geometry('750x500')
    # change the titles
    root.title('Click text to copy')

    #loop through the messages array
    for i in range(len(messages)):
        # create a button for each message in the array with width = 500 and text = to the message
        # the command is what is called whenever you click the button.
        button = tk.Button(root, text=messages[i], wraplength=500, command=lambda i=i : copy(i))
        # add the button to the winder with pack
        button.pack()

    # this is just used to loop so it doesnt only iterate once.
    root.mainloop()