# Note

> 亲测有效！

#### 手动添加git到右键菜单

- win + R 输入 regedit， 打开注册表。
- 路径：计算机\HKEY_CLASSES_ROOT\Directory\Background。
- 在[Background]下如果没有[shell],则右键-新建项[shell]。
- 在[shell]下右键-新建项[open in [Git](http://lib.csdn.net/base/28)],其值为“Git Bash Here",此为右键菜单显示名称。
- 在[shell]下右键-新建-字符串值[Icon],双击编辑，其值为“D:\...\Git\mingw64\share\git\git-for-windows.ico”。此为菜单加图标。
- 在[open in git]下右键-新建-项[command],其值为 "D:\Program Files\Git\git-bash.exe"。

> 参考 https://www.cnblogs.com/whm-blog/p/7525903.html

#### 下载部分github文件

##### linux 

- yum install subversion
- 复制项目文件网址 如 （https://github.com/PaddlePaddle/Research/tree/master/KG/DuEE_baseline）
- 把“tree/master”替换为“trunk”
- svn checkout https://github.com/PaddlePaddle/Research/trunk/KG/DuEE_baseline

> 参考 https://blog.csdn.net/weixin_40746796/article/details/90262646

##### window

- 下载chrome插件 http://t.cn/AipFZm6j
- 双击点击要下载的文件或文件夹的空白处
- 右下方出现下载按钮，点击下载

> 详细操作 https://blog.csdn.net/weixin_30483697/article/details/102358178

