## luogu-latex-and-markdown-ui
此文长期更新

[Also on Github](https://github.com/HanPiM/InterestingKaTex_ForLuogu/blob/main/luogu-latex-and-markdown-ui.md)
（一般会慢于洛谷云剪贴板更新，毕竟主要是我自己用来存放历史~~屎山~~代码的）

$
% 画框和阴影
\color{#00B8D4}
\rule{2pt}{170pt}
\color{#E5F8FB}
\rule[150pt]{240pt}{20pt}
\color{#e8e8e8}\rule{0.5pt}{170pt}
\color{#f5f5f5}\rule{0.5pt}{170pt}
\color{#fafafa}\rule{0.5pt}{170pt}
\kern{-240pt}\kern{-1.5pt}
\color{#bfbfbf}\rule[0pt]{240pt}{0pt}\kern{-240pt}
\color{#d6d6d6}\rule[-0.5pt]{240pt}{0pt}\kern{-240pt}
\color{#ececec}\rule[-1pt]{240pt}{0pt}\kern{-240pt}
\color{#f8f8f8}\rule[-1.5pt]{240pt}{0pt}\kern{-240pt}
\color{black}
% 画标题
\raisebox{150pt}{
  \raisebox{6pt}{
    \kern{-1pt}
    \color{#00B8D4}\large{\kern{2pt}\bf{i}\kern{5.5pt}}
    \raisebox{1.5pt}{
      \color{#404040}\footnotesize
      \kern{-4pt}\sf\bf{无版权声明}
    }
  }
}
\kern{-300pt}
$.$\footnotesize
{}^{\kern{4pt}
\begin{array}{l}
\textsf{这是发布到公共领域的免费且不受阻碍的源码。}\\
\\
\textsf{任何人都可以出于任何目的、商业或非商业目的，以任何方式自}\\
\textsf{由复制、修改、发布、使用、编译、销售或分发本源码，无论是}\\
\textsf{源代码形式还是编译后的二进制文件。}\\
\\
\textsf{在承认版权法的司法管辖区，本源码的作者将本软件的任何所有}\\
\textsf{的版权权益都归于公共领域。我们做出这种奉献是为了广大公众}\\
\textsf{的利益，而不是损害我们的继承人和继任者。我们打算将这种奉}\\
\textsf{献作为一种公开的行为，永久放弃根据版权法对该软件的所有当}\\
\textsf{前和未来权利。}\\
\\
\textsf{该源码“按原样”提供，不提供任何形式的明示或暗示的保证，包}\\
\textsf{括但不限于适销性、特定用途的适用性和不侵权的保证。在任何}\\
\textsf{情况下，作者均不对任何索赔、损害或其他责任承担责任（无论}\\
\textsf{是在合同、侵权行为或其他方面，由源码或源码的使用或其他交}\\
\textsf{易引起的、因源码引起的或与之相关的）。}\\
\\
\textsf{更多信息请参考}\ \texttt{<http://unlicense.org>}
\end{array}
}
$

（用这个是因为找不到不需要标注 原作者/所有者 的文章许可证）

---

重要更新：

- 2021/12/26 拆分成不同模块，此后本文仅作为目录和附录。
- 2022/02/04 目录贴的链接出现问题，现已修好

细节更新（添加于 2022/02/??）：

- 2022/02/?? 为 附录 增加 用 LaTeX 输出高亮代码
- 2022/02/18 为 模块一/基础命令 增加 `cancel` 系列命令
- 2022/02/21 为 模块一/基础命令/`cancel`系列命令 增加 示例 绘制心形曲线
- 2022/02/27 为 模块一 调整一些语句
- 2022/02/27 为 附录 增加 KaTeX 单位（转pt）
- 2022/03/02 为 附录/附 A 更名 & 完善 讨论区无法使用的命令

---

计划事项（添加于 2022/02/21）：

- 将 LaTeX 的渲染换成图片以方便在其他平台显示 【摆烂中】
- 完善 [复杂图像绘制程序](https://github.com/HanPiM/katex_complex_img_generator) 【摆烂中】
- 更名（感觉文章越来越偏离原定标题了。。。）【考虑中】

---

指出错误 & 提出建议：私信本人

---

#### 目录

- [模块一：基础部分](https://www.luogu.com.cn/paste/a9rq3vfr)

  - 一、编辑环境
  - 二、基础命令
  - 三、绘制
    1. 基础绘制
    2. 绘制特殊效果
    3. 杂项

- [模块二：无交互控件](https://www.luogu.com.cn/paste/xdfqclyv)

- [模块三：交互控件](https://www.luogu.com.cn/paste/qj1t8xv5)

- 附 A - 讨论区无法使用的命令
- 附 B - 其他样例
- 附 C - 用 $\LaTeX$ 输出高亮代码
- 附 D - $\KaTeX$ 单位（转pt）

- 参考资料

---

$
% w, h, fillcol, bordercol
\newcommand\BorderRect[4]{
    \color{#3}\rule{#1}{#2}\kern{-#1}
    \color{#4}\rule{0.5px}{#2}\kern{-0.5px}
    \rule{#1}{0px}\rule{0.5px}{#2}\kern{-0.5px}
    \kern{-#1}\rule[#2]{#1}{0px}
}
% w, h, title, subtitle, fillcol, iconch ,iconcol
\newcommand\BasicInfoBarFather[7]{
    \BorderRect{#1}{#2}{#5}{ghostwhite}
    \kern{-#1}
    \raisebox{#2}{
    \raisebox{-26pt}{
        \color{black}\kern{-4px}
        \raisebox{7px}{
        \color{#7}\Huge{∙}\kern{-1px}
        }
        \raisebox{10.6px}{
        \kern{-20.2px}
        \color{white}\scriptsize\textbf{#6}
        }
        \kern{-7px}\footnotesize
        \raisebox{10.2px}{\textbf{\textsf{#3}}}\kern{2px}
        \raisebox{10.2px}{\textsf{#4}}
    }
    }
}
\def\BasicWarnBarColorFill{#FFF4CE}\def\BasicWarnBarColorIcon{#9D5D00}
\newcommand\BasicWarnBar[4]{
    \BasicInfoBarFather{#1}{#2}{#3}{#4}
    {\BasicWarnBarColorFill}{i}{\BasicWarnBarColorIcon}
}
\BasicWarnBar{250px}{26px}{注意}{本文为方便，在文中常用 “块” 指代一段 \LaTeX 公式。}
$

---
#### 附 A - 讨论区无法使用的命令

  讨论区的 LaTeX 版本与剪贴板和博客不同。请注意以下：
  
  - 宏定义类
    
    包括但不限于 `\def \newcommand...`
    
    均无法使用。
    
  - 换行类
    
    `\\ \cr \newline`
    
    无法直接使用，但可在 `array gathered` 等排版环境下使用
    
  - 其他
    
    `\char` : 无法使用
  
---
#### 附 B - 其他样例
  
  这里是一些不知道该怎么分类的样例

  1. [绘制 note](https://www.luogu.com.cn/paste/j29i6yfi)
  2. 未命名示例-1
  
  $\kern{10pt}$
$\def\w{200pt}\def\h{64pt}
\def\titleoffest{54pt}
\def\arcoffest{57.7pt}
\def\drawx#1{\color{#1}\rule[-3pt]{0.5pt}{\h}}
\drawx{#fafafa}\drawx{#f7f7f7}
\drawx{#efefef}
\color{#bebebe}
\rule[-3pt]{0.5pt}{\h}\kern{-1.2pt}
\raisebox{\arcoffest}{◜}\kern{-5pt}
\rule[\h]{\w}{0pt}
\raisebox{\titleoffest}{\kern{-10pt}\color{#202020}{\large×}}
\kern{-4.5pt}\raisebox{\arcoffest}{◝}\kern{-1pt}
\rule[-3pt]{0.5pt}{\h}\kern{-\w}
\kern{-6.9pt}\raisebox{-6pt}{◟}\kern{-5pt}
\rule[-6pt]{\w}{0pt}\kern{-4.3pt}
\raisebox{-6pt}{◞}\kern{-0.5pt}
\drawx{#e8e8e8}\drawx{#f5f5f5}
\drawx{#fafafa}
\kern{-\w}\kern{-5pt}
\def\drawx#1#2{\color{#1}\rule[#2]{\w}{0pt}\kern{-\w}}
\drawx{#bfbfbf}{-6pt}
\drawx{#d6d6d6}{-6.5pt}
\drawx{#ececec}{-7pt}
\drawx{#f8f8f8}{-7.5pt}
%
\raisebox{\titleoffest}
{\kern{9pt}\color{#404040}\tiny\textsf{一个伪窗口}}
\kern{-\w}
$
$\kern{2pt}$
$%删去了不必要的内容
\color{#00B8D4}
\rule{2pt}{44pt}
\color{#E5F8FB}
\rule[24pt]{190pt}{20pt}
\color{#e8e8e8}\rule{0.5pt}{44pt}
\color{#f5f5f5}\rule{0.5pt}{44pt}
\color{#fafafa}\rule{0.5pt}{44pt}
\kern{-190pt}\kern{-1.5pt}
\color{#bfbfbf}\rule[0pt]{190pt}{0pt}\kern{-190pt}
\color{#d6d6d6}\rule[-0.5pt]{190pt}{0pt}\kern{-190pt}
\color{#ececec}\rule[-1pt]{190pt}{0pt}\kern{-190pt}
\color{#f8f8f8}\rule[-1.5pt]{190pt}{0pt}\kern{-190pt}
\color{black}
\raisebox{24pt}{ \raisebox{6pt}{ \kern{-1pt}
\color{#00B8D4}\large{\kern{2pt}\bf{i}\kern{5.5pt}}
\raisebox{1.5pt}{ \color{#404040}\footnotesize
\kern{-4pt}\sf\bf{这是一个伪嵌套到伪窗口上方的信息}
}}}\kern{-200pt}$.
$\kern{4pt}\raisebox{10pt}{\footnotesize\sf{伪嵌套 2：}}$
$
\def\w{130pt}
\def\h{18pt}
\color{#E4E7E8}
\rule[3pt]{0.1pt}{\h}\kern{-0.5pt}
\rule[21pt]{\w}{0pt}
\rule[3pt]{0.1pt}{\h}\kern{-\w}
\color{#0067C0}
\rule[3pt]{\w}{0.5pt}\kern{-\w}
\color{#616161}
\raisebox{10.2pt}
{\scriptsize\sf\kern{5pt}这是一个伪文本框
}
$

```
$\def\w{200pt}\def\h{64pt}
\def\titleoffest{54pt}
\def\arcoffest{57.7pt}
\def\drawx#1{\color{#1}\rule[-3pt]{0.5pt}{\h}}
\drawx{#fafafa}\drawx{#f7f7f7}
\drawx{#efefef}
\color{#bebebe}
\rule[-3pt]{0.5pt}{\h}\kern{-1.2pt}
\raisebox{\arcoffest}{◜}\kern{-5pt}
\rule[\h]{\w}{0pt}
\raisebox{\titleoffest}{\kern{-10pt}\color{#202020}{\large×}}
\kern{-4.5pt}\raisebox{\arcoffest}{◝}\kern{-1pt}
\rule[-3pt]{0.5pt}{\h}\kern{-\w}
\kern{-6.9pt}\raisebox{-6pt}{◟}\kern{-5pt}
\rule[-6pt]{\w}{0pt}\kern{-4.3pt}
\raisebox{-6pt}{◞}\kern{-0.5pt}
\drawx{#e8e8e8}\drawx{#f5f5f5}
\drawx{#fafafa}
\kern{-\w}\kern{-5pt}
\def\drawx#1#2{\color{#1}\rule[#2]{\w}{0pt}\kern{-\w}}
\drawx{#bfbfbf}{-6pt}
\drawx{#d6d6d6}{-6.5pt}
\drawx{#ececec}{-7pt}
\drawx{#f8f8f8}{-7.5pt}
%
\raisebox{\titleoffest}
{\kern{9pt}\color{#404040}\tiny\textsf{一个伪窗口}}
\kern{-\w}
$
$\kern{2pt}$
$%删去了不必要的内容
\color{#00B8D4}
\rule{2pt}{44pt}
\color{#E5F8FB}
\rule[24pt]{190pt}{20pt}
\color{#e8e8e8}\rule{0.5pt}{44pt}
\color{#f5f5f5}\rule{0.5pt}{44pt}
\color{#fafafa}\rule{0.5pt}{44pt}
\kern{-190pt}\kern{-1.5pt}
\color{#bfbfbf}\rule[0pt]{190pt}{0pt}\kern{-190pt}
\color{#d6d6d6}\rule[-0.5pt]{190pt}{0pt}\kern{-190pt}
\color{#ececec}\rule[-1pt]{190pt}{0pt}\kern{-190pt}
\color{#f8f8f8}\rule[-1.5pt]{190pt}{0pt}\kern{-190pt}
\color{black}
\raisebox{24pt}{ \raisebox{6pt}{ \kern{-1pt}
\color{#00B8D4}\large{\kern{2pt}\bf{i}\kern{5.5pt}}
\raisebox{1.5pt}{ \color{#404040}\footnotesize
\kern{-4pt}\sf\bf{这是一个伪嵌套到伪窗口上方的信息}
}}}\kern{-200pt}$.
$\kern{4pt}\raisebox{10pt}{\footnotesize\sf{伪嵌套 2：}}$
$
\def\w{130pt}
\def\h{18pt}
\color{#E4E7E8}
\rule[3pt]{0.1pt}{\h}\kern{-0.5pt}
\rule[21pt]{\w}{0pt}
\rule[3pt]{0.1pt}{\h}\kern{-\w}
\color{#0067C0}
\rule[3pt]{\w}{0.5pt}\kern{-\w}
\color{#616161}
\raisebox{10.2pt}
{\scriptsize\sf\kern{5pt}这是一个伪文本框
}
$
```

---
#### 附 C - 用 $\LaTeX$ 输出高亮代码 [link](https://www.luogu.com.cn/paste/bbe9ifkw)

---
#### 附 D - $\KaTeX$ 单位（转pt）

| KaTeX Unit | Value            | KaTeX Unit | Value               |
| ---------- | ---------------- | ---------- | ------------------- |
| em         | CSS em           | bp         | $\dfrac{1}{72}\text{inch}\times F \times G=\dfrac{72.27}{72}\text{pt}$ |
| ex         | CSS ex           | pc         | $12\text{ pt}$ |
| mu         | $\dfrac{1}{18}$ CSS em | dd         | $\dfrac{1238}{1157}\text{pt}$ |
| pt         | $\dfrac{1}{72.27} \text{inch}\times F \times G\Rightarrow1\text{ inch}=\dfrac{72.27\text{ pt}}{F\times G}$ | cc         | $\dfrac{14856}{1157}\text{pt}$ |
| mm         | $1\text{mm}\times F \times G=\dfrac{1}{100}\text{cm}=\dfrac{7227}{25400}\text{pt}$ | nd         | $\dfrac{685}{642}\text{pt}$ |
| cm         | $1\text{ cm}\times F \times G=\dfrac{7227}{254}\text{ pt}\quad(1\text{ cm}=\dfrac{1}{2.54}\text{inch})$ | nc         | $\dfrac{1370}{107}\text{pt}$ |
| in         | $1\text{ inch}\times F \times G=72.27\text{ pt}$ | sp         | $\dfrac{1}{65536}\text{pt}$ |

--- 

参考资料：

- @[Iowa_BattleShip](/user/60181) LaTeX 数学公式大全 \[
[$\tiny\tt\color{grey}www.luogu.com.cn/blog/IowaBattleship/latex-gong-shi-tai-quan$](
https://www.luogu.com.cn/blog/IowaBattleship/latex-gong-shi-tai-quan)
\]

- KaTeX support table \[
[$\tiny\tt\color{grey}katex.org/docs/support\_table.html$](
https://katex.org/docs/support_table.html)
\]

- @[离散小波变换°](/user/68344) KaTeX 画图技巧 - KaTeX 进阶
\[
[$\tiny\tt\color{grey}www.luogu.com.cn/paste/wmm62fg7$](https://www.luogu.com.cn/paste/wmm62fg7)
\]

- @[囧仙](/user/330759) 进行一个 LaTeX 的滥用 \[
[$\tiny\tt\color{grey}www.luogu.com.cn/blog/over-knee-socks/latex-xetal$](https://www.luogu.com.cn/blog/over-knee-socks/latex-xetal)
\]

---

一些无聊的统计：

自 2022/2/23 起

- 该页面浏览次数（人次） ![](https://hitwebcounter.com/counter/counter.php?page=7950136&style=0007&nbdigits=9&type=page&initCount=0)（![](https://hitwebcounter.com/counter/counter.php?page=7950138&style=0007&nbdigits=9&type=ip&initCount=0)）
