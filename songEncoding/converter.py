import sys

ON = 255
OFF = 0

with open("./jinglebells.csv", 'r') as f:
    with open("jingleNEW.csv", 'w') as f1:
        seq_data = f.readlines()
        newRow = [0] * 7
        printLines = []
        for i in range(len(seq_data)):
            origRow = seq_data[i].rstrip().split(",")
            #print(origRow)
            time = origRow[0]
            if newRow[0] != time:
                #print(newRow)
                printLine = ''
                for col in newRow:
                    printLine = printLine + str(col) + ","
                printLine = printLine[:-1]
                #printLines.append(printLine)
                f1.write(printLine+"\n")
                newRow = [0] * 7
                newRow[0] = time
            if origRow[2] == "1" and (origRow[1]) < "7":
                #print(int(origRow[1]))
                newRow[int(origRow[1])] = ON
        #f1.write(printLines)
            


                