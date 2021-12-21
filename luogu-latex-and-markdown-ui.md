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

#### 目录

注

零、 重要命令

一、

#### 注

本文主要提供示例，并给与少量教程。

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
  0. 原理\
    矩形+特殊字符 的排版
  1. 简单图形\
  如 $\huge\bigcirc$ `\huge\bigcirc`\
  可直接使用对应命令/字符。
  
  2. 圆角矩形\
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
  3. 简单图片
  
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

代码较长，这里不贴出，详见[此](https://www.luogu.com.cn/paste/ge525sta)
  
#### 一、按钮的实现

  0. 原理\
    Markdown 的链接名支持使用 $\LaTeX$
  1. 简单示例
  
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
  
#### 最后、确定发布位置
  讨论区与剪贴板和博客不同，讨论区的无法渲染使用了 `\def`、`\newcommand`、`\renewcommand` 等宏命令的源码，因此
