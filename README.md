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
unzip terraform-inventory_${terraform_inventory_ver}_linux_amd64.zip
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

Create config at `~/.tank.yml` and adjust it to your setup (see the inline comments below).
The essential steps are:
* providing (and possibly creating) a key pair;
* registering the public key with your cloud provider if needed;
* specifying a cloud provider access token.

```yaml
tank:
  # Unique ID of this test in your cloud account.
  # This ID prevents collisions of resources of different clusters created by Tank.
  # If you are planning to run multiple clusters simultaneously, make sure they have different setup_id.
  setup_id: "440"

  # Key pair to manage benchmark instances.
  # It's recommended to create a distinct key pair for benchmarking purposes.
  # The simplest way is:
  #   ssh-keygen -t rsa -b 2048 -f bench_key
  # (leave passphrase empty)
  # Please provide the full path to the key pair.
  pvt_key: /home/admin/tank-polkadot/bench_key
  pub_key: /home/admin/tank-polkadot/bench_key.pub
  
  # MD5 fingerprint of the public key.
  # Please note, in case of Digital Ocean you must add this key to your account at https://cloud.digitalocean.com/account/security (you can also get the fingerprint there).
  ssh_fingerprint: "3d:aa:76:55:25:4b:63:d3:e6:22:62:30:e0:9d:29:79"

  # short name of the benchmarked blockchain
  # (could be left as-is)
  blockchain_name: "polkadot"

  # the blockchain bindings role repository and branch
  # (could be left as-is)
  blockchain_ansible_repo: "https://github.com/mixbytes/tank.ansible-polkadot"
  blockchain_ansible_repo_version: "master"

  # cloud provider to use
  provider: "digitalocean"

  # number of validator instances to launch
  blockchain_instances: "2"

digitalocean:
  # Access token for a particular cloud provider.
  # In case of Digital Ocean the token can be created at https://cloud.digitalocean.com/account/api/tokens.
  token: "..."
```

#### 2. Deploy cluster

```shell
tank cluster deploy
```

#### 3. Login into the monitoring

Locate instance which name ends with `{your setup_id}-monitoring`, find the instance ip.
Open in browser `http://{monitoring ip}:3000/dashboards`, username and password are `tank`.

The dashboards can always be found at `http://{monitoring ip}:3000/dashboards`

#### 4. Create synthetic load

```shell
tank cluster bench [--tps N] [--total-tx N]
```

`--tps` - global transactions per second generation rate,

`--total-tx` - how many transactions to send (total).

#### 5. Shutdown and remove the cluster

```shell
tank cluster destroy
```
