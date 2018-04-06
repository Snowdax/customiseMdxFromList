# customiseMdxFromList
`COCA5000.txt` 储存了 `https://www.wordfrequency.info/free.asp?s=y` 页面上的 COCA5000 词汇表，每个单词一行

`COCA5000_list.py` 将上面的 txt 文件转换为 Python 中的列表数据格式，并将其赋值给 wordList 变量，该 .py 文件可作为模块导入其他 Python 程序。这个文件是由 `line2list.py` 生成的。

## line2list.py
输入：文件名.txt
输出：文件名_list.txt
功能：将每行的内容转换为 Python 中的列表数据格式，并将其赋值给 wordList 变量。

##
首先将所需词库的 .mdx 文件在 GetDict.exe 中转换为 `MDX 源文件`，如下图所示：
![](readmePictures/getDict.png)
生成的 .txt 类型的`MDX 源文件`，应该是一行词头，一行释义，一行 `</>`，如下图所示：
![](readmePictures/mdxStyle.png)

性能：约 2.5 秒/词，5000 词合共约 3.5 小时

## customiseMdxFromList.exe
由 customiseMdxFromList.py 封装。不用搭建 Python 环境，且程序里面集成了 COCA5000 的单词表，直接在 Windows 上就能使用。
