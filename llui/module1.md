此文属于 [luogu-latex-and-markdown-ui](https://www.luogu.com.cn/paste/xdfqclyv) 。

---

### 模块一：基础部分

#### 一、编辑环境

  本人推荐使用 Atom/VSCode + [Markdown Preview Enhanced](https://shd101wyy.github.io/markdown-preview-enhanced/#/zh-cn/) 插件。

  当然，使用洛谷自带的剪贴板也不是不可以。

#### 二、 基础命令
  如果想要使用 $\LaTeX$ + Markdown 编写简易 UI，您应当对一下命令非常熟悉。
  - `\rule[offest]{w}{h}` 绘制一个矩形

    例：\
    $\rule{10pt}{6pt}$ `\rule{10pt}{6pt}`
    $\rule[5pt]{10pt}{6pt}$ `\rule[5pt]{10pt}{6pt}`

    $\rule[-20pt]{10pt}{6pt}$ `\rule[-20pt]{10pt}{6pt}`
    $\rule[20pt]{10pt}{6pt}$ `\rule[20pt]{10pt}{6pt}`
  
    注意：
    - 如果指定的 `offest` 超出了当前块的范围，则会使当前块的高度改变以容纳绘制的矩形，而不是穿插到其他块。
    - 绘制的矩形会挡住同一层的文字，使用 `\raisebox` 或在另一个块输出可以解决。
  
  - `\raisebox{offest}{source}` 将文本 source 上移 offest（可以为负） 后输出
  
    例：
    text $\raisebox{20pt}{text}$ `\raisebox{20pt}{text}`
  
    注意：
    - 同 `\rule` 一样不会穿插到其他块。
    - 在行内公式中，内容不能含有数学公式。在行间公式中，如果内容包裹在 `$...$` 中，则可以含有数学公式。
    $$\sin\raisebox{5pt}{$\tan$}\cos$$
  
  - `\kern{offest}` 输出间距（或者说是移动当前位置），其中 offest 可以为负
    
    例：\
    $\tt a \kern{50pt} b$ `\tt a \kern{50pt} b`
    
    $\tt a \kern{-15pt} b\kern{15pt}$ `\tt a \kern{-15pt} b\kern{15pt}`
    
  理论上，综合使用 `\raisebox` 与 `\kern` 即可在页面上任何位置输出。
  
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