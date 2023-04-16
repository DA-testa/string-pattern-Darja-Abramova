# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    input = input().rstrip()
    
    if input =='I':
        a = input().rstrip()
        b = input().rstrip()
    elif input=='F':
        with open("tests/"+"06", 'r') as file:
            a=file.readline().rstrip()
            b = file.readline().rstrip()
    return a,b
    
  


def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    
    a_pat, b_text = len(a),len(b)
    a_pat1 = hash(a)
    b_text1 = hash(b[:a_pat])
    
    output=[]
    
    for i in range(b_text-a_pat+1):
        if b_text1 ==a_pat1 and b[i:i+a_pat]==a:
            output.append(i)
        if a_pat+i<b_text:
            b_text1=hash(b[i+1: i+a_pat+1])
    
    return output


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

