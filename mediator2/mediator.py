import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
print(sys.path)
from mediator2.button import Button
from mediator2.textarea import TextArea


class Mediator:
    def __init__(self, tb_id : TextArea, tb_pw : TextArea, bt_login : Button) -> None:
        self.id_textArea = tb_id
        self.pw_textArea = tb_pw
        self.login_button = bt_login
        tb_id.mediator = self
        tb_pw.mediator = self
        bt_login.mediator = self
    
    def on_change(self, elements):
        if isinstance(elements, TextArea):
            self.update_ui()
        elif elements is self.login_button:
            self.comfirm_id_pw()
            
    def update_ui(self):
        self.login_button.isActive = bool(self.id_textArea.text and self.pw_textArea.text)
    
    def comfirm_id_pw(self):
        if self.id_textArea.text == "hoge" and self.pw_textArea.text == "password":
            print("Login successed.")
        else:
            print("Login failed!")
    
    def ShowStatus(self):
        print("-"*30)
        print(f"id_textArea : {self.id_textArea.text}")
        print(f"pw_textArea : {self.pw_textArea.text}")
        print(f"login_button isActive : {self.login_button.isActive}")