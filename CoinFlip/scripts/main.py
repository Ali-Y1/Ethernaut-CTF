from time import sleep

from brownie import interface, network, config
from scripts.helpful import get_account


def exploit():
    # Get account address
    account = get_account()
    # Deploy Contract
    # attack = Attack.deploy({"from": account})

    # using interface
    attack = interface.Attack(config["Attack_add"])

    for i in range(10):
        attack.flip(config['Address'], {"from": account})
        sleep(30)


def main():
    exploit()
