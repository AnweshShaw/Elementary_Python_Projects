word = input("\nEnter a name in English: ").lower()
translated_word=""
i=0
while(i<len(word)):
    if word[i]=="s" and word[i+1]=="h":
        translated_word += chr(2358)
        i+=1
    elif word[i]=="c" and word[i+1]=="h":
        translated_word += chr(2330)
        i += 1
    elif word[i]=="d" and word[i+1]=="h":
        translated_word += chr(2343)
        i += 1
    #elif word[i]=="k" and word[i+1]=="h":
        #translated_word += chr(2331)
        #i += 1
    elif word[i]=="j" and word[i+1]=="h":
        translated_word += chr(2333)
        i += 1
    elif (word[i] == "t"):
        translated_word += chr(2340)
    elif word[i]=="t" and word[i+1]=="h":
        translated_word += chr(2341)
        i += 1
    elif word[i] == "g" and word[i + 1] == "h":
        translated_word += chr(2328)
        i += 1
    elif word[i]=="b" and word[i+1]=="h":
        translated_word += chr(2349)
        i += 1
    elif word[i]=="o" and word[i+1]=="o":
        translated_word += chr(2370)
        i += 1
    elif word[i]=="n" and word[i-1]=="i":
        translated_word += chr(2306)
    else:
        if (word[i]=="a" and not(i==0)):
            translated_word += chr(2366)
        elif (word[i] == "a"):
            translated_word += chr(2309)
        elif (word[i] == "b"):
            translated_word += chr(2348)
        elif (word[i] == "c" or word[i] == "k"):
            translated_word += chr(2325)
        elif (word[i] == "d"):
            translated_word += chr(2342)
        elif (word[i]=="e" and not(i==0)):
            translated_word += chr(2375)
        elif (word[i] == "e"):
            translated_word += chr(2319)
        elif (word[i] == "f"):
            translated_word += chr(2347)
        elif (word[i] == "g"):
            translated_word += chr(2327)
        elif (word[i] == "h"):
            translated_word += chr(2361)
        elif (word[i]=="i" and not(i==0)):
            translated_word += chr(2368)
        elif (word[i] == "i"):
            translated_word += chr(2311)
        elif (word[i] == "j"):
            translated_word += chr(2332)
        elif (word[i] == "l"):
            translated_word += chr(2354)
        elif (word[i] == "m"):
            translated_word += chr(2350)
        elif (word[i] == "n"):
            translated_word += chr(2344)
        elif (word[i]=="o" and not(i==0)):
            translated_word += chr(2379)
        elif (word[i] == "o"):
            translated_word += chr(2323)
        elif (word[i] == "p"):
            translated_word += chr(2346)
        elif (word[i] == "q"):
            translated_word += chr(2326)
        elif (word[i] == "r"):
            translated_word += chr(2352)
        elif (word[i] == "s"):
            translated_word += chr(2360)
        elif (word[i]=="u" and not(i==0)):
            translated_word += chr(2369)
        elif (word[i] == "u"):
            translated_word += chr(2313)
        elif (word[i] == "v" or word[i] == "w"):
            translated_word += chr(2357)
        elif (word[i] == "x"):
            translated_word += chr(2395)
        elif (word[i] == "y"):
            translated_word += chr(2351)
        elif (word[i] == "z"):
            translated_word += chr(2395)
        else:
            translated_word += " "
    i+=1
print(f"\nYour name in Hindi is: {translated_word}")