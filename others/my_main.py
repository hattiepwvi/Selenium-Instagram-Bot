from my_bot import InstaFollower

SIMILAR_ACCOUNT = "jiaojiaokuaidianhaoqilai"
USERNAME = "jiaojiaokuaidianhaoqilai"
PASSWORD = "jiaojiaokuaidianhaoqilai"

instaFollower = InstaFollower()
instaFollower.login()
instaFollower.find_followers(USERNAME, PASSWORD)
instaFollower.follow(SIMILAR_ACCOUNT)