# 経費承認システムを作りたいです。
# 承認者(Approver)には部長(Director)と課長(SectionChief)があります。
# 3000円以下の一般経費は、課長だけで承認できます。
# 3000を超える特別経費の申請は、部長でしか承認できない条件があります。
# また、部長が忙しいので、承認まで時間がかかります。

import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from time import sleep
from abc import abstractmethod, abstractproperty
from utils.abcd import ABCD
from utils.abcd import override
from utils.register import regist

class Claim:
    def __init__(self, amount_of_money: float) -> None:
        super().__init__()
        self.amount_of_money: float = amount_of_money


class Aprrover(ABCD):
    @abstractmethod
    def approve_general_expense(self, claim: Claim):
        pass
    
    @abstractmethod
    def approve_special_expense(self, claim: Claim):
        pass
    

class Director(Aprrover):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name:str = name
    
    @regist(override)
    def approve_general_expense(self, claim: Claim):
        if claim.amount_of_money < 3000:
            sleep(10)
            print(f"承認済み。承認者：{self.name}")
        else:
            raise PermissionError("金額が3000を超える場合、特別経費で申請する必要があります。")
    
    @regist(override)
    def approve_special_expense(self, claim: Claim):
        sleep(10)
        print(f"承認済み。承認者：{self.name}")


class SectionChief(Aprrover):
    def __init__(self, name: str, director: Director) -> None:
        super().__init__()
        self.name : str = name
        self.director : Director = director
        
    @regist(override)
    def approve_general_expense(self, claim: Claim):
        if claim.amount_of_money < 3000:
            print(f"承認済み。承認者：{self.name}")
        else:
            raise PermissionError("金額が3000を超える場合、特別経費で申請する必要があります。")
    
    @regist(override)
    def approve_special_expense(self, claim: Claim):
        self.director.approve_special_expense(claim)


if __name__ == "__main__":
    claim_1000 = Claim(1000)
    claim_5000 = Claim(5000)
    sakamoto = SectionChief("坂本", Director("桜井"))
    sakamoto.approve_general_expense(claim_1000)
    sakamoto.approve_special_expense(claim_5000)