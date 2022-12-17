$domain = "nice-assignment.local"
$hosts_path = "C:\Windows\System32\drivers\etc\hosts"
$vagrant_file_path = "C:\Users\talsh\Desktop\HomeAssignment"
$chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
$assigment_url = "https://" + $domain
$record = "127.0.0.1" + " " + $domain

Add-Content -Path $hosts_path -Value $record
cd $vagrant_file_path
vagrant up
Start-Process $chrome_path $assigment_url