import random
print(''' 
__                                            
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/           
     
     
 Persian names    
     
      ''')
stagepic = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_list=["maryam", "asal","roya","samira","mohammad","mobina","negin","negar","delsa"]
mainword= random.choice(word_list)
mainwordlength=len(mainword)
blanklist=[]
for i in range(mainwordlength):
    blanklist.append("_")
print(blanklist)
gameover= False
life=6
stage=0
print(stagepic[0])
while not gameover:
    guess=input("guess the letter:").lower()
    found=False
    for i in range(mainwordlength):
        if mainword[i]==guess:
            blanklist[i]=guess
            found=True
            print("correct answer.")
    if not found:
        life-=1
        stage+=1
        print (f"wrong! you have {life} left.")
        print(stagepic[stage])
    print(blanklist)
    if life==0 :
        gameover=True
        print("you lost")
    if "_" not in blanklist:
        gameover=True
        print("you won!")

