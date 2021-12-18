from PIL import Image

# 用于生成简单的图片的 LaTeX 表达方式（长*宽必须小于 234，大于会导致渲染失败）
path=input("图片路径: ")

img=Image.open(path)
img.convert('RGB')
data=img.getdata()
w=img.size[0]
h=img.size[1]

def hex_col(pos):
    return '#'+format(data[pos][0],'x').zfill(2)+format(data[pos][1],'x').zfill(2)+format(data[pos][2],'x').zfill(2)
    
bitw=float(input('每像素大小（mm）: '))

print(
        "$\\newcommand{\\x}{0}\\newcommand{\\bitsize}{"+str(bitw)+
        "mm}\\newcommand{\\b}[1]{\\color{#1}\\rule[-\\x mm]{\\bitsize}{\\bitsize}}\\newcommand{\\bw}{\\bitsize}\\newcommand {\\w}{"+
        str(bitw*w)+
        "mm}\\newcommand{\\rx}[1]{\\renewcommand{\\x}{#1}}\\newcommand{\\k}{\kern{-\\w}}")
res=''
cnt=0
for i in range(w*h):
    res+='\\b{'+hex_col(i)+'}'
    cnt+=1
    if((i+1)%w==0):
        res+='\\k\\rx{'+str(round((i//w)*bitw,1))+'}'
res+='$'

print(res)
