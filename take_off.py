#Mission Control Ch.2

#Make a list
take_off_checklist = ["Put on suit", "Seal hatch", "Check cabin pressure", "Fasten seatbelt"]
print(take_off_checklist)

#Adding and removing items
take_off_checklist.append("Tell Mission Control checks are complete")
print(take_off_checklist)
take_off_checklist.remove("Seal hatch")
print(take_off_checklist)

#Using index numbers
take_off_checklist.insert(1, "Seal hatch")
print(take_off_checklist)
print(take_off_checklist[0])
print(take_off_checklist[1])
print(take_off_checklist[2])

#Replacing an item
take_off_checklist[3] = "Take a selfie"
print(take_off_checklist)
take_off_checklist[3] = "Fasten seatbelt"
print(take_off_checklist)

#Deleting an item
del take_off_checklist[2]
print(take_off_checklist)

#Insert Check cabin pressure in correct place
take_off_checklist.insert(2, "Check cabin pressure")
print(take_off_checklist)

#Create spacewalk_checklist
spacewalk_checklist = ["Put on suit", "Check oxygen", "Seal helmet", "Test radio", "Open airlock"]
print(spacewalk_checklist)

#List of Lists, Flight Manual
flight_manual = [take_off_checklist, spacewalk_checklist]
print(flight_manual)

#Combining lists
skills_list = take_off_checklist + spacewalk_checklist
print(skills_list)

#Create PR list
pr_list = ["Taking a selfie, Delivering lectures, Doing TV interviews, Meeting the public"]
skills_list += pr_list
print(skills_list)

