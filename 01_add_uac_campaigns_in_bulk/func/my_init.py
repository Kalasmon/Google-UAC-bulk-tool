#!/usr/bin/env python
# -*- coding: utf-8 -*-


def myinitostype(ostype):

    os = {'adr':['adr'], 'ios':['ios'], 'both':['adr', 'ios']}
    return os[ostype]
    


def myinitgeolist(ostype, listtype):
    
    geodict = {
        'adr':{
            'all':['ae', 'au', 'bd', 'dz', 'eg', 'id', 'in', 'iq', 'jp', 'kh', 'kr', 'kw', 'ma', 'my', 'nz', 'ph', 'pk', 'qa', 'ru', 'sa', 'sg', 'th', 'tw', 'uk', 'us', 'vn'],
            'muslin':['ae', 'iq', 'kw', 'qa', 'sa'],
            'asia':['id', 'jp', 'kh', 'kr', 'my', 'sg', 'th', 'tw', 'vn'],
            'asia-big':['bd', 'id', 'in', 'jp', 'kh', 'kr', 'my', 'ph', 'pk', 'sg', 'th', 'tw', 'vn'],
            'ybm':['bd', 'in', 'pk'],
            'cnt':['tw', 'sg', 'my'],
            'xyx':['bd', 'eg', 'id', 'in', 'iq', 'jp', 'kh', 'kw', 'ma', 'my', 'ph', 'pk', 'qa', 'ru', 'sa', 'th', 'tr', 'vn'],
            'dan':['th'],
            'oumei':['au', 'nz', 'ru', 'sg', 'uk', 'us']
            },
        'ios':{
            'all':['ae', 'au', 'bd', 'dz', 'eg', 'id', 'in', 'iq', 'jp', 'kh', 'kr', 'kw', 'ma', 'my', 'nz', 'ph', 'pk', 'qa', 'ru', 'sa', 'sg', 'th', 'tw', 'uk', 'us', 'vn'],
            'muslin':['ae', 'iq', 'kw', 'qa', 'sa'],
            'asia':['id', 'jp', 'kh', 'kr', 'my', 'sg', 'th', 'tw', 'vn'],
            'asia-big':['bd', 'id', 'in', 'jp', 'kh', 'kr', 'my', 'ph', 'pk', 'sg', 'th', 'tw', 'vn'],
            'ybm':['bd', 'in', 'pk'],
            'cnt':['tw', 'sg', 'my'],
            'xyx':['bd', 'eg', 'id', 'in', 'iq', 'jp', 'kh', 'kw', 'ma', 'my', 'ph', 'pk', 'qa', 'ru', 'sa', 'th', 'tr', 'vn'],
            'dan':['th'],
            'oumei':['au', 'nz', 'ru', 'sg', 'uk', 'us']
            }
        }
    
    return geodict[ostype][listtype]



def myinitbanlist(ostype, bantype):
    bandict = {
        # Updated at 0707
        'adr':{
            'low':[ ],
            'mid':['jp', 'kr'],
            'nan':['au', 'nz']
            },
        # Updated at 0628
        'ios':{
            'low':[ ],
            'mid':['jp', 'kr'],
            'nan':[ ]
            }
        }

    return bandict[ostype][bantype]



def myinitgbbid(ostype, geo, mediatype):
     
    gbbiddict = {
        'gb':{
            'adr':{
                'ae':'0900000',
                'au':'3800000',# 170823 1.80->2.00 170920 2.00->1.60 171011 1.60->2.00
                'bd':'0240000',
                #'br':'0250000',
                'ca':'2200000',# 170920 2.00->1.60
                #'de':'1200000',
                'dz':'0210000',
                'eg':'0260000',
                'hk':'1500000',
                'id':'0700000',# 171011 0.45->0.48
                'in':'0360000',# 170823 0.20->0.22 170826 0.22->0.30 170908 0.30->0.22
                'iq':'0300000',# 170823 0.11->0.16 170908 0.16->0.13
                'jp':'3800000',# 170823 1.80->2.20
                'kh':'0500000',
                'kr':'2400000',
                'kw':'1100000',
                'ma':'0260000',
                'my':'1100000',
                #'ng':'0300000',
                'nz':'3800000',
                'ph':'0420000',
                'pk':'0300000',
                'qa':'1100000',
                'ru':'0750000',
                'sa':'1200000',# 180515 0.80->0.85
                'sg':'1600000',
                'th':'0600000',# 180211 0.70->0.65
                'tr':'0400000',
                'tw':'2000000',
                'uk':'2000000',
                'us':'2300000',# 180515 2.00->1.80
                'vn':'0650000', # 180211 0.60->0.55 180619 0.55->0.50
                #'za':'0500000'
                },
            'ios':{
                'ae':'1400000',
                'au':'4000000',
                'bd':'0700000',
                #'br':'0550000',
                'ca':'2500000',
                #'de':'1500000',
                'dz':'0800000',
                'eg':'0700000',
                'hk':'2000000',
                'id':'1400000',# 170823 0.70->0.90 170911 0.90->0.80
                'in':'0700000',# 170823 0.50->0.60 170826 0.60->0.80 170908 0.80->0.60
                'iq':'0800000',
                'jp':'4500000',# 170823 2.50->3.00 170911 
                'kh':'0800000',
                'kr':'2800000',
                'kw':'1400000',# 170823 0.30->0.60
                'ma':'0800000',
                'nz':'4000000',
                #'ng':'1000000',
                'my':'1600000',
                'ph':'0800000',
                'pk':'0700000',
                'qa':'1400000',# 170823 0.30->0.60
                'ru':'1200000',
                'sa':'1500000',# 170823 0.60->0.80 170826 0.80->1.00 170908 1.00->0.80
                'sg':'1700000',
                'th':'1000000',# 170823 0.80->1.00 170908 1.00->0.90
                'tr':'0600000',
                'tw':'2500000',
                'uk':'2800000',
                'us':'2700000',# 170823 1.20->1.50 170826 1.50->2.00
                'vn':'1000000',
                'za':'1000000'
                }
            },

        'gy':{
            'adr':{
                #'ae':'0430000',
                'au':'2000000',# 170823 1.50->2.00 170920 2.00->1.60 1.60->2.00
                #'br':'0220000',
                #'ca':'1600000',# 170920 2.00->1.60
                #'de':'1000000',
                #'eg':'0180000',
                #'hk':'1500000',
                'id':'0500000',# 171011 0.45->0.48
                'in':'0230000',# 170826 0.22->0.30 170908 0.30->0.22
                'iq':'0160000',# 170823 0.12->0.15 170908 0.15->0.12
                'jp':'2500000',# 170823 1.80->2.00
                'kr':'0750000',
                'kw':'0450000',
                #'ma':'0140000',
                'my':'0550000',
                'ph':'0370000',
                'qa':'0420000',
                #'ru':'0450000',
                'sa':'0550000',# 170823 0.45->0.48 170826 0.48->0.50 170908 0.50->0.45 20170918 0.45->0.55
                'sg':'1000000',
                'th':'0500000',
                'tw':'1000000',
                'uk':'1200000',
                'us':'1300000',
                'vn':'0400000'               
                },
            'ios':{
                #'ae':'0650000',
                'au':'2000000',
                'br':'0550000',
                #'ca':'2500000',
                #'de':'1200000',
                #'eg':'0000000',
                'hk':'2500000',
                'id':'1000000',
                'in':'0700000',# 170823 0.50->0.60 170826 0.60->0.80 170908 0.80->0.60
                'iq':'0500000',
                'jp':'3000000',# 170823 2.00->3.00
                'kr':'1600000',
                'kw':'0700000',# 170823 0.30->0.60
                #'ma':'0350000',
                'my':'1500000',
                'ph':'0600000',
                'qa':'0600000',# 170823 0.30->0.60
                'ru':'0900000',
                'sa':'0800000',# 170826 0.80->1.00 170908 1.00->0.80 170914 0.80->1.00
                'sg':'2000000',# 170823 1.00->1.50
                'th':'1000000',# 170823 0.60->0.80
                'tw':'0700000',
                'uk':'2000000',
                'us':'2000000',# 170823 1.20->1.50 170826 1.50->2.00
                'vn':'0700000'
                }
            }
        }
    
    return gbbiddict['gb'][ostype][geo]




def myinitcustomerid_div(ostype):
    
    customeriddict = {'adr':'814-932-3139', 'ios':'760-757-2931'}
    return customeriddict[ostype]




def myinitcustomerid(ostype, geo, listtype):
    
    if listtype == 'test':
        customeriddict = {
            'adr':{
                'my':'661-936-8874',
                'th':'661-936-8874',
                'sa':'661-936-8874',
                'vn':'661-936-8874'
                },
            'ios':{
                'my':'214-093-5105	',
                'th':'214-093-5105	',
                'sa':'214-093-5105	',
                'vn':'214-093-5105	'
                }            
            }

    else:
        customeriddict = {
            # Updated at 0704
            'adr':{  
                'ae':'814-932-3139', 
                'au':'814-932-3139',
                'bd':'814-932-3139',
                #'br':'243-285-2992', 
                #'ca':'847-363-6949', 
                #'de':'510-506-5001', 
                #'eg':'664-903-9286',
                #'hk':'364-837-3198',
                'id':'814-932-3139', # dvi 2
                'in':'814-932-3139', # dvi 2
                'iq':'814-932-3139', # dvi 2
                'jp':'814-932-3139', 
                'kr':'814-932-3139',
                'kw':'814-932-3139', 
                #'ma':'984-313-8954',
                'my':'814-932-3139', 
                'ph':'814-932-3139', 
                'qa':'814-932-3139', 
                'ru':'814-932-3139',
                'sa':'814-932-3139', # dvi 2
                'sg':'814-932-3139', 
                'th':'814-932-3139', # dvi 2
                'tr':'814-932-3139',
                #'tw':'855-547-0305',
                'uk':'814-932-3139', 
                'us':'814-932-3139',
                'vn':'814-932-3139'  # dvi 2
                },
            # Updated at 0628
            'ios':{
                'ae':'760-757-2931',
                'au':'760-757-2931',
                'bd':'760-757-2931',
                #'br':'696-420-2488',
                #'ca':'639-837-2849',
                #'de':'939-879-0223',
                #'eg':'357-547-0091', # dvi
                #'hk':'414-646-0411',
                'id':'760-757-2931', 
                'in':'760-757-2931', 
                'iq':'760-757-2931',
                'jp':'760-757-2931',
                'kr':'760-757-2931',
                'kw':'760-757-2931', 
                #'ma':'357-547-0091', 
                'my':'760-757-2931', 
                'ph':'760-757-2931', 
                'qa':'760-757-2931',
                'ru':'760-757-2931', 
                'sa':'760-757-2931',  # dvi
                'sg':'760-757-2931', 
                'th':'760-757-2931', 
                'tr':'760-757-2931', 
                #'tw':'113-926-3315',
                'uk':'760-757-2931',
                'us':'760-757-2931',
                'vn':'760-757-2931'
                }
            }
        
    return customeriddict[ostype]['ae']




def myinitgeocode(geo):

    geocodedict = {'ae':2784, 'au':2036, 'bd':2050, 'br':2076, 'ca':2124, 'de':2276, 'dz':2012, 'eg':2818, 'hk':2344, 'id':2360, 'in':2356, 'iq':2368, 'jp':2392, 'kh':2116, 'kr':2410, 'kw':2414, 'ma':2504, 'my':2458, 'ng':2566, 'nz':2554, 'ph':2608, 'pk':2586, 'qa':2634, 'ru':2643, 'sa':2682, 'sg':2702, 'th':2764, 'tr':2792, 'tw':2158, 'uk':2826, 'us':2840, 'vn':2704, 'za':2710}
    return geocodedict[geo]



def myinitimglan(geo):

    imglandict = {'ae':'阿拉', 'au':'英语', 'bd':'英语', 'br':'葡语', 'ca':'英语', 'de':'德语', 'eg':'阿拉', 'hk':'香港', 'id':'印尼', 'in':'英语', 'iq':'阿拉', 'jp':'日语', 'kr':'韩语', 'kw':'阿拉', 'ma':'阿拉', 'my':'马来', 'ng':'英语', 'nz':'英语', 'ph':'菲律', 'pk':'英语', 'qa':'阿拉', 'ru':'俄语', 'sa':'阿拉', 'sg':'英语', 'th':'泰语', 'tr':'土语', 'tw':'台湾', 'uk':'英语', 'us':'英语', 'vn':'越南', 'za':'英语'}
    return imglandict[geo]



def myinittxtlan(geo):
    
    txtlandict = {
        '英语':['Find who is nearby', 'Join a multi-guest room.', 'Watch and chat with me!', 'More fun for you'],
        '阿拉':['تحميل مجانا', 'شاهد هذا البث معى!', 'اعرف من بالقرب منك الأن.', 'مرحبا هل انت هناك؟'],
        '印尼':['Hi, apa kabar?', 'Tonton dan chat denganku!', 'Temukan orang di sekitar.', 'Download gratis'],
        '葡语':['18 garotas próximas', 'Oi, você é solteira?', 'Assista e fale comigo!', 'Quer jogar com a gente?'],
        '土语':['Selam orada mısın?', 'Hemen yayına katıl', 'gününü reklendir', 'Çevrimiçi parti yapalım'],
        '越南':['Xin chào,bạn có đó không?', 'Trò chuyện với tôi nhé!', 'Tìm người đang gần bạn', 'Tải miễn phí'],
        '泰语':['สวัสดีค่ะ อยู่ไหมคะ', 'ดูไลฟ์สดและแชทกับฉัน', 'ค้นหาคนอยู่ใกล้คุณ', 'โหลดฟรี'],
        '俄语':['Привет, Ты с нами?', 'Смотри и общайся со мной!', 'Скачать бесплатно', '17 и более'],
        '菲律':['18 Girls Kalapit.', 'Hi, Sigurado ka single?', 'kausapin mo ako!', 'Makipaglaro sa amin?'],
        '马来':['Hi, awak di sana?', 'Cari siapa berdekatan', 'Berbual dengan saya!', 'Muat-turun secara Percuma'],
        '香港':['全天在線等妳', '免費download', '睇周邊靓女直播', '驚喜不斷'],
        '台湾':['24小時在線等妳', '聽正妹各種專屬悄悄話', '看正妹玩遊戲', '與上千正妹親密互動'],
        '韩语':['안녕, 거기 있니?', '나랑 지켜보고 채팅해라', '근처에 누가 있을까요', '무료로 다운로드'],
        '日语':['パーティーしよう', '皆と楽しく遊ぼう', '毎日新しいビデオを更新', '無料ダウンロード']
        }
    
    pkdict = {
        '英语':['Watch funny PK battle', 'Make your bet now!', 'Win and get your prize', 'Watch more'],
        '阿拉':['مشاهدة معركة مضحك من PK', 'جعل الرهان الآن', 'الفوز بالجائزة الخاصة بك', 'شاهد المزيد'],
        '印尼':['Tonton lucu PK', 'Buat taruhan Anda!', 'Menangkan hadiahmu', 'Tonton lebih banyak'],
        '越南':['Xem trận chiến vui PK', 'Đặt cược ngay!', 'Giành giải thưởng của bạn', 'xem thêm'],
        '泰语':['ดูการต่อสู้ PK ตลก', 'ทำการเดิมพันของคุณ!', 'ชนะและได้รับรางวัลของคุณ', 'ดูเพิ่มเติม']
        }
    
    hqdict = {
        '英语':['Get your prize.', 'Your are next Winner.', 'Win and get your prize.', 'Get dollars now!'],
        '印尼':['Join Quiz', 'Hadiah terbagi', 'Pemenang', 'Dapatkan dollar sekarang!']
            }
    
    xmaslandict = {
        '英语':['Merry Christmas', 'Celebrate with you love.', 'Get your Christmas gifts!', ' Tap to know more'],
        '阿拉':[' شارك بغرفة البث المتعدد.', 'تابع وشاهد المزيد.', 'تعرف على شخص تحبة.', 'انا هنا كل يوم لك'],
        '印尼':['Hi, apa kabar?', 'Tonton dan chat denganku!', 'Temukan orang di sekitar.', 'Download gratis'],
        '葡语':['18 garotas próximas', 'Oi, você é solteira?', 'Assista e fale comigo!', 'Quer jogar com a gente?'],
        '土语':['Selam orada mısın?', 'Hemen yayına katıl', 'gününü reklendir', 'Çevrimiçi parti yapalım'],
        '越南':['Xin chào,bạn có đó không?', 'Trò chuyện với tôi nhé!', 'Tìm người đang gần bạn', 'Tải miễn phí'],
        '泰语':['สวัสดีค่ะ อยู่ไหมคะ', 'ดูไลฟ์สดและแชทกับฉัน', 'ค้นหาคนอยู่ใกล้คุณ', 'โหลดฟรี'],
        '俄语':['Привет, Ты с нами?', 'Смотри и общайся со мной!', 'Скачать бесплатно', '17 и более'],
        '菲律':['18 Girls Kalapit.', 'Hi, Sigurado ka single?', 'kausapin mo ako!', 'Makipaglaro sa amin?'],
        '马来':['Hi, awak di sana?', 'Cari siapa berdekatan', 'Berbual dengan saya!', 'Muat-turun secara Percuma'],
        '香港':['全天在線等妳', '免費download', '睇周邊靓女直播', '驚喜不斷'],
        '台湾':['24小時在線等妳', '聽正妹各種專屬悄悄話', '看正妹玩遊戲', '與上千正妹親密互動'],
        '韩语':['안녕, 거기 있니?', '나랑 지켜보고 채팅해라', '근처에 누가 있을까요', '무료로 다운로드'],
        '日语':['パーティーしよう', '皆と楽しく遊ぼう', '毎日新しいビデオを更新', '無料ダウンロード']
        }
    
    yxzhalandict = {
        '英语':['Join us to play cards.', 'Download for free.', 'Try more exciting games.', 'Make new friends.'],
        '阿拉':[' وكون صداقات.', 'المزيد من الألعاب المثيرة', 'تحميل مجاني.', 'انضم إلينا للعب الورق'],
        '印尼':['Untuk bermain kartu.', 'Download gratis.', 'Lebih banyak game asyik.', 'Bertemu teman baru'],
        '越南':['Hay chơi cùng chúng tôi', 'Tải miễn phí', 'Chơi game khác', 'Có thêm bạn'],
        '泰语':['เพื่อเล่นไพ่', 'ดาวน์โหลดฟรี', 'เล่นเกมส์อื่นๆเพิ่มเติม', 'ทำความรู้จักกับเพื่อน'],
        '俄语':['игре в карты', 'Скачать бесплатно', 'Посмотреть подобные игры', 'Убить время& найти друзей'],
        '马来':['Bermain kad.', 'Muat turun secara percuma', 'Cuba permainan yang lebih', 'Buat rakan baru semasa'],
        '日语':['一緒にポーカーを楽しもう', '無料ダウンロード', 'ゲームをもっと見る', '友達づくり']
        }
    
    yxflplandict = {
        '英语':['Tap to Fly', 'Download for free.', 'Try more exciting games.', 'Make new friends.'],
        '阿拉':[' وكون صداقات.', 'المزيد من الألعاب المثيرة', 'تحميل مجاني.', 'اضغط على الطيران'],
        '印尼':['Tap untuk Terbang.', 'Download gratis.', 'Lebih banyak game asyik.', 'Bertemu teman baru'],
        '越南':['Ấn để bay', 'Tải miễn phí', 'Chơi game khác', 'Có thêm bạn'],
        '泰语':['แตะเพื่อบิน', 'ดาวน์โหลดฟรี', 'เล่นเกมส์อื่นๆเพิ่มเติม', 'ทำความรู้จักกับเพื่อน'],
        '俄语':['Нажми для полета', 'Скачать бесплатно', 'Посмотреть подобные игры', 'Убить время& найти друзей'],
        '马来':['Tap untuk terbang.', 'Muat turun secara percuma', 'Cuba permainan yang lebih', 'Buat rakan baru semasa'],
        '日语':['タップして飛ぶ', '無料ダウンロード', 'ゲームをもっと見る', '友達づくり']
        }
    
    yxjmplandict = {
        '英语':['Tap to Jump', 'Download for free.', 'Try more exciting games.', 'Make new friends.'],
        '阿拉':[' وكون صداقات.', 'المزيد من الألعاب المثيرة', 'تحميل مجاني.', 'اضغط للقفز'],
        '印尼':['Tap to Jump .', 'Download gratis.', 'Lebih banyak game asyik.', 'Bertemu teman baru'],
        '越南':['Ấn để nhảy', 'Tải miễn phí', 'Chơi game khác', 'Có thêm bạn'],
        '泰语':['แตะเพื่อบิน', 'ดาวน์โหลดฟรี', 'เล่นเกมส์อื่นๆเพิ่มเติม', 'ทำความรู้จักกับเพื่อน'],
        '俄语':['Нажать и подпрыгнуть', 'Скачать бесплатно', 'Посмотреть подобные игры', 'Убить время& найти друзей'],
        '马来':['Tap untuk lompat.', 'Muat turun secara percuma', 'Cuba permainan yang lebih', 'Buat rakan baru semasa'],
        '日语':['タップしてジャンプ', '無料ダウンロード', 'ゲームをもっと見る', '友達づくり']
        }
    
    xyxgeolandic = {
                 'bd':'英语',
                 'eg':'阿拉',
                 'id':'印尼',
                 'in':'英语',
                 'iq':'阿拉',
                 'jp':'日语',
                 'kh':'英语',
                 'kw':'阿拉',
                 'ma':'阿拉',
                 'my':'马来',
                 'ph':'英语',
                 'pk':'英语',
                 'qa':'阿拉',
                 'ru':'俄语',
                 'sa':'阿拉',
                 'th':'泰语',      
                 'tr':'英语', 
                 'vn':'越南'
                 }
    
    

    geolandic = {'ae':'阿拉',
                 'au':'英语',
                 'bd':'英语',
                 'br':'葡语',
                 'ca':'英语', 
                 'de':'英语',
                 'eg':'阿拉',
                 'hk':'香港',
                 'id':'印尼',
                 'in':'英语',
                 'iq':'阿拉',
                 'jp':'日语',
                 'kh':'英语',
                 'kr':'韩语',
                 'kw':'阿拉',
                 'ma':'阿拉',
                 'my':'马来',
                 'nz':'英语',
                 'ng':'英语',
                 'ph':'菲律',
                 'pk':'英语',
                 'qa':'阿拉',
                 'ru':'俄语',
                 'sa':'阿拉',
                 'sg':'英语',
                 'th':'泰语',
                 'tr':'土语',
                 'tw':'台湾',
                 'uk':'英语',
                 'us':'英语',
                 'vn':'越南',
                 'za':'英语'
                 }
    
    
    pkgeolandic = {
                 'au':'英语',
                 'id':'印尼',
                 'in':'英语',
                 'iq':'阿拉',
                 'kw':'阿拉',
                 'my':'英语',
                 'ph':'英语',
                 'qa':'阿拉',
                 'ru':'俄语',
                 'sa':'阿拉',
                 'th':'泰语',
                 'uk':'英语',
                 'us':'英语',
                 'vn':'越南'
                 }
    
    

    return txtlandict[geolandic[geo]]
    ## return yxjmplandict[xyxgeolandic[geo]]
    ## return hqdict[geolandic[geo]]
    ## return xmaslandict['英语']



def myinitappid(ostype):

    appiddict = {'adr':'sg.bigo.live', 'ios':'1077137248'}
    return appiddict[ostype]

def myinitappvendor(ostype):

    appiddict = {'adr':'VENDOR_GOOGLE_MARKET', 'ios':'VENDOR_APPLE_APP_STORE'}
    return appiddict[ostype]


def myinitimgdir(imgtype):
    if imgtype == 'all':
        imgdir = 'C:/Python27/adwapi/04_finalsolution/material/images_all'
    elif imgtype == 'geo':
        imgdir = 'C:/Python27/adwapi/04_finalsolution/material/images_geo'
    return imgdir


def myinitvdodir():
    vdodir = 'C:/Python27/adwapi/04_finalsolution/material/videos/'
    return vdodir

    
    

