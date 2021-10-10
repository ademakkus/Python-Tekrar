def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
text = input("Herhangi bir metin giriniz: ")
sayac = ""
for harf in text:
    if harf not in sayac:
        sayac += harf
for harf in sayac:
    print("{} harfi {} kelimesinde {} kez geçiyor!".
          format(harf,text,text.count(harf)))
result=word_count(text)
print("{} metni {} kelimeden oluşuyor.".format(text,result))