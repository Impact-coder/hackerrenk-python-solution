def print_formatted(number):
    # your code goes here
    x=len(bin(number)[2:])
    for i in range(1,number+1):
        d=str(i)
        o=str(oct(i))
        h=str(hex(i).upper())
        b=str(bin(i))
        
        
        
        print(d.rjust(x," "),o[2:].rjust(x," "),h[2:].rjust(x," "),b[2:].rjust(x," "))
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)