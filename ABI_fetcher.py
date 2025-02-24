from web3 import Web3
from dotenv import load_dotenv
import os
import argparse
import requests
import json

load_dotenv()

def load_networks(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)

networks = load_networks("chainlist.json")

def get_user_input():   
    
    network_list = [network["chainname"] for network in networks["list"]]

    print("Pre-recorded Networks: " + ", ".join(network_list))

    network = input("select a network amongst pre-recorded ones or input the first part of the api URL manually : ")

    selected_network = next((net for net in networks["list"] if net["chainname"] == network), None)

    if selected_network:
        api_url = selected_network["apiurl"]
    else:
        api_url = network  # User entered a custom URL

    contract_address = input("enter contract address : ")

    api_key = input("enter your api key : ")
    

    return contract_address, api_url, api_key

def __main__():
    
    contract_address, api_url, api_key = get_user_input()
 
    print( contract_address, api_url, api_key )

    action = 'getabi'  # Adjust the action as per your API usage
    url = f"{etherscan_api_endpoint_mainnet}?module=contract&action={action}&address={contract_address}&apikey={etherscan_api}"

    response = requests.get(url)

    print (response.status_code)

    if response.status_code == 200:
        data = response.json()
        # Process the data as needed
        if 'result' in data:
            abi_json = data['result']
            with open("ABI/"+contract_address+".json", 'w') as abi_file:
                json.dump(abi_json, abi_file, indent=4)
        else:
            print("Error: 'result' key not found in the API response")
    else:
        print(f"Error: {response.status_code}")

    

if __name__ == '__main__':
    __main__()
