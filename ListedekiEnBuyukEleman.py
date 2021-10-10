list=[1, 4, 360, 200, -1, 67, -11, -100]
enkucuk=list[0]
enbuyuk=list[0]
for eleman in list:
    if eleman<enkucuk:
        enkucuk=eleman
    if enbuyuk<eleman:
         enbuyuk=eleman
print('En kucuk eleman:',enkucuk)
print('En büyük eleman:',enbuyuk)