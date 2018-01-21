# coding:utf-8
import requests
import json
from concurrent import futures
from pymongo import MongoClient
import time


def one(page):
    db = local_db()
    phone_num = db.phone.find().skip(int(page)).limit(1)[0]
    session = requests.Session()
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0",
              'Cookie': 'channel=cW11dG1fc291cmNlPWJhaWR1c2VvJnFtdXRtX2t3PQ; Um-C=CeVD4IlDCqBkNySv4kaDIdsg5FyAGu3zmecgJOIMjIVEzRjETgGBjomJZfOqTfig+TJhQM9Jcvc9fNDSnUP+eFTke+niL6kn51FrUSEqH3q2suQeE9YLfr17jNsImExCmeF+yZ4UGCQ=; Um-W=B6sL7dT5XyADRudiZYeS4nChaUHqQuGT82MhZgzz78vnDqP8Z7FaV30C4vnuMLAUPNiOvrW3q7rXxXnc8nQ6OlnYNGz9iBLnNNFUwLE6yH3I4HTWxohLw+M94ZUqmAnIfdIzIdUZ8jaciqfjIGy5QQVn0oMXhe2+7eQfrAhEuJhI4j+/BgmBoLsmrDMJ0q5G; Um-R=pgxoW1yakl9bU0fwAG0n7yPaYEbUOpCNu5JPagYfdt0gjm0mwG0QYRmd3HWs7YcJ3+xwGUQ+7IgyfScZPrVDytuzUkg8AbVW4VLpSOaEt8q2GvVH9mvcMBXWiE9E4Xf7pDLUNamAEJrVluofj8YeclwNG3tEqByAhP5Mtmvm+f9KZ4hedeal28O6OQFfHvm+nzOGQNubBevppGuFP/hwDIJM2dn7Y6sVxe9jvhmjpuiOknpeGHZfPnnZ+llUwNG9akwf14A99yiHYS6vHCwNNhKihVpD+wVrEAaBfeU7twzLD9jdtQHKcSqDr7oZlz/DBKIzgyvaDBksZVlZTPFaGxKby/3nw1i+mRfd2EvYEpp55/j3ShUKFCS3R4ps+PVYbLzIPi+srBl0C2HcZR4rf3EuSoRz6Mad4++QLw/RqhBLeso1D0+XS6vdiq1oeyyR; _ga=GA1.2.651950911.1513427333; _gid=GA1.2.1265022952.1513427333; gr_user_id=322f8b22-763d-4686-9e6f-56c2594b4da1; gr_session_id_a370b353401c73da=5787c8d9-924d-42f0-9270-873502f1458f; nTalk_CACHE_DATA={uid:kf_9575_ISME9754_guestA63EB54F-086E-CF,tid:1513427381548889}; NTKF_T2D_CLIENTID=guestA63EB54F-086E-CFAD-11AB-5F4D2D2C4991; SSOTICKET=; SSOCHILDTICKET=; SSOEXPIRES=; SSOTHRESHOLD=; a9a68f4fefd3b693f10be4a89799dc48=79a47bab347b4f119bea030ba0293e6b; OFCaptchaControl=OFCaptchaControl69d2cad9-8911-4f05-b849-e64f5815eb7f; PHPSESSID=4D5DD8A92832FB5CB062C62B14C11AD2; _gat=1',
              'Host': 'www.1000.com',
              'X-Requested-With': 'XMLHttpRequest'}
    with session:
        payload = {
            ''
            'mobile': '{}'.format(phone_num["phone"]),
            'qmext': '',
            'refer': 'https://www.baidu.com/link?url=RtleTEkTazCCeODUJbDd9211UkE2OEkzHS8sNwcJwWe&wd=&eqid=e1e08d0400046b22000000055a35117a'
        }
        url = "https://www.1000.com/reg/check/mobile"
        res = session.post(url, headers=header, params=payload).content
        result = json.loads(res)
        print(result)
        try:
            if result["rescode"] == 201:
                update_status(db, phone_num["phone"])
                save_file(phone_num["phone"])
        except:
            pass
    time.sleep(2)


def save_file(file):
    with open('phone1.txt', 'a') as fg:
        fg.write(file + "\n")


def local_db():
    conn = MongoClient("mongodb://127.0.0.1:27017/", connect=False, maxPoolSize=500)
    db = conn["51hao"]
    return db


def update_status(db, phone):
    db.phone.update({"phone": phone}, {"$set": {"status": 1, "retailers": "qianmi"}})


def get_pages(begin, end):
    print("程序开始运行了，请忍耐一会儿。。。。")
    page_lists = ["{page}".format(page=page) for page in range(begin, end)]
    return page_lists


if __name__ == '__main__':
    # 16332739，
    pages = get_pages(1100000, 1150000)
    with futures.ThreadPoolExecutor(32) as executor:
        executor.map(one, pages)
