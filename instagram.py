import json

FOLLOWERS_JSON = "followers_1.json"
FOLLOWING_JSON = "following.json"

with open(FOLLOWERS_JSON) as followers:
  followers_json = json.load(followers)

with open(FOLLOWING_JSON) as following:
  following_json = json.load(following)

# Who you follow
following_list = []
for following in following_json["relationships_following"]:
  following_list.append(following["string_list_data"][0]["value"])

# Remove those that follow you back
for follower in followers_json:
  if follower["string_list_data"][0]["value"] in following_list:
    following_list.remove(follower["string_list_data"][0]["value"])

# Remaining is who you follow that do not follow you back
with open("dont_follow_back.txt", "w") as file:
  for user in following_list:
    file.write(f"{user}\n")

# Or you can print them out
# for user in following_list:
#   print(user)