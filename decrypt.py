## Rohit Nawani
## Decrypt!!!!

## This program is designed to decrypt the secret message.

## IMPORT
import decrypt_functions as d

## Constants
print_num = 10

## Message
ps = "**Notice that all lower case letters == decrpyted letters while all upper case letters == encrpyted letters"

## Define myfile
myfile = "cipher_text.txt"

## open a file and read messages into a string
msg = open(myfile,"r")
mystring = msg.read()
msg.close()

## display the encrypted message
print("Here is the encrypted message:\n\n", mystring,"\n"*5, sep = "")



################################################
## STEP 1 --> Find e and replace it
## e
################################################
## Find e
print("\nStep1\nLetter 'e' is the most frequently used letter in Englsih")
## letter counts
alpha1, count1 = d.gram1(mystring)
## print letter counts
print("Letters Frequency\t", ps)
d.print_table(alpha1, count1,len(alpha1))
## Replace e
mystring_1 = d.find_e(mystring, alpha1)
## Calculate Completion %
com1 = d.complete(mystring_1)
print("Decryption Completion % --> \t",format(com1, ".2f"), "%")



################################################
## STEP 2 --> Find t,h and replace it
## e
## t h
################################################
## Find t, h
print("\nStep2\n'the' is one of the most frequent trigram.")
## Trigram counts
alpha3, count3 = d.gram3(mystring_1)
## print letter counts
print("Trigrams Frequency\t", ps)
d.print_table(alpha3, count3, print_num)
## Replace t, h
mystring_2 = d.find_t_h(mystring_1, alpha3)
## Calculate Completion %
com2 = d.complete(mystring_2)
print("Decryption Completion % --> \t",format(com2, ".2f"), "%")



################################################
## STEP 3 --> Find n and replace it
## e
## t h
## n
################################################
## Find n
print("\nStep3\n'ent' is the most frequent trigram of 'e(something)t'.")
## Trigram counts
alpha3, count3 = d.gram3(mystring_2)
print("Trigrams Frequency\t", ps)
d.print_table(alpha3, count3, print_num)
## Replace n
mystring_3 = d.find_n(mystring_2, alpha3)
## Calculate Completion %
com3 = d.complete(mystring_3)
print("Decryption Completion % --> \t",format(com3, ".2f"), "%")



################################################
## STEP 4 --> Find a and replace it
## e
## t h
## n
## a
################################################
## Find a
print("\nStep4\n'that' is the most frequent 4-gram of 'th(something)t'.")
## 4-gram counts
alpha4, count4 = d.gram4(mystring_3)
print("4-grams Frequency\t", ps)
d.print_table(alpha4, count4, print_num)
## Replace a
mystring_4 = d.find_a(mystring_3, alpha4)
## Calculate Completion %
com4 = d.complete(mystring_4)
print("Decryption Completion % --> \t",format(com4, ".2f"), "%")



################################################
## STEP 5 --> Find d and replace it
## e
## t h
## n
## a
## d
################################################
## Find d
print("\nStep5\n'and' is the most frequent trigram of 'an(something)'.")
## Trigram counts
alpha3, count3 = d.gram3(mystring_4)
print("Trigrams Frequency\t", ps)
d.print_table(alpha3, count3, print_num)
## Replace d
mystring_5 = d.find_d(mystring_4, alpha3)
## Calculate Completion %
com5 = d.complete(mystring_5)
print("Decryption Completion % --> \t",format(com5, ".2f"), "%")



################################################
## STEP 6 --> Find r and replace it
## e
## t h
## n
## a
## d
## r
################################################
## Find r
print("\nStep6\n're' is the most frequent bigram of '(something)e' excluding the bigrams that we have already decrypted.")
## Bigram counts
alpha2, count2 = d.gram2(mystring_5)
print("Bigrams Frequency\t", ps)
d.print_table(alpha2, count2, print_num)
## Replace r
mystring_6 = d.find_r(mystring_5, alpha2)
## Calculate Completion %
com6 = d.complete(mystring_6)
print("Decryption Completion % --> \t",format(com6, ".2f"), "%")



################################################
## STEP 7 --> Find o and replace it
## e
## t h
## n
## a
## d
## r
## o
################################################
## Find o
print("\nStep7\n'or' is the most frequent bigram of '(something)r' excluding the bigrams that we have already decrypted.")
## Bigram counts
alpha2, count2 = d.gram2(mystring_6)
print("Bigrams Frequency\t", ps)
d.print_table(alpha2, count2, print_num)
## Replace o
mystring_7 = d.find_o(mystring_6, alpha2)
## Calculate Completion %
com7 = d.complete(mystring_7)
print("Decryption Completion % --> \t",format(com7, ".2f"), "%")



################################################
## STEP 8 --> Find i and replace it
## e
## t h
## n
## a
## d
## r
## o
## i
################################################
## Find i
print("\nStep8\n'or' is the most frequent bigram of '(something)n' excluding the bigrams that we have already decrypted.")
## Bigram counts
alpha2, count2 = d.gram2(mystring_7)
print("Bigrams Frequency\t", ps)
d.print_table(alpha2, count2, print_num)
## replace i
mystring_8 = d.find_i(mystring_7, alpha2)
## Calculate Completion %
com8 = d.complete(mystring_8)
print("Decryption Completion % --> \t",format(com8, ".2f"), "%")



################################################
## STEP 9 --> Find s and replace it
## e
## t h
## n
## a
## d
## r
## o
## i
## s
################################################
## Find s
print("\nStep9\n's' is the most frequent letter count excluding the letters that we have already decrypted.")
print("The difference between the most frequent non-decrypted letter and the second most non-decrypted letter is statistically significant.")
## Letter counts
alpha1, count1 = d.gram1(mystring_8)
print("Letters Frequency\t", ps)
d.print_table(alpha1, count1, len(alpha1))
## replace s
mystring_9 = d.find_s(mystring_8, alpha1)
## Calculate Completion %
com9 = d.complete(mystring_9)
print("Decryption Completion % --> \t",format(com9, ".2f"), "%")




## THE END ##
