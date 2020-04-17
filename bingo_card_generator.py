#!/usr/bin/env python

import random, sys
import numpy as np

# check for the right # of args
if len(sys.argv) != 4:
    print("USAGE: " + sys.argv[0], " [file of terms] [output file] [# of cards]")
    print("Example: " + sys.argv[0] + " bingo_terms.txt bingo.html 20")
    sys.exit(1)

# read in the bingo terms
in_file = open(sys.argv[1], 'r')
terms = [line.strip() for line in in_file.readlines()]
terms = filter(lambda x: x != "", terms)
in_file.close()

print(terms)

gridSize = 5
minNum = 1
maxNum = 50
cards = 40
card = []

def card_gen():
    for h in range(cards):
        randRange = range(minNum, maxNum)
        card = random.sample(randRange, gridSize * gridSize)
        for i in range(gridSize):
            string = ""
            for j in range(gridSize):
                string +=  str(card[i + j * gridSize]) +','
            # print(string.split(','))
    return card


# XHTML4 Strict, y'all!
head = ("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">\n"
        "<html lang=\"en\">\n<head>\n"
        "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n"
        "<title>Bingo Cards</title>\n"
        "<style type=\"text/css\">\n"
        "\tbody { font-size: 12px; background-color:orange; font-family:'Verdana'; font-weight:bold;}\n"
        "\th1 { margin-left: 80px; text-align: center; font-size: 24px;font-family:'Verdana'; font-weight:bold; color:white; letter-spacing:2.7em;}\n"
        "\ttable { margin: 60px auto; border-spacing: 2px; }\n"
        "\t.newpage { page-break-after:always; }\n"
        "\ttr { height: 150px; }\n"
        "\th3 { font-size: 16px; font-family:'Verdana'; font-weight:bold;}\n"
        "\tp { font-size: 12px; font-family:'Verdana'; font-weight:bold;}\n"
        "\ttd { text-align: center; border: thin black solid; padding: 0px; width: 150px; color:white; }\n"
        "</style>\n</head>\n<body>\n")

# Generates an HTML table representation of the bingo card for terms
def generateTable(terms, pagebreak = True):
    ts = terms[:12] + ["FREE SPACE"] + terms[12:24]
    card = card_gen()
    card_idx = 0;
    if pagebreak:
        res = "<h1>" + "   B I N G O" + "</h1>"
        res += "<table class=\"newpage\">\n"
    else:
        res = "<h1>" + "B I N G O" + "</h1>"
        res += "<table>\n"
    for i, term in enumerate(ts):
        if term != 'FREE SPACE':
            term_num = card[card_idx]
            print(term)
        if i % 5 == 0:
            res += "\t<tr>\n"
        res += "\t\t<td><h3>" + str(term_num) + "</h3>\n"
        res += "\t\t<p>" + term + "</p></td>\n"
        if i % 5 == 4:
            res += "\t</tr>\n"
        card_idx +=1
    res += "</table>\n"
    
    return res

basename = 'bingo_card_'
cards = int(sys.argv[3])
for i in range(cards):
    filename= basename+str(i)+".html"
    out_file = open(filename, 'w')
    out_file.write(head)
    random.shuffle(terms)
    if i != cards - 1:
        out_file.write(generateTable(terms))
    else:
        out_file.write(generateTable(terms, False))
    out_file.write("</body></html>")
    out_file.close()
