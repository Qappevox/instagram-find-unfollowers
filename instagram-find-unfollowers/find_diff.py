

def sorting(name):

    with open(name, "r", encoding="utf-8") as dosya:
        kelimeler = dosya.read().split()

    kelimeler.sort()
    for kelime in kelimeler:
        with open("z"+name, "a", encoding="utf-8") as f:
            f.write(kelime + "\n")


def get_my_unfollowers(followers, following):
    followers_file = set(open(followers,encoding="utf-8").readlines())
    followees_file = set(open(following, encoding="utf-8").readlines())
    unfollowers_set = followees_file.difference(followers_file)
    for unfollowers in unfollowers_set:
        print(unfollowers)

#sorting("ztest.txt")
#sorting("zytest.txt")

#get_my_unfollowers("zzytest.txt", "zztest.txt")



