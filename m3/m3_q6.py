def adjust_recipe(recipe_kosaji, recipe_servs, cook_servs):
    adjust_kosaji = recipe_kosaji * (cook_servs / recipe_servs) #レシピの調味料の分量
    return adjust_kosaji

def round_kosaji(adjust_kosaji): #小さじの分量を0.5単位に丸めた文字列を返す
    int_part = int(adjust_kosaji) #整数部分の取得
    frac_part = adjust_kosaji - int_part #小数部分の取得
    if frac_part >= 0.5: #小数部分が0.5以上なら
        return str(int_part) + '.5' #整数部分 + 0.5の文字列を返す
    else:
        return str(int_part) #小数部分が0.5未満なら整数部分のみ文字列で返す

recipe_servs = int(input('レシピは何人前？: '))

saji_type = ''
while saji_type not in ['L', 'S']: #saji_typeが'L'または'S'でない限りループを続ける
    saji_type = input('レシピのさじの種類は？(大さじはL、小さじはS) : ')

saji_name = '大さじ' if saji_type == 'L' else '小さじ' #三項演算子：saji_typeが'L'のとき大さじ、それ以外は小さじ
recipe_saji = float(input(f'レシピは{saji_name}何杯？: '))

cook_servs = int(input('作る料理は何人前？: '))

recipe_kosaji = recipe_saji * 3 if saji_type == 'L' else recipe_saji #三項演算子：大さじなら小さじに換算
adjust_kosaji = adjust_recipe(recipe_kosaji, recipe_servs, cook_servs)

cook_oosaji, cook_kosaji = divmod(adjust_kosaji, 3) #小さじ→ 大さじ換算：商が大さじ、あまりが小さじ

print(f'{cook_servs}人前では、大さじが{cook_oosaji:.0f}杯と小さじが{round_kosaji(cook_kosaji)}杯です')
