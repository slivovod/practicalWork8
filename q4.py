arr = ["Akiyama", "Yui", "Aikko", "Kagami", "Yuko"]
first_letter = input().upper()
no_one = True
for i in range(len(arr)):
    if(arr[i][0] == first_letter):
        print(arr[i])
        no_one = False
if(no_one):
    print("there are no such :(")