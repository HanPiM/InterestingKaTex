此文属于 [luogu-latex-and-markdown-ui](https://www.luogu.com.cn/paste/om2r4sar) 。

---

### 模块一：基础部分

#### 一、编辑环境

  本人推荐使用 Atom/VSCode + [Markdown Preview Enhanced](https://shd101wyy.github.io/markdown-preview-enhanced/#/zh-cn/) 插件。

  当然，使用洛谷自带的剪贴板也不是不可以。

#### 二、 基础命令
  如果想要使用 $\LaTeX$ + Markdown 编写简易 UI，您应当对一下命令非常熟悉。
  
  - `\rule[offset]{w}{h}` 绘制一个矩形

    例：\
    $\rule{10pt}{6pt}$ `\rule{10pt}{6pt}`
    $\rule[5pt]{10pt}{6pt}$ `\rule[5pt]{10pt}{6pt}`

    $\rule[-20pt]{10pt}{6pt}$ `\rule[-20pt]{10pt}{6pt}`
    $\rule[20pt]{10pt}{6pt}$ `\rule[20pt]{10pt}{6pt}`
    
    $\color{green}\rule{50pt}{10pt}\kern{-10pt}\color{red}aaa$ `\color{green}\rule{50pt}{10pt}\kern{-10pt}\color{red}aaa` 文字被遮住了
    
    注意：
    - 如果指定的 `offset` 超出了当前块的范围，则会使当前块的高度改变以容纳绘制的矩形，而不是穿插到其他块。
    - 绘制的矩形会挡住同一层的文字，使用 `\raisebox` 或在另一个块输出可以解决。
    - 如果矩形较小，部分浏览器在绘制时会丢失一些像素。（原因未知）
  
  - `\raisebox{offset}{source}` 将文本 source 上移 offest（可以为负） 后输出
  
    例：
    text $\raisebox{20pt}{text}$ `\raisebox{20pt}{text}`
  
    注意：
    - 同 `\rule` 一样不会穿插到其他块。
    - 其输出区域会被设为文本环境，类似 `\text` ，一些公式用不了。在行内公式中救不了，但在行间公式中，如果内容包裹在 `$...$` 中，则可以含有公式（其实就是启用数学模式）。
    
    $$\sin\raisebox{5pt}{$\tan$}\cos$$
    
    `$$\sin\raisebox{5pt}{$\tan$}\cos$$`
  
  - `\kern{offset}` 输出大小为 offset（可以为负）的间距（水平移动当前位置）
    
    例：\
    $\tt a \kern{50pt} b$ `\tt a \kern{50pt} b`
    
    $\tt a \kern{-15pt} b\kern{15pt}$ `\tt a \kern{-15pt} b\kern{15pt}`

  - `\\[offset]` 带参数的换行（竖直方向上移动当前位置 offset 距离后回到开头）
    例：\
    $a \\[5px]bcd\\[-22px]efghija\\[8px]$ `$a \\[5px]bcd\\[-22px]efghij\\[8px]$`

    $averyveryverylonglonglongsentence....\\[-13px]\color{blue}\tt{cameback}$
    
    `$averyveryverylonglonglongsentence....\\[-13px]\color{blue}\tt{cameback}$`
    
    aaa $bb\\c$ `aaa $bb\\c$`
    
    注意：回到开头是指当前段落开头，而不是块的开头！
    
  - `\cancel{text}` / `\bcancel{text}` 给文字画斜线
    
    $\cancel{cancel}\quad\bcancel{bcancel}$ `$\cancel{cancel}\quad\bcancel{bcancel}$`
    
    简单的例子：
    
    $
    \def\xcline#1#2{
      \kern{2pt}
      \cancel{
        \raisebox{#2}
        {\kern{#1}\kern{-4pt}}
      }
      \kern{2pt}
    }
    \def\xbcline#1#2{
      \kern{2pt}
      \bcancel{
        \raisebox{#2}
        {\kern{#1}\kern{-4pt}}
      }
      \kern{2pt}
    }
    \xcline{10pt}{10pt}
    \xbcline{10pt}{10pt}
    \xcline{10pt}{20pt}
    \xbcline{10pt}{20pt}
    \xcline{10pt}{40pt}
    \xbcline{10pt}{40pt}
    $
       
    ```latex
    $
    \def\xcline#1#2{
      \kern{2pt}
      \cancel{
        \raisebox{#2}
        {\kern{#1}\kern{-4pt}}
      }
      \kern{2pt}
    }
    \def\xbcline#1#2{
      \kern{2pt}
      \bcancel{
        \raisebox{#2}
        {\kern{#1}\kern{-4pt}}
      }
      \kern{2pt}
    }
    \xcline{10pt}{10pt}
    \xbcline{10pt}{10pt}
    \xcline{10pt}{20pt}
    \xbcline{10pt}{20pt}
    \xcline{10pt}{40pt}
    \xbcline{10pt}{40pt}
    $
    ```
    
    人win节特供例：（该代码由程序生成，由于还未完善，因此暂不给出生成器）
    
    $$
    \color{#ccc}\rule[144pt]{288pt}{0pt}\kern{-144pt}\rule{1sp}{256pt}\kern{-144pt}\color{red}\kern{16pt}\raisebox{176pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{21.44pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{197.44pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{8.41pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{205.85pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{6.16pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{212pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{4.93pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{216.94pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{4.1pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{221.05pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{3.49pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{224.54pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{2.99pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{227.53pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{2.57pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{230.09pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{2.20pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{232.29pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{1.86pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{234.15pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{1.56pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{235.7pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{1.27pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{236.97pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{0.99pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{237.96pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{0.73pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{238.69pt}{$\rule{4pt}{0pt}$}\raisebox{239.16pt}{$\rule{4pt}{0pt}$}\raisebox{239.33pt}{$\rule{4pt}{0pt}$}\raisebox{239.02pt}{$\rule{4pt}{0pt}$}\raisebox{238.45pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{0.57pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{237.6pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{0.85pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{236.46pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{1.14pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{235.02pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{1.44pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{233.26pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{1.77pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{231.14pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{2.12pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{228.62pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{2.52pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{225.66pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{2.96pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{222.18pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{3.48pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{218.07pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{4.1pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{213.15pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{4.91pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{207.12pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{6.04pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{199.2pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{7.91pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{184pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{15.2pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{184pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{15.2pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{199.2pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{7.91pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{207.12pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{6.04pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{213.15pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{4.91pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{218.07pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{4.1pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{222.18pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{3.48pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{225.66pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{2.96pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{228.62pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{2.52pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{231.14pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{2.12pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{233.26pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{1.77pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{235.02pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{1.44pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{236.46pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{1.14pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{237.6pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{0.85pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{238.45pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{0.57pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{239.02pt}{$\rule{4pt}{0pt}$}\raisebox{239.33pt}{$\rule{4pt}{0pt}$}\raisebox{239.16pt}{$\rule{4pt}{0pt}$}\raisebox{238.69pt}{$\rule{4pt}{0pt}$}\raisebox{237.96pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{0.73pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{236.97pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{0.99pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{235.7pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{1.27pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{234.15pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{1.56pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{232.29pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{1.86pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{230.09pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{2.20pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{227.53pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{2.57pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{224.54pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{2.99pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{221.05pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{3.49pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{216.94pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{4.1pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{212pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{4.93pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{205.85pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{6.16pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{197.44pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{8.41pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{176pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{21.44pt}\kern{-4pt}}}\kern{2pt}$}\kern{-272pt}\color{green}\kern{16pt}\raisebox{153.83pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{22.17pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{144.57pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{9.26pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{137.44pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{7.13pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{131.4pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{6.04pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{126.05pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{5.35pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{121.19pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{4.87pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{116.67pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{4.52pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{112.43pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{4.24pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{108.39pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{4.03pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{104.52pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{3.87pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{100.79pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{3.73pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{97.16pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{3.63pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{93.61pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{3.55pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{90.12pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{3.49pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{86.68pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{3.44pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{83.26pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{3.42pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{79.85pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{3.4pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{76.44pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{3.41pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{73.01pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{3.43pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{69.55pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{3.46pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{66.04pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{3.51pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{62.46pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{3.58pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{58.78pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{3.67pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{55.00pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{3.79pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{51.07pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{3.93pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{46.95pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{4.12pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{42.6pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{4.35pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{37.93pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{4.67pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{32.83pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{5.1pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{27.07pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{5.76pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{20.1pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{6.96pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{8pt}{$\kern{2pt}\bcancel{\phantom{\rule{4pt}{12.1pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{8pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{12.1pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{20.1pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{6.96pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{27.07pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{5.76pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{32.83pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{5.1pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{37.93pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{4.67pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{42.6pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{4.35pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{46.95pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{4.12pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{51.07pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{3.93pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{55.00pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{3.79pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{58.78pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{3.67pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{62.46pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{3.58pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{66.04pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{3.51pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{69.55pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{3.46pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{73.01pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{3.43pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{76.44pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{3.41pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{79.85pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{3.4pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{83.26pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{3.42pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{86.68pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{3.44pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{90.12pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{3.49pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{93.61pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{3.55pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{97.16pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{3.63pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{100.79pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{3.73pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{104.52pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{3.87pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{108.39pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{4.03pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{112.43pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{4.24pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{116.67pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{4.52pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{121.19pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{4.87pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{126.05pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{5.35pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{131.4pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{6.04pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{137.44pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{7.13pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{144.57pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{9.26pt}\kern{-4pt}}}\kern{2pt}$}\raisebox{153.83pt}{$\kern{2pt}\cancel{\phantom{\rule{4pt}{22.17pt}\kern{-4pt}}}\kern{2pt}$}\kern{16pt}\\
    \color{black}
    \begin{cases}
    x=16\sin^3(t)\\
    y=13\cos(t)-5\cos(2t)-2cos(3t)-cos(4t)
    \end{cases}\\
    \Rightarrow
    \begin{cases}
    t(x)&=\arcsin((\dfrac{x}{16})^{\frac{1}{3}})\\
    \textcolor{red}{\rule[3pt]{10pt}{1pt}\ }
    f(x)&=13\cos(t(x))-5\cos(2t(x))-2\cos(3t(x))-\cos(4t(x))\\
    \textcolor{green}{\rule[2pt]{10pt}{1pt}\ }
    g(x)&=-13\cos(t(x))-5\cos(2t(x))+2\cos(3t(x))-\cos(4t(x))
    \end{cases}
    $$
    
    注意：
    
    - 内容高度/宽度太小会不显示（大概是 宽>4pt 高>0.5pt）

#### 三、绘制

1. 基础绘制

    对于常见的基本图形（如 $\huge\bigcirc$ `\huge\bigcirc` ）
    可直接使用对应命令/字符。

    但对于稍微复杂的图形，我们很难找到某个可以满足要求的字符/命令。此时我们则需要将多个基本图形结合到一起以达到目标效果。

    示例：

    - 圆角矩形边框

      可以拆分成 4 条线段和 4 段 $\dfrac{1}{4}$ 圆弧。

      对于线段，直接使用 `\rule` 绘制。\
      对于圆弧，由于 $\LaTeX$ 中没有 $\dfrac{1}{4}$ 圆弧的命令，所以使用特殊字符： `◜◝◟◞` 

      缺点：无法自定义圆角大小，无法在讨论区渲染。

      $
      \def\w{100pt}\def\h{61pt}
      \def\arcoffest{54.7pt}
      \color{#bebebe}
      \rule[-3pt]{0.5pt}{\h}\kern{-1.2pt}
      \raisebox{\arcoffest}{◜}\kern{-5pt}
      \rule[\h]{\w}{0pt}
      \kern{-4.5pt}\raisebox{\arcoffest}{◝}\kern{-1pt}
      \rule[-3pt]{0.5pt}{\h}\kern{-\w}
      \kern{-6.9pt}\raisebox{-6pt}{◟}\kern{-5pt}
      \rule[-6pt]{\w}{0pt}\kern{-4.3pt}
      \raisebox{-6pt}{◞}\kern{-0.5pt}
      $

      ```
      $
      \def\w{100pt}\def\h{61pt}
      \def\arcoffest{54.7pt}
      \color{#bebebe}
      \rule[-3pt]{0.5pt}{\h}\kern{-1.2pt}
      \raisebox{\arcoffest}{◜}\kern{-5pt}
      \rule[\h]{\w}{0pt}
      \kern{-4.5pt}\raisebox{\arcoffest}{◝}\kern{-1pt}
      \rule[-3pt]{0.5pt}{\h}\kern{-\w}
      \kern{-6.9pt}\raisebox{-6pt}{◟}\kern{-5pt}
      \rule[-6pt]{\w}{0pt}\kern{-4.3pt}
      \raisebox{-6pt}{◞}\kern{-0.5pt}
      $
      ```
      
2. 绘制特殊效果
  
    - 阴影
      
      原理：绘制由灰到白的渐变色。（计算渐变色的方法有很多，但那超出了本文的范围）
        
      示例：
  
      $\def\w{100pt}
      \def\drawx#1#2{\color{#1}\rule[#2]{\w}{0pt}\kern{-\w}}
      \drawx{#bfbfbf}{0pt}
      \drawx{#d6d6d6}{-0.5pt}
      \drawx{#ececec}{-1.0pt}
      \drawx{#f8f8f8}{-1.5pt}$
    
      ```
      $\def\w{100pt}
      \def\drawx#1#2{\color{#1}\rule[#2]{\w}{0pt}\kern{-\w}}
      \drawx{#bfbfbf}{0pt}
      \drawx{#d6d6d6}{-0.5pt}
      \drawx{#ececec}{-1.0pt}
      \drawx{#f8f8f8}{-1.5pt}$
      ```
      
3. 杂项
  
    - 简单图片

      原理：逐一绘制像素\
      缺点：洛谷貌似对公式中元素的数量有限制，绘制大小有限\
      可优化：对位于同一列/行的同颜色像素一起绘制

      $\newcommand{\x}{0}\newcommand{\bitsize}{2mm}\newcommand{\b}[1]{\color{#1}\rule[\x mm]{\bitsize}{\bitsize}}\newcommand{\bw}{\bitsize}\newcommand {\w}{26mm}\newcommand{\rx}[1]{\renewcommand{\x}{#1}}
      \newcommand{\k}{\kern{-\w}}
      \b{#281e0b}\b{#281e0b}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}
      \k\rx{2}\b{#493615}\b{#896727}\b{#281e0b}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}
      \k\rx{4}\b{#fff}\b{#493615}\b{#684e1e}\b{#281e0b}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}
      \k\rx{6}\b{#fff}\b{#fff}\b{#493615}\b{#896727}\b{#281e0b}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#181818}\b{#fff}
      \k\rx{8}\b{#fff}\b{#fff}\b{#fff}\b{#493615}\b{#684e1e}\b{#281e0b}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#181818}\b{#fff}\b{#181818}
      \k\rx{10}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#493615}\b{#896727}\b{#281e0b}\b{#fff}\b{#fff}\b{#fff}\b{#181818}\b{#d8d8d8}\b{#181818}
      \k\rx{12}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#493615}\b{#684e1e}\b{#281e0b}\b{#fff}\b{#fff}\b{#181818}\b{#c1c1c1}\b{#181818}
      \k\rx{14}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#493615}\b{#896727}\b{#281e0b}\b{#fff}\b{#181818}\b{#c1c1c1}\b{#181818}
      \k\rx{16}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#493615}\b{#684e1e}\b{#281e0b}\b{#c1c1c1}\b{#d8d8d8}\b{#181818}
      \k\rx{18}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#493615}\b{#d8d8d8}\b{#c1c1c1}\b{#181818}\b{#fff}
      \k\rx{20}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#444}\b{#181818}\b{#181818}\b{#181818}\b{#c1c1c1}\b{#c1c1c1}\b{#896727}\b{#281e0b}\b{#fff}
      \k\rx{22}\b{#fff}\b{#fff}\b{#fff}\b{#444}\b{#fff}\b{#d8d8d8}\b{#c1c1c1}\b{#c1c1c1}\b{#d8d8d8}\b{#444}\b{#493615}\b{#684e1e}\b{#fff}
      \k\rx{24}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#444}\b{#444}\b{#444}\b{#444}\b{#444}\b{#fff}\b{#fff}\b{#fff}\b{#fff}$
      （这是游戏 [minecraft](https://www.minecraft.net) 中的工具：铁镐）

      代码较长，详见[此](https://www.luogu.com.cn/paste/ge525sta)。
      
