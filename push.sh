git add .
git commit -m $1
git push -u origin master
git push -u github master
cd ../bookdown-pub/learningpython
git add .
git commit -m $1
git push
