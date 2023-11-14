def returnEmoji(sentence):
    words = sentence.split(" ")

    emojis = {
        ":)": "😊",
        ":(": "😞"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


sentence = input(">")
withEmoji = returnEmoji(sentence)
print(withEmoji)
