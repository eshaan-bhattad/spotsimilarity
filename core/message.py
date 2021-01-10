
# compatability score
# common_tracks + common_artists should explain itself
# explicit : number of explicit songs for account (1) and friend's playlist (2)
# duration : average song length in seconds
# popularity : how many of your songs are in the top 100
# songs : total number of songs analyzed for fractions

def message(compatability, common_tracks, common_artists, explicit1, explicit2, duration1, duration2, popularity1, popularity2, songs1, songs2):
	output = ""

	#compatability
	if compatability == 100:
		output += "WOW, you two are a perfect match. Congratulations on already finding your perfect music partner. "
	elif compatability > 75:
		output += "Congratulations you and your friend are a great match and "
		output += "will likely not have to argue about who is in charge of the aux with your score of " + str(compatability) + "%. "
	elif compatability > 50:
		output += "Looks like the two of may agree most of the time on what to listen to, but othertimes you might be fighting "
		output += "to skip over a certain song or two with a compatability score of " + str(compatability) + "%. "
	elif compatability > 25:
		output += "The two of you probably would not be able to make it through a road trip without getting in a fight over "
		output += "the radio. However, now with our shared playlist that we generated at the bottom, the two of you may be able "
		output += "to overcome your compatability score of " + str(compatability) + "%. "
	elif compatability > 0:
		output += "The two of you may still be able to be friends but I don't know if you should listen to music at the same time "
		output += "having a score of " + str(compatability) + "%. "
	elif compatability == 0:
		output += "The two of you should just never be together with a compatability score of 0... "

	#common tracks and artists
	output += "Overall, the two playlist had " + str(common_tracks) + " common tracks and " + str(common_artists) + " common artists. "

	#explicit
	explicit_one = float(explicit1) / float(songs1) * 100
	explicit_two = float(explicit2) / float(songs2) * 100

	if explicit_one > 66:
		if explicit_two > 66:
			output += "It seems like the two of you do listen to some music with a lot of expletives though. "
		elif explicit_two > 33:
			output += "It seems like you may enjoy a song with a swear word a little more than your friend though. "
		elif explicit_two > 0:
			output += "It seems like you and your friend have very different opinions are songs with swears. "
	elif explicit_one > 33:
		if explicit_two > 66:
			output += "It seems like your friend may enjoy a song with a swear word a little more than you though. "
		elif explicit_two > 33:
			output += "It seems like the two of you do listen to some music with some expletives though. "
		elif explicit_two > 0:
			output += "It seems like neither you or your friend care for swear words that much. "
	elif explicit_one >=0:
		if explicit_two > 66:
			output += "It seems like you and your friend have very different opinions are songs with swears. "
		elif explicit_two > 33:
			output += "It seems like neither you or your friend care for swear words that much. "
		elif explicit_two > 0:
			output += "Seems like the two of you are goody goodys when it comes to music language. "

	#duration
	if duration1 > 240:
		if duration2 > 240:
			output += "The two of you do have a lot of patience because you can listen through these longer songs. "
		elif duration2 > 180:
			output += "Your friend could learn a little about patience from you, seeing as though you listen to longer songs. "
		else:
			output += "I do not know how the two of you hang out with such different levels of patience, judging by the length of the songs you two listen to. "
	elif duration1 > 180:
		if duration2 > 240:
			output += "You could learn a little about patience from your friend, seeing as though you listen to shorter songs. "
		elif duration2 > 180:
			output += "The two of you do have a little bit of patience, judging by your song lengths. "
		else:
			output += "You should try learning a little bit of patience from your friend, judging by your song lengths."
	else:
		if duration2 > 240:
			output += "I do not know how the two of you hang out with such different levels of patience, judging by the length of the songs you two listen to. "
		elif duration2 > 180:
			output += "You should try learning a little bit of patience from your friend, judging by your song lengths."
		else:
			output += "You two need to learn some patience, judging by your song lengths. "

	#popularity 
	pop1 = float(popularity1) / float(songs1) * 100
	pop2 = float(popularity2) / float(songs2) * 100

	if pop1 > 66:
		if pop2 > 66:
			output += "Lastly, the two of you have some pretty basic song choices. Maybe you can check out our recommended playlist for some help..."
		elif pop2 > 33: 
			output += "You should try to be more like your friend, having a good balance with basic radio songs."
		else:
			output += "Your friend is a straight up hipster when it comes to music, unlike yourself..."
	elif pop1 > 33:
		if pop2 > 66:
			output += "You friend should try to be more like you, having a good balance with basic radio songs."
		elif pop2 > 33: 
			output += "The two of you have a good balance with basic radio songs."
		else:
			output += "Your friend is a straight up hipster when it comes to music, unlike you who is a little more balanced."
	else:
		if pop2 > 66:
			output += "You friend should try to be more like you, being a straight out hipster when it comes to music."
		elif pop2 > 33: 
			output += "You are a straight up hipster when it comes to music, unlike your friend who is a little more balanced."
		else:
			output += "Both of you are straight up hipsters when it comes to music!"

	return output + " We hope spotsimilarity can help you perfect your musical taste!"

# print(message(55, 11, 5, 10, 2, 15, 5, 23, 12, 40, 40))
