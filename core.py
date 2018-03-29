import os
import json
import yadisk

apiKeyTemplate = """{
	"yadisk" : {
		"application-id" : "",
		"application-secret" : "",
		"token" : ""
	}
}"""

if(os.path.exists("api_keys.json")):
	j = json.load(open("api_keys.json"))
else:
	f = open("api_keys.json","w")
	print(apiKeyTemplate,file=f)
	print("Api key file created. Please fill required fields and re-run script.")