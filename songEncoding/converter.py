import sys

# Convert old manual-encoded songs to vixen csv export format

ON = 255
OFF = 0

with open(sys.argv[1], 'r') as f:
    with open(sys.argv[2], 'w') as f1:
        seq_data = f.readlines()
        newRow = ["0"] * 7
        printLines = []
        for i in range(1,len(seq_data)):
            origRow = seq_data[i].rstrip().split(",")
            #print(origRow)
            time = origRow[0]
            if newRow[0] != time: # if the time of the new line changes we have completed converting the current millis so we write the line to the new file and continue with a new empty array for the new millis
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
            


                