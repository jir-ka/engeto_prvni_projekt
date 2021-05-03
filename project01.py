import task_template

regUsers = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
texts = task_template.TEXTS
state = 'login'


# -------------------------------------------fANALYZE---------------------------------------------------
def fAnalyze(txt):
    numb = 0
    lowC = 0
    uppC = 0
    titC = 0
    numbSum = 0
    wordsByCh = {}
    words = txt.split()

    for word in words:
        word = word.strip('.,!?')

        if not len(word) in wordsByCh:
            wordsByCh[len(word)] = 1
        else:
            wordsByCh[len(word)] += 1

        if word.isdigit():
            numb += 1
            numbSum += int(word)
        else:
            if word.islower():
                lowC += 1
            else:
                if word.isupper():
                    uppC += 1
                else:
                    titC += 1

    print(50 * '-')
    print('There are ' + str(len(words)) + ' words in the selected text.')
    print('There are ' + str(titC) + ' titlecase words.')
    print('There are ' + str(uppC) + ' uppercase words.')
    print('There are ' + str(lowC) + ' lowercase words.')
    print('There are ' + str(numb) + ' numeric strings.')
    print('The sum of all the numbers ' + str(numbSum))
    print(50 * '-')
    print('LEN|' + 'OCCURRENCES'.center(max(wordsByCh.values()), ' ') + '|NR.')
    for i in sorted(wordsByCh):
        print(str(i).rjust(3) + '|' + (wordsByCh[i] * '*').ljust(max(wordsByCh.values())) + '|' + str(wordsByCh[i]))
    print(50 * '-')


# ------------------------------------MAIN LOOP-----------------------------------------------------------------------
while state != 'exit':

    # ----------------------------------------------LOGIN-------------------------------------------------------------
    if state == 'login':
        username = input('User: ')
        if username in regUsers.keys():
            password = input('Password: ')
            if regUsers[username] == password:
                state = 'analyze'
                print(50 * '-')
                print('Welcome to app, ' + username)
                print('We have ' + str(len(texts)) + ' texts to be analyzed.')
                print(50 * '-')
            else:
                print('Incorrect password ' + username + '!')
        else:
            print("User " + username + " is not registered!")

    # -----------------------------ANALYZING--------------------------------------------------------------------------
    while state == 'analyze':
        key = input('Enter a number btw. 1 and ' + str(len(texts)) + ' to select: ')
        if key.isdigit():
            if 0 < int(key) <= len(texts):
                fAnalyze(texts[int(key) - 1])
                state = 'done'
            else:
                print('Entered number is out of range, try it again.')
        else:
            print('Input must be a number, try it again.')

    # ----------------------------------ENDING------------------------------------------------------------------------
    key = ''
    while (key != 'a') and (key != 'x'):
        key = input('Press "a" to start again or "x" to exit app. ')
    if key == 'x':
        state = 'exit'
    else:
        if state == 'done':
            state = 'analyze'
