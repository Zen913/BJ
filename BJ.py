import random

drawcard = []

def choice_card():
    number=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    mark=["♧","♤","♡","♢"]

    repeat_choice=False #同じカードを選ばないようにする
    choice_card=[]
    while repeat_choice !=True:
        choice_card = [random.choice(mark), random.choice(number)]
        drawcard.append(choice_card)
        repeat_choice =check_overlap_card(choice_card)
    return choice_card

def calc_score(card_list):
    i = 0
    score = 0
    while i < len(card_list):
        number = card_list[i][1]
        i+=1
        if number in ["J", "Q", "K"]: #絵札が選択されたとき、10になる処理
            score += 10
        elif number in ["A"]:      #Aが選択されたとき、1になる処理
            score += 1
        else:
            score +=int(number)
    return score

def check_overlap_card(choice_card):
    i = 0
    choiced_mark = choice_card[0]
    choiced_number  = choice_card[1]
    while i < len(drawcard):
        drawn_mark = drawcard[i][0]
        drawn_number = drawcard[i][1]
        if choiced_mark == drawn_mark:
            if choiced_number == drawn_number:
                return True
        i = i + 1
    return False

def print_card(card_list):
     i = 0
     while i < len(card_list):
         print (card_list[i])
         i = i + 1

def judge(player_score, dealer_score):
    if player_score > 21 and dealer_score > 21: #両者とも21を越えたらドロー
        return 2
    elif player_score > 21  and dealer_score < 21: #プレイヤーが21を越えたらドロー
        return 1
    else:
        if player_score > dealer_score:
            return 0                   #プレイヤーの勝利
        elif player_score < dealer_score:
            return 1                   #ディーラーの勝利
        else:
            return 2                   #ドロー

player_have_cards = []
player_have_cards.append(choice_card())
dealer_have_cards = []
dealer_have_cards.append(choice_card())

player_have_cards.append(choice_card())
dealer_have_cards.append(choice_card())
print ("プレイヤーが引いたカードは ")
print_card(player_have_cards)
print ("ディーラーのカードは ")
print_card(dealer_have_cards)
dealer_have_cards.append(choice_card())

player_draw_card = " YES"
count_player_drawn_card = 2

while (player_draw_card == "YES"):
    print (("プレイヤーは現在 ") + str(count_player_drawn_card) + "枚所持しています")
    print ("プレイヤーはもう一枚引きますか？YESかNOで答えてください")
    player_draw_card = input()

    if player_draw_card == "YES":
        count_player_drawn_card = count_player_drawn_card + 1
        choiced_more_card = choice_card()
        print("プレイヤーが引いたカードは" + str(choiced_more_card))
        player_have_cards.append(choiced_more_card)
    else :
        print ("プレイヤーはカードを引きませんでした")

    dealer_draw_card = random.randint(0,1)
    if dealer_draw_card == 1:
        print ("ディーラーはカードを引きました")
        choiced_more_card = choice_card()
        dealer_have_cards.append(choiced_more_card)
    else :
        print ("ディーラーはカードを引きませんでした")

player_score = calc_score(player_have_cards)
dealer_score = calc_score(dealer_have_cards)

result = judge(player_score, dealer_score)

print ("結果発表!")
print_card(player_have_cards)
print ("プレイヤーの合計点は" + str(player_score) + "点")
print_card(dealer_have_cards)
print ("ディーラーの合計点" + str(dealer_score) + "点")

if(result == 0):
    print ("プレイヤーの勝利です")
elif(result == 1):
    print ("ディーラーが勝ちました")
else:
    print ("引き分けです")
