import requests

url = 'https://breaking-bad-quotes.herokuapp.com/v1/quotes'

def get_quote():
    '''
    This is a description of my package
    '''
    response = requests.get(url).json()[0]

    return (f'quote: {response["quote"]} said by: {response["author"]}')

if __name__ == "__main__":
    print(get_quote())
