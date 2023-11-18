#Mission Python Chapter 2

#Make the Take Off list
take_off_checklist = ["Put on suit", "Seal hatch", "Check cabin pressure", "Fasten seatbelt"]
print(take_off_checklist)

#Append the list
take_off_checklist.append("Tell Mission Control checks are complete")
print(take_off_checklist)

#Remove an item
take_off_checklist.remove("Seal hatch")
print(take_off_checklist)

#Using Index Numbers to insert
take_off_checklist.insert(1, "Seal hatch")
print(take_off_checklist)

#To see individual items on the list
print(take_off_checklist[0])
print(take_off_checklist[1])
print(take_off_checklist[2])

#Replacing an item
take_off_checklist[3] = "Take a selfie"
print(take_off_checklist)

#Deleting an item
del take_off_checklist[2]
print(take_off_checklist)


#Create Spacewalk Checklist
spacewalk_checklist = ["Put on suit", "Check oxygen", "Seal helmet", "Test radio", "Open airlock"]
print(spacewalk_checklist)

#Check Indexing
print(spacewalk_checklist[0])
print(spacewalk_checklist[1])
print(spacewalk_checklist[2])
print(spacewalk_checklist[3])
print(spacewalk_checklist[4])

#Flight Manual List of Lists
flight_manual = [take_off_checklist, spacewalk_checklist]
print(flight_manual)

#Check indexing
print(flight_manual[0])
print(flight_manual[0][1])
print(flight_manual[1][3])

#Combining Lists
skills_list = take_off_checklist + spacewalk_checklist
print(skills_list)

pr_list = ["Taking a selfie", "Delivering lectures", "Doing TV interviews", "Meeting the public"]
skills_list += pr_list
print(skills_list)