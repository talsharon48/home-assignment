vm_memory = 4096
vm_cpu = 2
vm_name = "nice-assignment"

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  config.vm.box_check_update = false
  config.vm.provision "file", source: "./PythonScripts", destination: "/home/vagrant/src/home_assignment"
  config.vm.provision "file", source: "./Confs", destination: "/home/vagrant/confs"
  
  config.vm.network "forwarded_port", guest: 443, host: 443, host_ip: "127.0.0.1"

  config.vm.provider "virtualbox" do |vb|
    vb.name = vm_name
    vb.gui = true
    vb.memory = vm_memory
	vb.cpus = vm_cpu
  end

  config.vm.provision "shell", inline: <<-SHELL	
    yum install -y epel-release python3 && yum install -y nginx
	pip3 install --upgrade pip && pip3 install -r /home/vagrant/src/home_assignment/requirements.txt
	python3 /home/vagrant/src/home_assignment/main.py
	mkdir -p /etc/pki/nginx/private && cp self_signed.crt /etc/pki/nginx/ && cp private.key /etc/pki/nginx/private/ && cp holidays.json /usr/share/nginx/html/index.json
	cp -f /home/vagrant/confs/nginx.conf /etc/nginx/nginx.conf
    systemctl enable nginx --now
  SHELL
end
