github代码提交：

使用 SSH 密钥认证
1. 检查本地是否已有 SSH 密钥
打开终端，输入以下命令检查是否已有 SSH 密钥：
    
ls -al ~/.ssh

如果输出结果中包含 id_rsa.pub 或 id_ed25519.pub 等文件，则表示已有 SSH 密钥；若没有，则需要生成新的 SSH 密钥。

2. 生成新的 SSH 密钥（如果需要）
在终端输入以下命令生成新的 SSH 密钥，按照提示操作即可：
    
ssh-keygen -t ed25519 -C "your_email@example.com"

将 your_email@example.com 替换为你在 GitHub 上注册的邮箱地址。

3. 将 SSH 密钥添加到 SSH 代理
输入以下命令启动 SSH 代理：
    
eval "$(ssh-agent -s)"

然后将生成的 SSH 密钥添加到代理中：
    
ssh-add ~/.ssh/id_ed25519

这里的 id_ed25519 是生成密钥时默认的文件名，如果你的文件名不同，请相应修改。

4. 将 SSH 公钥添加到 GitHub 账户
打开公钥文件：
    
cat ~/.ssh/id_ed25519.pub

复制输出的公钥内容，登录 GitHub 账户，进入 Settings -> SSH and GPG keys，点击 New SSH key，将复制的公钥粘贴到 Key 字段中，然后点击 Add SSH key。

5. 修改远程仓库地址为 SSH 地址
在终端中进入项目目录，使用以下命令将远程仓库地址从 HTTPS 改为 SSH：
    
git remote set-url github git@github.com:duodoo-ai/DuodooBMS.git

这里的 git@github.com:duodoo-ai/DuodooBMS.git 是你 GitHub 仓库的 SSH 地址，可在 GitHub 仓库页面中找到。

6. 查看远程分支设置
   
   git remote -v   

7. 再次推送代码

    git push origin <分支名>

将 <分支名> 替换为你要推送的分支名称。


多分支分别提交：

(gitee或github上面内容有手动更新，先git stash 、 git pull gitee/github 、git stash apply)

git add .

git commit -m "提交说明"

git push origin master   / git push github master