## luogu-latex-and-markdown-ui

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

#### 目录

- 注
- 零、 重要命令
- 一、形状的绘制
  1. 原理
  2. 简单图形
  3. 圆角矩形
  4. 阴影
  5. 简单图片
- 二、按钮
  1. 原理
  2. 简单按钮
  3. 带边框的圆角按钮
  4. 伪立体按钮

- 附 A - 其他注意事项
- 附 B - 其他样例

以下为正文

---
  
#### 注

$
\def\notew{210pt}
\def\noteh{44pt}
\def\notetitlepos{24pt}
\def\notetitleh{20pt}
\def\noteSetT#1{
  \def\notetitle{\textsf{\textbf{#1}}}
}
\def\notetitleoffest{37pt}
\def\noteWarn{
  \def\notech{\kern{-1pt}⚠\kern{2.8pt}}
  \noteSetT{警告}
  \def\notelcol{#FF9100}\def\notetcol{#FFF4E5}
}
\def\noteinfo{}
\def\drawnote{
\color{\notelcol}
\rule{2pt}{\noteh}
\color{\notetcol}
\rule[\notetitlepos]{\notew}{\notetitleh}
\color{#e8e8e8}\rule{0.5pt}{\noteh}
\color{#f5f5f5}\rule{0.5pt}{\noteh}
\color{#fafafa}\rule{0.5pt}{\noteh}
\kern{-\notew}\kern{-1.5pt}
\def\drawx#1#2{\color{#1}\rule[#2]{\notew}{0pt}\kern{-\notew}}
\drawx{#bfbfbf}{0pt}
\drawx{#d6d6d6}{-0.5pt}
\drawx{#ececec}{-1.0pt}
\drawx{#f8f8f8}{-1.5pt}
\color{black}
\raisebox{\notetitlepos}{
  \raisebox{6pt}{
    \kern{-1pt}
    \color{\notelcol}\large{\notech}
    \raisebox{1.5pt}{
      \color{#404040}\footnotesize
      \kern{-4pt}\notetitle
    }
  }
}
\kern{-\notetitleoffest}
\raisebox{10pt}{
  \footnotesize
  \sf{阅读前请确保您已了解 \LaTeX 和 Markdown 的基本操作。}
}
}
\noteWarn\drawnote
$

#### 零、 重要命令
  
  - `\rule[offest]{w}{h}` 绘制一个矩形

    $\rule{10pt}{6pt}$ `\rule{10pt}{6pt}`
    $\rule[5pt]{10pt}{6pt}$ `\rule[5pt]{10pt}{6pt}`
  
    $\rule[-20pt]{10pt}{6pt}$ `\rule[-20pt]{10pt}{6pt}`
    $\rule[20pt]{10pt}{6pt}$ `\rule[20pt]{10pt}{6pt}`
  
    注意：如果指定的 `offest` 超出了当前块的范围，则会使当前块的高度改变以容纳绘制的矩形，而不是穿插到其他块。
    注意2：绘制的矩形会挡住同一层的文字，使用 `\raisebox` 或在另一个块输出可以解决。
  
  - `\raisebox{offest}{source}` 上下移动文本
  
    text $\raisebox{20pt}{text}$ `\raisebox{20pt}{text}`
  
    同 `\rule` 一样不会穿插到其他块。
  
    注意：在行内公式中，内容不能含有数学公式。在行间公式中，如果内容包裹在 `$...$` 中，则可以含有数学公式。
    $$\sin\raisebox{5pt}{$\tan$}\cos$$
  
  - `\kern{offest}` 设置间距（或者说是移动当前位置）
    
    $\tt a \kern{50pt} b$ `\tt a \kern{50pt} b`
    
    $\tt a \kern{-15pt} b\kern{15pt}$ `\tt a \kern{-15pt} b\kern{15pt}`
  
  使用 `\raisebox` 和 `\kern` 可以实现大量有趣的排版。
  
#### 一、形状的绘制
  1. 原理\
    矩形+特殊字符 的排版
  2. 简单图形\
  如 $\huge\bigcirc$ `\huge\bigcirc`\
  可直接使用对应命令/字符。
  
  3. 圆角矩形\
    缺点：无法自定义圆角大小\
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
  4. 阴影\
    原理：绘制渐变色\
    $\def\w{100pt}
    \def\drawx#1#2{\color{#1}\rule[#2]{\w}{0pt}\kern{-\w}}
    \drawx{#bfbfbf}{0pt}
    \drawx{#d6d6d6}{-0.5pt}
    \drawx{#ececec}{-1.0pt}
    \drawx{#f8f8f8}{-1.5pt}
    $
  ```
  $\def\w{100pt}
  \def\drawx#1#2{\color{#1}\rule[#2]{\w}{0pt}\kern{-\w}}
  \drawx{#bfbfbf}{0pt}
  \drawx{#d6d6d6}{-0.5pt}
  \drawx{#ececec}{-1.0pt}
  \drawx{#f8f8f8}{-1.5pt}
  $
  ```
  5. 简单图片\
  原理：逐一绘制像素\
  可优化：对位于同一列/行的像素一起绘制\
  缺点：洛谷貌似对公式中元素的数量有限制，绘制大小有限
  
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
\k\rx{24}\b{#fff}\b{#fff}\b{#fff}\b{#fff}\b{#444}\b{#444}\b{#444}\b{#444}\b{#444}\b{#fff}\b{#fff}\b{#fff}\b{#fff}
$ 

代码较长，详见[此](https://www.luogu.com.cn/paste/ge525sta)
  
#### 二、按钮

  1. 原理\
    Markdown 的链接名支持使用 $\LaTeX$
    
  2. 简单示例
  
   [$
   \rule{40pt}{14pt}\kern{-31.5pt}\color{white}
   \raisebox{4.5pt}{\footnotesize\sf Button}
   $]()
   
   ```
   [$
   \rule{40pt}{14pt}\kern{-31.5pt}\color{white}
   \raisebox{4.5pt}{\footnotesize\sf Button}
   $]()
   ```
   
  3. 带边框的圆角按钮
  
  [$
  \def\w{40pt}\def\h{10pt}
  \def\arcoffest{3.7pt}
  \color{#bebebe}
  \rule[-3pt]{0.5pt}{\h}\kern{-1.2pt}
  \raisebox{\arcoffest}{◜}\kern{-5pt}
  \rule[\h]{\w}{0pt}
  \kern{-4.5pt}\raisebox{\arcoffest}{◝}\kern{-1pt}
  \rule[-3pt]{0.5pt}{\h}\kern{-\w}
  \kern{-6.9pt}\raisebox{-6pt}{◟}\kern{-5pt}
  \rule[-6pt]{\w}{0pt}\kern{-4.3pt}
  \raisebox{-6pt}{◞}
  \kern{-\w}\color{#404040}\kern{5pt}
  \raisebox{-0.3pt}{\sf{\footnotesize Button}}
  $]()
  
  ```
  [$
  \def\w{40pt}\def\h{10pt}
  \def\arcoffest{3.7pt}
  \color{#bebebe}
  \rule[-3pt]{0.5pt}{\h}\kern{-1.2pt}
  \raisebox{\arcoffest}{◜}\kern{-5pt}
  \rule[\h]{\w}{0pt}
  \kern{-4.5pt}\raisebox{\arcoffest}{◝}\kern{-1pt}
  \rule[-3pt]{0.5pt}{\h}\kern{-\w}
  \kern{-6.9pt}\raisebox{-6pt}{◟}\kern{-5pt}
  \rule[-6pt]{\w}{0pt}\kern{-4.3pt}
  \raisebox{-6pt}{◞}
  \kern{-\w}\color{#404040}\kern{5pt}
  \raisebox{-0.3pt}{\sf{\footnotesize Button}}
  $]()
  ```
  
  4. 伪立体按钮\
    原理：~~选好颜色~~
    
  [$\kern{10pt}
  \color{#F6F8FA}\rule{79pt}{22pt}
  \kern{-66pt}
  \raisebox{9pt}{
  \color{#24292F}\sf{\footnotesize 这是一个按钮}
  }\kern{-65pt}
  \color{#D5D8DA}\rule{77pt}{0pt}\kern{1pt}
  \rule[1pt]{0.1pt}{20pt}
  $]()
  
  ```
  [$\kern{10pt}
  \color{#F6F8FA}\rule{79pt}{22pt}
  \kern{-66pt}
  \raisebox{9pt}{
  \color{#24292F}\sf{\footnotesize 这是一个按钮}
  }\kern{-65pt}
  \color{#D5D8DA}\rule{77pt}{0pt}\kern{1pt}
  \rule[1pt]{0.1pt}{20pt}
  $]()
  ```
  
#### 附 A - 其他注意事项
  讨论区与剪贴板和博客不同，讨论区的无法渲染使用了 `\def`、`\newcommand`、`\renewcommand` 等宏命令的源码，因此如果需要发布到讨论区，需将所有宏替换回对应字符。

#### 附 B - 其他样例
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
