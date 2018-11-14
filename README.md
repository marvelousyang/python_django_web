# python_django_web
## 需配合以下项目使用，
- https://github.com/dpressel/rude-carnie
- 基本运行命令是：
  - python /home/lee/git/rude-carnie/guess.py --model_type inception --model_dir /home/lee/Downloads/22801 --filename test.jpg
## 使用前需修改pic_age/pic/views.py中的

- str=('python /home/lee/git/rude-carnie/guess.py --model_type inception --model_dir /home/lee/Downloads/22801 --filename ' + filepath)
- p=os.system(str)
- file_object = open('/home/lee/git/rude-carnie/log.txt')
改成对应目录
## 修改后运行服务器：
python manage.py runserver

## 访问地址：
- localhost:8000

## git常用命令:
- git init //把这个目录变成Git可以管理的仓库

-　git add README.md //文件添加到仓库

-　　git add . //不但可以跟单一文件，还可以跟通配符，更可以跟目录。一个点就把当前目录下所有未追踪的文件全部add了 

-　　git commit -m "first commit" //把文件提交到仓库

-　　git remote add origin git@github.com:yourName/yourPro.git //关联远程仓库

-　　git push -u origin master //把本地库的所有内容推送到远程库上

