def are_vaild_groups()def are_valid_groups(litsOfStudent, listOfGroup):
    for i in litsOfStudent:
        for j in listOfGroup:
            if i in j:
                break
        print ("True")


print (are_valid_groups(["1","2","3"], [["1","2","3"],["3"]])):
