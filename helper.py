books = ["Matteus", "Markus", "Lukas", "Handelingen", "Romeinen", "1 Korinthiers", "2 Korinthiers", "Galaten", "Efeziers", "Filippenzen", "Kolossenzen", "1 Tessalonicenzen", "2 Tessalonicenzen", "1 Timotheus", "2 Timotheus", "Titus", "Filemon", "Hebreeen", "Jakobus", "1 Petrus", "2 Petrus", "1 Johannes", "2 Johannes", "3 Johannes", "Judas", "Openbaring"]
nr_of_chapters = [28, 16, 24, 21, 16, 16, 13, 6, 6, 4, 4, 5, 3, 6, 4, 3, 1, 13, 5, 5, 3, 5, 1, 1, 22]

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
    
    counter = 0

    for line in line_list:
        if line in books:
            counter += 1
            book = line
            print(f"Processing book {book}")
        else:
            if len(line) > 0:
                line_split = line.split(" ")
                if len(line_split) == 2 and line_split[0] == book:
                    line = f"<h5 class='chapter' id='ch{line_split[1]}'>" + line + "</h5>"
                NT_data[book].append(line)

    return NT_data

