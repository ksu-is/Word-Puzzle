import os
import functools
import random

from wordsearch import WordSearch
from flask import Flask, render_template, request, jsonify

def create_app():
    #create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    random_words = [
        "APPLE", "BANANA", "ORANGE", "GRAPES", "KIWI",
        "WATERMELON", "STRAWBERRY", "BLUEBERRY", "PINEAPPLE", "MANGO", 
        "PEACH", "PEAR", "APRICOT", "PLUM", "CHERRY",
        "LEMON", "LIME", "COCONUT", "POMEGRANATE", "RASPBERRY", 
        "FIG", "NETARINE", "CANTALOUPE", "HONEYDEW", "BLACKBERRY", 
        "CRANBERRY", "TANGERINE", "PAPAYA", "GUAVA", "PASSIONFRUIT", 
        "LYCHEE", "DRAGONFRUIT", "KIWIFRUIT", "PERSIMMON", "STARFRUIT", 
        "AVOCADO", "GRAPEFRUIT", "MULBERRY", "BOYSENBERRY", "APRICOT", 
        "MELON", "GOOSEBERRY", "KUMQUAT", "ELDERBERRY", "QUINCE", 
        "BREAD", "BUTTER", "CHEESE", "MILK", "YOGURT", 
        "EGG", "BACON", "SAUSAGE", "PANCAKES", "WAFFLE", 
        "CEREAL", "TOAST", "JAM", "HONEY", "SYRUP", 
        "COFFEE", "TEA", "JUICE", "SMOOTHIE", "SODA", 
        "WATER", "BEVERAGE", "DRINK", "SNACK", "CAKE", 
        "COOKIE", "BISCUIT", "SANDWICH", "PIZZA", "PASTA", 
        "SALAD", "SOUP", "STEAK", "CHICKEN", "FISH", 
        "VEGETABLE", "FRUIT", "DESSERT", "APPETIZER", "ENTREE", 
        "SIDE", "SNACK", "MEAL", "DINNER", "LUNCH"
    ]

    @app.route('/', methods=['GET'])
    def home_page():
        return render_template('pages/home.html')
    
    @app.route('/word-search', methods=['GET'])
    def word_search_page(): 
        word_list = random.sample(random_words, 10)
        word_search = WordSearch()
        word_search.generate(word_list)
        grid = word_search.grid
        return render_template('pages/word-search.html', grid=grid, words=word_list)

@app.route('/check_match', methods=['POST'])
def check_math():
    word = request.json.get('word')
    math_found = check_match_with_word_list(word)
    return jonsify({'match_found' : match_found})

def check_match_with_word_list(word):
    return word in random_words

return create_app

