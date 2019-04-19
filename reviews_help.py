
def main():
    neg = open("negative_reviews.txt", 'r') #opens the two movie review files
    pos = open("positive_reviews.txt", 'r')
    negfile = neg.readlines() #reads the files
    posfile = pos.readlines()
    neg.close()
    pos.close()

    def phraseorbatch():
        phrasebatch = input("Do you want to enter a (p)hrase or a (b)atch file?(p/b): ").lower()
        if phrasebatch == "p":
            sentiment(phrase_in())
        elif phrasebatch == 'b':
            sentiment(batch())

    def batch():
        batchfile = input("Enter the name of your batch file:\n")
        openbatch = open(batchfile, 'r')
        filesave = openbatch.readlines()
        openbatch.close()
        return filesave

    def phrase_in():
        phrase = input("please enter a phrase:")
        phrase_split = phrase.split()
        return phrase_split

    def counting(e):
        negcountot = 0
        poscountot = 0
        sentimenttotal = 0
        for word in e:
            word.rstrip(" ")
            print(word)
            negcount = negfile.count(word)
            poscount = posfile.count(word)
            poscountot += poscount
            negcountot += negcount
            print(negcountot)
        try:
            sentimenttotal = (poscountot - negcountot) / (poscountot + negcountot)
        except ZeroDivisionError:
            sentimenttotal = 0
        return sentimenttotal

    def sentiment(phrase):
        sent = counting(phrase)
        if sent >= 0:
            print('Sentiment score:', sent)
            print("That has a positive sentiment")
        elif sent < 0:
            print('Sentiment score:', sent)
            print('That has a negative sentiment')
    phraseorbatch()
main()
