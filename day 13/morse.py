code = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.",
        "H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.",
        "Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..",
        "_":"..--",',':".-.-",".":"---.","?":"----"}


decode = {".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G",
          "....":"H","..":"I",".---":"J","-.-":"K",".-..":"L","--":"M","-.":"N","---":"O",".--.":"P",
          "--.-":"Q",".-.":"R","...":"S","-":"T","..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z",
          "..--":"_",".-.-":',',"---.":".","----":"?"}


def decrypt(str):
    morse =""
    sufix = []

    for char in str:
        morse += code[char]
        sufix.append(len(code[char]))

    sufix = list(reversed(sufix))
    ans = ""
    prev = 0
    for i in range(len(sufix)):
        ans += decode[morse[prev:prev+sufix[i]]]
        prev = prev+sufix[i]

    return ans


n = int(input().strip())


for j in range(n):
    stri = input().strip()
    print(str(j+1)+': '+ decrypt(stri))
