#problem 3 of cs50p (week0)
def convert():
    text=input("say something : ")
    text=text.replace(":)","🙂")
    text=text.replace(":(","🙁")
    print(text)

convert()
