from flask import Flask,request,make_response
import requests
import os

app = Flask(__name__)
headers={

  "Referer": "https://streamservicehd.click/",

  "User-Agent": "Android"
}

headers2={
    "documentLifecycle": "active",
    "frameType": "sub_frame",
    "initiator": "https://daddylivehd.sx",
    "method": "GET",
    "parentDocumentId": "A31153FDF25B81A4ECF22A56A82FB21C",
    "url": "https://qwebplay.xyz/premiumtv/daddylivehd.php?id=369",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://daddylivehd.sx/stream/stream-369.php",
    "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Sec-Fetch-Dest": "iframe",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}


@app.route("/")
def credit():
    return " Made With ❤️ For DaddyLiveHD"

@app.route("/auto/<string:channel_id>.m3u8")
def handle_auto(channel_id):
    url=f"https://webudit.cdnhks.lol/lb/premium{channel_id}/index.m3u8"
    res=requests.head(url,headers=headers).headers
    link=res['location']
   
    link=link.replace("playlist.m3u8","tracks-v1a1/")
    print(link)
    res=requests.get(link+"mono.m3u8",headers=headers).text
    print(res)
    
 
   
    ara=res.splitlines()
    for i,line in enumerate(ara):
        if ".ts" in line:
            ara[i]="/ts?id="+line+"&base="+link
    
    return "\n".join(ara)
   
@app.route("/ts")
def handle_ts():
    ts_id = request.args.get("id")    
    base = request.args.get("base")  
    # base = request.args["base"]

    
    response = requests.get(base + ts_id,headers=headers)
    print(response)
    
    return response.content
   
  

        

    



if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
