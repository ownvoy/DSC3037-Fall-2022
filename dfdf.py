dd = "Statistical Data Analysis and Data Mining"
course_title_english = dd.split(" ")
new_english_title = []
for idx, s in enumerate(course_title_english):
    if idx == 0:
        new_english_title.append(s)
    else:
        if len(new_english_title[-1] + s) <= 15:
            new_english_title[-1] = new_english_title[-1] + " " + s
        else:
            new_english_title.append(s)

print(new_english_title)
