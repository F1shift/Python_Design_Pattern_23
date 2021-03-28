from interpreter.CalcExpression import CalcExpression
import sys
from pathlib import Path
from xml import etree
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from interpreter.IExpression import IExpression
from interpreter.Constant import Constant
from interpreter.CalcExpression import *
import xml.etree.ElementTree as ET
from typing import Optional, cast
    

class Context:
    def __init__(self, filename: str) -> None:
        self._filename_:str = filename

    def buildexpression(self, root: Optional[ET.Element] = None) -> IExpression:
        if root is None:
            root = ET.parse(self._filename_).getroot()
        if CalcMethod[root.tag] == CalcMethod.Constant:
            expression = Constant(float(root.attrib["Value"]))
        else:
            childs = [ self.buildexpression(e) for e in list(cast( ET.Element, root))]
            expression = CalcExpression(CalcMethod[root.tag], childs)
        return expression
