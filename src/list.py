
#now i'm writting here list. as like array and collections

#a list should have a name then after a equal sing the elements should be in third bracket 
friendsName = [
 "Friend zero",
 "Friend one",
 "Friend two",
 "Friend three",
 "Friend four",
 "Friend five"
]


print("This is list of friends name:",friendsName)
#the list of in py was correctly done

#now i will right list of friends age ..
friendsAge = [
 25,
 24,
 23,
 22,
 21,
 20
]


print("This is friendsAge output:",friendsAge)
#this seems also good.. .. ..

#now i will practice with list related works
#every elements has a position
#that's call index 
#i can see which element in which position
#and what is the index number of a element

#finding an element from the list by position
findAnElement=friendsName[0]

print("this is zero position Friend:",findAnElement)

#now i will find an element position

findPosition = friendsName.index("Friend one")

print("this is position of Friend one:",findPosition)

#now i will exchange an element with bew elemnet
friendsName[1] = "New friend"

print("this is one element exchange output",friendsName)
#i am glad. cz my code works well. 

#i have to practice list related works
#as like adding or removing elements and known the list lenght

#now i'm adding some new elements in those lists
friendsName.append("Friend 889")
friendsAge.append(787)

print(friendsName)
print(friendsAge)
#it works nicely 

#now i'm going to remove elements from those lists
friendsName.remove("Friend zero")
friendsAge.remove(25)

print(friendsName)
print(friendsAge)
#works nice

#len is lenght short form.
#it uses to know the list length

count_friendsName = len(friendsName)
count_friendsAge = len(friendsAge)
print(count_friendsName,count_friendsAge)
#debugged. works nicely


#This is a list operation
x=[4,5,6]
y=[4,5,6]
z=y[0] + x[0]

print(z)
#it has been worked

print("First line\n","second line")


















