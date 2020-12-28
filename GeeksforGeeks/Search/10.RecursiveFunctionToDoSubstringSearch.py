def ExactMatch(text,pat,text_index,pat_index):
    if text_index == len(text) and pat_index != len(pat):
        return 0

    if pat_index == len(pat):
        return 1
    if text[text_index] == pat[pat_index]:
        return ExactMatch(text,pat,text_index+1,pat_index+1)
    return 0

def Contains(text,pat,text_index,pat_index):
    if text_index == len(text):
        return 0

    if text[text_index] == pat[pat_index]:
        if ExactMatch(text,pat,text_index,pat_index):
            return 1
        else:
            return Contains(text,pat,text_index+1,pat_index)

    return Contains(text,pat,text_index+1,pat_index)


print(Contains("GeeksForGeeks","quiz",0,0))
print(Contains("GeeksquizGeeks","quiz",0,0))
