if __name__ == '__main__':
    string = input()

    for i in range (0,len(string)):   
        if string[i:].isalnum():
            print("True")
            break
    else:
        print("False")
        
    for i in string:   
        if i.isalpha():
            print("True")
            break
    else:
        print("False")
            
    for i in string:   
        if i.isdigit():
            print("True")
            break
    else:
        print("False")
        
    for i in string:   
        if i.islower():
            print("True")
            break
    else:
        print("False")
        
    for i in string:   
        if i.isupper():
            print("True")
            break
    else:
        print("False")
       
