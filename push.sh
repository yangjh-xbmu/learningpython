git add .
git commit -m $1
git push -u origin master
git push -u github master
echo '/n'
echo '文档信息推送完毕。开始推送静态文件仓库'
echo '/n'
cd ../bookdown-pub/learningpython
git add .
git commit -m $1
git push
