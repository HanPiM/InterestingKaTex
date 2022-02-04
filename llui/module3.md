此文属于 [luogu-latex-and-markdown-ui](https://www.luogu.com.cn/paste/om2r4sar) 。

---

### 模块三：交互控件

原理：Markdown 的链接名称支持使用 $\LaTeX$
    
1. 简单按钮
  
    [$
    \rule{40pt}{14pt}\kern{-31.5pt}\color{white}
    \raisebox{4.7pt}{\footnotesize\sf Button}
    $]()
   
    ```
    [$
    \rule{40pt}{14pt}\kern{-31.5pt}\color{white}
    \raisebox{4.7pt}{\footnotesize\sf Button}
    $]()
    ```
   
2. 带边框的圆角按钮
  
    其实就是 圆角边框+文本 的组合。

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
3. 伪立体按钮
  
    原理：
    
    [$
    \color{#F6F8FA}\rule{59pt}{16pt}
    \kern{-53pt}
    \raisebox{6pt}{
    \color{#24292F}\sf{\scriptsize 这是一个按钮}
    }\kern{-52pt}
    \color{#D5D8DA}\rule{57pt}{0pt}\kern{0.5pt}
    \rule[1pt]{0.1pt}{15pt}
    $]()

    ```
    [$
    \color{#F6F8FA}\rule{59pt}{16pt}
    \kern{-53pt}
    \raisebox{6pt}{
    \color{#24292F}\sf{\scriptsize 这是一个按钮}
    }\kern{-52pt}
    \color{#D5D8DA}\rule{57pt}{0pt}\kern{0.5pt}
    \rule[1pt]{0.1pt}{15pt}
    $]()
    ```