import gspread
import time
start = time.time()
gc = gspread.service_account(filename='add ur json file')

sh = gc.open_by_key('add ur key')

worksheet = sh.sheet1

key = sh.sheet1.cell(3,1).value

value = sh.sheet1.cell(3,2).value

list1 = []

for i in key:
    list1.append(i)

def Convert(string):
    li = list(string.split(" "))
    return li

#list1 = Convert(key)

list2 = Convert(value)

# print(list1)
#
# print(list2)

def decompress(listk,listv):
     temp = []
     f = open('compressed.txt','r')
     #print(listk)
     #print(listv)
     while True:
         line = f.readline()
         if not line:
            break
         else:
              for i in range(0,len(listv)):
                  if(line == f'{listv[i]}\n'):
                      temp.append(listk[i])
                      #print(listk[i],end =" ")
     f.close()

     print("\nThe Decoded Text:")
     for i in range(0,len(temp)):
         print(f"{temp[i]}",end =" ")

print("\n--Message Received--")
decompress(list1,list2)
end = time.time()
print(end - start)
