## luogu-latex-and-markdown-ui
此文长期更新

[Also on Github](https://github.com/HanPiM/InterestingKaTex_ForLuogu/blob/main/llui/main.md)

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

重要更新：

- 2021/12/26 拆分成不同模块，此后本文仅作为目录和附录。

#### 目录

- [模块一：基础部分](https://www.luogu.com.cn/paste/a9rq3vfr)

  - 一、编辑环境
  - 二、基础命令
  - 三、绘制
    1. 基础绘制
    2. 绘制特殊效果
    3. 杂项

- [模块二：无交互控件](https://www.luogu.com.cn/paste/xdfqclyv)

- [模块三：交互控件](https://www.luogu.com.cn/paste/xdfqclyv)


- 附 A - 其他注意事项
- 附 B - 其他样例

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
\BasicWarnBar{250px}{26px}{注意}{为方便，文中的 “块” 常用于指代一段 \LaTeX 公式。}\\
$

---

#### 附 A - 其他注意事项
  讨论区与剪贴板和博客不同，讨论区的无法渲染使用了 `\def`、`\newcommand`、`\renewcommand` 等宏命令的源码，因此如果需要发布到讨论区，需将所有宏替换回对应字符。

#### 附 B - 其他样例
  1. [绘制 note](https://www.luogu.com.cn/paste/j29i6yfi)
  2. 未命名示例-1
  
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
        $ $\kern{2pt}$ $%删去了不必要的内容
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
        }}}\kern{-200pt}$.$\kern{4pt}\raisebox{10pt}{\footnotesize\sf{伪嵌套 2：}}
        $ $
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
        $ $\kern{2pt}$ $%删去了不必要的内容
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
        }}}\kern{-200pt}$.$\kern{4pt}\raisebox{10pt}{\footnotesize\sf{伪嵌套 2：}}
        $ $
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
