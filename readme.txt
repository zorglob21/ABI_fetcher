This is a python module aiming to allow the user to quickly fetch any ABI from a verified smartcontract on any EVM blockchain.

Run it:
input a network name amongst those listed. If the network isn't listed, you can try inputing the beginning of the explorer API Url like this:

*https://api.etherscan.io/v2/api*
   ?chainid=1
   &module=contract
   &action=getabi
   &address=0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413
   &apikey=YourApiKeyToken

   replace the part between * * with your own url.

then input the contract address. The contract has to be verified for the operation to complete successfully

then input your etherscan API key. If you don't have one, just go there : https://etherscan.io/ and sign up to get one.

et voilà! The abi json should be in the ABI folder. If anything went wrong, you will find the recorded error message in the json file.