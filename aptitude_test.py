import json
json.load(open('data.json'))
r = json.load(open('data.json'))
ques_1 = r["data"]["text"]
option_1 = r["data"]["options"][0]["text"]
option_2 = r["data"]["options"][1]["text"]
option_3 = r["data"]["options"][2]["text"]
option_id_1 = r["data"]["options"][0]["option_id"]
ques_2 = r["data"]["next_question"]["text"]
option_40 = r["data"]["next_question"]["options"][0]["text"]
option_43 = r["data"]["next_question"]["options"][1]["text"]
option_39 = r["data"]["next_question"]["options"][2]["text"]
option_41 = r["data"]["next_question"]["options"][3]["text"]
option_42 = r["data"]["next_question"]["options"][4]["text"]
option_id_2 = r["data"]["next_question"]["options"][1]["option_id"]
ques_3 = r["data"]["next_question"]["next_question"]["text"]
option_13 = r["data"]["next_question"]["next_question"]["options"][0]["text"]
option_14 = r["data"]["next_question"]["next_question"]["options"][1]["text"]
option_15 = r["data"]["next_question"]["next_question"]["options"][2]["text"]
option_id_3 = r["data"]["next_question"]["next_question"]["options"][2]["option_id"]
right = r["data"]["next_question"]["next_question"]["is_last_question"]
wrong = r["data"]["is_last_question"]
print("Here is the question answer round")
input(print("press enter to start"))
print("input in numeric value")
print(ques_1)
print("1) %s    2)  %s  3)  %s   " % (option_1, option_2, option_3))
input(print("Answer : "))

print(ques_2)
print("39) %s    40)  %s  41)  %s 42) %s 43) %s " % (option_39, option_40, option_41, option_42, option_43))
input(print("Answer : "))
print(ques_3)
print("13) %s    14)  %s  15)  %s   " % (option_13, option_14, option_15))
input(print("Answer: "))
print("congrats you completed the aptitude")

