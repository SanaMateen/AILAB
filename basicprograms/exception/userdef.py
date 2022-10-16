class passE(Exception):
    def passEx(mk):
        try:
            if(mk<40):
                raise passE("u didn't clear")
            else:
                print("congrats u have cleared the exam")
        except passE as pe:
            print(pe)

if __name__=="__main__":
    marks=int(input("enter ur marks:"))
    passE.passEx(marks)
