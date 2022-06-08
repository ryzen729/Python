from logo import logo,vs
from game_data import data
import random


print(logo)
playing = True
#create random value
count = 0
while playing:
    def abgame():
        index_1 = random.randint(0, len(data) - 1)
        index_2 = random.randint(0, len(data) - 1)


        #create creat function for A and B
        def comparea(ab,index,logo):
            print(f'Compare {ab}: {data[index]["name"]}, {data[index]["description"]} from {data[index]["country"]}')
            if logo == 0:
                print(vs)
            a_value = data[index]["follower_count"]
            return a_value

        a_value = comparea("A",index_1,0)
        b_value = comparea("B",index_2,1)


        # Compare a and b followers
        def followers(a_value,b_value):
            if a_value > b_value:
                more_follower = "A"
            else:
                more_follower = "B"
            return more_follower
        result = followers(a_value, b_value)
        return result

    
    result_value = abgame()
    followers_input = input("Who has more followers? Type 'A' or 'B': ")
    print(result_value)
    if followers_input == result_value:
        count += 1
        result_value = ""
    else:
        playing = False
        print(f"Yor final score is {count}")

