# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "debian/bookworm64"

  config.vm.define "gcp" do |gcp|
    gcp.vm.hostname = "gcp"
    gcp.vm.network "private_network", ip: "192.168.60.60"
    # Redirection du port 5000 pour Flask
    gcp.vm.network "forwarded_port", guest: 8080, host: 8080
  end

  config.vm.provision "shell", inline: <<-SHELL
    # Mise à jour du système
    apt-get update -y

    # Installation des dépendances nécessaires
    apt-get install -y python3 python3-pip python3-venv git docker docker-compose

    # Ajout de l'hôte dans /etc/hosts
    echo "192.168.60.60 gcp" >> /etc/hosts

    # Message de confirmation
    echo "Environnement prêt pour le TP serverless."

    # Configuration de l'environnement virtuel
    python3 -m venv venv
    . venv/bin/activate
  SHELL
end
