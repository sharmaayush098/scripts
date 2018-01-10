import requests
import json
res = requests.get("https://randomuser.me/api/")
res.text
d_form = json.loads(res.text)
file_name = d_form["results"][0]["login"]["username"]
n = d_form["results"][0]["name"]["first"]
n +=  d_form["results"][0]["name"]["last"]
a = d_form["results"][0]["location"]["street"]
a2 = d_form["results"][0]["location"]["city"]
a3 = d_form["results"][0]["location"]["state"]
a4 = d_form["results"][0]["location"]["postcode"]
b = d_form["results"][0]["email"]
r = d_form["results"][0]["registered"]
p = d_form["results"][0]["phone"]
pic = d_form["results"][0]["picture"]["large"]
file = open(file_name + ".txt", 'w')
file.write("""The name of the user is %s .\nHe is belong to %s .\nHis user Id is %s With
            registration number %s.\nUser's phone number is %s . \nAnd his picture is in %s """
           % (str(n), a + a2 + str(a3) + str(a4), str(b), str(r), str(p), pic))
print(file_name)
file.close()
