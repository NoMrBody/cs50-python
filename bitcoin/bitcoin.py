import sys
import requests

def main():
    if len(sys.argv) <=1:
        sys.exit("Missing command-line argument")

    try:
        usr_input = float(sys.argv[1])

        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()

        output = usr_input * data["bpi"]["USD"]["rate_float"]

        print(f"${output:,.4f}")

    except requests.RequestException:
        sys.exit("Request error")
    except ValueError:
        sys.exit("Command-line argument is not a number")

if __name__ == "__main__":
    main()
