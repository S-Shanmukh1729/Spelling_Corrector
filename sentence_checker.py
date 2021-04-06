## Scentence corrector
import requests
word=input("Enter sentence: ")
#x=len(word.split())
urls="https://www.google.com/search?q="+word+"&oq="+word+"&aqs=chrome..69i57j46i10j0i10l7.3288j0j9&sourceid=chrome&ie=UTF-8"
x=requests.get(urls)
zz=str(x.content)
ss='''href="/search?ie'''
y=zz.find(ss)
ls1=zz[y:].split("&amp")
z=ls1[1][3:].split("+")
final=" ".join(z)
if '%' in final:
    print("corrected word is:", word)
else:
    print("corrected word is:",final)
