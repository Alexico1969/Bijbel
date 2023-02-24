books = ["Matteus", "Markus", "Lukas", "Handelingen", "Romeinen", "1 Korintiers", "2 Korintiers", "Galaten", "Efeziers", "Filippenzen", "Kolossenzen", "1 Tessalonicenzen", "2 Tessalonicenzen", "1 Timoteus", "2 Timoteus", "Titus", "Filemon", "Hebreeen", "Jakobus", "1 Petrus", "2 Petrus", "1 Johannes", "2 Johannes", "3 Johannes", "Judas", "Openbaring"]

def get_text():
    global books

    NT_data = {}

    for book in books:
        NT_data[book] = []

    line_list = []

    file = open("static/files/Nieuwe_Testament.txt", "r", encoding="utf-8")
    read = file.readlines()
    for line in read:
        line = line.replace('\ufeff','')
        line = line.replace('\n','')
        line = line.replace('\r','')
        line = line.replace('\t','')
        for c in range(len(line), 0, -1):
            if line[c-1] == " ":
                line = line[0:c-1]
            else:
                break
                
        line_list.append(line)
    
    print(line_list[0:10])            

    counter = 0

    for line in line_list:
        if line in books:
            counter += 1
            book = line
            print(f"Book: {book}")
        else:
            if len(line) > 0:
                NT_data[book].append(line)


    print()        
    print("Lukas, verse 1 - 10", NT_data["Lukas"][0:10])
    print()
    return NT_data

