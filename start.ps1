$existCheck = 0

$appdata = [Environment]::GetFolderPath([Environment+SpecialFolder]::ApplicationData)

$existCheck += (ls $appdata | Select-String -Pattern 'Python' -AllMatches).Matches.Count

if ($existCheck -eq 0) {
	$userprof = [Environment]::GetFolderPath('UserProfile')
    $gamedir = $PWD.Path
	cd $userprof
    echo 'PWD = $userprof'
	cd .\Downloads\
    echo 'PWD = $userprof \Downloads'
    echo 'Fetching Python 3.11 executable from www.python.org'
	wget https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe -OutFile python311.exe
    echo 'Running Python 3.11 setup...'
    .\python311.exe
    echo 'Please DO NOT touch the keyboard!'
    $wshell = New-Object -ComObject wscript.shell;
    Sleep 5
    $wshell.SendKeys('{DOWN}')
    Sleep 2
    $wshell.SendKeys('{DOWN}')
    Sleep 2
    $wshell.SendKeys('{DOWN}')
    Sleep 2
    $wshell.SendKeys('~')
    Sleep 2
    $wshell.SendKeys('{UP}')
    Sleep 2
    $wshell.SendKeys('{UP}')
    Sleep 2
    $wshell.SendKeys('{UP}')
    Sleep 2
    $wshell.SendKeys('~')
    Sleep 4
    $wshell.SendKeys('{LEFT}')
    Sleep 2
    $wshell.SendKeys('~')
    echo 'PWD = $gamedir'
    cd $gamedir
    ls -al
    Sleep 45
    echo 'Python 3.11 is successfully installed on your system!'
    echo 'Downloading pygame library...'
    py -m pip install pygame
    echo 'pygame installed successfully!'
    echo 'Starting Snake!...'
    py .\snake.py > lastgame.txt
    echo 'Thanks for playing!'
    $existCheck = 1
} else {
    echo 'Loading...'
    py .\snake.py > lastgame.txt
}