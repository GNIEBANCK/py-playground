exerciseOne = {
    "id" : "exercise_ID_1",
    "stuff" : "some other stuff whatever it doesn't matter",
    "deleted" : True
}

exerciseTwo = {
    "id" : "exercise_ID_2",
    "stuff" : "some other stuff whatever it doesn't matter"
}

print (exerciseOne.get('deleted')) # True  
print (exerciseTwo.get('deleted')) # None
print (exerciseTwo.get('deleted') != None) # False
print (exerciseOne.get('deleted') == None) # False
if (exerciseTwo.get('deleted')==None):
    print "Do stuff for exercises thtat aren't deleted"