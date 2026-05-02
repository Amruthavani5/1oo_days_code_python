#items in list can be any datatype
states_in_us=["delware","pennsylvania", "Alaska","Arizona", "New Mexico"]
print(states_in_us[0])  #acess values in list  using index
print(states_in_us[-1]) #negative indexing----> last value
states_in_us[1]="pencilvania"   #modifying value in list
states_in_us.append("Angelaland") #adding value at the end of list using append
states_in_us.extend(["jack bauer land", "georgia"]) #extending the list
print(len(states_in_us))

#nested list
fruits=["apple", "banana","grapes","cherries"]
veggies=["spinach","kale","tomatoes","celery"]
dozen=[fruits,veggies]
print(dozen)
#access grapes
print(dozen[0][2])