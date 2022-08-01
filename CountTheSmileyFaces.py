def count_smileys(arr):
    smileys = 0
    possibilities = [":)", ";)", ':D', ';D', ":-)", ";-)", ':-D', ';-D', ":~)", ";~)", ':~D', ';~D']
    for face in arr:
        if face in possibilities:
            smileys += 1
    return smileys

count_smileys([';]', ':[', ';*', ':$', ';-D'])