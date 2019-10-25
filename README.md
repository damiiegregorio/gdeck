# gdeck
##### Version 1
a python module that displays the value of a card's suit and rank when using the print function.


### Machine Problem: Cards

#### Requirements:

* This project should be used as a python module and not as a script
* A Python class that will represent a deck of cards named "Deck"
  * It should have a instance attribute "cards" which contains a list of Card objects upon initialization
* The Card class represents a card. It has 2 instance variables: suit and rank
  * The Card class should display the value of its suit and rank when using the print function on it
* An instance of class Deck should return a random card when the function choice is used on it (Do: from random import choice to be able to use choice)
  * Hint: choice takes in a sequence as parameter. To know more: https://pynative.com/python-random-choice/ and https://docs.python.org/3/library/random.html#random.choice
* An instance of class Deck should return a card/list of cards when slicing is used (To know more about slicing: https://www.oreilly.com/learning/how-do-i-use-the-slice-notation-in-python)


## Features

* Draw a random card
* Display deck
* Display deck length
* Display card position
* Slicing cards

## Usage

#### Installation
```
pip install gdeck
```

#### Draw a random card
```
>>> from gdeck import Deck
>>> deck = Deck()
>> print(deck.choice())
```

#### Display deck
```
>> print(deck.show_deck())
```

#### Show deck length
```
>> print(deck.__len__())
```

#### Display card position
```
>> print(deck.__getitem__(<number>))
```

#### Slicing cards
```
>> print(deck[<from>:<end>])
```

## Testing
```
pip install pytest-cov
pip install pytest-xdist
python -m pytest --cov=gdeck test_gdeck.py
```

## Built With
* [Python](https://www.python.org/downloads/) v3.7
* [Jetbrains PyCharm Community Edition 2019](https://www.jetbrains.com/pycharm/download/) - IDE

## Authors

* **Damaris Gregorio** - *Initial work* - [Dam Gregorio](https://github.com/damiiegregorio)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
