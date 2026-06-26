from django.shortcuts import render

article=[
    {
        'id':1,
        'pic':'https://bangaloretourism.in/images/v2/packages/places-to-visit-in-bangalore-header.jpg',
        'title':'Its all about the Bengluru',
        'disc':' Bengaluru is the capital of Karnataka and is widely known as the Silicon Valley of India. It is home to numerous IT companies, startups, and educational institutions, making it a major center for technology, innovation, and employment. The city enjoys a pleasant climate throughout most of the year.Apart from its technology sector, Bengaluru is famous for its beautiful parks, vibrant nightlife, shopping malls, and cultural heritage. Popular attractions include Lalbagh Botanical Garden, Cubbon Park, and Bangalore Palace, which attract visitors from around the world.'
    },
      {
        'id':2,
        'pic':'https://titosgoa.com/_next/image?url=%2Fapi%2Fuploads%2F1768282500728-why-tourists-visit-goa.png&w=1920&q=75',
        'title':'Its all about the Goa',
        'disc':' Goa is Indias smallest state by area and is famous for its beautiful beaches, Portuguese heritage, and vibrant tourism industry. It attracts millions of visitors every year who come to enjoy its scenic coastline, water sports, and relaxed lifestyle.Goa is also known for its historic churches, delicious seafood, and colorful festivals. Popular destinations include Basilica of Bom Jesus, Calangute Beach, and Dudhsagar Falls, making it one of Indias top holiday destinations.'
    },
      {
        'id':3,
        'pic':'https://cabbazar.com/blog/content/images/size/w2000/2025/03/Mangalore-tourist-places-4.jpg',
        'title':'Its all about the Mangalore',
        'disc':' Mangaluru is an important coastal city in Karnataka, known for its ports, educational institutions, and beautiful beaches. It plays a significant role in trade, banking, and the fishing industry along Indias western coast.The city is famous for its rich cultural heritage, temples, churches, and delicious coastal cuisine. Attractions such as Panambur Beach and Kadri Manjunath Temple make it a popular destination for tourists and pilgrims alike.'
    },
      {
        'id':4,
        'pic':'https://s7ap1.scene7.com/is/image/incredibleindia/red-fort-delhi1-attr-hero?qlt=82&ts=1742170492880',
        'title':'Its all about the Delhi',
        'disc':' Delhi is the capital of India and serves as the countrys political and administrative center. It is a city where ancient history blends with modern development, offering visitors a unique cultural experience.Delhi is home to many famous monuments, including Red Fort, India Gate, and Qutub Minar. The city is also renowned for its diverse cuisine, bustling markets, and vibrant festivals.'
    },
      {
        'id':5,
        'pic':'https://kstdc.co/wp-content/uploads/2021/08/Dollu.jpg',
        'title':'Its all about the north-karnataka',
        'disc':'North Karnataka is a culturally rich region known for its historical monuments, traditional arts, and agricultural economy. The region has a distinct Kannada dialect and is home to many important historical sites and religious centers. North Karnataka includes famous destinations such as Hampi, Badami Cave Temples, and Gol Gumbaz. It is celebrated for its warm hospitality, unique cuisine like jolada rotti, and rich traditions that reflect Karnatakas heritage.'
    },
      {
        'id':6,
        'pic':'https://www.backpacksters.com/wp-content/uploads/2021/02/India-Karnataka-Gadag-Basavanna-statue-6.jpg',
        'title':'Its all about the Gadag',
        'disc':' Gadag is a historic city in northern Karnataka known for its rich cultural heritage and ancient temples. It has made significant contributions to Kannada literature, music, and architecture over the centuries.One of the citys most famous landmarks is Trikuteshwara Temple, which showcases the beautiful Chalukyan style of architecture. Gadag is also known for its traditional handloom industry and peaceful atmosphere.'
    },
      {
        'id':7,
        'pic':'https://trekentrip.com/wp-content/uploads/2025/06/mysuru-palace-1024x640.jpg',
        'title':'Its all about the Mysore',
        'disc':' Mysore, officially known as Mysuru, is one of Karnatakas most beautiful and culturally rich cities. It is famous for its royal heritage, magnificent palaces, and well-planned roads. The city is also known for its educational institutions, sandalwood products, silk sarees, and traditional arts.Mysore attracts tourists from across the world with landmarks such as Mysore Palace, Chamundi Hill, and Brindavan Gardens. The grand Mysore Dasara celebration is one of Indias most famous festivals, showcasing the citys rich traditions and cultural heritage.'
    },
      {
        'id':8,
        'pic':'https://saishishirtours.in/wp-content/uploads/2024/12/The-Dubai-Museum-of-the-Future.webp',
        'title':'Its all about the Dubai',
        'disc':' Dubai is one of the worlds most modern and luxurious cities. It is known for its impressive skyscrapers, world-class shopping, and thriving business environment. The city has become a global hub for tourism, trade, and innovation.Dubai is home to famous landmarks such as Burj Khalifa, Palm Jumeirah, and Dubai Mall. Visitors also enjoy desert safaris, luxury resorts, and cultural experiences that showcase both tradition and modernity.'
    },
      {
        'id':9,
        'pic':'https://media-cdn.tripadvisor.com/media/photo-c/1280x250/11/30/d8/fa/bijapur.jpg',
        'title':'Its all about the Bijapur',
        'disc':' Vijayapura, formerly known as Bijapur, is a historic city in northern Karnataka renowned for its magnificent Islamic architecture and rich cultural heritage. It was once the capital of the Adil Shahi dynasty and remains an important center of history, education, and tourism.The city is best known for Gol Gumbaz, one of the largest domed structures in the world, along with attractions like Ibrahim Rauza and Jama Masjid. These monuments reflect the architectural brilliance of the medieval period and attract visitors from all over the world.'
    }
]
article1=[
    {
        'id':1,
        'pic':'https://th-i.thgim.com/public/incoming/ipx83f/article71125809.ece/alternates/LANDSCAPE_1200/20260503218L.jpg',
        'title':'NEET-UG re-exam: Nationwide mock drill under way; security tightened',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':2,
        'pic':'https://www.aljazeera.com/wp-content/uploads/2026/06/getty_6a36ab4391-1781967683.jpg?resize=770%2C513&quality=80',
        'title':'Trump insists Italy Meloni sought photos with him to boost popularity',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':3,
        'pic':'https://th-i.thgim.com/public/news/national/vq3mtv/article71125884.ece/alternates/LANDSCAPE_1200/Screenshot%202026-06-20%20175927.png',
        'title':'Bengal free of shackles and on path to creating history, says PM Modi',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':4,
        'pic':'https://images.indianexpress.com/2026/06/odisha-police.png?w=1600',
        'title':'Delhi woman intern with NGO stripped, molested in Odisha; 20 arrested',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':5,
        'pic':'https://newsonair.gov.in/wp-content/uploads/2026/06/zayn-6.jpg',
        'title':'Akshara Gupta scores triple century in Bihar Cricket Association tournament',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':6,
        'pic':'https://newsonair.gov.in/wp-content/uploads/2026/01/20260120127F-1980x1357.jpg',
        'title':'BJP National President Nitin Nabin begins three-day visit to Punjab',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':7,
        'pic':'https://th.bing.com/th?id=OMSN.AA26000k.webp-.5U&pid=wdpv2&w=1000&h=1000&qlt=90&c=1&rs=1',
        'title':'Smriti Mandhana only Indian in TIMEs 100 sports influencers',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':8,
        'pic':'https://cassette.sphdigital.com.sg/image/straitstimes/aa8c4518c58bf7d787d2fad12573c943db3a83ac3c892ec5bbc872532f5fd2bb',
        'title':'Have an Indian ancestor? A new proposal could soon let you play sport for India',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':9,
        'pic':'https://static.india.com/wp-content/uploads/2026/06/IPL_Dates.jpg?impolicy=Medium_Widthonly&w=700',
        'title':'Good news for fans of Indian Premier League,IPL 2027 is set to start EARLY',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    }
]
article2=[
    {
        'id':1,
        'pic':'https://www.kidsoutdoorzone.com/wp-content/uploads/kozcamp20211-500x500.webp',
        'title':'Fathers and Sons: Why Every Boy Needs a Godly Example',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':2,
        'pic':'https://www.kidsoutdoorzone.com/wp-content/uploads/IMG_20240623_181614-751x1024.webp',
        'title':'Don’t Stop When You’re Tired: Why Older Men Are Essential',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':3,
        'pic':'https://www.kidsoutdoorzone.com/wp-content/uploads/Fishing-and-Rick-300x400.webp',
        'title':'Mentoring Fatherless Boys: Why Knowing a Boy’s Father',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':4,
        'pic':'https://www.kidsoutdoorzone.com/wp-content/uploads/0B95853B-32DB-42F8-98C7-5ABEDBB01908-1-768x576.jpg',
        'title':'Helping Boys Process Anger: What’s Really Behind the',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':5,
        'pic':'https://www.kidsoutdoorzone.com/wp-content/uploads/Image-4-768x576.jpeg',
        'title':'Boys Are Watching: The Power of Leading by Example',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':6,
        'pic':'https://www.kidsoutdoorzone.com/wp-content/uploads/DSC08669-683x1024.jpg',
        'title':'How Sit Spot Cards Help Boys Open Their Hearts',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':7,
        'pic':'https://www.kidsoutdoorzone.com/wp-content/uploads/Image-5-14-26-at-10.52-AM-768x614.jpeg',
        'title':'The Little Moments That Change a Boy’s Life',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':8,
        'pic':'https://www.kidsoutdoorzone.com/wp-content/uploads/Crosspoint-Fishing-2-300x400.webp',
        'title':'Raising Boys with Purpose: Helping Them Live Out Their',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':9,
        'pic':'https://www.kidsoutdoorzone.com/wp-content/uploads/1965305552895731737-Larry-Cannon-768x432.webp',
        'title':'Get Boys Moving: Why It Matters More Than Ever',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    }
]
article3=[
    {
        'id':1,
        'pic':'https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcQbSNA225Q5vcjx02y-q4nFSevmVhpq1zHPvOTtGKC-aEfMiMFvCiQjBpyb8vxQEaIGK6clG77GYI7zP9y8WZvduyvbC0__6AgAOX5dHAt7smTPpktRg1GCavtp6GO2R5VsgJRp9SZnrl9s&s=19',
        'title':'Neeraj Chopra named AFIs Best Male Athlete of 2025',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':2,
        'pic':'https://www.awazthevoice.in/upload/news/1781950462Defending_champions_India_ready_for_Asia%E2%80%99s_biggest_bridge_championship_in_Goa.webp',
        'title':'Defending champions India ready for Asia’s biggest bridge championship in Goa',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':3,
        'pic':'https://www.awazthevoice.in/upload/news/1781948500Neeraj_Chopra.webp',
        'title':'Neeraj Chopra finishes fourth in Doha Diamond League opener',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':4,
        'pic':'https://www.awazthevoice.in/upload/news/1781939730ANI-20260620064623.webp',
        'title':'Koeman takes blame after Netherlands draw in World Cup clash',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':5,
        'pic':'https://www.awazthevoice.in/upload/news/1781867756ANI-20250928061640.webp',
        'title':'Palestinian Ambassador seeks Indias help for Gazas',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':6,
        'pic':'https://www.kidsoutdoorzone.com/wp-content/uploads/DSC08669-683x1024.jpg',
        'title':'How Sit Spot Cards Help Boys Open Their Hearts',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':7,
        'pic':'https://www.awazthevoice.in/upload/news/1781928311Yoga_10.webp',
        'title':'Floating Yoga by sportspersons in Srinagar sets mood for IYD 2026',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':8,
        'pic':'https://www.awazthevoice.in/upload/news/1781926318Sports(10)_(2).webp',
        'title':'Trailblazing Naheed Muqueetulla reinvents Indian denim through Urbano',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':9,
        'pic':'https://www.awazthevoice.in/upload/news/1781841500Tasir_Ali_with_his_sons_(1).webp',
        'title':'Tasir Ali is a proud father of five sons in uniform',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    }
]
article4=[
    {
        'id':1,
        'pic':'https://th-i.thgim.com/public/incoming/pufeim/article71126870.ece/alternates/LANDSCAPE_1200/2026-06-19T081318Z_1290285097_RC2TWLAENOH9_RTRMADP_3_IRAN-CRISIS-OMAN-HORMUZ.JPG',
        'title':'Three Indian-flagged oil tankers transit through Strait of Hormuz',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':2,
        'pic':'https://th-i.thgim.com/public/incoming/7372ks/article71079390.ece/alternates/LANDSCAPE_1200/2026-06-09T051153Z_1934998091_RC23QLAYEU01_RTRMADP_3_IRAN-CRISIS-HORMUZ-USA.JPG',
        'title':'Trump looms large over Brazils presidential election',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':3,
        'pic':'https://th-i.thgim.com/public/incoming/tvyad7/article71127003.ece/alternates/LANDSCAPE_1200/2026-06-20T132134Z_1075935216_RC2NNJAWEETF_RTRMADP_3_BANGLADESH-DIPLOMACY.JPG',
        'title':'Bangladesh PM to visit Malaysia, China on first foreign tour',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':4,
        'pic':'https://th-i.thgim.com/public/incoming/vlm0wu/article71126974.ece/alternates/LANDSCAPE_1200/Switzerland_WCup-Human_Rights__655_.jpg',
        'title':'UN rights chief troubled by new EU migrant return rules',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':5,
        'pic':'https://th-i.thgim.com/public/incoming/hcvha8/article71126397.ece/alternates/LANDSCAPE_1200/Spain-Politics_91806.jpg',
        'title':'Spanish PMs wife must stand trial on corruption charges, judge rules',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':6,
        'pic':'https://th-i.thgim.com/public/incoming/ksuuni/article71125851.ece/alternates/LANDSCAPE_1200/Switzerland_US_Iran_81353.jpg',
        'title':'Diplomats hold U.S.-Iran preparatory discussions at Swiss retreat',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':7,
        'pic':'https://th-i.thgim.com/public/incoming/klybt1/article71125313.ece/alternates/LANDSCAPE_1200/2026-06-19T195604Z_104162896_RC27XLAPVOF9_RTRMADP_3_USA-TRUMP.JPG',
        'title':'Trump unveils new Air Force One, a gift from Qatar',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':8,
        'pic':'https://th-i.thgim.com/public/incoming/2fovaz/article71123488.ece/alternates/LANDSCAPE_1200/2026-06-19T144517Z_142180161_RC21XLAT1296_RTRMADP_3_IRAN-CRISIS-ISRAEL-LEBANON.JPG',
        'title':'Talks between U.S., Iran called off because of fighting in Lebanon, officials say',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':9,
        'pic':'https://th-i.thgim.com/public/incoming/1btk12/article71122098.ece/alternates/LANDSCAPE_1200/AP06_18_2026_000240B.jpg',
        'title':'Pakistan delegation to attend funeral of Ali Khamenei: Shehbaz Sharif',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    }
]
article5=[
    {
        'id':1,
        'pic':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2DxU8eRsn3TadHoQTnkT_f4q2QTY3nnOOnHkR0UAkIg&s=10',
        'title':'Its all about the Bengluru',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },   {
        'id':2,
        'pic':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQLqjK8UJRe9KJThBpV2ec_HqowpKP0__Nwo_hY0kdcHA&s=10',
        'title':'Neeraj Chopra named AFIs Best Male Athlete of 2025',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':3,
        'pic':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlbkWaJGug2UgZrZwgJlF9k5noGlZCDfgT9p_cNwds2g&s=10',
        'title':'Neeraj Chopra finishes fourth in Doha Diamond League opener',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
        {
        'id':4,
        'pic':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSL5YACRj2pJEz3LK-YkgJsOph0pLRgZM_M5fK2ILZ3iw&s=10',
        'title':'Its all about the Delhi',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
       {
        'id':5,
        'pic':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsRK_Uqvjpqh8urMzeGPbE2ZKO1vL6PL7MFf7XsVwgNw&s=10',
        'title':'Get Boys Moving: Why It Matters More Than Ever',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
       {
        'id':6,
        'pic':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdKFxxoZ5aDLq0BZmfzgs-AChi9yzBLYcefpTM-JnKxg&s=10',
        'title':'How Sit Spot Cards Help Boys Open Their Hearts',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
    {
        'id':7,
        'pic':'https://www.kidsoutdoorzone.com/wp-content/uploads/kozcamp20211-500x500.webp',
        'title':'Fathers and Sons: Why Every Boy Needs a Godly Example',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
     {
        'id':8,
        'pic':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvqFcokjnuDgbUVfcRjCOSVPRuwqytq8NSNGsHwsf_3w&s=10',
        'title':'Trailblazing Naheed Muqueetulla reinvents Indian denim through Urbano',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    },
      {
        'id':9,
        'pic':'https://media-cdn.tripadvisor.com/media/photo-c/1280x250/11/30/d8/fa/bijapur.jpg',
        'title':'Its all about the Bijapur',
        'disc':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti minima hic similique iusto voluptas veniam officia, tempore  perspiciatis velit blanditiis!'
    }
]
def home(request):
    context={
        'data':article
    }
    return render(request,'home.html',context)

def news(request):
    context={
        'data':article1
    }
    return render(request,'news.html',context)

def blogs(request):
    context={
        'data':article2
    }
    return render(request,'blogs.html',context)

def sports(request):
    context={
        'data':article3
    }
    return render(request,'sports.html',context)

def international(request):
    context={
        'data':article4
    }
    return render(request,'international.html',context)

def about(request):
    context={
        'data':article5
    }
     
    return render(request,'about.html',context)


def read(request,pk):
  print(pk)
  for i in article:
      if i['id'] == pk:
          context = {
              'data': i
          }
           
  return render(request,'read.html',context)

def read1(request,pk):
  print(pk)
  for i in article1:
      if i['id'] == pk:
          context = {
              'data': i
          }
           
  return render(request,'read.html',context)
        
def read2(request,pk):
  print(pk)
  for i in article2:
      if i['id'] == pk:
          context = {
              'data': i
          }
           
  return render(request,'read.html',context)

def read3(request,pk):
  print(pk)
  for i in article3:
      if i['id'] == pk:
          context = {
              'data': i
          }
           
  return render(request,'read.html',context)

def read4(request,pk):
    for i in article4:
        if i['id']==pk:
            context={
                'data':i
            }
    return render(request,'read.html',context)


def read5(request,pk):
    for i in article5:
        if i['id']==pk:
            context={
                'data':i
            }
    return render(request,'read.html',context)