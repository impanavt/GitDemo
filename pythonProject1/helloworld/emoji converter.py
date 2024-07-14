message=input(">")
words=message.split(' ')
emojis={":)" : " 9"}#dictinery
#get each word of lists and potentially map to emoji
output=""
for word in words:
    output+=emojis.get(word,word) + " "#to search if has word as key
print(output)