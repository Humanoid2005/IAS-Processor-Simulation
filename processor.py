with open("outputfile.txt","r") as file_object:
    instructions = file_object.readlines()
    
#       a b c r n 1 1 -1 2 i
data = [0,1,0,0,8,1,1,-1,2,6]
memory = data + instructions

#data list stores variables
#memory = data + instructions -->memory implementation

PC = len(data)
MAR = ''
MBR = ''
IBR = ''
IR = ''
AC = 0
MQ = 0
runleft = True


while PC<len(memory):
    print("Fetch Cycle")
    MAR = bin(PC)
    print(f'PC : {PC}')
    print(f'MAR : {MAR}')
    print(f'MBR : {MBR}')
    print(f'IR : {IR}')
    print(f'IBR : {IBR}')
    print(f'AC : {AC:b}')
    print()

    MBR = memory[PC]
    IR = MBR[0:8]
    MAR = MBR[8:20]
    IBR = MBR[20:]
    
    print(f'PC : {PC+1}')
    print(f'MAR : {MAR}')
    print(f'MBR : {MBR}')
    print(f'IR : {IR}')
    print(f'IBR : {IBR}')
    print(f'AC : {AC:b}')
    print()

    if(runleft):
        print("Decode and Execute Cycle -> Left Instruction")
        print()
        
        if(IR == '00000001'):#LOAD M(X)
            MBR = bin(memory[int(MAR,2)])
            AC = int(MBR,2)

            print("LOAD M(X)")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()
            runleft = True
        
        elif(IR == '00001010'):#LOAD MQ
            AC = MQ

            print("LOAD MQ")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print(f'MQ : {MQ:b}')
            print()
            runleft = True
             
        elif(IR == '00001001'): #LOAD MQ,M(X)
            MBR = bin(memory[int(MAR,2)])
            MQ = memory[int(MAR,2)]

            print("LOAD MQ,M(X)")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print(f'MQ : {MQ:b}')
            print()
            runleft = True

        elif(IR == '000000010'):#LOAD -M(X)
            MBR = bin(memory[int(MAR,2)])
            AC = -1*int(MBR,2)

            print("LOAD -M(X)")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()
            runleft = True

        elif(IR == '00000001'):#LOAD |M(X)|
            MBR = bin(memory[int(MAR,2)])
            AC = abs(int(MBR,2))

            print("LOAD |M(X)|")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()
            runleft = True

        elif(IR == '00000100'):#LOAD -|M(X)|
            MBR = bin(memory[int(MAR,2)])
            AC = -1*abs(int(MBR,2))

            print("LOAD -|M(X)|")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()
            runleft = True
        
        elif(IR == '00100001'):#STOR M(X)
            MBR = bin(AC)
            memory[int(MAR,2)] = int(MBR,2)

            print("STOR M(X)")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print("Memory")
            for  i in range(len(memory)):
                print(f'{i} : {memory[i]}')
            print()
            runleft = True
        
        elif(IR == '00001101'):# JUMP M(X,0:19)
            PC = int(MAR,2)
            runleft = True
            continue

        elif(IR == '00001110'):#JUMP M(X,20:39)
            PC = int(MAR,2)
            runleft = False
            continue

        elif(IR == '00001111'):#JUMP+ M(X,0:19)
            print("JUMP +M(X,0:19)")
            if(AC>=0):
                PC = int(MAR,2)
                runleft = True
                continue
        
        elif(IR == '00010000'):#JUMP+ M(X,20:39)
            print("JUMP +M(X,20:39)")
            if(AC>=0):
                PC = int(MAR,2)
                runleft = False
                continue

        elif(IR == '00011000'):#DECR
            print("DECR ")
            n2 = memory[int(MAR,2)]
            MBR = bin(n2)

            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()

            memory[int(MAR,2)] = n2 - 1
            MBR = bin(n2-1)
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()

            runleft = True

        elif(IR == '00011110'): #COMP M(X)
            MBR = bin(memory[int(MAR,2)])
            print("COMP M(X)")
            n1 = memory[int(MAR,2)]
            if(n1<=AC):
                AC = 1 
            else:
                AC = -1 

            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()
            runleft = True
    
        elif(IR == '00000101'):#ADD M(X)
            MBR = bin(memory[int(MAR,2)])
            AC = AC + memory[int(MAR,2)]

            print("ADD M(X)")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()
            runleft = True

        elif(IR == '00000111'):# ADD |M(X)|
            MBR = bin(memory[int(MAR,2)])
            AC = AC + abs(memory[int(MAR,2)])

            print("ADD |M(X)|")
            print(f'PC : {PC}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()
            runleft = True

        elif(IR == '00000110'):# SUB M(X)
            MBR = bin(memory[int(MAR,2)])
            AC = AC - memory[int(MAR,2)]

            print("SUB M(X)")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}') 
            print()
            runleft = True
             
        elif(IR == '00001000'): # SUB |M(X)|
            MBR = bin(memory[int(MAR,2)])
            AC = AC - abs(memory[int(MAR,2)])

            print("SUB |M(X)|")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()
            runleft = True

        elif(IR =='00001011'): #MUL M(X)
            MBR = bin(memory[int(MAR,2)])
            AC = AC*MQ
            binary = bin(AC)
            mid = len(binary)//2
            ac = binary[0:mid]
            mq = binary[mid:]
            AC = int(ac,2)
            MQ = int(mq,2)

            print("MUL M(X)")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {binary[0:mid]}')
            print(f'MQ : {binary[mid:]}')
            print()
            runleft = True

        elif(IR == '00001100'): #DIV M(X)
            MBR = bin(memory[int(MAR,2)])
            MQ = AC%memory[int(MAR,2)]
            AC = AC//memory[int(MAR,2)]

            print("DIV M(X)")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR:b}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print(f'MQ : {MQ:b}')
            print()
            runleft = True

        elif(IR == '00010100'): #LSH
            AC = AC << 1

            print("LSH")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR:b}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()
            runleft = True

        elif(IR == '00010101'): #RSH
            AC = AC >> 1

            print("RSH")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR:b}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()
            runleft = True

        elif(IR == '00000000'): #HALT
            print("HALT")
            print(f'{memory[4]}th term of fibonacci sequence is {memory[3]}')
            runleft = True
            break

    
    if(IBR!= ''):
        print("Decode and execute right instruction")
        print()
        
        IR = IBR[0:8]
        MAR = IBR[8:]
        IBR = ''

        print(f'PC : {PC+1}')
        print(f'MAR : {MAR}')
        print(f'MBR : {MBR}')
        print(f'IR : {IR}')
        print(f'IBR : {IBR}')
        print(f'AC : {AC:b}')
        print()
            

        if(IR == '00000001'):#LOAD M(X)
            MBR = bin(memory[int(MAR,2)])
            AC = int(MBR,2)

            print("LOAD M(X)")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()
            runleft = True
    
        elif(IR == '00001010'):#LOAD MQ
            AC = MQ

            print("LOAD MQ")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print(f'MQ : {MQ:b}')
            print()
            runleft = True
             
        elif(IR == '00001001'): #LOAD MQ,M(X)
            MBR = bin(memory[int(MAR,2)])
            MQ = memory[int(MAR,2)]

            print("LOAD MQ M(X)")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print(f'MQ : {MQ:b}')
            print()
            runleft = True

        elif(IR == '000000010'):#LOAD -M(X)
            MBR = bin(memory[int(MAR,2)])
            AC = -1*int(MBR,2)

            print("LOAD -M(X)")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()
            runleft = True

        elif(IR == '00000001'):#LOAD |M(X)|
            MBR = bin(memory[int(MAR,2)])
            AC = abs(MBR)

            print("LOAD |M(X)|")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()
            runleft = True

        elif(IR == '00000100'):#LOAD -|M(X)|
            MBR = bin(memory[int(MAR,2)])
            AC = -1*abs(int(MBR,2))

            print("LOAD -|M(X)|")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()
            runleft = True
        
        elif(IR == '00100001'):#STOR M(X)
            MBR = bin(AC)
            memory[int(MAR,2)] = int(MBR,2)

            print("STOR M(X)")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print("Memory")
            for i in range(len(memory)):
                print(f'{i} : {memory[i]}')
            print()
            runleft = True
        
        elif(IR == '00001101'):# JUMP M(X,0:19)
            PC = int(MAR,2)
            runleft = True
            continue

        elif(IR == '00001110'):#JUMP M(X,20:39)
            PC = int(MAR,2)
            runleft = False
            continue

        elif(IR == '00001111'):#JUMP+ M(X,0:19)
            print("JUMP + M(X,0:19)")
            if(AC>=0):
                PC = int(MAR,2)
                continue
        
        elif(IR == '00010000'):#JUMP+ M(X,20:39)
            print("JUMP + M(X,20:39)")
            if(AC>=0):
                PC = int(MAR,2)
                runleft = False
                continue

        elif(IR == '00011000'):#DECR
            print("DECR ")
            n2 = memory[int(MAR,2)]
            MBR = bin(n2)

            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()

            memory[int(MAR,2)] = n2 - 1
            MBR = bin(n2-1)
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()

            runleft = True

        elif(IR == '00011110'): #COMP M(X)
            print("COMP M(X)")
            n1 = memory[int(MAR,2)]
            if(n1<=AC):
                AC = 1 
            else:
                AC = -1 

            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()
            runleft = True
        
        elif(IR == '00000101'):#ADD M(X)
            MBR = bin(memory[int(MAR,2)])
            AC = AC + memory[int(MAR,2)]

            print("ADD M(X)")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()
            runleft = True

        elif(IR == '00000111'):# ADD |M(X)|
            MBR = bin(memory[int(MAR,2)])
            AC = AC + abs(memory[int(MAR,2)])

            print("ADD |M(X)|")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR:b}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()
            runleft = True

        elif(IR == '00000110'):# SUB M(X)
            MBR = bin(memory[int(MAR,2)])
            AC = AC - memory[int(MAR,2)]

            print("SUB M(X)")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()
            runleft = True
             
        elif(IR == '00001000'): # SUB |M(X)|
            MBR = bin(memory[int(MAR,2)])
            AC = AC - abs(memory[int(MAR,2)])

            print("SUB |M(X)|")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()
            runleft = True

        elif(IR =='00001011'): #MUL M(X)
            MBR = bin(memory[int(MAR,2)])
            AC = AC*MQ
            binary = bin(AC)
            mid = len(binary)//2
            ac = binary[0:mid]
            mq = binary[mid:]
            AC = int(ac,2)
            MQ = int(mq,2)

            print("MUL M(X)")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {binary[0:mid]}')
            print(f'MQ : {binary[mid:]}')
            print()
            runleft = True

        elif(IR == '00001100'): #DIV M(X)
            MBR = bin(memory[int(MAR,2)])
            if(memory[int(MAR,2)] != 0):
                MQ = AC%memory[int(MAR,2)]
                AC = AC//memory[int(MAR,2)]

            print("DIV M(X)")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print(f'MQ : {MQ:b}')
            print()
            runleft = True

        elif(IR == '00010100'): #LSH
            AC = AC << 1

            print("LSH")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()
            runleft = True

        elif(IR == '00010101'): #RSH
            AC = AC >> 1
            
            print("RSH")
            print(f'PC : {PC+1}')
            print(f'MAR : {MAR}')
            print(f'MBR : {MBR}')
            print(f'IR : {IR}')
            print(f'IBR : {IBR}')
            print(f'AC : {AC:b}')
            print()
            runleft = True

        elif(IR == '00000000'): #HALT
            print("HALT")
            print(f'{memory[4]}th term of fibonacci sequence is {memory[3]}')
            runleft = True
            break
        
    PC = PC + 1

