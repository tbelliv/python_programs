import pyinputplus as pyip
import random, time

while True:
    numcorrect = 0
    numincorrect = 0
    numquestions = pyip.inputInt(prompt = 'How many questions do you want to answer?', min = 3, max = 9)

    for i in range(numquestions):
        num1 = random.randint(0, 20)
        num2 = random.randint(0, 20)
        correctanswer = num1 * num2
        prompt = f'{num1} x {num2} = '
        try:
            useranswer = pyip.inputInt(prompt = prompt, allowRegexes = [f'^{correctanswer}$'], blockRegexes = ['.*', '0'], timeout = 30, limit = 3)
            if useranswer == correctanswer:
                numcorrect += 1
            else:
                numincorrect += 1
        except pyip.TimeoutException:
            print('Out of time!')
        except pyip.RetryLimitException:
            print('Out of tries!')
        time.sleep(1)
        print(f'Score: {numcorrect} correct, {numincorrect} incorrect.')

    print(f'Final score: {numcorrect} correct, {numincorrect} incorrect.')