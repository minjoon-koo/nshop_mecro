import requests,json,time
ID = 
PW = 
shopPW = 
login_url = 
shop_url = 
purch_url = 

login_token = []
shop_token = []


def login(login_url):
    datas = {
    "login_name":ID,
    "password":PW,
    "login_type":"np_email",
    "persistent":"false",
    "credential_result":"cookie",
    }

    headers = {'Content-Type': 'application/json; charset=utf-8'}
    
    res = requests.post(login_url, data=json.dumps(datas),headers=headers)
    hd = res.headers
    login_token.append(hd['set-cookie'].split(';')[0].split('=')[1])
    login_token.append(hd['set-cookie'].split(';')[2].split('=')[1])

def shop_auth(login_token,shop_url):
    datas = {
    "shopName":"aionc",
    "password0":shopPW,
    "timeFlag":"true",
    "authType":"PAYMENTPASSWORD"
    }
    cookies = {
        'GPVLU': login_token[1],
        'JSESSIONID':login_token[0]
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    res = requests.post(shop_url, data=datas,headers=headers,cookies=cookies)
    shop_token.append(res.headers['Set-Cookie'].split(';')[2].split('=')[2])

def purch(login_token,shop_token,purch_url):
    datas = {
    "point":"false",
    "totalRewardAmount":"297",
    "tid":"tid%3A66c07b2e-6336-4a68-92da-4b32ee1b4ab7",
    "receiverCharacterHtml":"",
    "additionalOption":"ZnJvbUNoYXJhY3RlciUzRDQ0XzQwMzExMV8lRUIlODIlOTglRUIlQTUlQjQlRUMlOTUlQTAlRUIlQUYlQjglN0MlN0N0b0NoYXJhY3RlciUzRDI1XzQwMzExMV8lRUIlODIlOTglRUIlQTUlQjQlRUMlOTUlQTAlRUIlQUYlQjglN0MlN0NzZW5kZXJEYXRhJTNEMSUyQzElN0MlN0NyZWNlaXZlckRhdGElM0QxJTJDMSU3QyU3Q2FkZGl0aW9uYWxTZXJ2aWNlVHlwZSUzRDE2JTdDJTdDZGlzcGxheSUzRCVFQyU5NyU5MCVFQiVBMCU4OCVFQyU4QSU4OCVFQiU5RSU4MCVFRCU4MyU4MCUyQyVFQiU4MiU5OCVFQiVBNSVCNCVFQyU5NSVBMCVFQiVBRiVCOCUyQyVlZCU4YSViOCVlYiVhNiVhYyVlYiU4YiU4OCVlYyU5NyU5OA%3D%3D",
    "email":"puppa22%40nate.com",
    "goodsCounts":"1",
    "fromCharacter":"44_403111_%EB%82%98%EB%A5%B4%EC%95%A0%EB%AF%B8",
    "toCharacter":"25_403111_%EB%82%98%EB%A5%B4%EC%95%A0%EB%AF%B8",
    "receiverData":"1%2C1",
    "additionalServiceType":"16",
    "displayGoodsIds":"410803",
    "displayGoodsTypes":"10",
    "goodsIds":"410803",
    "useCoupons":"false",
    "discountUserCouponIds":"0",
    "couponDiscountAmounts":"0",
    "subTotalRewardAmounts":"297"
    }    
    cookies = {
        'GPVLU': login_token[1],
        'JSESSIONID':login_token[0],
        'GP_SP': shop_token[0]
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    res = requests.post(purch_url, data=datas,headers=headers,cookies=cookies)
    print(res)

login()
shop_auth(login_token)
n = 1 
while(1):
    print(n)
    n = n + 1
    purch(login_token,shop_token)
    if(n % 900 == 0):
        shop_auth(login_token)
        shop_token.clear()
    
