# import matplotlib.pyplot as plt;
# import numpy as np;
import array;

print ("Capulus Programming Launguage")
print ("Created by Branch.exe 2020\n")

store = {}
terminal = ""
checkTrue = False;

    
#       ~~~~~ Functions ~~~~~
    

def prnt(terminal, store):


    #colors
    reset = "\u001b[0m";
    black = "\u001b[30m";
    red = "\u001b[31m";
    green = "\u001b[32m";
    yellow = "\u001b[33m";
    blue = "\u001b[34m";
    magenta = "\u001b[35m";
    cyan = "\u001b[36m";
    white = "\u001b[37m";

    val1 = 0;
    val2 = 0;
    search = 0;
    index = 0;
    color = "";
    var = "";
    actualVar = "";
    varLocation = 0;
    word = "";
    checkWord = "";
    if "{" and "}" in terminal:
        val1 = terminal.find("{");
        varLocation = terminal.find("{");
        val2 = terminal.find("}");

        search = val1;

        while search < val2-1:
            search+=1;
            checkWord+=terminal[search];
            if search == val2-1:
                #print(word);
                var = checkWord;
                actualVar = store[var];
                
        val1=0;
        val2=0;
        search=0;
        word="";


    if "(" and ")" in terminal:
        val1 = terminal.find("(");
        val2 = terminal.find(")");

        search = val1;

        while search < val2-1:
            search+=1;
            word+=terminal[search];
            if search == val2-1:
                #print(word);
                color = word;
        val1=0;
        val2=0;
        search=0;
        word="";



    if "\"" in terminal:
        while index < len(terminal):
            if index < 1:
                index = terminal.find("\"", index);
                if index == -1:
                    break;
                val1 = index;
            else:
                index = terminal.find("\"", index);
                if index == -1:
                    break;
                val2 = index;
            index += 1;
    
    search = val1;
    word = "";
    while search < val2-1:
        search += 1;
        word += terminal[search];

        if search == val2-1:
            if checkWord != "":
                word = word.replace("{" + checkWord + "}", "");
                word = (word[:varLocation] + str(store[var]) + word[varLocation:]);
            
            #color decision
            if color != "":
                if color == "red":
                    print(red+word+reset);
                if color == "black":
                    print(black+word+reset);
                if color == "green":
                    print(green+word+reset);
                if color == "yellow":
                    print(yellow+word+reset);
                if color == "blue":
                    print(blue+word+reset);
                if color == "magenta":
                    print(magenta+word+reset);
                if color == "cyan":
                    print(cyan+word+reset);
                if color == "white":
                    print(white+word+reset);

                #capitals
                if color == "RED":
                    print(red+word+reset);
                if color == "BLACK":
                    print(black+word+reset);
                if color == "GREEN":
                    print(green+word+reset);
                if color == "YELLOW":
                    print(yellow+word+reset);
                if color == "BLUE":
                    print(blue+word+reset);
                if color == "MAGENTA":
                    print(magenta+word+reset);
                if color == "CYAN":
                    print(cyan+word+reset);
                if color == "WHITE":
                    print(white+word+reset);


            else:
                print(word);

#~~~~~ graphing ~~~~~~~
# def trig(terminal):
#     x = np.linspace(0, 10, 100);
#     y = 0;

#     index = 0;
#     val1 = 0;
#     val2 = 0;
#     search = 0;
#     word = "";
#     var = "";

#     if "\"" in terminal:
#         while index < len(terminal):
#             if index < 1:
#                 index = terminal.find("\"", index);
#                 if index == -1:
#                     break;
#                 val1 = index;
#             else:
#                 index = terminal.find("\"", index);
#                 if index == -1:
#                     break;
#                 val2 = index;
#             index += 1;
    
#     search = val1;
#     numbers = 0;
#     while search < val2-1:
#         search += 1;
#         word += terminal[search];

# #       ~~~~~~~~~~~~~~~~~~~cos~~~~~~~~~~~~~~~~~~
#         if "sin" in word:
#             word = "";
#             if "(" and ")" in terminal:
#                 val1 = terminal.find("(");
#                 val2 = terminal.find(")");
#                 search = val1;
#             while search < val2-1:
#                 search+=1;
#                 word+=terminal[search];
#                 if search == val2-1:
#                     print(word);    
#             y = np.sin(eval(word));
#             val1=0;
#             val2=0;
#             search=0;
# #       ~~~~~~~~~~~~~~~~~~~tan~~~~~~~~~~~~~~~~~~
#         elif "tan" in word:
#             word = "";
#             if "(" and ")" in terminal:
#                 val1 = terminal.find("(");
#                 val2 = terminal.find(")");
#                 search = val1;
#             while search < val2-1:
#                 search+=1;
#                 word+=terminal[search];
#                 if search == val2-1:
#                     print(word);    
#             y = np.tan(eval(word));
#             val1=0;
#             val2=0;
#             search=0;
# #       ~~~~~~~~~~~~~~~~~~~cos~~~~~~~~~~~~~~~~~~
#         elif "cos" in word:
#             word = "";
#             if "(" and ")" in terminal:
#                 val1 = terminal.find("(");
#                 val2 = terminal.find(")");
#                 search = val1;
#             while search < val2-1:
#                 search+=1;
#                 word+=terminal[search];
#                 if search == val2-1:
#                     print(word);    
#             y = np.cos(eval(word));
#             val1=0;
#             val2=0;
#             search=0;
#     plt.plot(x,y);
#     plt.show();
    
# def graf(terminal):
#     x = np.linspace(0, 10, 100);
#     y = 0;
#     index = 0;
#     val1 = 0;
#     val2 = 0;
#     search = 0;
#     word = "";
#     if "\"" in terminal:
#         while index < len(terminal):
#             if index < 1:
#                 index = terminal.find("\"", index);
#                 if index == -1:
#                     break;
#                 val1 = index;
#             else:
#                 index = terminal.find("\"", index);
#                 if index == -1:
#                     break;
#                 val2 = index;
#             index += 1;
#     search = val1;
#     numbers = 0;
#     while search < val2-1:
#         search += 1;
#         word += terminal[search];
#     y  += eval(word);
#     plt.plot(x,y);
#     plt.show();

#       ~~~~~~~~~~~~~~~~~~~~~~~~~~vARIABLEAS~~~~~~~~~~~~~~~~~~~~~~~~~~
def storage(terminal, store):    
    name = "";
    val1 = 0;
    val2 = 0;
    search = 0;
    index = 0;
    word = "";
    if "(" and ")" in terminal:
        val1 = terminal.find("(");
        val2 = terminal.find(")");
        search = val1;
        while search < val2-1:
            search+=1;
            word+=terminal[search];
            if search == val2-1:
                name = word;      
        val1=0;
        val2=0;
        search=0;
        word="";
    if "\"" in terminal:
        while index < len(terminal):
            if index < 1:
                index = terminal.find("\"", index);
                if index == -1:
                    break;
                val1 = index;
            else:
                index = terminal.find("\"", index);
                if index == -1:
                    break;
                val2 = index;
            index += 1;
    search = val1;
    word = ""
    while search < val2-1:
        search += 1;
        word += terminal[search]; 
    
    store[name] = word;
    #print(store[name]);

def inpt(terminal, store):    
    name = "";
    val1 = 0;
    val2 = 0;
    search = 0;
    index = 0;
    word = "";
    inVar = "";
    if "(" and ")" in terminal:
        val1 = terminal.find("(");
        val2 = terminal.find(")");
        search = val1;
        while search < val2-1:
            search+=1;
            word+=terminal[search];
            if search == val2-1:
                name = word;      
        val1=0;
        val2=0;
        search=0;
        word="";
    if "\"" in terminal:
        while index < len(terminal):
            if index < 1:
                index = terminal.find("\"", index);
                if index == -1:
                    break;
                val1 = index;
            else:
                index = terminal.find("\"", index);
                if index == -1:
                    break;
                val2 = index;
            index += 1;
    search = val1;
    word = ""
    while search < val2-1:
        search += 1;
        word += terminal[search]; 
    inVar = input(word);
    store[name] = inVar;
    #print(store[name]);


                






def rept(terminal):
    index = 0;
    val1 = 0;
    val2 = 0;
    search = 0;
    word = "";
    repeatCount = 0;
    if "<" and ">" in terminal:
        val1 = terminal.find("<");
        val2 = terminal.find(">");
        search = val1;
        while search < val2-1:
            search+=1;
            word+=terminal[search];
            if search == val2-1:
                repeatCount = int(word);

        for x in range(0,repeatCount-1):
            if "print" in terminal or "PRINT" in terminal:
                prnt(terminal, store);
        

            #graphing
            # if "graph" in terminal or "GRAPH" in terminal:
            #     graf(terminal);
                

            # if "trig" in terminal or "TRIG" in terminal:
            #     trig(terminal)
                

            #variables
            if "set" in terminal or "SET" in terminal:
                storage(terminal, store);

            if "input" in terminal or "INPUT" in terminal:
                inpt(terminal, store);


#           ~~~~~~~~~~~~~~~goto~~~~~~~~~~~~~~~
def goto(terminal):
    index = 0;
    val1 = 0;
    val2 = 0;
    search = 0;
    terminalEmulator = "";
    word = "";
    if "<" and ">" in terminal:
        val1 = terminal.find("<");
        val2 = terminal.find(">");
        search = val1;
        while search < val2-1:
            search+=1;
            word+=terminal[search];   

        file = open('par.txt');
        lines = file.readlines()
        index = 0;
        for line in lines:
            index += 1;
            terminalEmulator = lines[index];
            if ":" + word in terminalEmulator:
                return index;


#       ~~~~~~~~~~~~~~~~Logic Check~~~~~~~~~~~~~~~~
            


def ifCheck(terminal, store, lines):
    beforeEdit = terminal;
    name = "";
    val1 = 0;
    val2 = 0;
    search = 0;
    index = 0;
    word = "";
    checkValue = "";
    if "(" and ")" in terminal:
        val1 = terminal.find("(");
        val2 = terminal.find(")");
        search = val1;
        while search < val2-1:
            search+=1;
            word+=terminal[search];
            if search == val2-1:
                name = word;      
        val1=0;
        val2=0;
        search=0;
        word="";

    if "<" and ">" in terminal:
        val1 = terminal.find("<");
        val2 = terminal.find(">");
        search = val1;
        while search < val2-1:
            search+=1;
            word+=terminal[search];
            if search == val2-1:
                checkValue = word;

        val1=0;
        val2=0;
        search=0;
        word="";

    
    if "\"" in terminal:
        while index < len(terminal):
            if index < 1:
                index = terminal.find("\"", index);
                if index == -1:
                    break;
                val1 = index;
            else:
                index = terminal.find("\"", index);
                if index == -1:
                    break;
                val2 = index;
            index += 1;
    search = val1;
    word = ""
    while search < val2-1:
        search += 1;
        word += terminal[search]; 
    if store[name] == checkValue:
        terminal = word;
        return terminal;
    else:
        return lines[lineIndex+1];
        
        #allMain(terminal)




#print
def allMain(terminal):
    if "print" in terminal or "PRINT" in terminal:
        prnt(terminal, store);
        

    
    # if "graph" in terminal or "GRAPH" in terminal:
    #     graf(terminal);
        

    # if "trig" in terminal or "TRIG" in terminal:
    #     trig(terminal)
        

    #variables
    if "set" in terminal or "SET" in terminal:
        storage(terminal, store);

    if "input" in terminal or "INPUT" in terminal:
        inpt(terminal, store);

    if "repeat" in terminal or "REPEAT" in terminal:
        rept(terminal)
    

        



#       ~~~~~~~~~~~~~~~~~~~main stuff~~~~~~~~~~~~~~~


parse = open('par.txt')
lines = parse.readlines()
lineIndex = 0;
for i in lines:
    try:
        terminal = lines[lineIndex];
        if "if" in terminal or "IF" in terminal:
            terminal = ifCheck(terminal, store, lines[lineIndex])
            if "goto" in terminal or "GOTO" in terminal:
                lineIndex = goto(terminal)
                terminal = lines[lineIndex]
        
        if "goto" in terminal or "GOTO" in terminal:
            lineIndex = goto(terminal)
            terminal = lines[lineIndex]
        allMain(terminal)
        lineIndex += 1;
    except IndexError:
        pass
    