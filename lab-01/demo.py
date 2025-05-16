x = 10                      #Biến x lưu trữ giá trị số nguyên 10
name = " Alice "            #Biến name lưu trữ chuỗi "Alice"
is_valid = True             #Biến is_valid lưu trữ giá trị boolean True

if = 5 #Lỗi " if" là từ khoá , không thể sử dụng làm tên biến

#Cộng(+)
a=5
b=3
result = a+b # Kết quả : 8

#Trừ(-)
a=8
b=4
result = a-b # Kết quả : 4

#Nhân(*)
a=6
b=7
result = a*b # Kết quả : 42

#Chia(/)
a=20
b=5
result = a/b # Kết quả : 4

#Chia lấy phần nguyên(//)
a=20
b=3
result = a//b # Kết quả : 6

#Chia lấy dư(%)
a=20
b=7
remainder = a%b # Kết quả: 6

#Luỹ thừa(**)
a=2
b=3
result = a ** b # Kết quả: 8 

#Phép toán AND
x=5
y=3
result = (x >2 ) and (y< 4) # Kết quả: true

#Phép toán OR
x=5
y=3
result = (x>2) (y<4) #Kết quả: True

#Phép toán NOT
x=5
result = not (x==5) # Kết quả : False

#Phép so sánh bằng(==)
x=5
result = (x==5) # Kết quả : True

#Phép so sánh không bằng(!=)
x=5
result = (x!=3) # Kết quả : True

#Phép so sánh lớn hơn(>) nhỏ hơn (<)
x=5
result1 = (x>3) # Kết quả : True
result2 = (x<3) # Kết quả : False

#Hàm "input()"
name = input("Nhập tên của bạn :")
print("Xin chào,",name)

#Hàm "print()"
age = 25
print("tuổi của bạn là:", age)

#"sep"(ký tự phân cách) "end"(ký tự kết thúc)
print("Python","là", "ngôn","ngữ","lập","trình",sep="_")
# Kết quả: Python-là-ngôn-ngữ-lập-trình
print("Xin chào", end="_")
print("các bạn!") # Kết quả : Xin chào các bạn!

# Câu lệnh điều kiện(Condination Statements)
x=10
if x>5 ;
print ("x lớn hơn 5")
elif x==5;
print("x bằng 5")
else:
    print("x nhỏ hơn 5")

#Vòng lặp for
fruits = ["apple", "banana" , "cherry"]
for fruit in fruits :
    print(fruit)

#Vòng lặp white
count =0
white count < 5;
print(count)
count +=1

# Câu lệnh nhảy(Jump Statenments)
#break
#Tìm số chia hết cho 5 đầu tiên trong khoảng từ 1 đến 100
for i in range(1,100):
    if i%5 ==0;
    print("Số chia hết cho 5 đầu tiên là:",i)
    break

#Continue
#In các số chẵn từ 1 đến 10 và bỏ qua các số lẻ\
for  i in range(1,11):
    if i % 2 !=0:
        continue
    print(i)

#pass
#Kiểm tra điều kiện nếu đúng thì thực hiện , nếu sai thì không làm gì 
x=5
if x > 10:
    print("x lớn hơn 10")
    else:
        pass

#Chuỗi
#Khai báo chuỗi trong python
#Truy cập ký tự trong chuỗi:
my_string = "Hello world"
print(my_string[0]) # Kết quả : 'H'
print(my_string[7]) # Kết quả : 'W'
#Các phép sử lý chuỗi trong Python
my_string = "Hello world!"
print(my_string[7:] )  # Lấy ký tự thứ 7 đến hết : Kết quả : "World!"
print(my_string[:5])   #Lấy từ đầu đến ký tự thứ 4 : Kết quả : "Hello"
print(my_string[3:8])  #Lấy từ ký tự thứ 3 đến 7 : Kết quả : "lo,W"

#Ghép chuỗi(Concateation)
string1 = " Hello"
string2 = "World"
concatenated_string = string1 + " " + string2 #Kết quả : "Hello World "
#Độ dài chuỗi(Length)
my_string = "Hello , World!"
length = len(my_string) #Kết quả : 13
 #Một số hàm để sử lý chuỗi trong Python :
my_string = "     Hello,World!     "
print(my_string.strip()) #Loại bỏ khoảng trắng : Kết quả : 'Hello,World!'

my_string = "Hello,World!"
print (my_string.split(","))
#Phân tách chuỗi : Kết quả : ['Hello' , 'World!']

my_string = "Hello,World!"
print(my_string.replace("Hello" , "Hi"))
#Thay thế chuỗi : Kết quả: ;Hi,World!'