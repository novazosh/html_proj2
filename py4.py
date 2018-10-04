import random

colors = input("Please enter a series of colors separated by a comma and no space: ")
colors = colors.split(",")
for color in colors:
    print(color)
print(colors)
indexPos = input("What position do you want to change?: ")
indexPos = int(indexPos)
newColor = input("What new color do you want to go there?: ")
colors[indexPos] = newColor
print (colors)

user=input("Give me a sentence: ")
user=user.split()
for word in user:
    print(word)

adjs = ["beautiful", "handsome", "pretty", "warm", "fantastic"]
sentence = "Hello, you are looking *adj today."
sentence = sentence.split()

indexCount= 0
for word in sentence:
    if word == "*adj":
        wordChoice = random.choice(adjs)
        sentence [indexCount] = wordChoice
    indexCount += 1
st=""
for word in sentence:
    st+=word+" "
print(st)

avocados="Green fruits which are mostly healthy fats and vitamins"
avocados=avocados.split()
print(avocados)
for r in avocados:
    print(r)
    if r == "healthy":
        break
print("Yes they are healthy.")

counter=0
while counter <5:
    init = "The *noun looks quite *adj today."
    adjs = ["beatiful", "handsome", "pretty", "fantastic", "warm"]
    nouns = ["weather", "sweater", "dog", "cat", "teacher"]
    init=init.split()

    indexCount=0
    for word in init:
        if word == "*adj":
            wordChoice=random.choice(adjs)
            if "." in word:
                wordChoice += "."
            init[indexCount] = wordChoice
        if "*noun" in word:
            wordChoice=random.choice(nouns)
            init[indexCount]=wordChoice
        indexCount += 1
    st=""
    for word in init:
        st += word + " "
    print(st)
    counter += 1
    
        

