### Git

#### 部署GitHub远程库

- 设置本地用户和邮箱

  ```
  git config --global user.email "w@qq.com"
  git config --global user.name "w"
  ```

- 创建SSH Key。

  ```
   ssh-keygen -t rsa -C "w@qq.com"
  ```

  > 在用户主目录下，看看有没有.ssh目录，如果有，再看看这个目录下有没有`id_rsa`和`id_rsa.pub`这两个文件，如果已经有了，可直接跳到下一步。

  > 如果一切顺利的话，可以在用户主目录里找到`.ssh`目录，里面有`id_rsa`和`id_rsa.pub`两个文件，这两个就是SSH Key的秘钥对，`id_rsa`是私钥，不能泄露出去，`id_rsa.pub`是公钥，可以放心地告诉任何人。

  > cat /home/yssong/.ssh/id_rsa.pub

- 登陆GitHub

  > 用户 -> setting -> SSH and GPG keys -> New SSh key。

  > 填上任意Title，在Key文本框里粘贴`id_rsa.pub`文件的内容。


#### 从GitHub获取代码开始工作

- 克隆远程库代码到本地

  ```
  git clone git@github.com:ARDUJS/learngit.git
  cd learngit
  ```

- 上传本地库

  ```
  git push origin master
  ```

  

#### 本地git库部署至GitHub上

- 初始化并构建本地库

  ```
  mkdir xx
  cd xx
  git init
  git add xx
  git commit -m "message"
  ```

- 构建远程库

  > \+ --> New repository -->  Create repository 

- 将本地库与远程库关联

  ```
  git remote add origin git@github.com:ARDUJS/learngit.git
  git push -u origin master
  ```

- 修改本地库上传网络库

  ```
  git push -u origin master
  ```
  

#### 远程库相关命令

- 查看远程库

  ```
  git remote -v
  ```

- 删除远程库

  ```
  git remote remove origin
  ```

  

