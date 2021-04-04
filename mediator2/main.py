import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from mediator2.button import Button
from mediator2.textarea import TextArea
from mediator2.mediator import Mediator

id_textarea = TextArea()
pw_textarea = TextArea()
login_button = Button()
mediator = Mediator(id_textarea, pw_textarea, login_button)

mediator.ShowStatus()

id_textarea.changeText("hoge")
mediator.ShowStatus()
login_button.click()

pw_textarea.changeText("password")
mediator.ShowStatus()
login_button.click()