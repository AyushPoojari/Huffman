#Imported library
import os
import gspread
gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1qGr0lGTK0r1GDyRR69A6PmBDvXzkI7IgTtJN0O3R5J4')
# Huffman Coding in python
#Taking text message as input
string = input("Enter the Text :")
#Variables
character_list = []
character_list2 = []
huffman_codes = []
f = 0
#Converting Ascii to Binary Equivalent
ascii_binary = ''.join(format(ord(i), '08b') for i in string)
#For string compressed text
file1 = open("compressed.txt", "a")
#For storing normal text
file2 = open("normal.txt", "a")
file2.write(f"{ascii_binary}")
file2.close()
# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)

# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d

# Calculating frequency
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
nodes = freq
while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])
#Huffman Characters
for char in freq:
    charachter = char
    character_list.append(char)
    f += 1
#Huffman Codes
for (char,frequency) in freq:
    codes = huffmanCode[char]
    huffman_codes.append(codes)
print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))

#We are getting tuple we want to access only characters (a,1) so (i,0)
for i in range(0,f):
    #print(character_list[i][0])
    character_list2.append(character_list[i][0])
    #file1.write(f"{character_list[i][0]}\n")

#Encoded Message:
for x in string:
    for k in range(0,len(character_list)):
        if( x == character_list[k][0]):
            #print(huffman_codes[k], end ='')
            file1.write(f"{huffman_codes[k]}\n")
file1.write("\n")
file1.close()
file_size2 = os.path.getsize('normal.txt')
print("\nFile Size of Normal File :", file_size2, "bytes")
file_size1 = os.path.getsize('compressed.txt')
print("\nFile Size of Compressed File :", file_size1, "bytes")
reduced_filesize = ((file_size2 - file_size1)/file_size2)*100
print(f"\nReduced Size : {reduced_filesize} %")
print(f"\nCompression Ratio:{(file_size1/file_size2)}")
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
    file1.close()

    print("\nThe Decompressed Text:")
    for i in range(0,len(temp)):
        print(f"{temp[i]}",end =" ")

decompress_yn = input("\nDo you want to decompress(Y/N):")
if(decompress_yn == 'Y' or decompress_yn == 'y'):
    decompress(character_list2,huffman_codes)
else:
    print("\nFile created without decompressing")
def listToString1(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1
def listToString2(s):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))

q = listToString1(character_list2)
p = listToString2(huffman_codes)

#Google Sheets for Database
worksheet = sh.sheet1
sh.sheet1.update_cell(3,1,f'{q}')
sh.sheet1.update_cell(3,2,f'{p}')

print("\n--Message Sent--")

