# import tinify
# tinify.key = "sXTzGmYX5WwlzHmVcH9T90rfM90QZDtn"


# source = tinify.tinify.from_url("https://imgs.ysscores.com/teams/128/2231690298782.png")
# print()

import requests

# url ="https://api.tinify.com/shrink"
# headers = {
#     "Host": "api.tinify.com",
#     "Authorization": "Basic c1hUekdtWVg1V3dsekhtVmNIOVQ5MHJmTTkwUVpEdG4=",
#     "Content-Type": "application/json"
# }
# data = '''{
#     "source": {
#         "url": "https://imgs.ysscores.com/teams/128/2231690298782.png"
#     }
# }'''
# return requests.post(url,data=data,headers=headers).json()["output"]["url"]

def shrinkImg(urlimg):
    url ="https://api.tinify.com/shrink"
    headers = {
        "Host": "api.tinify.com",
        "Authorization": "Basic c1hUekdtWVg1V3dsekhtVmNIOVQ5MHJmTTkwUVpEdG4=",
        "Content-Type": "application/json"
    }
    data = '{"source": {"url": "'+f"{urlimg}"+'"}}'


    return requests.post(url,data=data,headers=headers).json()["output"]["url"]

print(shrinkImg("https://imgs.ysscores.com/teams/128/2231690298782.png"))