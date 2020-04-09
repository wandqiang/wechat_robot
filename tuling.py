import  requests
import json
def tuling_reply(ask):
    ques = ask
    #or your tuling_key that you should get from http://openapi.tuling123.com
    tuling_key = "f222eaa9ede84cc6bfdd6f6d2ca4a589"
    tuling_url = "http://openapi.tuling123.com/openapi/api/v2"
    # or your id
    userId = "503198"
    data = {
	    "reqType":0,
        "perception": {
          "inputText": {
             "text": ques
          },
      },
        "userInfo": {
            "apiKey": tuling_key,
         "userId": userId
         }
    }
    data = json.dumps(data).encode(encoding="utf-8")
    response = requests.post(tuling_url,data).content.decode(encoding="utf-8")
    response=json.loads(response)
    ans=response["results"][0]["values"]["text"]
    return ans
