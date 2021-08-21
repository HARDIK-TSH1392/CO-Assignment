import sys

#lines = ["var x", "mov R1 $4", "mov R2 $4", "cmp R1 R2", "mov R4 $1", "cmp R3 R4", "jgt label", "label: hlt"]
#file_object = open('test2')
#lines = file_object.readlines()
read_file = sys.stdin.read()
lines = read_file.split("\n")
#lines = ["var x", "mov R1 $26", "mov R1 $4", "hlt"]

n = len(lines)

#============================================================================================================
error_clear = False
def check_error():
    global error
    

    def error_check1():
        global error_clear

        last = lines[-1].split()
        if len(last) > 1 and last[1] == "hlt":
            pass
        elif lines[-1] != "hlt":
            print("Error: hlt statement not present!")
            error_clear = True
        
    def error_check2():
        global error_clear

        for i in range(0,n):
            if lines[i] == "hlt" and i != n-1:
                print("Error: hlt can only be used at the end!")
                error_clear = True
                break

    def error_check3():
        global error_clear

        for i in range(0,n):
            l = lines[i].split()

            if l[0] == "ld" or l[0] == "st":
                if l[2] not in variable:
                    print("Error: Undefined variable used in line:", i)
                    error_clear = True
                    break

    def error_check4():
        global error_clear

        for i in range(0, n):
            l = lines[i].split()
            if l[0] == "jmp" or l[0] == "jlt" or l[0] == "jgt" or l[0] == "je":
                if l[1] not in label:
                    print("Error: Undefined label used in line:", i)
                    error_clear = True
                    break

    def error_check5():
        global error_clear

        for i in range(0, n):
            l = lines[i].split()
            if l[0] == "mov":
                if l[2] == "FLAGS":
                    print("Error: Illegal use of FLAGS register in line:", i)
                    error_clear = True
                    break

    def error_check6():
        global error_clear
        
        for i in range(0, n):
            l = lines[i].split()
            if l[0] == "mov" or l[0] == "ls" or l[0] == "rs":
                if l[2][0] == "$":
                    if int(l[2][1:]) < 0 or int(l[2][1:]) > 255:
                        print("Error: Illegal Immediate value used in line:", i)
                        error_clear = True
                        break


    def error_check7():
        global error_clear

        for i in range(0, n):
            l = lines[i].split()
            if l[0] == "jmp" or l[0] == "jlt" or l[0] == "je" or l[0] == "jgl":
                if l[1] in variable:
                    print("Error: Misuse of variable as label in line:", i)
                    error_clear = True
                    break
            elif l[0] == "st" or l[0] == "ld":
                if l[2] in label:
                    print("Error: Misuse of label as variable in line:", i)
                    error_clear = True
                    break

    def error_check8():
        global error_clear
        flag_checker = False
        l = lines[0].split()
        if l[0] != "var":
            flag_checker = True
        for i in range(0, n):
            l = lines[i].split()
            if l[0] == "var" and flag_checker == True:
                print("Error: Variables can only be defined in the beginning but defined in line:", i)
                error_clear = True
                break

    def error_check9():
        global error_clear

        for i in range(0, n):
            l = lines[i].split()
            if l[0] not in ins:
                print("Error: Typo in instructions name or registers in line:", i)
                error_clear = True
                break
            elif l[0] == "add" or l[0] == "sub" or l[0] == "mul" or l[0] == "or" or l[0] == "and" or l[0] == "xor":
                if l[1] not in ins or l[2] not in ins or l[3] not in ins:
                    print("Error: Typo in instructions name or registers in line:", i)
                    error_clear = True
                    break
            elif l[0] == "mov" or l[0] == "rs" or l[0] == "ls":
                if l[1] not in ins:
                    print("Error: Typo in instructions name or registers in line:", i)
                    error_clear = True
                    break
            elif l[0] == "div" or l[0] == "not" or l[0] == "cmp":
                if l[1] not in ins or l[2] not in ins:
                    print("Error: Typo in instructions name or registers in line:", i)
                    error_clear = True
                    break
            elif l[0] == "ld" or l[0] == "st":
                if l[1] not in ins:
                    print("Error: Typo in instructions name or registers in line:", i)
                    error_clear = True
                    break

    def error_check10():
        global error_clear
        loop_flag = False

        var_dict = [':', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(0, len(variable)):
            for j in variable[i]:
                if j not in var_dict:
                    print("Error: Variable name should consist of only alphanumeric characters or underscores!")
                    error_clear = True
                    loop_flag = True
                    break
            if loop_flag == True:
                break

    def error_check11():
        global error_clear
        loop_flag = False

        var_dict = [':', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(0, len(label)):
            for j in label[i]:
                if  j not in var_dict:
                    print("Error: Variable name should consist of only alphanumeric characters or underscores!")
                    error_clear = True
                    loop_flag = True
                    break
            if loop_flag == True:
                break


    def error_check12():
        global error_clear

    
    
    for i in range(0,len(lines)):
        #checker_line = lines[i].split()
        error_check1()
        if error_clear == False:
            error_check2()
        if error_clear == False:
            error_check3()
        if error_clear == False:
            error_check4()
        if error_clear == False:
            error_check5()
        if error_clear == False:
            error_check6()
        if error_clear == False:
            error_check7()
        if error_clear == False:
            error_check8()
        if error_clear == False:
            error_check9()
        if error_clear == False:
            error_check10()
        if error_clear == False:
            error_check11()
        if error_clear == False:
            error_check12()
        
        if error_clear == True:
            break

    if error_clear == False:
        error = False
    else:
        error = True


#============================================================================================================
mem_add = {} 
error = True
ins = ["add", "sub", "mov", "ld", "st", "mul", "div", "ls", "rs", "xor", "or", "label:", "and", "not", "cmp", "jlt", "jmp", "jgt", "je", "hlt", "R0", "R1", "R2", "R3", "R4", "R5", "R6", "FLAGS", "var"]
variable = []
label = []
r = {'000':0000000000000000, '001':0000000000000000, '010':0000000000000000, 
              #R0                     #R1                     #R2
                #R6                   #FLAG
         '011':0000000000000000, '100':0000000000000000, '101':0000000000000000,
                #R3                   #R4                   #R5
         '110':0000000000000000, '111':0000000000000000}

output = []
start1 = 0
end1 = n
start2 = 0
end2 = n
start3 = 0
end3 = n
count = 0

while(start3<end3):
    u = lines[start3].split()
    if len(u)>0 and u[0] == "var":
        variable.append(u[1])
        ins.append(u[1])
        count += 1
    start3 += 1

variable_pointer = end2 - count
while(start2<end2):
    #Code to find location of lables and variables yet to written and stored in
    #mem_add
    t = lines[start2].split()
    if len(t)>0 and t[0][-1] == ":":
        label.append(t[0])
        label.append(t[0][:-1])
        ins.append(t[0][:-1])
        mem_add.update({t[0][:-1]: start2-count})
    if len(u)>0 and t[0] == "var":
        mem_add.update({t[1]:variable_pointer })
        variable_pointer += 1
    if len(u)>0 and t[0] == "mov":
        if t[2][0] == "$":
            ins.append(t[2])
    start2+=1
#=============================================================================================================

#=============================================================================================================
if error == True:
    check_error()
#=============================================================================================================




global flag
flag = True
if error == False:
    for i in range(0,n):
        
        def convert_to_8bit(z):
            bnr = bin(z).replace('0b','')
            x = bnr[::-1] #this reverses an array
            while len(x) < 8:
                x += '0'
            bnr = x[::-1]
            return bnr
        
        def convert_to_16bits(z):
            bnr = bin(z).replace('0b','')
            x = bnr[::-1] #this reverses an array
            while len(x) < 16:
                x += '0'
            bnr = x[::-1]
            return bnr

        def ins_add(r,s):
                
                if s[2] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[2] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[2] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[2] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[2] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[2] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[2] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[2] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"
                
                if s[3] == "R0":
                    b = r["000"]
                    locate_b = "000"
                elif s[3] == "R1":
                    b = r["001"]
                    locate_b = "001"
                elif s[3] == "R2":
                    b = r["010"]
                    locate_b = "010"
                elif s[3] == "R3":
                    b = r["011"]
                    locate_b = "011"
                elif s[3] == "R4":
                    b = r["100"]
                    locate_b = "100"
                elif s[3] == "R5":
                    b = r["101"]
                    locate_b = "101"
                elif s[3] == "R6":
                    b = r["110"]
                    locate_b = "110"
                elif s[3] == "FLAGS":
                    b = r["111"]
                    locate_b = "111"

                #sum = convert_to_16bits(int(a, 2) + int(b, 2))
                
                #need to check overflow

                if s[1] == "R0":
                    #c = r["000"]
                    locate_c = "000"
                elif s[1] == "R1":
                    #c = r["001"]
                    locate_c = "001"
                elif s[1] == "R2":
                    #c = r["010"]
                    locate_c = "010"
                elif s[1] == "R3":
                    #c = r["011"]
                    locate_c = "011"
                elif s[1] == "R4":
                    #c = r["100"]
                    locate_c = "100"
                elif s[1] == "R5":
                    #c = r["101"]
                    locate_c = "101"
                elif s[1] == "R6":
                    #c = r["110"]
                    locate_c = "110"
                elif s[1] == "FLAGS":
                    #c = r["111"]
                    locate_c = "111"

                
                #r[locate_c] = sum

                output.append("0000000"+locate_c+locate_a+locate_b)

        def ins_sub(r,s):
                
                if s[2] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[2] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[2] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[2] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[2] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[2] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[2] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[2] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"
                
                if s[3] == "R0":
                    b = r["000"]
                    locate_b = "000"
                elif s[3] == "R1":
                    b = r["001"]
                    locate_b = "001"
                elif s[3] == "R2":
                    b = r["010"]
                    locate_b = "010"
                elif s[3] == "R3":
                    b = r["011"]
                    locate_b = "011"
                elif s[3] == "R4":
                    b = r["100"]
                    locate_b = "100"
                elif s[3] == "R5":
                    b = r["101"]
                    locate_b = "101"
                elif s[3] == "R6":
                    b = r["110"]
                    locate_b = "110"
                elif s[3] == "FLAGS":
                    b = r["111"]
                    locate_b = "111"

                #diff = int(a, 2) - int(b, 2)
                #if diff < 0:
                #    diff = 0
                #diff = convert_to_16bits(diff)
                    #set flag
                
                #need to check overflow

                if s[1] == "R0":
                    #c = r["000"]
                    locate_c = "000"
                elif s[1] == "R1":
                    #c = r["001"]
                    locate_c = "001"
                elif s[1] == "R2":
                    #c = r["010"]
                    locate_c = "010"
                elif s[1] == "R3":
                    #c = r["011"]
                    locate_c = "011"
                elif s[1] == "R4":
                    #c = r["100"]
                    locate_c = "100"
                elif s[1] == "R5":
                    #c = r["101"]
                    locate_c = "101"
                elif s[1] == "R6":
                    #c = r["110"]
                    locate_c = "110"
                elif s[1] == "FLAGS":
                    #c = r["111"]
                    locate_c = "111"

                #c = "0000000000000000"
                #r[locate_c] = diff

                output.append("0000100"+locate_c+locate_a+locate_b)

        def ins_mov(r,s):
    
                if s[1] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[1] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[1] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[1] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[1] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[1] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[1] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[1] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"

                if s[2][0] == "R" or s[2] == "FLAGS":
                    
                    if s[2] == "R0":
                        b = r["000"]
                        locate_b = "000"
                    elif s[2] == "R1":
                        b = r["001"]
                        locate_b = "001"
                    elif s[2] == "R2":
                        b = r["010"]
                        locate_b = "010"
                    elif s[2] == "R3":
                        b = r["011"]
                        locate_b = "011"
                    elif s[2] == "R4":
                        b = r["100"]
                        locate_b = "100"
                    elif s[2] == "R5":
                        b = r["101"]
                        locate_b = "101"
                    elif s[2] == "R6":
                        b = r["110"]
                        locate_b = "110"
                    elif s[2] == "FLAGS":
                        b = r["111"]
                        locate_b = "111"

                    #r[locate_a] = r[locate_b]

                    output.append("0001100000"+locate_a+locate_b)
                elif s[2][0] == "$":
                    if s[2][0] == "$":
                        c = int(s[2][1:])
                        c = convert_to_8bit(c)
                        #r[locate_a] = c    convert to 16 bit for this
                        
                        output.append("00010"+locate_a+c)
        
        def ins_ld(r,s,mem_add):
                
                if s[2] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[2] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[2] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[2] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[2] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[2] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[2] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[2] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"

                for k in mem_add:
                    if k == s[1]:
                        address = mem_add[k]
                address = convert_to_8bit(address)

                output.append("00100"+ locate_a+address)

        def ins_st(r,s,mem_add):
                if s[1] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[1] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[1] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[1] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[1] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[1] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[1] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[1] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"

                for k in mem_add:
                    if k == s[2]:
                        address = mem_add[k]
                address = convert_to_8bit(address)

                output.append("00101"+ locate_a+address)

        def ins_mul(r,s):
                
                if s[2] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[2] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[2] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[2] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[2] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[2] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[2] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[2] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"
                
                if s[3] == "R0":
                    b = r["000"]
                    locate_b = "000"
                elif s[3] == "R1":
                    b = r["001"]
                    locate_b = "001"
                elif s[3] == "R2":
                    b = r["010"]
                    locate_b = "010"
                elif s[3] == "R3":
                    b = r["011"]
                    locate_b = "011"
                elif s[3] == "R4":
                    b = r["100"]
                    locate_b = "100"
                elif s[3] == "R5":
                    b = r["101"]
                    locate_b = "101"
                elif s[3] == "R6":
                    b = r["110"]
                    locate_b = "110"
                elif s[3] == "FLAGS":
                    b = r["111"]
                    locate_b = "111"

                #prod = int(a, 2) * int(b, 2)
                #prod = convert_to_16bits(prod)
                
                
                #need to check overflow

                if s[1] == "R0":
                    #c = r["000"]
                    locate_c = "000"
                elif s[1] == "R1":
                    #c = r["001"]
                    locate_c = "001"
                elif s[1] == "R2":
                    #c = r["010"]
                    locate_c = "010"
                elif s[1] == "R3":
                    #c = r["011"]
                    locate_c = "011"
                elif s[1] == "R4":
                    #c = r["100"]
                    locate_c = "100"
                elif s[1] == "R5":
                    #c = r["101"]
                    locate_c = "101"
                elif s[1] == "R6":
                    #c = r["110"]
                    locate_c = "110"
                elif s[1] == "FLAGS":
                    #c = r["111"]
                    locate_c = "111"

                
                #r[locate_c] = prod

                output.append("0011000"+locate_c+locate_a+locate_b)

        def ins_div(r,s):
                
                if s[1] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[1] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[1] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[1] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[1] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[1] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[1] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[1] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"
                
                if s[2] == "R0":
                    b = r["000"]
                    locate_b = "000"
                elif s[2] == "R1":
                    b = r["001"]
                    locate_b = "001"
                elif s[2] == "R2":
                    b = r["010"]
                    locate_b = "010"
                elif s[2] == "R3":
                    b = r["011"]
                    locate_b = "011"
                elif s[2] == "R4":
                    b = r["100"]
                    locate_b = "100"
                elif s[2] == "R5":
                    b = r["101"]
                    locate_b = "101"
                elif s[2] == "R6":
                    b = r["110"]
                    locate_b = "110"
                elif s[2] == "FLAGS":
                    b = r["111"]
                    locate_b = "111"

                output.append("0011100000"+locate_a+locate_b)

        def ins_rs(r,s):
                
                if s[1] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[1] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[1] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[1] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[1] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[1] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[1] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[1] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"

                p = int(s[2][1:])
                q = int(r[locate_a],2) >> p
                #r[locate_a] = convert_to_16bits(q)
                d = convert_to_8bit(p)

                output.append("01000"+ locate_a+d)

        def ins_ls(r,s):
                if s[1] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[1] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[1] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[1] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[1] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[1] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[1] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[1] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"

                p = int(s[2][1:])
                q = int(r[locate_a],2) << p
                #r[locate_a] = convert_to_16bits(q)
                d = convert_to_8bit(p)

                output.append("01000"+ locate_a+d)

        def ins_xor(r,s):
                
                if s[2] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[2] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[2] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[2] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[2] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[2] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[2] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[2] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"
                
                if s[3] == "R0":
                    b = r["000"]
                    locate_b = "000"
                elif s[3] == "R1":
                    b = r["001"]
                    locate_b = "001"
                elif s[3] == "R2":
                    b = r["010"]
                    locate_b = "010"
                elif s[3] == "R3":
                    b = r["011"]
                    locate_b = "011"
                elif s[3] == "R4":
                    b = r["100"]
                    locate_b = "100"
                elif s[3] == "R5":
                    b = r["101"]
                    locate_b = "101"
                elif s[3] == "R6":
                    b = r["110"]
                    locate_b = "110"
                elif s[3] == "FLAGS":
                    b = r["111"]
                    locate_b = "111"

                #xor = int(a, 2) ^ int(b, 2)
                #xor = convert_to_16bits(xor)
                
                
                

                if s[1] == "R0":
                    #c = r["000"]
                    locate_c = "000"
                elif s[1] == "R1":
                    #c = r["001"]
                    locate_c = "001"
                elif s[1] == "R2":
                    #c = r["010"]
                    locate_c = "010"
                elif s[1] == "R3":
                    #c = r["011"]
                    locate_c = "011"
                elif s[1] == "R4":
                    #c = r["100"]
                    locate_c = "100"
                elif s[1] == "R5":
                    #c = r["101"]
                    locate_c = "101"
                elif s[1] == "R6":
                    #c = r["110"]
                    locate_c = "110"
                elif s[1] == "FLAGS":
                    #c = r["111"]
                    locate_c = "111"

                
                #r[locate_c] = xor

                output.append("0101000"+locate_c+locate_a+locate_b)

        def ins_or(r,s):
                
                if s[2] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[2] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[2] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[2] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[2] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[2] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[2] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[2] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"
                
                if s[3] == "R0":
                    b = r["000"]
                    locate_b = "000"
                elif s[3] == "R1":
                    b = r["001"]
                    locate_b = "001"
                elif s[3] == "R2":
                    b = r["010"]
                    locate_b = "010"
                elif s[3] == "R3":
                    b = r["011"]
                    locate_b = "011"
                elif s[3] == "R4":
                    b = r["100"]
                    locate_b = "100"
                elif s[3] == "R5":
                    b = r["101"]
                    locate_b = "101"
                elif s[3] == "R6":
                    b = r["110"]
                    locate_b = "110"
                elif s[3] == "FLAGS":
                    b = r["111"]
                    locate_b = "111"

                #orr = int(a, 2) | int(b, 2)
                #orr = convert_to_16bits(orr)
                
                
                

                if s[1] == "R0":
                    #c = r["000"]
                    locate_c = "000"
                elif s[1] == "R1":
                    #c = r["001"]
                    locate_c = "001"
                elif s[1] == "R2":
                    #c = r["010"]
                    locate_c = "010"
                elif s[1] == "R3":
                    #c = r["011"]
                    locate_c = "011"
                elif s[1] == "R4":
                    #c = r["100"]
                    locate_c = "100"
                elif s[1] == "R5":
                    #c = r["101"]
                    locate_c = "101"
                elif s[1] == "R6":
                    #c = r["110"]
                    locate_c = "110"
                elif s[1] == "FLAGS":
                    #c = r["111"]
                    locate_c = "111"

                
                #r[locate_c] = orr

                output.append("0000100"+locate_c+locate_a+locate_b)

        def ins_and(r,s):
                
                if s[2] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[2] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[2] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[2] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[2] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[2] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[2] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[2] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"
                
                if s[3] == "R0":
                    b = r["000"]
                    locate_b = "000"
                elif s[3] == "R1":
                    b = r["001"]
                    locate_b = "001"
                elif s[3] == "R2":
                    b = r["010"]
                    locate_b = "010"
                elif s[3] == "R3":
                    b = r["011"]
                    locate_b = "011"
                elif s[3] == "R4":
                    b = r["100"]
                    locate_b = "100"
                elif s[3] == "R5":
                    b = r["101"]
                    locate_b = "101"
                elif s[3] == "R6":
                    b = r["110"]
                    locate_b = "110"
                elif s[3] == "FLAGS":
                    b = r["111"]
                    locate_b = "111"

                #andd = int(a, 2) & int(b, 2)
                #andd = convert_to_16bits(andd)
                

                if s[1] == "R0":
                    #c = r["000"]
                    locate_c = "000"
                elif s[1] == "R1":
                    #c = r["001"]
                    locate_c = "001"
                elif s[1] == "R2":
                    #c = r["010"]
                    locate_c = "010"
                elif s[1] == "R3":
                    #c = r["011"]
                    locate_c = "011"
                elif s[1] == "R4":
                    #c = r["100"]
                    locate_c = "100"
                elif s[1] == "R5":
                    #c = r["101"]
                    locate_c = "101"
                elif s[1] == "R6":
                    #c = r["110"]
                    locate_c = "110"
                elif s[1] == "FLAGS":
                    #c = r["111"]
                    locate_c = "111"

                #c = "0000000000000000"
                #r[locate_c] = andd

                output.append("0000100"+locate_c+locate_a+locate_b)

        def ins_not(r,s):
                
                if s[1] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[1] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[1] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[1] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[1] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[1] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[1] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[1] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"
                
                if s[2] == "R0":
                    b = r["000"]
                    locate_b = "000"
                elif s[2] == "R1":
                    b = r["001"]
                    locate_b = "001"
                elif s[2] == "R2":
                    b = r["010"]
                    locate_b = "010"
                elif s[2] == "R3":
                    b = r["011"]
                    locate_b = "011"
                elif s[2] == "R4":
                    b = r["100"]
                    locate_b = "100"
                elif s[2] == "R5":
                    b = r["101"]
                    locate_b = "101"
                elif s[2] == "R6":
                    b = r["110"]
                    locate_b = "110"
                elif s[2] == "FLAGS":
                    b = r["111"]
                    locate_b = "111"

                output.append("0110100000"+ locate_a+locate_b)

        def ins_cmp(r,s):
                
                if s[1] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[1] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[1] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[1] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[1] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[1] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[1] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[1] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"

                if s[2] == "R0":
                    b = r["000"]
                    locate_b = "000"
                elif s[2] == "R1":
                    b = r["001"]
                    locate_b = "001"
                elif s[2] == "R2":
                    b = r["010"]
                    locate_b = "010"
                elif s[2] == "R3":
                    b = r["011"]
                    locate_b = "011"
                elif s[2] == "R4":
                    b = r["100"]
                    locate_b = "100"
                elif s[2] == "R5":
                    b = r["101"]
                    locate_b = "101"
                elif s[2] == "R6":
                    b = r["110"]
                    locate_b = "110"
                elif s[2] == "FLAGS":
                    b = r["111"]
                    locate_b = "111"
                
                output.append("0111000000"+locate_a+locate_b)

        def ins_jmp(mem_add,s):
    
                for k in mem_add:
                    if s[1] == k:
                        address = mem_add[k]
                address = convert_to_8bit(address)
                

                output.append("01111000"+ address)

        def ins_jlt(mem_add,s):
                for k in mem_add:
                    if s[1] == k:
                        address = mem_add[k]
                address = convert_to_8bit(address)
                

                output.append("10000000"+ address)

        def ins_jgt(mem_add,s):
                for k in mem_add:
                    if s[1] == k:
                        address = mem_add[k]
                address = convert_to_8bit(address)
                

                output.append("10001000"+ address)

        def ins_je(mem_add,s):
                for k in mem_add:
                    if s[1] == k:
                        address = mem_add[k]
                address = convert_to_8bit(address)
                

                output.append("10010000"+ address)
        
        def ins_hlt():
            output.append("1001100000000000")

        s = lines[i].split()
        if len(s)>0: 
            if len(s)>0 and s[0] == "add":
                #pc += 1
                ins_add(r,s)
            elif len(s)>0 and s[0] == "sub":
                #pc += 1
                ins_sub(r,s)
            elif len(s)>0 and s[0] == "mov":
                #pc += 1
                ins_mov(r,s)
            elif len(s)>0 and s[0] == "ld":
                #pc += 1
                ins_ld(r,s, mem_add)
            elif len(s)>0 and s[0] == "st":
                #pc += 1
                ins_st(r,s, mem_add)
            elif len(s)>0 and s[0] == "mul":
                #pc += 1
                ins_mul(r,s)
            elif len(s)>0 and s[0] == "div":
                #pc += 1
                ins_div(r,s)
            elif len(s)>0 and s[0] == "rs":
                #pc += 1
                ins_rs(r,s)
            elif len(s)>0 and s[0] == "ls":
                #pc += 1
                ins_ls(r,s)
            elif len(s)>0 and s[0] == "xor":
                #pc += 1
                ins_xor(r,s)
            elif len(s)>0 and s[0] == "or":
                #pc += 1
                ins_or(r,s)
            elif len(s)>0 and s[0] == "and":
                #pc += 1
                ins_and(r,s)
            elif len(s)>0 and s[0] == "not":
                #pc += 1
                ins_not(r,s)
            elif len(s)>0 and s[0] == "cmp":
                #pc += 1
                ins_cmp(r,s)
            elif len(s)>0 and s[0] == "jmp":
                flag = True
                #pc += 1
                ins_jmp(mem_add,s)
            elif len(s)>0 and s[0] == "jlt":
                flag = True
                #pc += 1
                ins_jlt(mem_add,s)
            elif len(s)>0 and s[0] == "jgt":
                flag = True
                #pc += 1
                ins_jgt(mem_add,s)
            elif len(s)>0 and s[0] == "je":
                flag = True
                #pc += 1
                ins_je(mem_add,s)
            elif len(s)>0 and s[0] == "hlt":
                #pc += 1
                ins_hlt()
            elif len(s)>0 and s[0] == "var":
                pass
            elif len(s)>0 and s[0][-1] == ":":
                if flag == True:
                    sub = s[1:]
                    if sub[0] == "add":
                        #pc += 1
                        ins_add(r,sub)
                    elif sub[0] == "sub":
                        #pc += 1
                        ins_sub(r,sub)
                    elif sub[0] == "mov":
                        #pc += 1
                        ins_mov(r,sub)
                    elif sub[0] == "ld":
                        #pc += 1
                        ins_ld(r,sub, mem_add)
                    elif sub[0] == "st":
                        #pc += 1
                        ins_st(r,sub, mem_add)
                    elif sub[0] == "mul":
                        #pc += 1
                        ins_mul(r,sub)
                    elif sub[0] == "div":
                        #pc += 1
                        ins_div(r,sub)
                    elif sub[0] == "rs":
                        #pc += 1
                        ins_rs(r,sub)
                    elif sub[0] == "ls":
                        #pc += 1
                        ins_ls(r,sub)
                    elif sub[0] == "xor":
                        #pc += 1
                        ins_xor(r,sub)
                    elif sub[0] == "or":
                        #pc += 1
                        ins_or(r,sub)
                    elif sub[0] == "and":
                        #pc += 1
                        ins_and(r,sub)
                    elif sub[0] == "not":
                        #pc += 1
                        ins_not(r,sub)
                    elif sub[0] == "cmp":
                        #pc += 1
                        ins_cmp(r,sub)
                    elif sub[0] == "hlt":
                        #pc += 1
                        ins_hlt()
                
                
for i in output:
    print(i) 
