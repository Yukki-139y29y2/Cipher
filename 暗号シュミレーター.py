import unicodedata
import random

#プログラム実行の順序の指定
num=0
#passに格納するための値
pass_one=0
#暗号文を格納するためのリスト
ciphertext_list=[]
#平文を英数字に変更した文字列をリストに変更する
change_plaintext_list=[]
#pass_codeを格納するためのリスト
pass_code_list=[]
#復号化の計算をするためのリスト
decode_list=[]
#平文を格納するためのリスト
plaintext_list=[]

#リストは乱数を用いる場合に扱う
random_list1=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i",
       "j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

random_list2=["α","β","γ","a","b","c","d","e","f","g","h","i","j","k","l","m","o","p","q",
       "r","t","u","v","w","x","y","z"]

#辞書は左の文字を右の文字に変更する場合に扱う
dic1= {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',
       12:'c',13:'d',14:'e',15:'f',16:'g',17:'h',18:'i',19:'j',20:'k',21:'l',22:'m',
       23:'n',24:'o',25:'p',26:'q',27:'r',28:'s',29:'t',30:'u',31:'v',32:'w',33:'x', 
       34:'y',35:'z'}

dic2= {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:'a',11:'b',12:'c',13:'d',14:'e',
       15:'f',16:'g',17:'h',18:'i',19:'j',20:'k',21:'l',22:'m',23:'n',24:'o',25:'p',
       26:'q',27:'r',28:'s',29:'t',30:'u',31:'v',32:'w',33:'x', 34:'y',35:'z'}

dic3= {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"a":10,"b":11,
       "c":12,"d":13,"e":14,"f":15,"g":16,"h":17,"i":18,"j":19,"k":20,"l":21,"m":22,
       "n":23,"o":24,"p":25,"q":26,"r":27,"s":28,"t":29,"u":30,"v":31,"w":32,"x":33,
       "y":34,"z":35}

dic4= {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,"a":10,"b":11,"c":12,"d":13,"e":14,
       "f":15,"g":16,"h":17,"i":18,"j":19,"k":20,"l":21,"m":22,"n":23,"o":24,"p":25,
       "q":26,"r":27,"s":28,"t":29,"u":30,"v":31,"w":32,"x":33,"y":34,"z":35}

#暗号化の計算
def encryption(change_plaintext,random_number1,random_number2):
    global pass_one
    #change_plaintextに格納を行った文字数分処理を行う
    for i in range(len(change_plaintext)):
        #英数字の偶数の部分（0~9）
        if i%2==0:
            #該当する数字と一つ目の乱数と文字の順番を足した数がcipher_oneに代入される
            #そして、iの場所が11なら3、７なら2、５なら１が足される
            if i%11==0:
                cipher_one=int(change_plaintext_list[i])+random_number1+int(i)+3
            elif i%7==0:
                cipher_one=int(change_plaintext_list[i])+random_number1+int(i)+2
            elif i%5==0:
                cipher_one=int(change_plaintext_list[i])+random_number1+int(i)+1
            else:
                cipher_one=int(change_plaintext_list[i])+random_number1+int(i)
            #cipher_oneが36を超えたら36を超えなくなるまでcipher_oneを36で引き続ける
            #cipher_oneから36を弾き続けた回数がpass_oneに代入される。
            #そのpass_oneが9未満ならそのままで、10を超えたらa~zの文字に置き換わり、pass_code_listに格納される。
            #cipher_oneは0~zに文字が置き換わり、ciphertext_listに格納される。
            if cipher_one >=36:
                while cipher_one>=36:
                    cipher_one-=36
                    pass_one+=1
                if pass_one>=10:
                    pass_one=dic1.get(pass_one)
                cipher_one=str(dic1.get(cipher_one))
                ciphertext_list.append(cipher_one)
                pass_code_list.append(pass_one)
                pass_one=0
            #cipher_oneが35以下ならcipher_oneが0~zに変更され、ciphertext_listに格納される。
            #そして、pass_code_listには0が格納される。
            else:
                cipher_one=str(dic1.get(cipher_one))
                ciphertext_list.append(cipher_one)
                pass_code_list.append(0)
                
        #英数字の奇数の部分（0~z）
        else:
            #該当する数字と二つ目の乱数と文字の順番を足した数がcipher_twoに代入される
            #そして、iの場所が11の倍数なら1、７の倍数なら2、５の倍数なら3が足される
            if i%11==0:
                cipher_two=int(dic3[change_plaintext_list[i]])+int(dic3[random_number2])+int(i)+1
            elif i%7==0:
                cipher_two=int(dic3[change_plaintext_list[i]])+int(dic3[random_number2])+int(i)+2
            elif i%5==0:
                cipher_two=int(dic3[change_plaintext_list[i]])+int(dic3[random_number2])+int(i)+3
            else:
                cipher_two=int(dic3[change_plaintext_list[i]])+int(dic3[random_number2])+int(i)
            #cipher_twoが36を超えたら36を超えなくなるまでcipher_twoを36で引き続ける
            #cipher_twoから36を弾き続けた回数がpass_oneに代入される。
            #そのpass_oneが9未満ならそのままで、10を超えたらa~zの文字に置き換わり、pass_code_listに格納される。
            #cipher_twoは0~zに文字が置き換わり、ciphertext_listに格納される。
            if cipher_two>=36:
                while cipher_two>=36:
                    cipher_two-=36
                    pass_one+=1
                if pass_one >=10:
                    pass_one=dic1.get(pass_one)
                cipher_two=str(dic1.get(cipher_two))
                ciphertext_list.append(cipher_two)
                pass_code_list.append(pass_one)
                pass_one=0
            #cipher_twoが35以下ならcipher_twoが0~zに変更され、ciphertext_listに格納される。
            #そして、pass_code_listには0が格納される。
            else:
                cipher_two=str(dic1.get(cipher_two))
                ciphertext_list.append(cipher_two)
                pass_code_list.append(0)
           
#復号化の計算               
def decode(ciphertext_nodummy,random_number1,random_number2,pass_code):
    #暗号を英数字に変換した文字数分実行を行う
    for i in range(len(ciphertext_nodummy)):
        #英数字の偶数の部分
        if i % 2 == 0:
            #decode_oneに該当する英数字を数字に直し、パスの数字文36をかけて代入する。
            #そして、求めたdecode_oneに文字の順番と一つ目の乱数分値を引く。
            #その時に、順番が11の倍数なら3、7の倍数なら2、5の倍数なら1をさらに引く。
            #そして、計算した文字を英数字に変換して、decode_listに格納する。
            decode_one=int(dic3.get(ciphertext_nodummy[i]))+int(dic3.get(pass_code[i]))*36
            if i%11==0:
                decode_one=decode_one-i-int(random_number1)-3
            elif i%7==0:
                decode_one=decode_one-i-int(random_number1)-2
            elif i%5==0:
                decode_one=decode_one-i-int(random_number1)-1
            else:
                decode_one=decode_one-i-int(random_number1)
            decode_one=str(dic2.get(decode_one))
            decode_list.append(str(decode_one))
        #奇数の部分
        else:
            #decode_twoに該当する英数字を数字に直し、パスの数字文36をかけて代入する。
            #そして、求めたdecode_twoに文字の順番と一つ目の乱数分値を引く時に、順番が11の倍数
            #なら１、7の倍数なら2、5の倍数なら3を引く。
            #そして、計算した文字を英数字に変換して、decode_listに格納する。
            decode_two=int(dic3.get(ciphertext_nodummy[i]))+int(dic3.get(pass_code[i]))*36
            if i%11==0:
                decode_two=decode_two-i-int(dic3.get(random_number2))-1
            elif i%7==0:
                decode_two=decode_two-i-int(dic3.get(random_number2))-2
            elif i%5==0:
                decode_two=decode_two-i-int(dic3.get(random_number2))-3
            else:
                decode_two=decode_two-i-int(dic3.get(random_number2))
            decode_two=str(dic2.get(decode_two))
            decode_list.append(decode_two)
             
#平文を英数字で表示する 
def change1(change_text):
    change_text = change_text.replace("0","00")
    change_text = change_text.replace("1","01")
    change_text = change_text.replace("2","02")
    change_text = change_text.replace("3","03")
    change_text = change_text.replace("4","04")
    change_text = change_text.replace("5","05")
    change_text = change_text.replace("6","06")
    change_text = change_text.replace("7","07")
    change_text = change_text.replace("8","08")
    change_text = change_text.replace("9","09")
    change_text = change_text.replace("a","0a")
    change_text = change_text.replace("b","0b")
    change_text = change_text.replace("c","0c")
    change_text = change_text.replace("d","0d")
    change_text = change_text.replace("e","0e")
    change_text = change_text.replace("f","0f")
    change_text = change_text.replace("g","0g")
    change_text = change_text.replace("h","0h")
    change_text = change_text.replace("i","0i")
    change_text = change_text.replace("j","0j")
    change_text = change_text.replace("k","0k")
    change_text = change_text.replace("l","0l")
    change_text = change_text.replace("m","0m")
    change_text = change_text.replace("n","0n")
    change_text = change_text.replace("o","0o")
    change_text = change_text.replace("p","0p")
    change_text = change_text.replace("q","0q")
    change_text = change_text.replace("r","0r")
    change_text = change_text.replace("s","0s")
    change_text = change_text.replace("t","0t")
    change_text = change_text.replace("u","0u")
    change_text = change_text.replace("v","0v")
    change_text = change_text.replace("w","0w")
    change_text = change_text.replace("x","0x")
    change_text = change_text.replace("y","0y")
    change_text = change_text.replace("z","0z")
    change_text = change_text.replace("A","10")
    change_text = change_text.replace("B","11")
    change_text = change_text.replace("C","12")
    change_text = change_text.replace("D","13")
    change_text = change_text.replace("E","14")
    change_text = change_text.replace("F","15")
    change_text = change_text.replace("G","16")
    change_text = change_text.replace("H","17")
    change_text = change_text.replace("I","18")
    change_text = change_text.replace("J","19")
    change_text = change_text.replace("K","1a")
    change_text = change_text.replace("L","1b")
    change_text = change_text.replace("M","1c")
    change_text = change_text.replace("N","1d")
    change_text = change_text.replace("O","1e")
    change_text = change_text.replace("P","1f")
    change_text = change_text.replace("Q","1g")
    change_text = change_text.replace("R","1h")
    change_text = change_text.replace("S","1i")
    change_text = change_text.replace("T","1j")
    change_text = change_text.replace("U","1k")
    change_text = change_text.replace("V","1l")
    change_text = change_text.replace("W","1m")
    change_text = change_text.replace("X","1n")
    change_text = change_text.replace("Y","1o")
    change_text = change_text.replace("Z","1p")
    change_text = change_text.replace("あ","1q")
    change_text = change_text.replace("い","1r")
    change_text = change_text.replace("う","1s")
    change_text = change_text.replace("え","1t")
    change_text = change_text.replace("お","1u")
    change_text = change_text.replace("か","1v")
    change_text = change_text.replace("き","1w")
    change_text = change_text.replace("く","1x")
    change_text = change_text.replace("け","1y")
    change_text = change_text.replace("こ","1z")
    change_text = change_text.replace("さ","20")
    change_text = change_text.replace("し","21")
    change_text = change_text.replace("す","22")
    change_text = change_text.replace("せ","23")
    change_text = change_text.replace("そ","24")
    change_text = change_text.replace("た","25")
    change_text = change_text.replace("ち","26")
    change_text = change_text.replace("つ","27")
    change_text = change_text.replace("て","28")
    change_text = change_text.replace("と","29")
    change_text = change_text.replace("な","2a")
    change_text = change_text.replace("に","2b")
    change_text = change_text.replace("ぬ","2c")
    change_text = change_text.replace("ね","2d")
    change_text = change_text.replace("の","2e")
    change_text = change_text.replace("は","2f")
    change_text = change_text.replace("ひ","2g")
    change_text = change_text.replace("ふ","2h")
    change_text = change_text.replace("へ","2i")
    change_text = change_text.replace("ほ","2j")
    change_text = change_text.replace("ま","2k")
    change_text = change_text.replace("み","2l")
    change_text = change_text.replace("む","2m")
    change_text = change_text.replace("め","2n")
    change_text = change_text.replace("も","2o")
    change_text = change_text.replace("や","2p")
    change_text = change_text.replace("ゐ","2q")
    change_text = change_text.replace("ゆ","2r")
    change_text = change_text.replace("ゑ","2s")
    change_text = change_text.replace("よ","2t")
    change_text = change_text.replace("わ","2u")
    change_text = change_text.replace("を","2v")
    change_text = change_text.replace("ん","2w")
    change_text = change_text.replace("ぁ","2x")
    change_text = change_text.replace("ぃ","2y")
    change_text = change_text.replace("ぅ","2z")
    change_text = change_text.replace("ぇ","30")
    change_text = change_text.replace("ぉ","31")
    change_text = change_text.replace("ゃ","32")
    change_text = change_text.replace("ゅ","33")
    change_text = change_text.replace("ょ","34")
    change_text = change_text.replace("っ","35")
    change_text = change_text.replace("が","36")
    change_text = change_text.replace("ぎ","37")
    change_text = change_text.replace("ぐ","38")
    change_text = change_text.replace("げ","39")
    change_text = change_text.replace("ご","3a")
    change_text = change_text.replace("ざ","3b")
    change_text = change_text.replace("じ","3c")
    change_text = change_text.replace("ず","3d")
    change_text = change_text.replace("ぜ","3e")
    change_text = change_text.replace("ぞ","3f")
    change_text = change_text.replace("だ","3g")
    change_text = change_text.replace("ぢ","3h")
    change_text = change_text.replace("づ","3i")
    change_text = change_text.replace("で","3j")
    change_text = change_text.replace("ど","3k")
    change_text = change_text.replace("ば","3l")
    change_text = change_text.replace("び","3m")
    change_text = change_text.replace("ぶ","3n")
    change_text = change_text.replace("べ","3o")
    change_text = change_text.replace("ぼ","3p")
    change_text = change_text.replace("ぱ","3q")
    change_text = change_text.replace("ぴ","3r")
    change_text = change_text.replace("ぷ","3s")
    change_text = change_text.replace("ぺ","3t")
    change_text = change_text.replace("ぽ","3u")
    change_text = change_text.replace("ア","3v")
    change_text = change_text.replace("イ","3w")
    change_text = change_text.replace("ウ","3x")
    change_text = change_text.replace("エ","3y")
    change_text = change_text.replace("オ","3z")
    change_text = change_text.replace("カ","40")
    change_text = change_text.replace("キ","41")
    change_text = change_text.replace("ク","42")
    change_text = change_text.replace("ケ","43")
    change_text = change_text.replace("コ","44")
    change_text = change_text.replace("サ","45")
    change_text = change_text.replace("シ","46")
    change_text = change_text.replace("ス","47")
    change_text = change_text.replace("セ","48")
    change_text = change_text.replace("ソ","49")
    change_text = change_text.replace("タ","4a")
    change_text = change_text.replace("チ","4b")
    change_text = change_text.replace("ツ","4c")
    change_text = change_text.replace("テ","4d")
    change_text = change_text.replace("ト","4e")
    change_text = change_text.replace("ナ","4f")
    change_text = change_text.replace("ニ","4g")
    change_text = change_text.replace("ヌ","4h")
    change_text = change_text.replace("ネ","4i")
    change_text = change_text.replace("ノ","4j")
    change_text = change_text.replace("ハ","4k")
    change_text = change_text.replace("ヒ","4l")
    change_text = change_text.replace("フ","4m")
    change_text = change_text.replace("ヘ","4n")
    change_text = change_text.replace("ホ","4o")
    change_text = change_text.replace("マ","4p")
    change_text = change_text.replace("ミ","4q")
    change_text = change_text.replace("ム","4r")
    change_text = change_text.replace("メ","4s")
    change_text = change_text.replace("モ","4t")
    change_text = change_text.replace("ヤ","4u")
    change_text = change_text.replace("ユ","4v")
    change_text = change_text.replace("ヨ","4w")
    change_text = change_text.replace("ラ","4x")
    change_text = change_text.replace("リ","4y")
    change_text = change_text.replace("ル","4z")
    change_text = change_text.replace("レ","50")
    change_text = change_text.replace("ロ","51")
    change_text = change_text.replace("ワ","52")
    change_text = change_text.replace("ヲ","53")
    change_text = change_text.replace("ン","54")
    change_text = change_text.replace("ァ","55")
    change_text = change_text.replace("ィ","56")
    change_text = change_text.replace("ゥ","57")
    change_text = change_text.replace("ェ","58")
    change_text = change_text.replace("ォ","59")
    change_text = change_text.replace("ャ","5a")
    change_text = change_text.replace("ュ","5b")
    change_text = change_text.replace("ョ","5c")
    change_text = change_text.replace("ッ","5d")
    change_text = change_text.replace("ガ","5e")
    change_text = change_text.replace("ギ","5f")
    change_text = change_text.replace("グ","5g")
    change_text = change_text.replace("ゲ","5h")
    change_text = change_text.replace("ゴ","5i")
    change_text = change_text.replace("ザ","5j")
    change_text = change_text.replace("ジ","5k")
    change_text = change_text.replace("ズ","5l")
    change_text = change_text.replace("ゼ","5m")
    change_text = change_text.replace("ゾ","5n")
    change_text = change_text.replace("ダ","5o")
    change_text = change_text.replace("ヂ","5p")
    change_text = change_text.replace("ヅ","5q")
    change_text = change_text.replace("デ","5r")
    change_text = change_text.replace("ド","5s")
    change_text = change_text.replace("バ","5t")
    change_text = change_text.replace("ビ","5u")
    change_text = change_text.replace("ブ","5v")
    change_text = change_text.replace("ベ","5w")
    change_text = change_text.replace("ボ","5x")
    change_text = change_text.replace("パ","5y")
    change_text = change_text.replace("ピ","5z")
    change_text = change_text.replace("プ","60")
    change_text = change_text.replace("ペ","61")
    change_text = change_text.replace("ポ","62")
    change_text = change_text.replace("ー","63")
    change_text = change_text.replace("!","64")
    change_text = change_text.replace('"',"65")
    change_text = change_text.replace("'","66")
    change_text = change_text.replace("#","67")
    change_text = change_text.replace("$","68")
    change_text = change_text.replace("%","69")
    change_text = change_text.replace("&","6a")
    change_text = change_text.replace("(","6b")
    change_text = change_text.replace(")","6c")
    change_text = change_text.replace("=","6d")
    change_text = change_text.replace("-","6e")
    change_text = change_text.replace("~","6f")
    change_text = change_text.replace("^","6g")
    change_text = change_text.replace("@","6h")
    change_text = change_text.replace("|","6i")
    change_text = change_text.replace("￥","6j")
    change_text = change_text.replace("`","6k")
    change_text = change_text.replace("{","6l")
    change_text = change_text.replace("[","6m")
    change_text = change_text.replace("「","6n")
    change_text = change_text.replace("+","6o")
    change_text = change_text.replace("*","6p")
    change_text = change_text.replace(";","6q")
    change_text = change_text.replace(":","6r")
    change_text = change_text.replace("}","6s")
    change_text = change_text.replace("]","6t")
    change_text = change_text.replace("」","6u")
    change_text = change_text.replace("<","6v")
    change_text = change_text.replace(",","6w")
    change_text = change_text.replace("、","6x")
    change_text = change_text.replace(">","6y")
    change_text = change_text.replace(".","6z")
    change_text = change_text.replace("。","70")
    change_text = change_text.replace("?","71")
    change_text = change_text.replace("/","72")
    change_text = change_text.replace("・","73")
    change_text = change_text.replace("_","74")
    change_text = change_text.replace(" ","75")
    change_text = change_text.replace("ゔ","76")
    change_text = change_text.replace("ヴ","77")
    return change_text

#暗号文をを英数字で表示する
def change2(change_text):
    change_text = change_text.replace("10","A")
    change_text = change_text.replace("11","B")
    change_text = change_text.replace("12","C")
    change_text = change_text.replace("13","D")
    change_text = change_text.replace("14","E")
    change_text = change_text.replace("15","F")
    change_text = change_text.replace("16","G")
    change_text = change_text.replace("17","H")
    change_text = change_text.replace("18","I")
    change_text = change_text.replace("19","J")
    change_text = change_text.replace("1a","K")
    change_text = change_text.replace("1b","L")
    change_text = change_text.replace("1c","M")
    change_text = change_text.replace("1d","N")
    change_text = change_text.replace("1e","O")
    change_text = change_text.replace("1f","P")
    change_text = change_text.replace("1g","Q")
    change_text = change_text.replace("1h","R")
    change_text = change_text.replace("1i","S")
    change_text = change_text.replace("1j","T")
    change_text = change_text.replace("1k","U")
    change_text = change_text.replace("1l","V")
    change_text = change_text.replace("1m","W")
    change_text = change_text.replace("1n","X")
    change_text = change_text.replace("1o","Y")
    change_text = change_text.replace("1p","Z")
    change_text = change_text.replace("1q","あ")
    change_text = change_text.replace("1r","い")
    change_text = change_text.replace("1s","う")
    change_text = change_text.replace("1t","え")
    change_text = change_text.replace("1u","お")
    change_text = change_text.replace("1v","か")
    change_text = change_text.replace("1w","き")
    change_text = change_text.replace("1x","く")
    change_text = change_text.replace("1y","け")
    change_text = change_text.replace("1z","こ")
    change_text = change_text.replace("20","さ")
    change_text = change_text.replace("21","し")
    change_text = change_text.replace("22","す")
    change_text = change_text.replace("23","せ")
    change_text = change_text.replace("24","そ")
    change_text = change_text.replace("25","た")
    change_text = change_text.replace("26","ち")
    change_text = change_text.replace("27","つ")
    change_text = change_text.replace("28","て")
    change_text = change_text.replace("29","と")
    change_text = change_text.replace("2a","な")
    change_text = change_text.replace("2b","に")
    change_text = change_text.replace("2c","ぬ")
    change_text = change_text.replace("2d","ね")
    change_text = change_text.replace("2e","の")
    change_text = change_text.replace("2f","は")
    change_text = change_text.replace("2g","ひ")
    change_text = change_text.replace("2h","ふ")
    change_text = change_text.replace("2i","へ")
    change_text = change_text.replace("2j","ほ")
    change_text = change_text.replace("2k","ま")
    change_text = change_text.replace("2l","み")
    change_text = change_text.replace("2m","む")
    change_text = change_text.replace("2n","め")
    change_text = change_text.replace("2o","も")
    change_text = change_text.replace("2p","や")
    change_text = change_text.replace("2q","ゐ")
    change_text = change_text.replace("2r","ゆ")
    change_text = change_text.replace("2s","ゑ")
    change_text = change_text.replace("2t","よ")
    change_text = change_text.replace("2u","わ")
    change_text = change_text.replace("2v","を")
    change_text = change_text.replace("2w","ん")
    change_text = change_text.replace("2x","ぁ")
    change_text = change_text.replace("2y","ぃ")
    change_text = change_text.replace("2z","ぅ")
    change_text = change_text.replace("30","ぇ")
    change_text = change_text.replace("31","ぉ")
    change_text = change_text.replace("32","ゃ")
    change_text = change_text.replace("33","ゅ")
    change_text = change_text.replace("34","ょ")
    change_text = change_text.replace("35","っ")
    change_text = change_text.replace("36","が")
    change_text = change_text.replace("37","ぎ")
    change_text = change_text.replace("38","ぐ")
    change_text = change_text.replace("39","げ")
    change_text = change_text.replace("3a","ご")
    change_text = change_text.replace("3b","ざ")
    change_text = change_text.replace("3c","じ")
    change_text = change_text.replace("3d","ず")
    change_text = change_text.replace("3e","ぜ")
    change_text = change_text.replace("3f","ぞ")
    change_text = change_text.replace("3g","だ")
    change_text = change_text.replace("3h","ぢ")
    change_text = change_text.replace("3i","づ")
    change_text = change_text.replace("3j","で")
    change_text = change_text.replace("3k","ど")
    change_text = change_text.replace("3l","ば")
    change_text = change_text.replace("3m","び")
    change_text = change_text.replace("3n","ぶ")
    change_text = change_text.replace("3o","べ")
    change_text = change_text.replace("3p","ぼ")
    change_text = change_text.replace("3q","ぱ")
    change_text = change_text.replace("3r","ぴ")
    change_text = change_text.replace("3s","ぷ")
    change_text = change_text.replace("3t","ぺ")
    change_text = change_text.replace("3u","ぽ")
    change_text = change_text.replace("3v","ア")
    change_text = change_text.replace("3w","イ")
    change_text = change_text.replace("3x","ウ")
    change_text = change_text.replace("3y","エ")
    change_text = change_text.replace("3z","オ")
    change_text = change_text.replace("40","カ")
    change_text = change_text.replace("41","キ")
    change_text = change_text.replace("42","ク")
    change_text = change_text.replace("43","ケ")
    change_text = change_text.replace("44","コ")
    change_text = change_text.replace("45","サ")
    change_text = change_text.replace("46","シ")
    change_text = change_text.replace("47","ス")
    change_text = change_text.replace("48","セ")
    change_text = change_text.replace("49","ソ")
    change_text = change_text.replace("4a","タ")
    change_text = change_text.replace("4b","チ")
    change_text = change_text.replace("4c","ツ")
    change_text = change_text.replace("4d","テ")
    change_text = change_text.replace("4e","ト")
    change_text = change_text.replace("4f","ナ")
    change_text = change_text.replace("4g","ニ")
    change_text = change_text.replace("4h","ヌ")
    change_text = change_text.replace("4i","ネ")
    change_text = change_text.replace("4j","ノ")
    change_text = change_text.replace("4k","ハ")
    change_text = change_text.replace("4l","ヒ")
    change_text = change_text.replace("4m","フ")
    change_text = change_text.replace("4n","ヘ")
    change_text = change_text.replace("4o","ホ")
    change_text = change_text.replace("4p","マ")
    change_text = change_text.replace("4q","ミ")
    change_text = change_text.replace("4r","ム")
    change_text = change_text.replace("4s","メ")
    change_text = change_text.replace("4t","モ")
    change_text = change_text.replace("4u","ヤ")
    change_text = change_text.replace("4v","ユ")
    change_text = change_text.replace("4w","ヨ")
    change_text = change_text.replace("4x","ラ")
    change_text = change_text.replace("4y","リ")
    change_text = change_text.replace("4z","ル")
    change_text = change_text.replace("50","レ")
    change_text = change_text.replace("51","ロ")
    change_text = change_text.replace("52","ワ")
    change_text = change_text.replace("53","ヲ")
    change_text = change_text.replace("54","ン")
    change_text = change_text.replace("55","ァ")
    change_text = change_text.replace("56","ィ")
    change_text = change_text.replace("57","ゥ")
    change_text = change_text.replace("58","ェ")
    change_text = change_text.replace("59","ォ")
    change_text = change_text.replace("5a","ャ")
    change_text = change_text.replace("5b","ュ")
    change_text = change_text.replace("5c","ョ")
    change_text = change_text.replace("5d","ッ")
    change_text = change_text.replace("5e","ガ")
    change_text = change_text.replace("5f","ギ")
    change_text = change_text.replace("5g","グ")
    change_text = change_text.replace("5h","ゲ")
    change_text = change_text.replace("5i","ゴ")
    change_text = change_text.replace("5j","ザ")
    change_text = change_text.replace("5k","ジ")
    change_text = change_text.replace("5l","ズ")
    change_text = change_text.replace("5m","ゼ")
    change_text = change_text.replace("5n","ゾ")
    change_text = change_text.replace("5o","ダ")
    change_text = change_text.replace("5p","ヂ")
    change_text = change_text.replace("5q","ヅ")
    change_text = change_text.replace("5r","デ")
    change_text = change_text.replace("5s","ド")
    change_text = change_text.replace("5t","バ")
    change_text = change_text.replace("5u","ビ")
    change_text = change_text.replace("5v","ブ")
    change_text = change_text.replace("5w","ベ")
    change_text = change_text.replace("5x","ボ")
    change_text = change_text.replace("5y","パ")
    change_text = change_text.replace("5z","ピ")
    change_text = change_text.replace("60","プ")
    change_text = change_text.replace("61","ペ")
    change_text = change_text.replace("62","ポ")
    change_text = change_text.replace("63","ー")
    change_text = change_text.replace("64","!")
    change_text = change_text.replace("65",'"')
    change_text = change_text.replace("66","'")
    change_text = change_text.replace("67","#")
    change_text = change_text.replace("68","$")
    change_text = change_text.replace("69","%")
    change_text = change_text.replace("6a","&")
    change_text = change_text.replace("6b","(")
    change_text = change_text.replace("6c",")")
    change_text = change_text.replace("6d","=")
    change_text = change_text.replace("6e","-")
    change_text = change_text.replace("6f","~")
    change_text = change_text.replace("6g","^")
    change_text = change_text.replace("6h","@")
    change_text = change_text.replace("6i","|")
    change_text = change_text.replace("6j","￥")
    change_text = change_text.replace("6k","`")
    change_text = change_text.replace("6l","{")
    change_text = change_text.replace("6m","[")
    change_text = change_text.replace("6n","「")
    change_text = change_text.replace("6o","+")
    change_text = change_text.replace("6p","*")
    change_text = change_text.replace("6q",";")
    change_text = change_text.replace("6r",":")
    change_text = change_text.replace("6s","}")
    change_text = change_text.replace("6t","]")
    change_text = change_text.replace("6u","」")
    change_text = change_text.replace("6v","<")
    change_text = change_text.replace("6w",",")
    change_text = change_text.replace("6x","、")
    change_text = change_text.replace("6y",">")
    change_text = change_text.replace("6z",".")
    change_text = change_text.replace("70","。")
    change_text = change_text.replace("71","?")
    change_text = change_text.replace("72","/")
    change_text = change_text.replace("73","・")
    change_text = change_text.replace("74","_")
    change_text = change_text.replace("75"," ")
    change_text = change_text.replace("76","ゔ")
    change_text = change_text.replace("77","ヴ")
    change_text = change_text.replace("0z","z")
    change_text = change_text.replace("0y","y")
    change_text = change_text.replace("0x","x")
    change_text = change_text.replace("0w","w")
    change_text = change_text.replace("0v","v")
    change_text = change_text.replace("0u","u")
    change_text = change_text.replace("0t","t")
    change_text = change_text.replace("0s","s")
    change_text = change_text.replace("0r","r")
    change_text = change_text.replace("0q","q")
    change_text = change_text.replace("0p","p")
    change_text = change_text.replace("0o","o")
    change_text = change_text.replace("0n","n")
    change_text = change_text.replace("0m","m")
    change_text = change_text.replace("0l","l")
    change_text = change_text.replace("0k","k")
    change_text = change_text.replace("0j","j")
    change_text = change_text.replace("0i","i")
    change_text = change_text.replace("0h","h")
    change_text = change_text.replace("0g","g")
    change_text = change_text.replace("0f","f")
    change_text = change_text.replace("0e","e")
    change_text = change_text.replace("0d","d")
    change_text = change_text.replace("0c","c")
    change_text = change_text.replace("0b","b")
    change_text = change_text.replace("0a","a")
    change_text = change_text.replace("09","9")
    change_text = change_text.replace("08","8")
    change_text = change_text.replace("07","7")
    change_text = change_text.replace("06","6")
    change_text = change_text.replace("05","5")
    change_text = change_text.replace("04","4")
    change_text = change_text.replace("03","3")
    change_text = change_text.replace("02","2")
    change_text = change_text.replace("01","1")
    change_text = change_text.replace("00","0")
    return change_text
    
#プログラムの実行開始場所
while True:
    if num == 0:
        input("こんにちは私は暗号化シュミレーターです。")
        num = 1
        
    elif num == 1:
        #モード選択
        mode = input("1:暗号化,2:暗号解除,3:終了\n")
        #modeに１を代入すると暗号化の場所に指示される
        if mode == str("1") or mode == str("１"):
            num = 2
        #modeに２を代入すると暗号化の場所に指示される
        elif mode == str("2") or mode == str("２"):
            num = 10
        #modeに３を代入するとプログラムが終了される
        elif mode == str("3") or mode == str("３"):
            break
        #1,2,3以外が代入されるとやり直し
        else:
            continue
        
    elif num == 2:
        #plaintextに平文（暗号化したい文）を挿入
        plaintext = input("暗号化したい言葉を入力してください！\nただし、漢字または記号を使用しないでください\n")
        #plaintextに何も文字を打たないで進めるとエラーが発生し、ループを行う
        if plaintext == str(""):
            continue
        else:
            num = 3
            
    elif num == 3:
        #plaintextの文の全角の英単語を半角に直す処理を行う
        plaintext=unicodedata.normalize('NFKC', plaintext)
        #plaintextを英数字に変換してchange_plaintextに代入する
        change_plaintext=change1(plaintext)
        num = 4
        
    #乱数の算出
    elif num == 4:
        #random_number1は3~9までの数字の乱数
        random_number1=int(random.randint(3,9))
        #random_number2は0~zまでの英数字を含む乱数
        random_number2=random.choice(random_list1)
        num=5
        
    #文字列の格納
    elif num==5:
        #change_plaintextに格納されている英数字をリストであるchange_plaintext_listに格納
        for i in change_plaintext:
            change_plaintext_list.append(i)
        num=6
        
    #暗号化
    elif num==6:
        #暗号化の計算
        try:
            encryption(change_plaintext,random_number1,random_number2)
        except ValueError:
            num=50
        else:
            num=7
    elif num==7:
        #dummy1とdummy2はダミー文字
        dummy1=pass_code_list[-2]
        dummy2=int(random.randint(0,2))+dic4[pass_code_list[-1]]
        if dummy2>=10:
            dummy2=random.choice(random_list2)
        #求めた暗号を二つの乱数を暗号の後ろに代入してciphertextを作成する
        ciphertext=''.join(ciphertext_list)+str(random_number1)+str(random_number2)
        #求めたpass_code_listをダミー文字二つを暗号の後ろに代入してpass_codeを作成する
        pass_code=''.join(map(str, pass_code_list))+str(dummy1)+str(dummy2)
        #結果の出力
        print(f"暗号 {ciphertext}")
        print(f"pass {pass_code}")
        #リストの初期化
        change_plaintext_list=[]
        ciphertext_list=[]
        pass_code_list=[]
        num=1
    
    elif num==10:
        ciphertext=input("復号化させたい暗号文を入力してください！\n")
        if len(ciphertext)%2==0:
            num=11
        else:
            num=51
            
    elif num==11:
        for i in ciphertext:
            change_plaintext_list.append(i)
        #ダミー文字を抜いた暗号文
        ciphertext_nodummy=change_plaintext_list[:-2]
        #偶数の乱数
        random_number1=change_plaintext_list[-2]
        #奇数の乱数
        random_number2=change_plaintext_list[-1]
        num=12
        
    elif num==12:
        pass_code=input("passを教えてください！\n")
        #passと暗号文が等しくないならエラーが起こる
        if len(ciphertext)==len(pass_code):
            num=13
        else:
            num=52
            
    elif num==13:
        #復号化の計算を行う
        #ciphertext_nodummyは暗号文、random_number1は一つ目の乱数、random_number2は二つ目の乱数、pass_codeはpass
        try:
            decode(ciphertext_nodummy,random_number1,random_number2,pass_code)
        except ValueError:
            num=51
        else:
            num=14
        
    elif num==14:
        #元に戻した平文の英数字を文字に戻す作業をし平文に変更する
        for i in range(0,len(decode_list),2):
            #decode_twotextという文字に二つの英数字の格納
            decode_twotext=''.join(decode_list[i:i+2])
            #格納した二つの文字を一つの文字に変更する
            plaintext_one=change2(decode_twotext)
            #文字をplaintext_listに格納する
            plaintext_list.append(str(plaintext_one))
        num=15
        
    elif num==15:
        #格納した文字を取り出す作業を行う
        plaintext=''.join(plaintext_list)
        #結果の出力
        print(f"文章 {plaintext}")
        #リストの初期化
        change_plaintext_list=[]
        decode_list=[]
        plaintext_list=[]
        num=1
        
    #num=50~52はエラー表示
    elif num == 50:
        print("漢字もしくは対応していない記号を暗号化することができません！")
        ciphertext=[]
        change_plaintext_list=[]
        pass_code_list=[]
        num = 2
        
    elif num == 51:
        print("その文を暗号化することができません！")
        change_plaintext_list=[]
        decode_list=[]
        plaintext_list=[]
        num = 10
        
    elif num == 52:
        print("そのpassは使用できません！")
        change_plaintext_list=[]
        num = 13
        