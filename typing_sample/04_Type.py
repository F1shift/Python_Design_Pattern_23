class Pizza:
    pass


class CheesePizza(Pizza):
    pass


class BeconPizza(Pizza):
    pass


class Drink:
    pass

# やりたい事-------------------------------------------------------------
# menu = { “ピザ名”: ピザのクラス}

# def order_pizza(pizza_name: str) -> Pizza:
# 	pizza_class = menu[pizza_name]
# 	new_pizza = pizza_class()
# 	return new_pizza


# 変数型がクラスで特定のクラスのみを許可したいの場合---------------------------
# またはGenerics対処がクラスで特定のクラスのみ許可したい場合
from typing import Dict

pizza_menu1: Dict[str, Pizza] = {} 
pizza_menu1["チーズピザ"] = CheesePizza() # Pizzaインスタンスしか渡せない。
pizza_menu1["チーズピザ"] = CheesePizza # Pizzaインスタンスしか渡せない。

pizza_menu2: Dict[str, type] = {}      # isinstance(Pizza, type) == true
pizza_menu2["チーズピザ"] = CheesePizza # 全てのクラスがtypeのインスタンスのため、どんなクラスでも入れてしまう。
pizza_menu2["ベーコンピザ"] = BeconPizza
pizza_menu2["ドリンク"] = Drink # ピザのメニューなのにドリンクが入ってしまった！

def order_pizza(pizza_name: str) -> Pizza:
    return pizza_menu2["ベーコンピザ"]()

# クラス変数にPizzaを制限したい場合如何すれば?

# 変数型がクラスで特定のクラスのみを許可したいの場合----------------------------------------
# またはGenerics対処がクラスで特定のクラスのみ許可したい場合
from typing import Type, Dict

#ケース１
pizza_menu3: Dict[str, Type[Pizza]] = {}
pizza_menu3[""]
pizza_menu3["チーズピザ"] = CheesePizza  # value型チェック：OK
pizza_menu3["ベーコンピザ"] = BeconPizza # value型チェック：OK
pizza_menu3["ドリンク"] = Drink          # value型チェック：警告、ドリンクはピザではない！

def order_pizza(pizza_name: str) -> Pizza:
    return pizza_menu3["ベーコンピザ"]()