#查看一段文本中的在单词表中的单词数目

def checkio(text,words):
	count = 0
	for word in words:
		if word in text.lower():
			count += 1
	return count




#count_words = lambda text,words:sum(1 for word in words if word in text.lower())