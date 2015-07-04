# box_webapp
box_webapp test

how to setup
==================


## OS X

### insatll brew
http://brew.sh/index_ja.html
```shell
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### install git
```shell
brew install git
```

or using Xcode command line utils

(command line utils)[http://apple.stackexchange.com/questions/161648/how-to-use-gcc-or-git-without-installing-xcode]

### install pyenv
``` shell
$ brew install pyenv
$ brew install pyenv-virtualenv
```

### install python
``` shell
$ pyenv install 3.4.3
```

### create virutalenv
``` shell
pyenv virtualenv 3.4.3 box-webapp-test
```

### pull this repository
```shell
$ cd ~/Documents
$ git clone https://github.com/box/box-ios-browse-sdk.git
```

### install 
``` shell
$ cd ~/Documents/box-ios-browse-sdk
$ pyenv local box-webapp-test
$ pip install -r ./requirements.txt
```


### migrate 
``` shell
$ ./manage.py migrate
```


### runserver
``` shell
$ ./manage.py runserver_plus 0.0.0.0:8000 --cert ./webapp/server.crt
```


### and goto box web site 
open your test app!

