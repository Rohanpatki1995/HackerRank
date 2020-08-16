'''
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String  S= BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:
'''

def minion_game(s):
    word_list=[]
    stuart_list=[]
    kevin_list=[]
    vovels='aeiou'
    for i in range(len(s)):
        for j in range(len(s),i,-1):
            word_list.append(s[i:j])
    #print(word_list)

    for word in word_list:
        if word[0].lower() in vovels:
            kevin_list.append(word)
        else:
            stuart_list.append(word)
    stuart_score=len(stuart_list)
    kevin_score=len(kevin_list)

    if stuart_score>kevin_score:
        print('Stuart {}'.format(stuart_score))
    elif kevin_score>stuart_score:
        print('Kevin {}'.format(kevin_score))
    else:
        print('DRAW')
    #print(kevin_list)
    #print(stuart_list)

if __name__=='__main__':
    s=input()
    minion_game(s)