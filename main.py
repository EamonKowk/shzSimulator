import os, re
import random, readJSON

data = readJSON.读JSON文件("data.json")
famousWords = data["famous"]  # a 代表前面垫话，b代表后面垫话
before = data["before"]  # 在名人名言前面弄点废话
after = data['after']  # 在名人名言后面弄点废话
trash = data['bosh']  # 代表文章主要废话来源
repeatability = 2
def shuffle(n):
    global repeatability
    pool = list(n) * repeatability
    while True:
        random.shuffle(pool)
        for elements in pool:
            yield elements

nextTrash = shuffle(trash)
nextFamous = shuffle(famousWords)

def getSomeFamous():
    global nextFamous
    xx = next(nextFamous)
    xx = xx.replace("a", random.choice(before))
    xx = xx.replace("b", random.choice(after))
    return xx


def another():
    xx = ". "
    xx += "\r\n"
    xx += "    "
    return xx


if __name__ == "__main__":
    xx = input("请输入文章主题:")
    for x in xx:
        tmp = str()
        while (len(tmp) < 6000):
            branch = random.randint(0, 100)
            if branch < 5:
                tmp += another()
            elif branch < 20:
                tmp += getSomeFamous()
            else:
                tmp += next(nextTrash)
        tmp = tmp.replace("x", xx)
        print(tmp)
