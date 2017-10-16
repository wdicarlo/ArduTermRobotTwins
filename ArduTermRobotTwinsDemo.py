from Serial import Serial
from YinBoard import YinBoard
from YangBoard import YangBoard


yin = YinBoard('/dev/ttyS0')
yin.send("print \"hello from yin\"")

yang = YangBoard('/dev/ttyS1')
yang.send("print \"hello from yang\"")
