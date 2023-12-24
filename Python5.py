import csv
def event(user):
    file_path="Mail_merge_exercise\\templates\event_reminder.txt"
    temp=open(file_path,mode='r')
    er=temp.read()
    print(user)
    er=er.replace('{{event_name}}',user[4])
    er=er.replace("{{event_date}}",user[3])
    er=er.replace("{{recipient_name}}",user[0])
    er=er.replace("{{event_location}}",user[1])
    er=er.replace("{{event_time}}","7:30")
    er=er.replace("{{organizer_name}}",'Ajeth S')
    er=er.replace("{{organizer_contact_info}}","69699751097")
    name=user[0]+".txt"
    wr=open(name,"w")
    wr.write(er)
    wr.close()
    
con=open('Mail_merge_exercise\contacts.csv',mode='r') 
content=list(csv.reader(con))
for i in range(len(content)):
    if  i!=0:
        if content[i][5]=="Event Reminder":
            event(content[i])

