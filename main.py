
#Question at column
A = []
#Type at column
B = []
#Description at column
C = []
#Answer starts at column
D = []
E =[]
F = []
G = []
H = []
#Required at column
I = []
#Add other at column
J = []
#Correct answer at column
K = []
#Points at column
L =[]
#Correct answer feedback at column
M =[]
#Correct answer URL at column
N = []
#Incorrect answer feedback at column
O = []
#Incorrect answer URL at column
P = []


li = []
liq = []

count = 0

## 진행 순서
## 1 = 문제
## 2 = 문제설명
## 3 = 보기
## 4 = 정답
## 5 = 정답,커뮤니티 투표

proceed = 0

with open('q.txt', 'r', encoding='utf-8') as file:
    # contents = file.read()
    
    
    for i in file.readlines():
    
        if proceed == 0:
            if "질문 #" in i:
                A.append(i)
                C.append("")
                proceed = 1
                continue
        if proceed == 1:
            if "A." in i:
                proceed = 2
            else:
                C[-1] += i
        if proceed == 2:
            
            if "정답:" in i:
                print(i)
                print(D[-1])
                # print(E[-1])
                # print(F[-1])
                # print(G[-1])
                # print(H[-1])
                if len(G) > len(H):
                    H.append("")
                proceed = 3
            else:
                if "A." in i:
                    D.append(i)
                elif "B." in i:
                    E.append(i)
                elif "C." in i:
                    F.append(i)
                elif "D." in i:
                    G.append(i)
                    H.append("")
                elif "E." in i:
                    H[-1] += i
                    
  

        if proceed == 3:
            if "정답:" in i:
                proceed = 0
        
                # temp = i.split(" : ")
                # temp2 = temp.split()
                
                M.append("")
                N.append("")
                O.append("")
                P.append("")

print(len(A))
print(len(B))
print(len(C))
print(len(D))
print(len(E))
print(len(F))
print(len(G))
print(len(H))
print(len(I))
print(len(J))
print(len(K))
print(len(L))
print(len(M))
print(len(N))
print(len(O))
print(len(P))


# while True:
#     if '#' in contents:
#         key, value = contents.split('#')
#         dic[key] = value
#         contents = contents.replace(key + '=', '')
#     else:
#         break

# print(contents)

x = []
y = []
if len(x) == len(y):
    print("ADSfasdfasd")