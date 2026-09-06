#word count
def word_count(sentence):
    return len(sentence.split())

#longest word
def longest_word(sentence):
 word = sentence.split()
 return max(word, key=len)

#reverse sentence
def reverse_sentence(sentence):
    return sentence[::-1]

#prime check
def is_prime(number):
   if number < 2:
      return False

   for i in range(2, number):
       if number % i == 0:
          return False

   return True

sentence = input("Enter a sentence: ")
number = int(input("Enter a number: "))

print("\n--- Results ---") 
print("Word count:", word_count(sentence))
print("Longest word:", longest_word(sentence))
print("Reversed sentence:", reverse_sentence(sentence))

if is_prime(number):
    print("Prime check: Yes")
else:
    print("Prime check: No")

