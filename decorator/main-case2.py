#【背景紹介】
#   PythonのABCMetaクラスでは、抽象クラスを宣告するabstractmethodデコレータがありますが、
#   override対象が存在しているかをチェックする方法が実装されていないため、
#   overrideするつもりでしたが、新しいメソッドを作ってしまったことが発生する可能性があります、
#   それクラス作成時自動的にチェックするために、ABCMetaの改良クラスABCDMetaを作成しました。

#【コード内容説明】
#   デコレータを使って、overrideチェックを実現したABCMetaの改良クラスABCDMetaを作成しました。
#   詳細はPython_Design_Pattern_23\utilsに参照してください。
#   utilsではregisterとoverrideデコレーターを新しく作成し、
#   それを利用して、overrideチェックを実現したABCDMetaを作成しました。