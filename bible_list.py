import json

szGAEBook = []
szGAEBook.append(["창세기", "gen", "1", "9"])

# szGAEBook.append(["창세기", "gen", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50"])
# szGAEBook.append(["출애굽기", "exo", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40"])
# szGAEBook.append(["레위기", "lev", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27"])
# szGAEBook.append(["민수기", "num", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"])
# szGAEBook.append(["신명기", "deu", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34"])
# szGAEBook.append(["여호수아", "jos", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"])
# szGAEBook.append(["사사기", "jdg", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"])
# szGAEBook.append(["룻기", "rut", "1", "2", "3", "4"])
# szGAEBook.append(["사무엘상", "1sa", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"])
# szGAEBook.append(["사무엘하", "2sa", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"])
# szGAEBook.append(["열왕기상", "1ki", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"])
# szGAEBook.append(["열왕기하", "2ki", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"])
# szGAEBook.append(["역대상", "1ch", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29"])
# szGAEBook.append(["역대하", "2ch", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"])
# szGAEBook.append(["에스라", "ezr", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
# szGAEBook.append(["느헤미야", "neh", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"])
# szGAEBook.append(["에스더", "est", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
# szGAEBook.append(["욥기", "job", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42"])
# szGAEBook.append(["시편", "psa", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120", "121", "122", "123", "124", "125", "126", "127", "128", "129", "130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "140", "141", "142", "143", "144", "145", "146", "147", "148", "149", "150"])
# szGAEBook.append(["잠언", "pro", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"])
# szGAEBook.append(["전도서", "ecc", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
# szGAEBook.append(["아가", "sng", "1", "2", "3", "4", "5", "6", "7", "8"])
# szGAEBook.append(["이사야", "isa", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66"])
# szGAEBook.append(["예레미야", "jer", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52"])
# szGAEBook.append(["예레미야애가", "lam", "1", "2", "3", "4", "5"])
# szGAEBook.append(["에스겔", "ezk", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48"])
# szGAEBook.append(["다니엘", "dan", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
# szGAEBook.append(["호세아", "hos", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"])
# szGAEBook.append(["요엘", "jol", "1", "2", "3"])
# szGAEBook.append(["아모스", "amo", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
# szGAEBook.append(["오바댜", "oba", "1"])
# szGAEBook.append(["요나", "jnh", "1", "2", "3", "4"])
# szGAEBook.append(["미가", "mic", "1", "2", "3", "4", "5", "6", "7"])
# szGAEBook.append(["나훔", "nam", "1", "2", "3"])
# szGAEBook.append(["하박국", "hab", "1", "2", "3"])
# szGAEBook.append(["스바냐", "zep", "1", "2", "3"])
# szGAEBook.append(["학개", "hag", "1", "2"])
# szGAEBook.append(["스가랴", "zec", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"])
# szGAEBook.append(["말라기", "mal", "1", "2", "3", "4"])
# szGAEBook.append(["마태복음", "mat", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"])
# szGAEBook.append(["마가복음", "mrk", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"])
# szGAEBook.append(["누가복음", "luk", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"])
# szGAEBook.append(["요한복음", "jhn", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"])
# szGAEBook.append(["사도행전", "act", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"])
# szGAEBook.append(["로마서", "rom", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"])
# szGAEBook.append(["고린도전서", "1co", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"])
# szGAEBook.append(["고린도후서", "2co", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"])
# szGAEBook.append(["갈라디아서", "gal", "1", "2", "3", "4", "5", "6"])
# szGAEBook.append(["에베소서", "eph", "1", "2", "3", "4", "5", "6"])
# szGAEBook.append(["빌립보서", "php", "1", "2", "3", "4"])
# szGAEBook.append(["골로새서", "col", "1", "2", "3", "4"])
# szGAEBook.append(["데살로니가전서", "1th", "1", "2", "3", "4", "5"])
# szGAEBook.append(["데살로니가후서", "2th", "1", "2", "3"])
# szGAEBook.append(["디모데전서", "1ti", "1", "2", "3", "4", "5", "6"])
# szGAEBook.append(["디모데후서", "2ti", "1", "2", "3", "4"])
# szGAEBook.append(["디도서", "tit", "1", "2", "3"])
# szGAEBook.append(["빌레몬서", "phm", "1"])
# szGAEBook.append(["히브리서", "heb", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"])
# szGAEBook.append(["야고보서", "jas", "1", "2", "3", "4", "5"])
# szGAEBook.append(["베드로전서", "1pe", "1", "2", "3", "4", "5"])
# szGAEBook.append(["베드로후서", "2pe", "1", "2", "3"])
# szGAEBook.append(["요한1서", "1jn", "1", "2", "3", "4", "5"])
# szGAEBook.append(["요한2서", "2jn", "1"])
# szGAEBook.append(["요한3서", "3jn", "1"])
# szGAEBook.append(["유다서", "jud", "1"])
# szGAEBook.append(["요한계시록", "rev", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"])

# print(szGAEBook)

#create dictionary
bible_title_chapters_dict = {}

for i in szGAEBook:
    chapters = []
    for n in range(2,len(i)):
        chapters.append(i[n])
    one_book = {'eng': i[1], 'chapters':chapters}
    bible_title_chapters_dict[i[0]] = one_book
