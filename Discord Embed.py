from discord_webhook import DiscordEmbed, DiscordWebhook
from tkinter.font import BOLD
from tkinter import *

bgc = "#464646"

def server():      
    web = DiscordWebhook(url="https://discord.com/api/webhooks/1032315409652781146/v0yQdnJ0nhmWrgUj-6KD1QMhIvd1CTBRjqUeCW827My7HtrcwtoGf-JnYmtedV7lhPD-", username="The Seekers  Lair PH | General Rules ", content=eOverMessage.get())    
    
    embed = DiscordEmbed(color='D3D3D3')
    embed.set_author(name=eEmbedUser.get() ,icon_url=eIcon.get())
    embed.add_embed_field(name="Sector I.2",value=eDetails.get(1.0,END))
    #embed.set_image(url=eIcon.get())

    #embed.color(color='#1ABC9C')
    web.add_embed(embed)
    response = web.execute()
     
     
root = Tk()
#root.geometry("600x450")
root.configure(background=bgc)
mainframe = LabelFrame(root, text="Main Frame",pady=10,padx=50,bg = bgc)
appHeader = Label(mainframe, text="Discord Webhook", font=('Poiret One', 20, BOLD),bg = bgc)
txtHk = Label(mainframe,text="Weebhook",bg = bgc)
eWebhook = Entry(mainframe)
txtBT = Label(mainframe,text="Bot Name",bg = bgc)
eNamebot = Entry(mainframe)
txtOM = Label(mainframe,text="Message",bg = bgc)
eOverMessage = Entry(mainframe)
Embedframe = LabelFrame(root, text="Embed Field",pady=10,padx=60,bg = bgc)
txtTitle = Label(Embedframe,text="Content Title",bg = bgc)#
eTitle = Entry(Embedframe)
txtEmbedUser = Label(Embedframe,text="User Name",bg = bgc)#
eEmbedUser = Entry(Embedframe)
txtIconUser = Label(Embedframe,text="Icon User",bg = bgc)#
eIcon = Entry(Embedframe)
txtDetails = Label(Embedframe,text="Details",bg = bgc , )#
eDetails = Text(Embedframe,height=15,width=80)
submitBtn = Button(Embedframe,text="Submit",command=server,bg = bgc)




mainframe.grid(row=0, column=0,padx=10,pady=10)
appHeader.grid(row=0, column=0,columnspan=3)
txtHk.grid(row=1,column=0)
eWebhook.grid(row=2)
txtBT.grid(row=1,column=1)
eNamebot.grid(row=2,column=1)
txtOM.grid(row=1,column=2)
eOverMessage.grid(row=2,column=2)
Embedframe.grid(row=1, column=0,padx=10,pady=10)
txtTitle.grid(row=0,column=0)
eTitle.grid(row=1,column=0,)
txtEmbedUser.grid(row=0,column=1)
eEmbedUser.grid(row=1,column=1)
txtIconUser.grid(row=0,column=2)
eIcon.grid(row=1,column=2)
txtDetails.grid(row=2,columnspan=3)
eDetails.grid(row=3,column=0,columnspan=3)
submitBtn.grid(row=4,columnspan=3)

#server()
root.resizable(False,False)
root.mainloop()  
