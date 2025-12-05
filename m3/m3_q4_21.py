a = 0b101100
b = 0b110110
c = []

c.append(bin(a & b).count('1'))# 2
c.append(bin(a | b).count('1'))# 5
c.append(bin(a ^ b).count('1'))# 3
c.append(bin(a >> 2).count('1'))# 3
print(c)

'''
AND(&):論理積
    両方のビットが１のとき１
    a & bは0b100100

OR(|):論理和
    どちらかが１だと１
    A | bは0b111110
XOR(^):排他的論理和
    a ^ bは0b011010
右シフト(>>):ビットを右にnだけ移動
    左は０または符号で補う
    0b101100 >> 2 →　0b00101
'''
