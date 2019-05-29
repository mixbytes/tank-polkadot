# MixBytes Tank

### Requirements

- Python3
- Terraform 0.11.13
- Terraform-Inventory v0.8

### Install

#### Terraform

For Ubuntu Linux
```shell
sudo apt-get install -y wget unzip
export TER_VER="0.11.13"
wget https://releases.hashicorp.com/terraform/${VER}/terraform_${VER}_linux_amd64.zip
unzip terraform_${VER}_linux_amd64.zip
sudo mv terraform /usr/local/bin/
```
#### Terraform Inventory
```shell
export terraform_inventory_ver="v0.8"
wget https://github.com/adammck/terraform-inventory/releases/download/${terraform_inventory_ver}/terraform-inventory_${terraform_inventory_ver}_linux_amd64.zip terraform-inventory.zip
unzip terraform-inventory_v0.8_linux_amd64.zip
sudo mv terraform-inventory /usr/local/bin/
```

#### Tank
```shell
pip3 install tank-polkadot
```

### Use

#### 1. Create cluster and provision with default blockchain

Create config

```
### ~/.tank.yml
---
tank:
  setup_id: "47956"
  pvt_key: ~/.ssh/id_rsa
  pub_key: ~/.ssh/id_rsa.pub
  ssh_fingerprint: "a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1"
  blockchain_name: "polkadot"
  blockchain_ansible_repo: "https://github.com/mixbytes/tank.ansible-polkadot"
  blockchain_ansible_repo_version: "master"
  provider: "digitalocean"
  blockchain_instances: "2"
digitalocean:
  token: "****************************************"
```

#### 2. Deploy cluster

```shell
tank deploy
```
