import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        url = "https://api.coincap.io/v2/assets/bitcoin" 
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        
        price_str = data["data"]["priceUsd"]
        price_per_btc = float(price_str) 
        
        total_cost = amount * price_per_btc
        
        print(f"${total_cost:,.4f}")

    except requests.RequestException:
        sys.exit("Request error")
    except (KeyError, TypeError):
        sys.exit("JSON structure error")

if __name__ == "__main__":
    main()