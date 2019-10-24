import requests
import json

key = "YOUR_KEY_HERE"#ﾊｲﾋﾟ内で/apiとｺﾏﾝﾄﾞを打つとAPIｷｰを入手できます。ここに入れてください。
name = "YOUR_MCID_HERE"#MCIDをここに入れてください
profilename = "YOUR_PROFILE_NAME_HERE"#SBﾒﾆｭｰから、ﾌﾟﾛﾌｧｲﾙ設定に飛んで現在のﾌﾟﾛﾌｧｲﾙ名(大体果物の名前です)を入れてください。
#あとで上3つのﾃﾞｰﾀをjsonで読み込めるようにします。今はメンドイ（）
def searchid(key, name, profilename):#まずここでSBのﾌﾟﾛﾌｧｲﾙIDってやつを導出
    url = str("https://api.hypixel.net/player?key=" + (key) + "&name=" + (name))#URLスキーム構築
    headers = {"content-type": "application/json"}#ﾚｽﾎﾟﾝｽをjsonで取得
    r = requests.get(url, headers=headers)
    data = r.json()#jsonﾛｰﾄﾞ
    profiles = (data["player"]["stats"]["SkyBlock"]["profiles"])#ﾌﾟﾛﾌｧｲﾙ一覧を参照
    for profs in profiles.values():
        if (profs["cute_name"]) == profilename:#欲しいﾌﾟﾛﾌｧｲﾙのIDをここで検索
            return (profs["profile_id"])
        else:
            pass

def main():#ここでようやくSBのﾃﾞｰﾀにｱｸｾｽできるのす
    url = str("https://api.hypixel.net/skyblock/profile?key=" + (key) + "&name=" + (name) + "&profile=" + (searchid(key,name,profilename)))#さっきsearchidで見つけ出したﾌﾟﾛﾌｧｲﾙIDを使ってSBAPIを叩く
    headers = {"content-type": "application/json"}
    sb = requests.get(url, headers=headers)
    sbdata = sb.json()
    myinfo = (sbdata["profile"]["members"][(searchid(key,name,profilename))])#SBの個人ﾃﾞｰﾀをmyinfoのdict型に格納
    fairy_souls_collected= (myinfo["fairy_souls_collected"])#各数値を検索。同じようにして他のﾃﾞｰﾀも取ることができます
    fairy_exchanges = (myinfo["fairy_exchanges"])
    fairy_soul = (myinfo["fairy_souls"])
    print("今までに集めたソウルの総数は"+str(fairy_souls_collected)+"個です。"+str(fairy_exchanges)+"回交換しているので、"+str(fairy_soul)+"個手元に残っています。")

main()