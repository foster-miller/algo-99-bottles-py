def bottle_song():
	bottles = int(input("How many bottles are on the wall?"))
	start = bottles
	while bottles > 0:
		print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.\
\nTake one down and pass it around, {bottles-1} bottles of beer on the wall.")
		bottles -= 1
		if bottles == 1:
			print(f"1 bottle of beer on the wall, 1 bottle of beer.\
\nTake one down and pass it around, no more bottles of beer on the wall.")
			bottles -= 1
		if bottles == 0:
			print(f"No more bottles of beer on the wall, no more bottles of beer.\
\nGo to the store and buy some more, {start} bottles of beer on the wall.")
			bottles -= 1
bottle_song()

####kldjsfalkfdajalskdfjdfls