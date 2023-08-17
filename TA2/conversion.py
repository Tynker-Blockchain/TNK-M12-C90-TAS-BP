from web3 import Web3

API_URL = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 =  Web3( Web3.HTTPProvider(API_URL))

def getGasPrices():
    try:
        gasPrices={}
        gweiPrices={}
        etherPrices={}
        dollarPrices={}

        gasPrices["current"] = web3.eth.gas_price

        gasPrices["slow"] = int(gasPrices["current"] * 0.9)  
        gasPrices["standard"] = int(gasPrices["current"] * 1.0)   
        gasPrices["fast"] = int(gasPrices["current"] * 1.1)     
        gasPrices["rapid"] = int(gasPrices["current"] * 1.2)   
                
        # Conversion of gas price into ether
        

        
        # Conversion of gas price into ether to dollars
        
     
        return gasPrices, gweiPrices, etherPrices, dollarPrices

    except Exception as e:
        print(f"Error: {e}")
        return None, None, None
