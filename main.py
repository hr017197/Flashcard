"""Basic code before splitting into model view controller portion. Not split into classes yet"""
#python does not need return statements

"""global variable for flash card packs"""
#packs doesn't need to be a dictionary, it just needs to be a list of the packs that are accessible.
packs = []

#Potential pack within packs: {'name': name, 'prompts': ['prompt-one', 'prompt-two'] 'answers': ['answer1', 'answer2']}

"""first portion is the main packs portion"""
def list_packs():
    """print out all packs"""
    global packs
    #exception
    if len(packs) == 0:
        print("There are currently no flash card packs")
    for item in packs:
        print(item)

def add_pack(new_pack):
    """add new pack from input to the packs"""
    global packs
    for pack in packs:
        #exception error -- make user eventually reinput what they want the pack to be named
        if new_pack == pack:
            print("Pack name already taken, please enter a different name")
        else:
            packs.append(new_pack)

def delete_pack(del_pack):
    global packs
    for pack in packs:
        if del_pack == pack:
            packs.pop(del_pack)

#TODO somehow make a function to access card packs


"""Portion for actually getting inside a pack"""



def main():
    pass
#test the functions here after they have been added to the main portion
    
if __name__ == "__main__":
    main()