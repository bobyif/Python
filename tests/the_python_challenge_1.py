alphabet = ["a", "b", "c", "d", "e", "f", "g", 'h','i',"j", 'k', "l", 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',"u", 'v',"w", 'x', 'y', 'z']

user_input = input("")

x = ""
for l in user_input:
    if l == ".":
        l = "."
        x = x + l
        continue
        
    if l == "y":
        l = "a"
        x = x + l
        continue
    if l == "(":
        l = "("
        x = x + l
        continue
    if l == ")":
        l = ")"
        x = x + l
        continue
    if l == "z":
        l = "b"
        x = x + l
        continue
    if l == " ":
        l = " "
        x = x + l
        continue
    if l in alphabet:
        index = alphabet.index(l)
        l = alphabet[index+2]
        x = x + l

    print(x)



#g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.