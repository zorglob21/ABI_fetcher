This is a python module aiming to allow the user to quickly fetch any ABI from a verified smartcontract on any EVM compatible blockchain.

commands:<br>
abi-fetcher help or h => display this message<br>
abi-fetcher list => display all available networks<br>
abi-fetcher fetch --contract xxx --network xxx --api-key xxx --output xxx<br>

--contract = the contract address on the blockchain<br>
--network = network name as displayed in the list (use quotation marks)<br>
--api-key = your personnal etherscan api key. If you don't have one, just go there : https://etherscan.io/ and sign up to get one.<br>
--output(optional) = output directory for the generated ABI. Default directory is /ABI from the root<br>

example :
abi-fetcher fetch --contract 0xXXXXXX --network "base mainnet" --api-key XXXXXXXXXXXX

If you are unsure about the network name you can browse the abi_fetcher/chainlist.json file to search via chain ID. If the network isn't listed, you can either add a network entry into the json abi_fetcher/chainlist.json or try inputing the beginning of the explorer API Url like this :

*https://api.etherscan.io/v2/api
   ?chainid=1*
   &module=contract
   &action=getabi
   &address=0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413
   &apikey=YourApiKeyToken

   replace the part between * * with your own url.


The abi json should be in the ABI folder. If anything went wrong, you will find the recorded error message in the created json file.