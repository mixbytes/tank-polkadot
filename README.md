# MixBytes Tank for Polkadot

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
wget https://releases.hashicorp.com/terraform/${TER_VER}/terraform_${TER_VER}_linux_amd64.zip
unzip terraform_${TER_VER}_linux_amd64.zip
sudo mv terraform /usr/local/bin/
```
#### Terraform Inventory
```shell
export terraform_inventory_ver="v0.8"
wget https://github.com/adammck/terraform-inventory/releases/download/${terraform_inventory_ver}/terraform-inventory_${terraform_inventory_ver}_linux_amd64.zip
unzip terraform-inventory_v0.8_linux_amd64.zip
sudo mv terraform-inventory /usr/local/bin/
```

#### Optional: create virtualenv

Optionally, create and activate virtualenv

```shell
sudo apt-get install -y python3-virtualenv
python3 -m virtualenv -p python3 venv
```

After virtualenv creation and each time after opening a terminal, activate virtualenv to work with the tank:

```shell
. venv/bin/activate
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
