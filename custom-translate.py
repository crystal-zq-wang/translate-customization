from google.cloud import translate_v2 as translate
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ".credentials/translation.json"
client = translate.Client()

pov = input("What is your gender? Enter the corresponding number:\n1) Male\n2) Female\n\n")
print()

if pov == "1":
	speaker_gender = "male"
elif pov == "2":
	speaker_gender = "female"

audience = input("Who are you speaking to? Enter the corresponding number:\n1) Stranger(s)\n" +
	"2) Older family member(s)\n3) Younger family member(s)\n4) Spouse\n5) Friend(s)\n6) Other\n\n")
print()

if audience == "1" or audience == "2" or audience == "6":
	respect = 3
elif audience == "3" or audience == "5":
	respect = 2
elif audience == "4":
	respect = 1

addressee_info = input("What is your audience's gender? Enter the corresponding number:\n" + 
	"1) Male/group of people with at least one man\n2) Female/all-female group\n\n")
print()

if addressee_info == "1":
	audience_gender = "male"
elif addressee_info == "2":
	audience_gender = "female"
