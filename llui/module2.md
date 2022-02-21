此文属于 [luogu-latex-and-markdown-ui](https://www.luogu.com.cn/paste/om2r4sar) 。

---

### 模块二：无交互控件

1. 信息角标

    $
    \def\w{4.5px}
    {\color{#FA5151}
    \LARGE\bullet
    \kern{-3.7px}
    \rule[1px]{\w}{6.15px}
    \kern{-3.7px}
    \LARGE\bullet}
    \kern{-\w}\kern{-5.9px}
    \color{white}
    \raisebox{2.2px}{\tiny\textsf{99}}
    $
    $
    \def\w{8.5px}
    {\color{#1485EE}
    \LARGE\bullet
    \kern{-3.7px}
    \rule[1px]{\w}{6.15px}
    \kern{-3.7px}
    \LARGE\bullet}
    \kern{-\w}\kern{-5.9px}
    \color{white}
    \raisebox{2.2px}{\tiny\textsf{new}}
    $
    
    这个比较容易实现，使用 两个圆 + 一个矩形 就可以画出。

    ```
    $
    \def\w{4.5px}
    {\color{#FA5151}
    \LARGE\bullet
    \kern{-3.7px}
    \rule[1px]{\w}{6.15px}
    \kern{-3.7px}
    \LARGE\bullet}
    \kern{-\w}\kern{-5.9px}
    \color{white}
    \raisebox{2.2px}{\tiny\textsf{99}}
    $
    ```

	综合应用：参见附录-3

2. 信息块

    1. 简单的信息块
    
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
        \def\BasicInfoBarColorFill{#F4F4F4}\def\BasicInfoBarColorIcon{#0078D4}
        \def\BasicWarnBarColorFill{#FFF4CE}\def\BasicWarnBarColorIcon{#9D5D00}
        \def\BasicOkBarColorFill{#DFF6DD}\def\BasicOkBarColorIcon{#0F7B0F}
        \def\BasicErrBarColorFill{#FDE7E9}\def\BasicErrBarColorIcon{#C42B1C}
        \newcommand\BasicInfoBar[4]{
          \BasicInfoBarFather{#1}{#2}{#3}{#4}
          {\BasicInfoBarColorFill}{i}{\BasicInfoBarColorIcon}
        }
        \newcommand\BasicWarnBar[4]{
          \BasicInfoBarFather{#1}{#2}{#3}{#4}
          {\BasicWarnBarColorFill}{i}{\BasicWarnBarColorIcon}
        }
        \newcommand\BasicOkBar[4]{
          \BasicInfoBarFather{#1}{#2}{#3}{#4}
          {\BasicOkBarColorFill}
          {\tiny\kern{-2px}\raisebox{0.8px}{√}}
          {\BasicOkBarColorIcon}
        }
        \newcommand\BasicErrBar[4]{
          \BasicInfoBarFather{#1}{#2}{#3}{#4}
          {\BasicErrBarColorFill}
          {\kern{-2px}\raisebox{0.6px}{×}}
          {\BasicErrBarColorIcon}
        }
        \BasicInfoBar{200px}{26px}{标题}{副标题}\\
        \BasicWarnBar{200px}{26px}{标题}{副标题}\\
        \BasicOkBar{200px}{26px}{标题}{副标题}\\
        \BasicErrBar{200px}{26px}{标题}{副标题}\\
        $
        
        ```
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
        \def\BasicInfoBarColorFill{#F4F4F4}\def\BasicInfoBarColorIcon{#0078D4}
        \def\BasicWarnBarColorFill{#FFF4CE}\def\BasicWarnBarColorIcon{#9D5D00}
        \def\BasicOkBarColorFill{#DFF6DD}\def\BasicOkBarColorIcon{#0F7B0F}
        \def\BasicErrBarColorFill{#FDE7E9}\def\BasicErrBarColorIcon{#C42B1C}
        \newcommand\BasicInfoBar[4]{
          \BasicInfoBarFather{#1}{#2}{#3}{#4}
          {\BasicInfoBarColorFill}{i}{\BasicInfoBarColorIcon}
        }
        \newcommand\BasicWarnBar[4]{
          \BasicInfoBarFather{#1}{#2}{#3}{#4}
          {\BasicWarnBarColorFill}{i}{\BasicWarnBarColorIcon}
        }
        \newcommand\BasicOkBar[4]{
          \BasicInfoBarFather{#1}{#2}{#3}{#4}
          {\BasicOkBarColorFill}
          {\tiny\kern{-2px}\raisebox{0.8px}{√}}
          {\BasicOkBarColorIcon}
        }
        \newcommand\BasicErrBar[4]{
          \BasicInfoBarFather{#1}{#2}{#3}{#4}
          {\BasicErrBarColorFill}
          {\kern{-2px}\raisebox{0.6px}{×}}
          {\BasicErrBarColorIcon}
        }
        \BasicInfoBar{200px}{26px}{标题}{副标题}\\
        \BasicWarnBar{200px}{26px}{标题}{副标题}\\
        \BasicOkBar{200px}{26px}{标题}{副标题}\\
        \BasicErrBar{200px}{26px}{标题}{副标题}\\
        $
        ```

