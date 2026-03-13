#智能算术教练(AI Math Coach) v3.0

import random
import time
def generate_question(low, high):
    a = random.randint(low,high)
    b = random.randint(low,high)
    return a + b, f"{a} + {b}"

wrong_dict = {}
game_over = False
score = 0

cur_low = 1
cur_high = 50


start_time = time.time()
for i in range(5):
    right_answer, text = generate_question(cur_low, cur_high)
    answer = None

    while True:
        try:
            user_input = input(f"第{i+1}题: {text}= ")
            if user_input.lower() == "q":
                game_over = True
                break

            answer = int(user_input)
            break

        except ValueError:
            print("请输入有效数字或q退出")

    if game_over:
        print("今天的练习到此结束，欢迎下次光临。")
        break

    if answer == right_answer:
        print("回答正确")
        score += 1
        cur_low = cur_low * 15
        cur_high = cur_high * 15

    else:
        wrong_dict[text] = answer
        print(f"回答错误，正确答案为{right_answer}")
        cur_low = cur_low // 15
        cur_high = cur_high // 15


end_time = time.time()
use_time = end_time - start_time
print(f"你的用时为{use_time:.2f}秒")
print(f"你的最终分数是{score}")


if score == 5:
    print(f"彦卿同学真是天才")
elif 4 >= score >= 3 :
    print("彦卿同学做的不错")
else:
    print("彦卿同学还得练啊")

if wrong_dict:
    print(f"你的错题清单为：")
    for x, y  in wrong_dict.items():
        print(f"题干：{x}, 你的答案：{y}")
else:
    print("欢迎下次光临，炎卿同学")

input("\n按回车键退出练习...")


