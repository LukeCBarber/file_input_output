def main():
    #retrieve file
    invalid = True
    while invalid == True:
        try:
            filename = input("Enter a filename: ") + ".txt"
            file_obj = open(filename, "r")
            print('Successfully opened',filename)
            invalid = False
        except:
            print("Sorry, I can't find this filename")
            invalid = True
    print()
    print('**** ANALYZING ****')
    print()
    data = file_obj.read()

    #split string into list
    import re
    splitdata = re.split(', |\n',data)


    #check for item validity
    error =0
    for item in splitdata:
        charlist = re.split(',',item)
        ID = charlist[0]
        if ID[0] != "N":
            print("Invalid line of data: N# is invalid")
            print(item)
            print()
            splitdata.remove(item)
            error +=1
            continue
        
        for i in range(1,len(ID)):
            num = ID[i].isnumeric()
            if num == False:
                print("Invalid line of data: N# is invalid")
                print(item)
                print()
                splitdata.remove(item)
                error+=1
                continue
            
        if len(ID) != 9:
            print("Invalid line of data: N# is invalid")
            print(item)
            print()
            splitdata.remove(item)
            error+=1
            continue
        
        chartotal = len(charlist) - 1
        if chartotal != 25:
            print("Invalid line of data: does not contain exactly 26 values:")
            print(item)
            print()
            splitdata.remove(item)
            error+=1
            continue
        
    if error == 0:
        print("No errors found!")
        

    print()
    print('**** REPORT ****')
    #check total number of valid items
    valid = 0
    for item in splitdata:
        valid +=1
    print()
    print('Total valid lines of data:', valid)

    #check total number of invlid items
    print('Total invalid lines of data:', error)

    #Grade tests

    answerkey = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"

    answer_key = re.split(',',answerkey)
    scoretotal = 0
    scorelist = []
    IDlist = []
    for item in splitdata:
        points = 0
        charlist = re.split(',',item)
        ID = charlist[0]
        IDlist.append(ID)
        charlist.remove(ID)
        for i in range(25):
            if charlist[i] == answer_key[i]:
                points +=4
            elif charlist[i] == '':
               continue
            else:
                if charlist[i] != answer_key[i]:
                    points -=1
        scoretotal += points
        scorelist.append(points)
       
        
    print()

    #results file
    results = filename + '_grades.txt'
    results_file = open(results, 'w')   
    for i in range(len(IDlist)):
        line = str(IDlist[i]) + ',' + str(scorelist[i])
        results_file.write(line)
        results_file.write('\n')
    results_file.close()

    
    #average
    avg = scoretotal / len(splitdata)
    print('Mean (average) score:', format(avg,'.2f'))
    #highest/lowest
    high = max(scorelist)
    print('Highest score:', high)
    low = min(scorelist)
    print('Lowest score', low)
    #range
    rang = int(high) - int(low)
    print('Range of scores:',rang)
    #median
    def get_median(l):
        l_sort = l.sort()
        if len(l) % 2 != 0:
            m = int((len(l)+1)/2 - 1)
            return l[m]
        else:
            m1 = int(len(l)/2 - 1)
            m2 = int(len(l)/2)
            return (int(l[m1])+int(l[m2]))/2
        
    med = get_median(scorelist)
        
    print('Median score:',med)
        

    
main()
        

