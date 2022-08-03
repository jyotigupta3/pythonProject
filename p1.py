
abs = "Energetic Software engineer engineer with 1+ year of experience developing robust code for high volume business. " \
      "Have gained commercial experience during my gap year with exposure to software development. Including carrying out " \
      "straightforward design, testing or support of network design and solutions. Looking forward to enrich skills and " \
      "knowledge to have a lasting influence for future endeavor."
# counts = {}
#
words = abs.split()
# for word in words:
#     if word.lower() in counts:
#         counts[word.lower()] += 1
#     else:
#         counts[word.lower()] = 1
#
# print(counts)
length = len(set(words))
print(length)

for i in range(0, length-1):
    if words[i] == words[i+1]:
        words.remove(words[i+1])


print(words)


