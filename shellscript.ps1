$param = $args[0]
echo $param
cd 'C:\Program Files\Google\Chrome\Application\'
.\chrome.exe --remote-debugging-port=8000 --user-data-dir=$param
