import requests
from bs4 import BeautifulSoup as bs

link='https://www.ssts.si/kontakti-uciteljev-2/'#define a link
webpage_response=requests.get(link)#a response object
webpage=webpage_response.content#content filtered out of a response

soup=bs(webpage,'html.parser')#define a parsed object
#with open('html_file.txt','w',encoding='utf-8') as file:#write the html for easier debugging
    #file.write(str(soup))


mail_mess=[]#get an unorganized array of mails
instances=soup.find_all('tr')#find the instances
for i in instances:#loop through found tags
    for x in i.children:#loop trough tags children 
        if x!='\n' and x!=None:#check if it's not empty data
            mail_mess.append(x.string)#append to array
            #with open('mails_mess.txt','a',encoding='utf-8') as mails: #for debugging
                #mails.write(str(x.string))

mails=[i for i in mail_mess if '@' in str(i)]#check if element has @ and append if it does
mails_sorted=[]#empty array for sorted mails
data=''#empty for later file writing
for i in mails:#loop trough elements
    index=i.find('(')#fing the email blocker
    index2=i.find('.')#for name and surname later
    mail=i[:index]+'@'+i[index+3:]#gets the name and surname, appends @ and gets the mail endind
    mails_sorted.append(mail)#appends to array
    name=i.split('.')[0]#splits for name
    surname=i[index2+1:index]#gets the surname
    info=name.title()+' '+surname.title()+': '+str(mail)+'\n'#makes a formatted string
    data+=info#adds string to data that will get written to file
    print(info)
with open('mails.txt','w',encoding='utf-8') as file:#opens as write and encoding for non-crashing purposes
        file.write(data)#writes data to file